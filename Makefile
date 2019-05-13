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
MPICC ?= $(shell which mpicc)
MPICXX ?= $(shell which mpicxx)
CC ?= $(shell cc)
CXX ?= $(shell c++)

CXXFLAGS ?= -std=gnu++11 

#
# location of lib/include
#
PREFIX ?= /usr/local/lib
PETRAM ?= ${PetraM}

# MFEM lib/include directory
MFEM_BASE ?= ${PREFIX}/mfem-git
MFEM_SER_INC = ${MFEM_BASE}/ser/include
MFEM_PAR_INC = ${MFEM_BASE}/par/include

# PyMFEM
PYMFEM_SRC ?= ${PREFIX}/src/PyMFEM

# HYPRE/Metis include
# There are needed for mfem.hpp
HYPRE_INC_DIR ?= ${PREFIX}/include
METIS_INC_DIR ?= ${PREFIX}/include

# the location of mpi4py.i (asking Python for the location usually works)
MPI4PYINCDIR = $(shell $(PYTHON) -c "import mpi4py;print mpi4py.get_include()")

UNAME := $(shell uname)
SUBDIRS = ext
export 


default: build_ext install_ext build_so build_py install_py
all: clean build_ext install_ext cxx build_so build_py install_py

.PHONEY: all install build_ext install_ext parcxx sercxx cxx so build_so

##
build_ext:
	mkdir -p $(PREFIX)
	mkdir -p ext/cmbuild_par
	mkdir -p ext/cmbuild_ser
	cd ext/cmbuild_ser; $(CMAKE) .. -DCMAKE_INSTALL_NAME_DIR=${MFEM_BASE}/ser/lib \
                                      -DCMAKE_INSTALL_PREFIX=${MFEM_BASE}/ser   \
                                      -DMFEM_INC_DIR=${MFEM_SER_INC}            \
                                      -DMFEM_LNK_DIR=${MFEM_BASE}/ser/lib       \
                                      -DCMAKE_C_COMPILER=${CC}                  \
                                      -DCMAKE_CXX_COMPILER=${CXX}               \
                                      -DPETRAM_PREFIX=${PREFIX};                \
        $(MAKE) VERBOSE=1             
	cd ext/cmbuild_par; $(CMAKE) .. -DCMAKE_INSTALL_NAME_DIR=${MFEM_BASE}/par/lib \
                                      -DCMAKE_INSTALL_PREFIX=${MFEM_BASE}/par   \
                                      -DMFEM_INC_DIR=${MFEM_PAR_INC}            \
                                      -DMFEM_LNK_DIR=${MFEM_BASE}/par/lib       \
				      -DMFEM_USE_PARALLEL=1                     \
                                      -DMETIS_INCDIR=${METIS_INC_DIR}           \
                                      -DHYPRE_INC_DIR=${HYPRE_INC_DIR}          \
                                      -DCMAKE_C_COMPILER=${MPICC}               \
                                      -DCMAKE_CXX_COMPILER=${MPICXX}            \
                                      -DPETRAM_PREFIX=${PREFIX};                \
        $(MAKE) VERBOSE=1

install_ext:
	cd ext/cmbuild_ser;$(MAKE) install
	cd ext/cmbuild_par;$(MAKE) install

parcxx:
	$(MAKE) -C petram/ext/_base/_par cxx MFEM_PAR_INC=${MFEM_PAR_INC} \
                                                 PYMFEM_SRC=${PYMFEM_SRC}

sercxx:
	$(MAKE) -C petram/ext/_base/_ser cxx MFEM_SER_INC=${MFEM_SER_INC} \
                                                 PYMFEM_SRC=${PYMFEM_SRC}

cxx:parcxx sercxx

parso: 
	$(MAKE) -C petram/ext/_base/_par so MFEM_PAR_INC=${MFEM_PAR_INC}

serso:
	$(MAKE) -C petram/ext/_base/_ser so MFEM_SER_INC=${MFEM_SER_INC}

so:parso serso
build_so:parso serso

build_py:
	$(PYTHON) setup.py build

install_py:
	$(PYTHON) setup.py install --prefix=$(PETRAM)


#	
#_ext --inplace
#	$(MAKE) -C mfem_ext_sample so

clean_ext:
	rm -rf ext/cmbuild_par
	rm -rf ext/cmbuild_ser
clean_so:
	$(MAKE) -C  petram/ext/_base/_ser clean
	$(MAKE) -C  petram/ext/_base/_par clean
clean_build:
	rm -rf build/*
clean:clean_ext clean_so clean_build


