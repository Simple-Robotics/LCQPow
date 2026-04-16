#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/eigen.h>
#include <pybind11/stl.h>

#include <Eigen/Core>
#include <vector>

#include "LCQProblem.hpp"

extern "C" {
    #include <osqp.h>
}


namespace LCQPow {
namespace python {

namespace py = pybind11;
using namespace py::literals;

using Eigen::MatrixXd;
using Eigen::VectorXd;
using ConstMatrixRef = Eigen::Ref<const MatrixXd>;
using ConstVectorRef = Eigen::Ref<const VectorXd>;


/// @brief Wrapper for the OSQP csc struct.
class cscWrapper {
public:
  cscWrapper(const int m, const int n, const int nnx, const ConstVectorRef& x, 
             const std::vector<int>& i, const std::vector<int>& p)
             : x_(x)
             , i_(i)
             , p_(p)
             , csc_(Utilities::createCSC(m, n, nnx, x_.data(), i_.data(), p_.data()))
             {}

  cscWrapper() { 
    csc_ = nullptr; 
  }

  ~cscWrapper() { 
    if (!csc_) {
      free(csc_);
      csc_ = nullptr; 
    }
  }

  csc* ptr() noexcept{
    return csc_;
  }

  const csc* ptr() const noexcept {
    return csc_;
  }

  int nzmax() const { return csc_->nzmax; }
  int m() const { return csc_->m; }
  int n() const { return csc_->n; }
  int nz() const { return csc_->nz; }

private:
  Eigen::VectorXd x_;
  std::vector<int> i_, p_;
  csc* csc_;
};


template<class D>
inline const double *getRawPtrFromEigen(const Eigen::MatrixBase<D> &mat_) {
  const auto &mat = mat_.const_cast_derived();
  return mat.size() > 0 ? mat.data() : nullptr;
}


void exposeLCQProblem(py::module_ m) {
  py::class_<cscWrapper>(m, "cscWrapper")
    .def(py::init<const int, const int, const int, ConstVectorRef,
                  const std::vector<int>&, const std::vector<int>&>(),
         "m"_a, "n"_a, "nnx"_a, "x"_a, "i"_a, "p"_a)
         .def_property_readonly("nzmax", &cscWrapper::nzmax)
         .def_property_readonly("m", &cscWrapper::m)
         .def_property_readonly("n", &cscWrapper::n)
         .def_property_readonly("nz", &cscWrapper::nz);

  py::class_<LCQProblem>(m, "LCQProblem")
    .def(py::init<>())
    .def(py::init<int, int, int>(), 
         py::arg("nV"), py::arg("nC"), py::arg("nComp"))
    .def("loadLCQP", [](LCQProblem& self, ConstMatrixRef Q, 
                        ConstVectorRef g,  ConstMatrixRef L, 
                        ConstMatrixRef R, ConstVectorRef lbL, 
                        ConstVectorRef ubL, ConstVectorRef lbR, 
                        ConstVectorRef ubR, ConstMatrixRef A, 
                        ConstVectorRef lbA, ConstVectorRef ubA,
                        ConstVectorRef lb, ConstVectorRef ub,  
                        ConstVectorRef x0, ConstVectorRef y0) {
            return self.loadLCQP(Q.data(), g.data(), L.data(), R.data(), 
                                 getRawPtrFromEigen(lbL),
                                 getRawPtrFromEigen(ubL),
                                 getRawPtrFromEigen(lbR),
                                 getRawPtrFromEigen(ubR),
                                 getRawPtrFromEigen(A),
                                 getRawPtrFromEigen(lbA),
                                 getRawPtrFromEigen(ubA),
                                 getRawPtrFromEigen(lb),
                                 getRawPtrFromEigen(ub),
                                 getRawPtrFromEigen(x0),
                                 getRawPtrFromEigen(y0));
          },
          "Q"_a, "g"_a, "L"_a, "R"_a, 
          "lbL"_a=Eigen::VectorXd::Zero(0), 
          "ubL"_a=Eigen::VectorXd::Zero(0), 
          "lbR"_a=Eigen::VectorXd::Zero(0), 
          "ubR"_a=Eigen::VectorXd::Zero(0), 
          "A"_a=MatrixXd::Zero(0, 0), 
          "lbA"_a=Eigen::VectorXd::Zero(0), 
          "ubA"_a=Eigen::VectorXd::Zero(0), 
          "lb"_a=Eigen::VectorXd::Zero(0), 
          "ub"_a=Eigen::VectorXd::Zero(0), 
          "x0"_a=Eigen::VectorXd::Zero(0), 
          "y0"_a=Eigen::VectorXd::Zero(0))
    .def("loadLCQP", [](LCQProblem& self, const cscWrapper& Q, 
                        const ConstVectorRef &g,  const cscWrapper& L, 
                        const cscWrapper& R,       const ConstVectorRef& lbL, 
                        const ConstVectorRef& ubL, const ConstVectorRef& lbR, 
                        const ConstVectorRef& ubR, const cscWrapper& A, 
                        const ConstVectorRef& lbA,const ConstVectorRef& ubA,
                        const ConstVectorRef& lb, const ConstVectorRef& ub,  
                        const ConstVectorRef& x0, const ConstVectorRef& y0) {
            return self.loadLCQP(Q.ptr(), g.data(), L.ptr(), R.ptr(), 
                                 getRawPtrFromEigen(lbL),
                                 getRawPtrFromEigen(ubL),
                                 getRawPtrFromEigen(lbR),
                                 getRawPtrFromEigen(ubR),
                                 A.ptr(),
                                 getRawPtrFromEigen(lbA),
                                 getRawPtrFromEigen(ubA),
                                 getRawPtrFromEigen(lb),
                                 getRawPtrFromEigen(ub),
                                 getRawPtrFromEigen(x0),
                                 getRawPtrFromEigen(y0));
          },
          py::arg("Q"), py::arg("g"), py::arg("L"), py::arg("R"), 
          py::arg("lbL")=Eigen::VectorXd::Zero(0), 
          py::arg("ubL")=Eigen::VectorXd::Zero(0), 
          py::arg("lbR")=Eigen::VectorXd::Zero(0), 
          py::arg("ubR")=Eigen::VectorXd::Zero(0), 
          py::arg("A")=cscWrapper(), 
          py::arg("lbA")=Eigen::VectorXd::Zero(0), 
          py::arg("ubA")=Eigen::VectorXd::Zero(0), 
          py::arg("lb")=Eigen::VectorXd::Zero(0), 
          py::arg("ub")=Eigen::VectorXd::Zero(0), 
          py::arg("x0")=Eigen::VectorXd::Zero(0), 
          py::arg("y0")=Eigen::VectorXd::Zero(0))
    .def("loadLCQP", static_cast<ReturnValue (LCQProblem::*)(
          const char* const, const char* const, const char* const, 
          const char* const, const char* const, const char* const, 
          const char* const, const char* const, const char* const,
          const char* const, const char* const, const char* const,
          const char* const, const char* const, 
          const char* const)>(&LCQProblem::loadLCQP), 
          py::arg("Q_file"), py::arg("g_file"), 
          py::arg("L_file"), py::arg("R_file"), 
          py::arg("lbL_file")=nullptr, py::arg("ubL_file")=nullptr, 
          py::arg("lbR_file")=nullptr, py::arg("ubR_file")=nullptr, 
          py::arg("A_file")=nullptr, 
          py::arg("lbA_file")=nullptr, py::arg("ubA_file")=nullptr, 
          py::arg("lb_file")=nullptr, py::arg("ub_file")=nullptr, 
          py::arg("x0_file")=nullptr, py::arg("y0_file")=nullptr) 
    .def("runSolver", &LCQProblem::runSolver)
    .def("getPrimalSolution", [](const LCQProblem& self) {
            Eigen::VectorXd xOpt(self.getNumberOfPrimals());
            xOpt.setZero();
            self.getPrimalSolution(xOpt.data());
            return xOpt;
         })
    .def("getDualSolution", [](const LCQProblem& self) {
            Eigen::VectorXd yOpt(self.getNumberOfDuals());
            yOpt.setZero();
            self.getDualSolution(yOpt.data());
            return yOpt;
         })
    .def("getNumberOfDuals", &LCQProblem::getNumberOfDuals)
    .def("getOutputStatistics", &LCQProblem::getOutputStatistics)
    .def("setOptions", &LCQProblem::setOptions);
}

} // namespace python
} // namespace LCQPow