# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class PyAzuremlTrainRestclientsHyperdrive(Package):
    """The azureml-train-restclients-hyperdrive contains functionality for
    azureml-train metapackage."""

    homepage = "https://docs.microsoft.com/en-us/azure/machine-learning/service/"
    url      = "https://pypi.io/packages/py3/a/azureml_train_restclients_hyperdrive/azureml_train_restclients_hyperdrive-1.8.0-py3-none-any.whl"

    version('1.8.0', sha256='1633c7eb0fd96714f54f72072ccf1c5ee1ef0a8ba52680793f20d27e0fd43c87', expand=False)

    extends('python')
    depends_on('python@3.5:3.999', type=('build', 'run'))
    depends_on('py-pip', type='build')
    depends_on('py-requests@2.19.1:', type=('build', 'run'))
    depends_on('py-msrest@0.5.1:', type=('build', 'run'))
    depends_on('py-msrestazure@0.4.33:', type=('build', 'run'))

    def install(self, spec, prefix):
        pip = which('pip')
        pip('install', self.stage.archive_file, '--prefix={0}'.format(prefix))
