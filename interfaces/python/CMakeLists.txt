find_package(Eigen3 REQUIRED)
set(PYTHON_INTERFACE_NAME lcqpow)
set(PYMODULE LCQPow_py)

function(pybind11_add_lcqpow_module)
    pybind11_add_module(${PYMODULE} MODULE
      LCQProblem.cpp
      Options.cpp
      OutputStatistics.cpp
      Utilities.cpp
      module.cpp
    )
    target_link_libraries(
        ${PYMODULE}
        PRIVATE
            ${PROJECT_NAME}-static
            Eigen3::Eigen
    )
    set_target_properties(
        ${PYMODULE}
        PROPERTIES
            LIBRARY_OUTPUT_DIRECTORY
                ${CMAKE_CURRENT_BINARY_DIR}/${PYTHON_INTERFACE_NAME}
    )
endfunction()

pybind11_add_lcqpow_module()
set(PYTHON_INTERFACE_DESTINATION ${CMAKE_BINARY_DIR}/interfaces/python)
set(PYFILES ${PYTHON_INTERFACE_NAME}/__init__.py)

file(COPY ${PYFILES} DESTINATION ${PYTHON_INTERFACE_DESTINATION}/${PYTHON_INTERFACE_NAME})

file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/examples/ DESTINATION ${PYTHON_INTERFACE_DESTINATION})

file(COPY ${PROJECT_SOURCE_DIR}/examples/example_data DESTINATION ${PYTHON_INTERFACE_DESTINATION})

install(TARGETS ${PYMODULE} DESTINATION ${Python_SITELIB}/${PYTHON_INTERFACE_NAME})
install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/lcqpow/ DESTINATION ${Python_SITELIB}/lcqpow)
