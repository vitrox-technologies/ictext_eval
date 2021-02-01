from setuptools import setup, Extension
import numpy as np

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

ext_modules = [
    Extension(
        'pycocotools._mask',
        sources=['maskApi.c', '_mask.pyx'],
        include_dirs = [np.get_include(), '../common'],
        extra_compile_args=['-Wno-cpp', '-Wno-unused-function', '-std=c99'],
        # extra_compile_args={'gcc': ['/Qstd=c99']},
    )
]

setup(
    name='pycocotools',
    packages=['pycocotools'],
    package_dir = {'pycocotools': ''},
    install_requires=[
        'setuptools>=18.0',
        'cython>=0.27.3',
        'matplotlib>=2.1.0',
        'scikit-learn>=0.24.0'
    ],
    version='2.0',
    ext_modules= ext_modules
)
