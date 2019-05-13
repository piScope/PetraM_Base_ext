%module(package="petram.ext._base._ser") fancy_coefficient
%{
#include "mfem.hpp"
#include "numpy/arrayobject.h"
#include "pycoefficient.hpp"
#include "../../../../ext/fancy_coefficient.hpp"
%}

%init %{
import_array();
%}
%include "exception.i"
%import "coefficient.i"
%import "gridfunc.i"

%include "../../../../ext/fancy_coefficient.hpp"

