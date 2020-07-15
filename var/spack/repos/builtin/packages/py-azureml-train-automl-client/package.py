# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class PyAzuremlTrainAutomlClient(Package):
    """The azureml-train-automl-client package contains functionality for
    automatically finding the best machine learning model and its parameters,
    given training and test data."""

    homepage = "https://docs.microsoft.com/en-us/azure/machine-learning/service/"
    url      = "https://pypi.io/packages/py3/a/azureml_train_automl_client/azureml_train_automl_client-1.8.0-py3-none-any.whl"

    version('1.8.0', sha256='562300095db6c4dea7b052e255c53dd95c4c3d0589a828b545497fe1ca7e9677', expand=False)

    extends('python')
    depends_on('python@3.5:3.999', type=('build', 'run'))
    depends_on('py-pip', type='build')
    depends_on('py-azureml-dataprep@1.8.0:1.8.999', type=('build', 'run'))
    depends_on('py-azureml-automl-core@1.8.0:1.8.999', type=('build', 'run'))
    depends_on('py-azureml-core@1.8.0:1.8.999', type=('build', 'run'))
    depends_on('py-azureml-telemetry@1.8.0:1.8.999', type=('build', 'run'))

    def install(self, spec, prefix):
        pip = which('pip')
        pip('install', self.stage.archive_file, '--prefix={0}'.format(prefix))
