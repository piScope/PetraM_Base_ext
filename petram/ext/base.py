from mfem import mfem_mode
if mfem_mode == 'serial':
    import petram.ext._base._ser.fancy_coefficient as fancy_coefficient
    from petram.ext._base._ser.fancy_coefficient import *    
elif mfem_mode == 'parallel':
    import petram.ext._base._par.fancy_coefficient as fancy_coefficient
    from petram.ext._base._par.fancy_coefficient import *
else:
    assert False, "PyMFEM is not loaded (use import mfem.ser or import mfem.par)"
        
