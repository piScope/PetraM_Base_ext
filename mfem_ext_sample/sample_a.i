%module sample_a
%{
#include "mfem.hpp"
#include "numpy/arrayobject.h"
#include "../ext/sample_pymfem_ext.hpp"
%}

%init %{
import_array();
%}

%include "../ext/sample_pymfem_ext.hpp"

