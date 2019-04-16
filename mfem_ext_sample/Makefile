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
	$(PYTHON) setup.py build_ext --inplace
%_wrap.cxx: %.i
	$(SWIG) $(SWIGFLAG) -I$(MFEM_INC_DIR) -I$(MFEM_INC_DIR)/mfem -I$(MPI4PYINCDIR)  $<

clean:
	rm -f *.cxx
	rm -r -f build
	rm -f *.so
