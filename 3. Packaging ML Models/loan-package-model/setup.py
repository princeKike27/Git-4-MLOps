# import modules
import io
import os 
from pathlib import Path 

from setuptools import find_packages, setup 

# Metadata of package 
NAME = 'prediction_model'
DESCRIPTION = 'Loan Prediction Model'
URL = 'https://github.com/princeKike27/Git-4-MLOps'
EMAIL = 'enriquebaron27@hotmail.com'
AUTHOR = 'Kike1027'
REQUIRES_PYTHON = '>=3.7.0'

# print working directory
pwd = os.path.abspath(os.path.dirname(__file__))


# Get list of packages to be installed
def list_reqs(file_name='requirements.txt'):
    with io.open(os.path.join(pwd, file_name), encoding='utf-8') as f:
        # read file
        return f.read().splitlines()
    

# try reading README.md file    
try:
    with io.open(os.path.join(pwd, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


# load package's __version__.py module as a dictionary 
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / NAME 
# about dict
about = {}
# open VERSION file
with open(PACKAGE_DIR / 'VERSION') as f:
    _version = f.read().strip()
    # save version to dict
    about['__version__'] = _version



# SETUP dict 
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    package_data={'prediction_model': ['VERSION']},
    install_requires=list_reqs(),
    extra_requires={},
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)



