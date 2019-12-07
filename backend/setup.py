"""Packaging for the website's backend library."""
from setuptools import find_packages, setup


def get_version():
    """Get backend version."""
    with open("VERSION") as f:
        return f.read()


setup(
    name="website-backend",
    version=get_version(),
    url="",
    author="Camen",
    author_email="camenpihor@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=open("requirements.in").readlines(),
    dependency_links=open("requirements.private.in").readlines(),
    tests_require=open("requirements-dev.in").readlines(),
    description="TODO",
    long_description="\n" + open("README.md").read(),
)
