from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements

setup(
Name = "Student Mark Prediction",
Author = "Biswajit Jena",
Version = '0.1',
packages = find_packages(),
install_requires= get_requirements('requirement.txt')

)