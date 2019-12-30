import os
import platform
import sys
from distutils.command.build import build

import pkg_resources

import setuptools
from setuptools import setup, find_packages
from setuptools.command.install import install

with open("docs/README.md", "r") as readme_file:
    readme = readme_file.read()

base_dir = os.path.dirname(__file__)
src_dir = os.path.join(base_dir, "src")

# When executing the setup.py, we need to be able to import ourselves, this
# means that we need to add the src/ directory to the sys.path.
sys.path.insert(0, src_dir)

about = {}
with open(os.path.join(src_dir, "django_treedform", "__about__.py")) as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__email__'],
    description=about['__summary__'],
    long_description=readme,
    long_description_content_type="text/markdown",
    url=about['__uri__'],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=about['__requirements__'],
    include_package_data=True,
    package_data=about['__includedatafiles__'],
    exclude_package_data=about['__excludedatafiles__'],
    classifiers=[
        "Programming Language :: Python :: 3.8.0",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)