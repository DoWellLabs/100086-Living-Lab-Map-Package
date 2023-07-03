from setuptools import find_packages, setup

setup(
    name='dowell-map',
    packages=find_packages(include=['dowell-map']),
    version='0.1.0',
    description='Dowell Maps Library',
    author='Steve Alila',
    license='MIT',
    install_requires=[
        'requests==2.31.0',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)