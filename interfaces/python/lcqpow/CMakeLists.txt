find_package(Eigen3 REQUIRED)

macro(pybind11_add_lcqpow_module MODULE)
  pybind11_add_module(
    ${MODULE} 
    MODULE
    ${MODULE}.cpp
  )
  target_include_directories(
    ${MODULE} 
    PRIVATE
  )
  target_link_libraries(
    ${MODULE} 
    PRIVATE
    ${PROJECT_NAME}-shared
    Eigen3::Eigen
    ${qpoases_lib}
  )
endmacro()

pybind11_add_lcqpow_module(LCQProblem)
pybind11_add_lcqpow_module(Options)
pybind11_add_lcqpow_module(OutputStatistics)
pybind11_add_lcqpow_module(Utilities)