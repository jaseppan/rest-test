from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='rest_test',
    version='0.1.0',
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        'dynamic-content-generator'
    ],
    author='Janne Seppänen',
    author_email='j.v.seppanen@gmail.com',
    description='A module to test REST API and create and manipulate test data',
    keywords='REST API testing test content generating',
    url='https://github.com/jaseppan/module_name',
)
