from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_reqirements(file_path:str)->List[str]:
    '''
    this Function will return the list of requirements
    '''
    requirements =[]
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace("\n",'') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements 


setup(
    name='MLProject',
    version='0.0.1',
    author='Guru Alampalli',
    author_email='guru.alampalli@gmail.com',
    packages=find_packages(),
    install_requires=get_reqirements('requirements.txt')
    
   )
