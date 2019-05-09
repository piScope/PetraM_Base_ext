# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_fancy_coefficient')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_fancy_coefficient')
    _fancy_coefficient = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_fancy_coefficient', [dirname(__file__)])
        except ImportError:
            import _fancy_coefficient
            return _fancy_coefficient
        try:
            _mod = imp.load_module('_fancy_coefficient', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _fancy_coefficient = swig_import_helper()
    del swig_import_helper
else:
    import _fancy_coefficient
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

try:
    import weakref
    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


import mfem.par.coefficient
import mfem.par.array
import mfem.par.ostream_typemap
import mfem.par.matrix
import mfem.par.vector
import mfem.par.operators
import mfem.par.intrules
import mfem.par.sparsemat
import mfem.par.densemat
import mfem.par.eltrans
import mfem.par.fe
class Scalar_PiecewiseLinear_MaterialProperty(mfem.par.coefficient.Coefficient):
    """Proxy of C++ PetraM_Base_extra::Scalar_PiecewiseLinear_MaterialProperty class."""

    __swig_setmethods__ = {}
    for _s in [mfem.par.coefficient.Coefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Scalar_PiecewiseLinear_MaterialProperty, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem.par.coefficient.Coefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Scalar_PiecewiseLinear_MaterialProperty, name)
    __repr__ = _swig_repr

    def __init__(self, _gf, _x, _y):
        """__init__(PetraM_Base_extra::Scalar_PiecewiseLinear_MaterialProperty self, mfem::GridFunction * _gf, Vector _x, Vector _y) -> Scalar_PiecewiseLinear_MaterialProperty"""
        this = _fancy_coefficient.new_Scalar_PiecewiseLinear_MaterialProperty(_gf, _x, _y)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetGridFunction(self, gf):
        """SetGridFunction(Scalar_PiecewiseLinear_MaterialProperty self, mfem::GridFunction * gf)"""
        return _fancy_coefficient.Scalar_PiecewiseLinear_MaterialProperty_SetGridFunction(self, gf)


    def GetGridFunction(self):
        """GetGridFunction(Scalar_PiecewiseLinear_MaterialProperty self) -> mfem::GridFunction *"""
        return _fancy_coefficient.Scalar_PiecewiseLinear_MaterialProperty_GetGridFunction(self)


    def Eval(self, T, ip):
        """Eval(Scalar_PiecewiseLinear_MaterialProperty self, ElementTransformation T, IntegrationPoint ip) -> double"""
        return _fancy_coefficient.Scalar_PiecewiseLinear_MaterialProperty_Eval(self, T, ip)

    __swig_destroy__ = _fancy_coefficient.delete_Scalar_PiecewiseLinear_MaterialProperty
    __del__ = lambda self: None
Scalar_PiecewiseLinear_MaterialProperty_swigregister = _fancy_coefficient.Scalar_PiecewiseLinear_MaterialProperty_swigregister
Scalar_PiecewiseLinear_MaterialProperty_swigregister(Scalar_PiecewiseLinear_MaterialProperty)

class Scalar_Poly1D_MaterialProperty(mfem.par.coefficient.Coefficient):
    """Proxy of C++ PetraM_Base_extra::Scalar_Poly1D_MaterialProperty class."""

    __swig_setmethods__ = {}
    for _s in [mfem.par.coefficient.Coefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Scalar_Poly1D_MaterialProperty, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem.par.coefficient.Coefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Scalar_Poly1D_MaterialProperty, name)
    __repr__ = _swig_repr

    def __init__(self, _gf, _coeff):
        """__init__(PetraM_Base_extra::Scalar_Poly1D_MaterialProperty self, mfem::GridFunction * _gf, Vector _coeff) -> Scalar_Poly1D_MaterialProperty"""
        this = _fancy_coefficient.new_Scalar_Poly1D_MaterialProperty(_gf, _coeff)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetGridFunction(self, gf):
        """SetGridFunction(Scalar_Poly1D_MaterialProperty self, mfem::GridFunction * gf)"""
        return _fancy_coefficient.Scalar_Poly1D_MaterialProperty_SetGridFunction(self, gf)


    def GetGridFunction(self):
        """GetGridFunction(Scalar_Poly1D_MaterialProperty self) -> mfem::GridFunction *"""
        return _fancy_coefficient.Scalar_Poly1D_MaterialProperty_GetGridFunction(self)


    def Eval(self, T, ip):
        """Eval(Scalar_Poly1D_MaterialProperty self, ElementTransformation T, IntegrationPoint ip) -> double"""
        return _fancy_coefficient.Scalar_Poly1D_MaterialProperty_Eval(self, T, ip)

    __swig_destroy__ = _fancy_coefficient.delete_Scalar_Poly1D_MaterialProperty
    __del__ = lambda self: None
Scalar_Poly1D_MaterialProperty_swigregister = _fancy_coefficient.Scalar_Poly1D_MaterialProperty_swigregister
Scalar_Poly1D_MaterialProperty_swigregister(Scalar_Poly1D_MaterialProperty)

class Uniaxial_constant_MaterialProperty(mfem.par.coefficient.MatrixCoefficient):
    """Proxy of C++ PetraM_Base_extra::Uniaxial_constant_MaterialProperty class."""

    __swig_setmethods__ = {}
    for _s in [mfem.par.coefficient.MatrixCoefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Uniaxial_constant_MaterialProperty, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem.par.coefficient.MatrixCoefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Uniaxial_constant_MaterialProperty, name)
    __repr__ = _swig_repr

    def __init__(self, _gf, m):
        """__init__(PetraM_Base_extra::Uniaxial_constant_MaterialProperty self, mfem::GridFunction * _gf, DenseMatrix m) -> Uniaxial_constant_MaterialProperty"""
        this = _fancy_coefficient.new_Uniaxial_constant_MaterialProperty(_gf, m)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetGridFunction(self, gf):
        """SetGridFunction(Uniaxial_constant_MaterialProperty self, mfem::GridFunction * gf)"""
        return _fancy_coefficient.Uniaxial_constant_MaterialProperty_SetGridFunction(self, gf)


    def GetGridFunction(self):
        """GetGridFunction(Uniaxial_constant_MaterialProperty self) -> mfem::GridFunction *"""
        return _fancy_coefficient.Uniaxial_constant_MaterialProperty_GetGridFunction(self)


    def Eval(self, K, T, ip):
        """Eval(Uniaxial_constant_MaterialProperty self, DenseMatrix K, ElementTransformation T, IntegrationPoint ip)"""
        return _fancy_coefficient.Uniaxial_constant_MaterialProperty_Eval(self, K, T, ip)

    __swig_destroy__ = _fancy_coefficient.delete_Uniaxial_constant_MaterialProperty
    __del__ = lambda self: None
Uniaxial_constant_MaterialProperty_swigregister = _fancy_coefficient.Uniaxial_constant_MaterialProperty_swigregister
Uniaxial_constant_MaterialProperty_swigregister(Uniaxial_constant_MaterialProperty)

# This file is compatible with both classic and new-style classes.


