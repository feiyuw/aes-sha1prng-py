import os
from setuptools import setup

CURDIR = os.path.abspath(os.path.dirname(__file__))


setup(
    name='aes-sha1prng-py',
    version='0.2',
    description='AES sha1prng algrithom library for python',
    author='Zhang Yu',
    author_email='feiyuw@gmail.com',
    url='https://github.com/feiyuw/aes-sha1prng-py.git',
    python_requires='>=2.7,>=3.5',
    install_requires=['pycryptodome'],
    packages=[
        'aes_sha1prng'],
    platforms='any',
)
