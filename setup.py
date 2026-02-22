from setuptools import setup, find_packages
setup(
    name='citibike_etl',
    version='0.0.1',
    description='A simple ETL pipeline for Citibike data',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'setuptools'
    ],
)