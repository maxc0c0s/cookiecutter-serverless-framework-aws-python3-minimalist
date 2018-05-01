from setuptools import setup, find_packages
setup(
    name="{{cookiecutter.package_name}}",
    version="{{cookiecutter.package_version}}",
    packages=find_packages(exclude=['tests']),
)
