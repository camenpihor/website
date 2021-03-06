"""Packaging for the website's backend library."""
from setuptools import find_packages, setup


def get_version():
    """Get backend version."""
    with open("VERSION") as buffer:
        return buffer.read()


setup(
    name="website-backend",
    version=get_version(),
    url="",
    author="Camen",
    author_email="camenpihor@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    description="Backend for personal website.",
)
