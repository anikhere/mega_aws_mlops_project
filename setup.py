from setuptools import find_packages,setup
import os
HYPHEN_E_DOT = '-e .'
def get_requirements(path:str)-> list[str]:
    with open(path,'r') as files:
        reqs = [ req.strip() for req in files if req.strip() and req.strip() != HYPHEN_E_DOT]
    return reqs


setup(
    name = 'aws_mega_project',
    version = '0.0.1',
    author='taha_anik',
    author_email='tahaanik729@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)