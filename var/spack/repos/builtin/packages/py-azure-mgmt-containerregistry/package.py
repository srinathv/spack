# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class PyAzureMgmtContainerregistry(PythonPackage):
    """Microsoft Azure Container Registry Client Library for Python."""

    homepage = "https://github.com/Azure/azure-sdk-for-python"
    url      = "https://pypi.io/packages/source/a/azure-mgmt-containerregistry/azure-mgmt-containerregistry-2.8.0.zip"

    version('2.8.0', sha256='b24be1050d54f3158e8be7f6ad677f0c8888dddefd09fb8391ebfc73d40173a4')

    depends_on('py-setuptools', type='build')
    depends_on('py-msrest@0.5.0:', type=('build', 'run'))
    depends_on('py-msrestazure@0.4.32:1.999', type=('build', 'run'))
    depends_on('py-azure-common@1.1:1.999', type=('build', 'run'))
    depends_on('py-azure-mgmt-nspkg', when='^python@:2', type=('build', 'run'))
