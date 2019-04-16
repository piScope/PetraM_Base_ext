##   Makefile
##
##   default variable setting
##

#
# exectuables
#
MAKE ?= $(shell which make)
CMAKE ?= $(shell which cmake)
PYTHON ?= $(shell which python)
SWIG ?= $(shell which swig)
PYTHONCONFIG ?= $(shell which python-config)

# compileres
CC ?= $(shell which mpicc)
CXX ?= $(shell which mpicxx)
CXXFLAGS ?= -std=gnu++11 

#
# location of lib/include
#
PREFIX ?= /usr/local/lib

# MFEM lib/include directory
MFEM_LNK_DIR ?= ${PREFIX}/lib
MFEM_INC_DIR ?= ${PREFIX}/include

# HYPRE/Metis include
# There are needed for mfem.hpp
HYPRE_INC_DIR ?= ${PREFIX}/include
METIS_INC_DIR ?= ${PREFIX}/include

# the location of mpi4py.i (asking Python for the location usually works)
MPI4PYINCDIR = $(shell $(PYTHON) -c "import mpi4py;print mpi4py.get_include()")

UNAME := $(shell uname)
SUBDIRS = ext
export 

default: so
.PHONEY: all install extension cxx so

##
extension:
	mkdir -p $(PREFIX)
	mkdir -p build_ext
	cd build_ext; $(CMAKE) ../ext -DCMAKE_INSTALL_NAME_DIR=${PREFIX}/lib  \
                                      -DCMAKE_INSTALL_PREFIX=${PREFIX}        \
                                      -DMFEM_INC_DIR=${MFEM_INC_DIR}          \
                                      -DMFEM_LNK_DIR=${MFEM_LNK_DIR}          \
                                      -DMETIS_INCDIR=${METIS_INC_DIR}          \
                                      -DHYPRE_INC_DIR=${HYPRE_INC_DIR}          \
                                      -DCMAKE_C_COMPILER=${CC}               \
                                      -DCMAKE_CXX_COMPILER=${CXX}; \
        $(MAKE) VERBOSE=1; \
        $(MAKE) install

cxx:
	$(MAKE) -C mfem_ext_sample cxx

so:
	$(PYTHON) setup.py build
#_ext --inplace
#	$(MAKE) -C mfem_ext_sample so

install:
	$(PYTHON) setup.py install --prefix=$(PREFIX)

clean:
	rm -rf build_ext
	$(MAKE) -C mfem_ext_sample clean
	rm -rf build/*

