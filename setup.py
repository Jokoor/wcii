from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in wcii/__init__.py
from wcii import __version__ as version

setup(
	name="wcii",
	version=version,
	description="Education app",
	author="Royalsmb",
	author_email="info@royalsmb.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
