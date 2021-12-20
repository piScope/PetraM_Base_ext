%module(package="petram.ext._base._par") fancy_coefficient
%{
#include "mfem.hpp"
#include "numpy/arrayobject.h"
#include "../common/pycoefficient.hpp"  
#include "../../../../ext/fancy_coefficient.hpp"
%}

%init %{
import_array();
%}

%import "coefficient.i"
%import "gridfunc.i"
%import "pgridfunc.i"

%include "../../../../ext/fancy_coefficient.hpp"

