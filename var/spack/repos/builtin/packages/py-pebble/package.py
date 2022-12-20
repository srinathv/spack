# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPebble(PythonPackage):
    """Pebble provides a neat API to manage threads and 
    processes within an application."""

    pypi = "pebble/pebble-5.0.3.zip"
    maintainers = ["noxdafox", "srinathv"]

    version("5.0.3", sha256="c85b91ab752900c9a857a7ecd8981a5efa41918e50a4b52c20e69964b3d3dac3")

    depends_on("py-setuptools", type="build")
   