%module fancy_coefficient
%{
#include "mfem.hpp"
#include "numpy/arrayobject.h"
#include "pycoefficient.hpp"
#include "../../../../ext/fancy_coefficient.hpp"
%}

%init %{
import_array();
%}

%import "coefficient.i"

%include "../../../../ext/fancy_coefficient.hpp"

