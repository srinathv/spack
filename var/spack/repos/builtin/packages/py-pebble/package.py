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
#     spack install py-pebble
#
# You can edit this file again by typing:
#
#     spack edit py-pebble
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyPebble(Package):
    """Pebble provides a neat API to manage threads and processes within an application."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://pebble.readthedocs.io/"
    url = "https://github.com/noxdafox/pebble/releases/tag/5.0.3"
    pypi = "https://pypi.org/project/Pebble/"

    maintainers = ["noxdafox", "srinathv"]

    version("master", branch="master")
    version("5.0.3", sha256="bf79c021046dd28ca35e425482f14d714c266033602b1be1b46d6d6bb3a6bfd5")

    depends_on("py-setuptools", type="build")
   