IFILE = $(wildcard *.i)
ALLCXX = $(IFILE:.i=_wrap.cxx)
SWIGFLAG = -Wall -c++ -python

# uncomment if you want to do always make clean + make all
#.PHONY: all clean
.PHONEY:clean cxx allso install

defaut: so
all: so

cxx: $(ALLCXX)
so:
	CC=${MPICC} CFLAGS=${CXXFLAGS} $(PYTHON) setup.py build_ext --inplace

%_wrap.cxx: %.i
	echo "Processing" $<
	$(SWIG) $(SWIGFLAG) -I$(PYMFEM_SRC)/mfem/par -I$(MFEM_PAR_INC)/mfem -I$(MPI4PYINCDIR)  $<

clean:
	rm -f *.cxx
	rm -r -f build
	rm -f *.so
