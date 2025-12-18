from typing import List
from setuptools import setup,find_packages

HIPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """This function will return the list of requirements"""
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
        if HIPEN_E_DOT in requirements:
            requirements.remove(HIPEN_E_DOT)
    return requirements

setup(
name="Ml_Project",
version="0.0.1",
author="Harsha Srinatth",
author_email="harshasrinatth18@gmail.com",
description="A machine learning project setup",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)