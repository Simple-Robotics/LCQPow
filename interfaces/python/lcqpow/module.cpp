#include <pybind11/pybind11.h>


namespace LCQPow{
namespace python {
namespace py = pybind11;

void exposeLCQProblem(py::module_ m);
void exposeOptions(py::module_ m);
void exposeOutputStatistics(py::module_ m);
void exposeUtilities(py::module_ m);

PYBIND11_MODULE(LCQPow_py, m) {
    exposeLCQProblem(m);
    exposeOptions(m);
    exposeOutputStatistics(m);
    exposeUtilities(m);
}

} // namespace python
} // namespace LCQPow
