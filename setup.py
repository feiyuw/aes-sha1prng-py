from setuptools import setup


setup(
    name='aes-sha1prng-py',
    version='0.2',
    description='AES sha1prng algrithom library for python',
    author='Zhang Yu',
    author_email='feiyuw@gmail.com',
    url='https://github.com/feiyuw/aes-sha1prng-py.git',
    python_requires='>=3.5',
    install_requires=['pycryptodome'],
    packages=['aes_sha1prng'],
    platforms='any',
)
