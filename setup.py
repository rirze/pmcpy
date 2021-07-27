from setuptools import setup, find_packages
import os

with open('pmcpy/version.py', 'r') as vfile:
    exec(vfile.read())

try:
    long_description = open(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            'README.md')).read()
except:
    long_description = ""


setup(
    name='pmcpy',
    version=version,
    description="Python library to interact with ParkMyCloud's Restful API.",
    author='Sourabh Cheedella',
    long_description=long_description,
    author_email='cheedella.sourabh@gmail.com',
    license='AGPL',
    packages=find_packages(),
    install_requires=[],
)
