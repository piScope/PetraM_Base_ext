"""

  Petra-M setuptools based setup module.

"""
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path, listdir
import re

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README')) as f:
    long_description = f.read()
    
setup(
    name='PetraM_Base_ext',
    version='1.2',
    description='PetraM_Base_ext',
    long_description=long_description,
    url='https://github.com/piScope/PetraM_Base_ext',
    author='S. Sihraiwa',
    author_email='shiraiwa@psfc.mit.edu',
    license='LGPL-2.1',

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Physics'
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='MFEM physics',
    packages=find_packages(),
    install_requires=[],
    extras_require={},
    package_data={'petram.ext._base._par':['*.so'], 'petram.ext._base._ser':['*.so']},
    entry_points={},
)
