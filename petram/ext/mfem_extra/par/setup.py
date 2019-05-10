
"""
setup.py file for SWIG example
"""
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
import sys
import os

here = os.path.abspath(os.path.dirname(__file__))

###

with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()
modules = [f[:-2] for f in os.listdir(here) if f.endswith(".i")]

### base_dir = package base directory

base_dir = os.path.abspath(os.path.realpath(__file__))
for i in range(5):
    base_dir = os.path.dirname(base_dir)

###

ext_incdir = os.path.join(base_dir, "ext")

from distutils.core import *
from distutils      import sysconfig

sources = {name: [os.path.join(here ,name + "_wrap.cxx")] for name in modules}
proxy_names = {name: '_'+name for name in modules}

import numpy
numpyincdir = numpy.get_include()

import mpi4py
mpi4pyincdir = mpi4py.get_include()

prefix_incdir = os.path.join(os.getenv("PREFIX"), "include")
mfem_incdir = os.getenv("MFEM_PAR_INC")
mfem_incdir2 = os.path.join(os.getenv("MFEM_PAR_INC"), "mfem")
hypre_incdir = os.getenv("HYPRE_INC_DIR")
metis_incdir = os.getenv("METIS_INC_DIR")
pymfem_incdir = os.path.join(os.getenv("PYMFEM_SRC"), 'mfem', '_par')

include_dirs = [ext_incdir, prefix_incdir,  hypre_incdir, metis_incdir,
                mfem_incdir, mfem_incdir2,
                numpyincdir, mpi4pyincdir, pymfem_incdir]

#lib_list = ["pord", "parmetis", "metis5", "scalapack",  "blas"]
lib_list = []
library_dirs = [os.path.join(os.getenv("MFEM_BASE"), "par", "lib")]
libraries = ["petram_base"]
        
ext_modules = []
for kk, name in enumerate(modules):

   ext_modules.append(Extension(proxy_names[name],
                        sources=sources[name],
                        extra_compile_args = ['-DSWIG_TYPE_TABLE=PyMFEM_EXT'],   
                        include_dirs = include_dirs,
                        library_dirs = library_dirs,
                        libraries = libraries ))

setup (name = 'PetraM_Base_ext',
       url='https://github.com/piScope/PetraM_Base_ext',
       version = '0.1',
       description = 'Extension module for PetraM',
       long_description=long_description,       
       author      = "S. Shiraiwa",
       author_email='shiraiwa@psfc.mit.edu',
       license='LGPL v2.1',
       classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Physics',
        'Programming Language :: Python :: 2.7',
       ],

       keywords='MFEM physics',
       packages=find_packages(),
       ext_modules = ext_modules,
)
