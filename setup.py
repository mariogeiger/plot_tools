from setuptools import find_packages, setup

setup(
    name='plot_tools',
    version="0.0.0",
    license="MIT",
    license_files="LICENSE",
    packages=find_packages(exclude=["tests.*", "tests"]),
)
