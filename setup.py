# it helps us to find and package the modules we require

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will returm the list of requirements
    '''

    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements




setup(
    name='mlproject',
    version='0.0.1',
    author='atul2501',
    author_email='yatul247@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')      
    # file want in list form ['pandas','numpy'] thats why we use that function and in list form to get proper input here using function 
)
