from setuptools import setup, find_packages

setup(
    name='my_pyzbar',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyzbar',
    ],
    python_requires='>=3.6',
)
