from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will help us to get out required pakages list
        
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','')for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='fashion classification',
    version='0.0.1',
    author='karhtik',
    author_email='karthikknights80@gmail.com',
    packages=find_packages(),
    install_require=get_requirements('requirements.txt')
)