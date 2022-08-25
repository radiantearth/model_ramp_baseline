import os
from setuptools import setup


def readme() -> str:
    """Utility function to read the README.md.

    Used for the `long_description`. It's nice, because now
    1) we have a top level README file and
    2) it's easier to type in the README file than to put a raw string in below.

    Args:
        nothing

    Returns:
        String of README.md file.
    """
    return open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='ramp',
    version='0.1.0',
    author='Carolyn Johnston',
    author_email='carolyn.johnston@dev.global',
    description='Replicable AI for Microplanning',
    python_requires='>=3',
    license='',
    url='',
    packages=[
        'ramp',
        'ramp.data_mgmt',
        'ramp.training',
        'ramp.utils',
    ],
    package_dir={"":"."},
    long_description=readme(),
    long_description_content_type="text/markdown",
    install_requires=[
        'gdal>=3.0.2',
        'geopandas==0.10.2',
        'rasterio==1.2.10',
        'scikit-fmm==2022.08.15',
        'tqdm==4.62.3',
    ]
)
