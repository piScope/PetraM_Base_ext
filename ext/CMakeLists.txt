cmake_minimum_required(VERSION 3.1.0)

project(PetraM_Base_ext)

find_package(MPI  REQUIRED)

set(FPIC " -fPIC ")
set(LINK_FLAGS ${FPIC})
set(DEFAULT_INC ${PETRAM_PREFIX}/include)

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
add_library(PetraM_Base_ext SHARED fancy_coefficient.cpp)

if (MFEM_USE_PARALLEL)
    target_include_directories(PetraM_Base_ext PRIVATE ${DEFAULT_INC}  ${MFEM_INC_DIR} ${HYPRE_INC_DIR} ${METIS_INC_DIR})
else()
    target_include_directories(PetraM_Base_ext PRIVATE ${DEFAULT_INC} ${MFEM_INC_DIR})
endif()

target_link_libraries(PetraM_Base_ext
			    -L${MFEM_LNK_DIR}
			    mfem)
			    
set_target_properties(PetraM_Base_ext PROPERTIES
                      COMPILE_FLAGS ${CMP_FLAG}
                      LINK_FLAGS ${LINK_FLAGS}
                      OUTPUT_NAME petram_base )
		      
install(TARGETS PetraM_Base_ext
        DESTINATION ${CMAKE_INSTALL_PREFIX}/lib
        )
