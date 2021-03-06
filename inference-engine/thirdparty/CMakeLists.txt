# Copyright (C) 2018 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
#

if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-unknown-warning-option -Wno-inconsistent-missing-override -Wno-pass-failed")
  set(CMAKE_CC_FLAGS "${CMAKE_CC_FLAGS} -Wno-unknown-warning-option -Wno-inconsistent-missing-override -Wno-pass-failed")
endif()

add_subdirectory(pugixml)
add_subdirectory(stb_lib)
add_subdirectory(ade)

if (ENABLE_CLDNN)
    set(CLDNN__OUTPUT_DIR ${CMAKE_LIBRARY_OUTPUT_DIRECTORY})
    set(CLDNN__INCLUDE_TESTS OFF CACHE BOOL "" FORCE)
    set(CLDNN__INCLUDE_EXAMPLES OFF CACHE BOOL "" FORCE)
    set(CLDNN__INCLUDE_TUTORIAL OFF CACHE BOOL "" FORCE)
    if (WIN32)
        set(CLDNN__ARCHITECTURE_TARGET "Windows64" CACHE STRING "" FORCE)
    else()
        set(CLDNN__ARCHITECTURE_TARGET "Linux64" CACHE STRING "" FORCE)
    endif()

    remove_definitions(-fvisibility=default)
    add_subdirectory(clDNN)
    add_definitions(-fvisibility=default)
endif()

if(ENABLE_MKL_DNN)
    include(mkldnn.cmake)
endif()

add_subdirectory("${IE_MAIN_SOURCE_DIR}/thirdparty/fluid/modules/gapi")
