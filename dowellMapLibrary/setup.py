from setuptools import find_packages, setup
from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dowell-map',
    version='0.1.0',
    description='Dowell Maps Library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://dowell-map.readthedocs.io/",
    author='Steve Alila',
    license='MIT',
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    include_package_data=True,
    packages=find_packages(include=['dowell_map']),
    install_requires=[
        'requests==2.31.0',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)