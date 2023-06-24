from setuptools import setup, find_packages
#requeriments form requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="src",
    version="0.1",
    packages= find_packages(),
    install_requires=required
)