# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class PyAzuremlTrain(Package):
    """The azureml-train package provides estimators for training models using
    different deep learning frameworks and functionality for hyperparameter
    tuning using Azure cloud."""

    homepage = "https://docs.microsoft.com/en-us/azure/machine-learning/service/"
    url      = "https://pypi.io/packages/py3/a/azureml_train/azureml_train-1.8.0-py3-none-any.whl"

    version('1.8.0', sha256='124e5b7d8d64bac61db022f305bd31c25e57fdcb4be93eefd4244a04a13deab3', expand=False)

    extends('python')
    depends_on('python@3.5:3.999', type=('build', 'run'))
    depends_on('py-pip', type='build')
    depends_on('py-azureml-train-core@1.8.0:1.8.999', type=('build', 'run'))

    def install(self, spec, prefix):
        pip = which('pip')
        pip('install', self.stage.archive_file, '--prefix={0}'.format(prefix))
