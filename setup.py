#!/usr/bin/env python

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()\
                        .replace('.io/en/latest/', '.io/en/stable/')\
                        .replace('?badge=latest', '?badge=stable')\
                        .replace('projects/steam/badge/?version=latest', 'projects/steam/badge/?version=stable')
with open(path.join(here, 'steam/__init__.py'), encoding='utf-8') as f:
    __version__ = f.readline().split('"')[1]

install_requires = [
    'pycryptodomex>=3.7.0',
    'requests>=2.9.1',
    'urllib3<2', # See https://github.com/kevin1024/vcrpy/pull/699#issuecomment-1551439663
    'vdf @ git+https://github.com/solsticegamestudios/vdf.git@v4.0',
    'cachetools>=3.0.0',
]

install_extras = {
    'client': [
        'gevent>=1.3.0',
        'protobuf~=3.0',
        'gevent-eventemitter~=2.1',
        'wsproto~=1.2.0',
    ],
}

setup(
    name='steam',
    version=__version__,
    description='Module for interacting with various Steam features',
    long_description=long_description,
    url='https://github.com/solsticegamestudios/steam',
    author="Rossen Georgiev / Solstice Game Studios",
    author_email='py-steam@solsticegamestudios.com',
    license='MIT',
    python_requires=">=3.7",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        #'Programming Language :: Python :: 3.12', # TODO: Needs vcrpy>=6.0.0
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords='valve steam steamid api webapi steamcommunity',
    packages=['steam'] + ['steam.'+x for x in find_packages(where='steam')],
    install_requires=install_requires,
    extras_require=install_extras,
    zip_safe=True,
)
