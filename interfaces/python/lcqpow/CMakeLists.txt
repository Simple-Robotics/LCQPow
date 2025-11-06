find_package(Eigen3 REQUIRED)

function(pybind11_add_lcqpow_module)
  set(MODULE LCQPow_py)
  pybind11_add_module(${MODULE} MODULE
    LCQProblem.cpp
    Options.cpp
    OutputStatistics.cpp
    Utilities.cpp
    module.cpp 
  )
  target_link_libraries(
    ${MODULE} 
    PRIVATE
      ${PROJECT_NAME}-shared
      Eigen3::Eigen
  )
  set_target_properties(
    ${MODULE}
    PROPERTIES
      LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
  )
endfunction()

pybind11_add_lcqpow_module()
