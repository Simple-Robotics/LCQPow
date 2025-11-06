##
##	This file is part of LCQPow.
##
##	LCQPow -- A Solver for Quadratic Programs with Commplementarity Constraints.
##	Copyright (C) 2020 - 2022 by Jonas Hall et al.
##
##	LCQPow is free software; you can redistribute it and/or
##	modify it under the terms of the GNU Lesser General Public
##	License as published by the Free Software Foundation; either
##	version 2.1 of the License, or (at your option) any later version.
##
##	LCQPow is distributed in the hope that it will be useful,
##	but WITHOUT ANY WARRANTY; without even the implied warranty of
##	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
##	See the GNU Lesser General Public License for more details.
##
##	You should have received a copy of the GNU Lesser General Public
##	License along with LCQPow; if not, write to the Free Software
##	Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
##

# cmake minimum required version
cmake_minimum_required(VERSION 3.22)

# Project name
project(lcqpow CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(CMAKE_POLICY_VERSION_MINIMUM 3.5)

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release CACHE STRING "Build type" FORCE)
endif()

# Output directories
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin")

## Options ------------------------------------------------------------------------------
option(
    BUILD_EXAMPLES
    "Option to build examples"
    ON
)

option(
    UNIT_TESTS
    "Option to build and run unit tests"
    ON
)

option(
    PROFILING
    "Option to enable profiling (gprof)."
    OFF
)

option(
    QPOASES_SCHUR
    "Use the Schur Complement Method with MA57 Solver"
    OFF
)

option(
    BUILD_MATLAB_INTERFACE
    "Option to build Matlab interface"
    ON
)

option(
    BUILD_PYTHON_INTERFACE
    "Option to build Python interface"
    ON
)

set(BUILD_SHARED_LIBS OFF CACHE BOOL "" FORCE)

# print options
message(
    "CMAKE_BUILD_TYPE           ${CMAKE_BUILD_TYPE}\n"
    "EXAMPLES                   ${BUILD_EXAMPLES}\n"
    "BUILD_MATLAB_INTERFACE     ${BUILD_MATLAB_INTERFACE}\n"
    "BUILD_PYTHON_INTERFACE     ${BUILD_PYTHON_INTERFACE}\n"
    "UNIT_TESTS                 ${UNIT_TESTS}\n"
    "PROFILING                  ${PROFILING}\n"
    "QPOASES_SCHUR              ${QPOASES_SCHUR}\n"
)

## ADD ALL EXTERNAL PROJECTS ------------------------------------------------------------
# external modules
include(FetchContent)

# 1) qpOASES
set(DEF_SOLVER "SOLVER_NONE")

if (${QPOASES_SCHUR})

    find_package(Matlab)
    if (NOT ${Matlab_FOUND})
        # throw error if schur is enabled and matlab not found
        message(
            FATAL_ERROR
            "qpOASES with Schur Complement method is currently only supported in combination with matlab, which can not be located."
        )
    endif()
    
    message(STATUS "qpOASES Matlab found")

    # if found, then set some variables
    get_filename_component(
        MATLAB_LIBDIR
        ${Matlab_MEX_LIBRARY}
        DIRECTORY
    )

    set(LIB_SOLVER "${MATLAB_LIBDIR}/libmwma57.so")
    set(DEF_SOLVER "SOLVER_MA57")
    set(USE_SOLVER "MA57")
    set(LINKHSL "-Wl,-rpath=${MATLAB_LIBDIR}")
    set(LIB_LAPACK "${MATLAB_LIBDIR}/libmwlapack.so")
    set(LIB_BLAS "${MATLAB_LIBDIR}/libmwblas.so")
    set(LIB_METIS "${MATLAB_LIBDIR}/libmwmetis.so")
    set(sparse_libs "${LIB_SOLVER} ${LIB_BLAS} ${LIB_LAPACK} ${LIB_METIS}")

    set(
        qpOASES_MAKE_ARGS
        ${qpOASES_MAKE_ARGS} LIB_SOLVER=${LIB_SOLVER} LIB_BLAS=${LIB_BLAS} LIB_LAPACK=${LIB_LAPACK} LINKHSL=${LINKHSL}
    )

    if(NOT EXISTS ${LIB_SOLVER} OR NOT EXISTS ${LIB_BLAS} OR NOT EXISTS ${LIB_LAPACK} OR NOT EXISTS ${LIB_METIS})
        message(
            FATAL_ERROR
            "Failed to locate one of the following dependencies for Schur Complement Method:\n"
            "MA57   ${LIB_SOLVER}\n"
            "BLAS   ${LIB_BLAS}\n"
            "LAPACK ${LIB_LAPACK}\n"
            "METIS  ${LIB_METIS}"
        )
    else()
        message(
            "Located the following dependencies for Schur Complement Method:\n"
            "MA57   ${LIB_SOLVER}\n"
            "BLAS   ${LIB_BLAS}\n"
            "LAPACK ${LIB_LAPACK}\n"
            "METIS  ${LIB_METIS}"
        ) 
    endif()
endif()

cmake_policy(SET CMP0169 OLD)

FetchContent_Declare(qpoases SOURCE_DIR "${CMAKE_SOURCE_DIR}/external/qpOASES")
FetchContent_GetProperties(qpoases)
if (NOT qpoases_POPULATED)
    FetchContent_Populate(qpoases)
    set(QPOASES_BUILD_EXAMPLES OFF)
    add_subdirectory(${qpoases_SOURCE_DIR} ${qpoases_BINARY_DIR} EXCLUDE_FROM_ALL)
    add_library(qpoases_custom INTERFACE IMPORTED)
    target_link_libraries(qpoases_custom INTERFACE qpOASES)
    target_include_directories(qpoases_custom INTERFACE ${qpoases_SOURCE_DIR}/include)
    # compile options
    target_compile_options(
        qpoases_custom
        INTERFACE
        -D__USE_LONG_FINTS__
        -D${DEF_SOLVER}
    )
    set_target_properties(qpOASES PROPERTIES POSITION_INDEPENDENT_CODE ON)
endif()

# 2) OSQP
FetchContent_Declare(osqp SOURCE_DIR "${CMAKE_SOURCE_DIR}/external/osqp")
set(DLONG OFF CACHE BOOL "Use long integers" FORCE)
FetchContent_GetProperties(osqp)
if (NOT osqp_POPULATED)
    FetchContent_Populate(osqp)
    add_subdirectory(${osqp_SOURCE_DIR} ${osqp_BINARY_DIR} EXCLUDE_FROM_ALL)
endif()

# 3) googletest
if(${UNIT_TESTS})
    find_package(GTest)
    if (NOT GTest_FOUND)
        FetchContent_Declare(gtest SOURCE_DIR "${CMAKE_SOURCE_DIR}/external/googletest")
        set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
        FetchContent_MakeAvailable(gtest)
    endif()
endif()

## CREATE LCQPow libraries ----------------------------------------------------------
# Include project headers

# Save auxiliar source files to variable
file(GLOB LCQPOW_SOURCES src/*.cpp)

# create shared lib
add_library(${PROJECT_NAME}-static STATIC ${LCQPOW_SOURCES})
set_target_properties(
    ${PROJECT_NAME}-static
    PROPERTIES
    OUTPUT_NAME ${PROJECT_NAME}
)
target_include_directories(
    ${PROJECT_NAME}-static
    PUBLIC 
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
)
target_link_libraries(
    ${PROJECT_NAME}-static
    PUBLIC
    qpoases_custom
    osqpstatic
)
set_target_properties(lcqpow-static PROPERTIES POSITION_INDEPENDENT_CODE ON)
if (${PROFILING})
    target_compile_options(${PROJECT_NAME}-static PUBLIC -pg)
endif()
add_library(lcqpow::lcqpow-static ALIAS lcqpow-static)

if (${QPOASES_SCHUR})
    target_link_libraries(
        ${PROJECT_NAME}-static
        PRIVATE ${Matlab_LIBRARIES}
    )

    get_filename_component(LIB_SOLVER_NAME ${LIB_SOLVER} NAME)
    get_filename_component(LIB_BLAS_NAME ${LIB_BLAS} NAME)
    get_filename_component(LIB_LAPACK_NAME ${LIB_LAPACK} NAME)
    get_filename_component(LIB_METIS_NAME ${LIB_METIS} NAME)


    ADD_CUSTOM_TARGET(link_schur ALL 
        COMMAND ${CMAKE_COMMAND} -E create_symlink ${LIB_SOLVER} lib/${LIB_SOLVER_NAME}
        COMMAND ${CMAKE_COMMAND} -E create_symlink ${LIB_BLAS} lib/${LIB_BLAS_NAME}
        COMMAND ${CMAKE_COMMAND} -E create_symlink ${LIB_LAPACK} lib/${LIB_LAPACK_NAME}
        COMMAND ${CMAKE_COMMAND} -E create_symlink ${LIB_METIS} lib/${LIB_METIS_NAME}
    )

endif()

## Build examples -----------------------------------------------------------------------
if (${BUILD_EXAMPLES})
    file(GLOB EXAMPLE_FILES examples/*.cpp)

    foreach(ELEMENT ${EXAMPLE_FILES})
        get_filename_component(EXAMPLE_NAME ${ELEMENT} NAME_WE)

        add_executable(${EXAMPLE_NAME} ${ELEMENT})

        target_link_libraries(${EXAMPLE_NAME} PRIVATE ${PROJECT_NAME}-static)

        if (${QPOASES_SCHUR})
            target_link_libraries(
                ${EXAMPLE_NAME}
                PRIVATE ${Matlab_LIBRARIES}
            )
        endif()

        # specify output directory
        set_target_properties(
            ${EXAMPLE_NAME}
            PROPERTIES
            RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin/examples"
        )
    endforeach()
endif()

## Build Matlab interface ---------------------------------------------------------------
if (${BUILD_MATLAB_INTERFACE})

    # Ensure cmake can locate matlab and set matlab paths
    find_package(Matlab)
    if (NOT ${Matlab_FOUND})
        # send warning that the matlab interface could not be built
        message(
            WARNING
            "Unable to build Matlab interface (Matlab was not found)."
        )
    
    # if found, then build interface
    else()
        get_filename_component(
            MATLAB_LIBDIR
            ${Matlab_MEX_LIBRARY}
            DIRECTORY
        )

        if (${QPOASES_SCHUR})
            set(
                MA57_lib
                -lmwma57
            )
        endif()

        set(
            MATLAB_INTERFACE_DIR
            ${CMAKE_SOURCE_DIR}/interfaces/matlab
        )

        set(
            MATLAB_INTERFACE_NAME
            LCQPow
        )

        set(
            MATLAB_INTERFACE_DESTINATION
            ${CMAKE_BINARY_DIR}/lib
        )

        matlab_add_mex(
            NAME matlab_interface
            SRC ${MATLAB_INTERFACE_DIR}/${MATLAB_INTERFACE_NAME}.cpp
            OUTPUT_NAME ${MATLAB_INTERFACE_DESTINATION}/${MATLAB_INTERFACE_NAME}
            LINK_TO "-llcqpow -lqpOASES -losqp -lmwblas -lmwlapack -lmwma57"
        )

        target_link_libraries(matlab_interface PUBLIC ${PROJECT_NAME}-static)

        target_compile_options(
            matlab_interface
            PUBLIC -D${DEF_SOLVER}
                   -D__cpluplus
                   -O
                   -largeArrayDims
                   -lmwblas
                   -lmwlapack
                   -lmwma57
        )

        file(
            COPY ${MATLAB_INTERFACE_DIR}/${MATLAB_INTERFACE_NAME}.m
            DESTINATION ${MATLAB_INTERFACE_DESTINATION}
        )
    
    endif()

endif()


## Build Python interface ---------------------------------------------------------------
if (${BUILD_PYTHON_INTERFACE})
    
    find_package(Python COMPONENTS Interpreter Development)
    find_package(pybind11 CONFIG)
    if (NOT pybind11_FOUND)
        message(STATUS "Pybind11 not found through find_package(). Using submodule external/pybind11.")
        add_subdirectory(external/pybind11)
    endif()
    add_subdirectory(interfaces/python)
endif()

## Build unit tests ---------------------------------------------------------------------
if (${UNIT_TESTS})
    enable_testing()
    add_executable(RunUnitTests test/RunUnitTests.cpp)

    set_target_properties(
        RunUnitTests
        PROPERTIES
        RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin/tests"
    )

    # Add libraries: gtest, qpOASES, OSQP
    target_link_libraries(
        RunUnitTests
        PUBLIC lcqpow::lcqpow-static
        PRIVATE GTest::gtest_main ${LIB_SOLVER} -lpthread
    )

    add_test(NAME UnitTests COMMAND RunUnitTests)

    # Build examples for testing
    file(GLOB TEST_FILES test/examples/*.cpp)

    foreach(ELEMENT ${TEST_FILES})
        get_filename_component(EXAMPLE_NAME ${ELEMENT} NAME_WE)

        set(EXAMPLE_TARGET "${EXAMPLE_NAME}_TEST")

        add_executable(${EXAMPLE_TARGET} ${ELEMENT})
        message(STATUS "Adding unit C++ test ${EXAMPLE_TARGET}")

        target_link_libraries(${EXAMPLE_TARGET} PRIVATE lcqpow::lcqpow-static)

        # specify output directory
        set_target_properties(
            ${EXAMPLE_TARGET}
            PROPERTIES
            RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin/tests"
        )
    endforeach()
endif()

## Installation -------------------------------------------------------------------------
include(GNUInstallDirs)

install(TARGETS lcqpow-static
    EXPORT lcqpowTargets
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

install(DIRECTORY include/
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/lcqpow
    FILES_MATCHING PATTERN "*.h" PATTERN "*.hpp"
)

install(EXPORT lcqpowTargets
    FILE lcqpowTargets.cmake
    NAMESPACE lcqpow::
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/lcqpow
)

# uninstall target
configure_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/cmake_uninstall.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/cmake_uninstall.cmake"
    IMMEDIATE @ONLY)

if(NOT TARGET uninstall)
    add_custom_command(uninstall)
endif()
add_custom_target(${PROJECT_NAME}-uninstall
    COMMAND ${CMAKE_COMMAND} -P ${CMAKE_CURRENT_BINARY_DIR}/cmake_uninstall.cmake)
add_dependencies(uninstall ${PROJECT_NAME}-uninstall)
