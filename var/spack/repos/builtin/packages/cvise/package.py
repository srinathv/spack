# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install cvise
#
# You can edit this file again by typing:
#
#     spack edit cvise
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Cvise(CMakePackage):
    """C-Vise is a super-parallel Python port of the C-Reduce. The port is fully compatible to the C-Reduce and uses the same efficient LLVM-based C/C++ reduction tool named clang_delta.

"""

    homepage = "https://github.com/marxin/cvise"
    url = "https://github.com/marxin/cvise/archive/refs/tags/v2.6.0.tar.gz"
    git = "https://github.com/marxin/cvise"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ["marxin", "srinathv"]

    version("master", branch="master")
    version("2.6.0", sha256="770b88851901c8c7ce14c47809ba9989e99de35c564917cf2f686a7e48484b75")

    # FIXME: Add dependencies if required.
    depends_on("flex")
    depends_on("clang")
    depends_on("python")
    depends_on("py-pebble")
    depends_on("py-chardet")
    depends_on("py-psutil")
    depends_on("unidef")
    

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
