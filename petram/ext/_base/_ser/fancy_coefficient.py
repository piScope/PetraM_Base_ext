# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _fancy_coefficient
else:
    import _fancy_coefficient

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

import mfem._ser.coefficient
import mfem._ser.array
import mfem._ser.mem_manager
import mfem._ser.matrix
import mfem._ser.vector
import mfem._ser.operators
import mfem._ser.intrules
import mfem._ser.sparsemat
import mfem._ser.densemat
import mfem._ser.eltrans
import mfem._ser.fe
import mfem._ser.geom
import mfem._ser.gridfunc
import mfem._ser.mesh
import mfem._ser.ncmesh
import mfem._ser.element
import mfem._ser.table
import mfem._ser.hash
import mfem._ser.vertex
import mfem._ser.fespace
import mfem._ser.fe_coll
import mfem._ser.lininteg
import mfem._ser.handle
import mfem._ser.bilininteg
import mfem._ser.linearform
class PiecewiseLinearMaterialProperty(mfem._ser.coefficient.Coefficient):
    r"""Proxy of C++ PetraM_Base_extra::PiecewiseLinearMaterialProperty class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(PiecewiseLinearMaterialProperty self, Coefficient _cf, Vector x, Vector y) -> PiecewiseLinearMaterialProperty
        __init__(PiecewiseLinearMaterialProperty self, GridFunction _gf, Vector x, Vector y, int comp=1) -> PiecewiseLinearMaterialProperty
        """
        _fancy_coefficient.PiecewiseLinearMaterialProperty_swiginit(self, _fancy_coefficient.new_PiecewiseLinearMaterialProperty(*args))

    def SetRangeCheck(self, f):
        r"""SetRangeCheck(PiecewiseLinearMaterialProperty self, int f)"""
        return _fancy_coefficient.PiecewiseLinearMaterialProperty_SetRangeCheck(self, f)

    def Eval(self, T, ip):
        r"""Eval(PiecewiseLinearMaterialProperty self, ElementTransformation T, IntegrationPoint ip) -> double"""
        return _fancy_coefficient.PiecewiseLinearMaterialProperty_Eval(self, T, ip)
    __swig_destroy__ = _fancy_coefficient.delete_PiecewiseLinearMaterialProperty

# Register PiecewiseLinearMaterialProperty in _fancy_coefficient:
_fancy_coefficient.PiecewiseLinearMaterialProperty_swigregister(PiecewiseLinearMaterialProperty)

class Poly1DMaterialProperty(mfem._ser.coefficient.Coefficient):
    r"""Proxy of C++ PetraM_Base_extra::Poly1DMaterialProperty class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(Poly1DMaterialProperty self, Coefficient _cf, Vector coeff, double _max_range=std::numeric_limits< double >::infinity(), double _min_range=-std::numeric_limits< double >::infinity()) -> Poly1DMaterialProperty
        __init__(Poly1DMaterialProperty self, GridFunction _gf, Vector coeff, int comp=1, double _max_range=std::numeric_limits< double >::infinity(), double _min_range=-std::numeric_limits< double >::infinity()) -> Poly1DMaterialProperty
        """
        _fancy_coefficient.Poly1DMaterialProperty_swiginit(self, _fancy_coefficient.new_Poly1DMaterialProperty(*args))

    def Eval(self, T, ip):
        r"""Eval(Poly1DMaterialProperty self, ElementTransformation T, IntegrationPoint ip) -> double"""
        return _fancy_coefficient.Poly1DMaterialProperty_Eval(self, T, ip)
    __swig_destroy__ = _fancy_coefficient.delete_Poly1DMaterialProperty

# Register Poly1DMaterialProperty in _fancy_coefficient:
_fancy_coefficient.Poly1DMaterialProperty_swigregister(Poly1DMaterialProperty)

class UniaxialConstantMaterialProperty(mfem._ser.coefficient.MatrixCoefficient):
    r"""Proxy of C++ PetraM_Base_extra::UniaxialConstantMaterialProperty class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(UniaxialConstantMaterialProperty self, Coefficient _cf, DenseMatrix m) -> UniaxialConstantMaterialProperty
        __init__(UniaxialConstantMaterialProperty self, GridFunction _gf, DenseMatrix m, int comp=1) -> UniaxialConstantMaterialProperty
        """
        _fancy_coefficient.UniaxialConstantMaterialProperty_swiginit(self, _fancy_coefficient.new_UniaxialConstantMaterialProperty(*args))

    def Eval(self, K, T, ip):
        r"""Eval(UniaxialConstantMaterialProperty self, DenseMatrix K, ElementTransformation T, IntegrationPoint ip)"""
        return _fancy_coefficient.UniaxialConstantMaterialProperty_Eval(self, K, T, ip)
    __swig_destroy__ = _fancy_coefficient.delete_UniaxialConstantMaterialProperty

# Register UniaxialConstantMaterialProperty in _fancy_coefficient:
_fancy_coefficient.UniaxialConstantMaterialProperty_swigregister(UniaxialConstantMaterialProperty)



