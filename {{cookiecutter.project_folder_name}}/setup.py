from setuptools import setup, find_packages
from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip

pfile = Project(chdir=False).parsed_pipfile
requirements = convert_deps_to_pip(pfile['packages'], r=False)
test_requirements = convert_deps_to_pip(pfile['dev-packages'], r=False)

print(requirements)

setup(
    name="{{cookiecutter.project_folder_name}}",
    version="{{cookiecutter.package_version}}",
    packages=find_packages(exclude=['tests']),
    install_requires=requirements,
    tests_require=test_requirements
)
