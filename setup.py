# Here i will generate my code for generating the .egg file for logs
'''
This setup.py file really important because for any project that you probably develop you really need to have this setup.py because it is an essential part of packaging and distributing python projects. it is used by setup tools to define the configuration of a project such as this metadata, dependency and more.
'''
from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    try:
        with open(file_path) as file_obj:
            requirements=file_obj.readlines()
            requirements=[req.replace("\n","") for req in requirements]
            
            if "-e ." in requirements:
                requirements.remove("-e .")
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirements

setup(
    name="network_security_project",
    version="0.0.1",
    author="Mayank Meghwal",
    author_email="mayankmeg207@gmail.com",
    description="A project for network security using machine learning",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)