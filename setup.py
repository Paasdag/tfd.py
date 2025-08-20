from setuptools import setup, find_packages

setup(
    name='tfd-py',
    version='0.1',    
    description='Async Python library for TFD OpenAPI',
    url='https://github.com/Paasdag/tfd.py',
    author='Dean',
    license='Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International',
    packages=find_packages(include=['tfd_py', 'tfd_py.*']),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.10",
    install_requires=[
        'asyncio',
        'aiohttp',
        'orjson',
    ],
)