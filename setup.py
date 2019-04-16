"""
setup.py file for SWIG example
"""
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
import sys
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README')) as f:
    long_description = f.read()

## 
setup_dir = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
ext_incdir = os.path.join(here, "ext")

from distutils.core import *
from distutils      import sysconfig


modules= ["sample_a", ]

sources = {name: ["mfem_ext_sample/"+ name + "_wrap.cxx"] for name in modules}
proxy_names = {name: '_'+name for name in modules}
print(sources)
print(proxy_names)

import numpy
numpyincdir = numpy.get_include()

import mpi4py
mpi4pyincdir = mpi4py.get_include()

mpi_inc_dir = os.getenv("MPI_INC_DIR")
mfem_inc_dir = os.getenv("MFEM_INC_DIR")
mfem_inc_dir2 = os.path.join(os.getenv("MFEM_INC_DIR"), "mfem")
hypre_inc_dir = os.getenv("HYPRE_INC_DIR")
metis_inc_dir = os.getenv("METIS_INC_DIR")

include_dirs = [ext_incdir, mfem_inc_dir, mfem_inc_dir2, hypre_inc_dir, metis_inc_dir,
                numpyincdir, mpi4pyincdir, ]

lib_list = []
library_dirs = [os.getenv("PREFIX")+"/lib"]
libraries = ["sample_PyMFEM_ext"]
        
ext_modules = []
for kk, name in enumerate(modules):

   ext_modules.append(Extension(proxy_names[name],
                                sources=sources[name],
                                extra_compile_args = ['-DSWIG_TYPE_TABLE=PyMFEM_EXT','-std=c++11'],
                                include_dirs = include_dirs,
                                library_dirs = library_dirs,
                                libraries = libraries,
                                
                                language ='c++'))

setup (name = 'PyMFEM_ext_sample',
       url='https://github.com/piScope/PyMFEM_ext_sample',       
       version = '0.1',
       description = 'PyMFEM extension sample',
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
