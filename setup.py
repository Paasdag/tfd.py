from setuptools import setup, find_packages

setup(
    name='tfd-py',
    version='0.0.1',    
    description='Async Python library for TFD OpenAPI',
    url='https://github.com/Paasdag/tfd.py',
    author='Dean',
    author_email='',
    license='Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International',
    packages=find_packages(include=['tfd_py', 'tfd_py.*']),
    install_requires=[
        'asyncio',
        'aiohttp',
        'orjson',
    ],
)