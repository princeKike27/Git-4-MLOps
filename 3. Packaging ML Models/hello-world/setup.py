# Details of the Package and How it should work

# import modules
from setuptools import setup, find_packages

# create distributable python package
setup(
    name='hello_world-kike271203',
    version='0.0.1',
    author='PrinceKike',
    author_email='princekike27@gmail.com',
    url='https://www.manifoldailearning.in',
    description='A hello-world example package',
    packages=find_packages(),
    # list to help classify package
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)