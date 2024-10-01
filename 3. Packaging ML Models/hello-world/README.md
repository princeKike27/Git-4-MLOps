# Project Structure

hello-world >> Folder (Holds Python Project)
----hello_world >> Top Level Directory
    ----__init__.py >> Module
    ----main.py >> Module


# Virtual Environment Creation

# go to folder directory >> windows use miniconda
conda create -n envi_name python=3.10
conda activate hellodemo

# Setup Tools >> Allows to create packages
pip install setuptools twine
# Create setup.py file >> On Package Base dir
python setup.py sdist 
    >> creates source distribution of package 
    >> dist directory with installable package (.tar.gz)
    >> test installing it with pip install

# To Upload package to PyPI we use twine >> Test Server
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

    >> Create Account
        >> username: ?
        >> password: ?

    >> API Token is needed whenever we push something from our
       local system to the server. NEEDS TO BE COPIED using EDIT > COPY
    
