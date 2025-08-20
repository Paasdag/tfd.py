from setuptools import setup, find_packages

with open("readme.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setup(
    name='tfd-py',
    version='0.1',    
    description='Async Python library for TFD OpenAPI',
    url='https://github.com/Paasdag/tfd.py',
    author='Dean',
    license='Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International',
    packages=find_packages(include=['tfd_py', 'tfd_py.*']),
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.10",
    install_requires=[
        'asyncio',
        'aiohttp',
        'orjson',
    ],
)