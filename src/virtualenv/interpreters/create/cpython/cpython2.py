from __future__ import absolute_import, unicode_literals

import abc

import six

from virtualenv.interpreters.create.via_global_ref.python2 import Python2

from .common import CPython, CPythonPosix, CPythonWindows


@six.add_metaclass(abc.ABCMeta)
class CPython2(CPython, Python2):
    """Create a CPython version 2  virtual environment"""

    def modules(self):
        return ["os"]  # add landmarks for detecting the python home


class CPython2Posix(CPython2, CPythonPosix):
    """CPython 2 on POSIX"""

    def fixup_python2(self):
        super(CPython2Posix, self).fixup_python2()
        # linux needs the lib-dynload, these are builtins on Windows
        self.add_folder("lib-dynload")


class CPython2Windows(CPython2, CPythonWindows):
    """CPython 2 on Windows"""