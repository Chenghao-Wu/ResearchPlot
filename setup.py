"""
setup.py
========
:license: BSD, see LICENSE.txt for more details.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os
import sys
cwd = os.path.dirname(os.path.abspath(__file__))

# Read __version__ from _version.py and add it into the current variable space.
exec(open('ResearchPlot/_version.py').read())

setup(
    name='ResearchPlot',
    version=__version__,
    license='BSD',
    description='is a python package based on mpltex of liuyxpp for producing publication quality images using matplotlib.',
    author='Zhenghao Wu',
    author_email='w415146142@gmail.com',
    url='https://github.com/Chenghao-Wu/ResearchPlot',
    packages=['ResearchPlot'],
    include_package_data=True,
    zip_safe=False,
    long_description=open(os.path.join(cwd, 'README.md')).read(),
    install_requires=[
        'matplotlib',
        'palettable',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',],
)
