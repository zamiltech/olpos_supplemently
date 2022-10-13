from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in olpos_supplemently/__init__.py
from olpos_supplemently import __version__ as version

setup(
	name="olpos_supplemently",
	version=version,
	description="Olpos Supplemently",
	author="Mahmoud",
	author_email="hello@zamiltec.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
