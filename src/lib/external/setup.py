import numpy
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import platform


if platform.system() == 'Linux':
    extensions = [
        Extension(
            "nms",
            ["nms.pyx"],
            extra_compile_args=["-Wno-cpp", "-Wno-unused-function"]
        )
    ]
else:
    extensions = [
        Extension(
            "nms",
            ["nms.pyx"]
        )
    ]

setup(
    name="coco",
    ext_modules=cythonize(extensions),
    include_dirs=[numpy.get_include()]
)
