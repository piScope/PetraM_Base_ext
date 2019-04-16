cmake_minimum_required(VERSION 3.1.0)

#  example cmake command
#  cmake .. -DCMAKE_INSTALL_NAME_DIR=${HOME}/sandbox/lib
#           -DCMAKE_INSTALL_PREFIX=${HOME}/sandbox
#	    -DMFEM_INC_DIR=${HOME}/sandbox/lib
#	    -DMFEM_LNK_DIR=${HOME}/sandbox/lib

project(sample_PyMFEM_ext)

find_package(MPI  REQUIRED)

set(FPIC " -fPIC ")
set(LINK_FLAGS ${FPIC})

#
#  USE C++11
#
set (CMAKE_CXX_STANDARD 11)
# Fix behavior of CMAKE_CXX_STANDARD when targeting macOS.
if (POLICY CMP0025)
  cmake_policy(SET CMP0025 NEW)
endif ()

if (APPLE)
    set(SHARED_SC_COMPILE_FLAGS " -fPIC ")
    set(CMAKE_BUILD_WITH_INSTALL_NAME_DIR true)  # this writes full path using install_name_dir  
else()
    set(SHARED_SC_COMPILE_FLAGS " -fPIC")
endif()

set( CMP_FLAG ${SHARED_SC_COMPILE_FLAGS})

### message(STATUS ${CMP_FLAG}) (THIS IS HOW TO WRITE DEBUG STATEMENT )

#
# make target
#
add_library(sample_PyMFEM_ext SHARED sample_PyMFEM_ext.cpp)
target_include_directories(sample_PyMFEM_ext PRIVATE ${MFEM_INC_DIR} ${HYPRE_INC_DIR} ${METIS_INC_DIR})
target_link_libraries(sample_PyMFEM_ext
			    -L${MFEM_LNK_DIR}
			    mfem)
			    
set_target_properties(sample_PyMFEM_ext PROPERTIES
                      COMPILE_FLAGS ${CMP_FLAG}
                      LINK_FLAGS ${LINK_FLAGS}
                      OUTPUT_NAME sample_PyMFEM_ext )
		      
install(TARGETS sample_PyMFEM_ext 
        DESTINATION ${CMAKE_INSTALL_PREFIX}/lib
        )
