import io
from typing import Iterator
from setuptools import setup, find_packages


def read_requirements() -> Iterator[str]:
    with open("requirements.txt", "r") as f:
        contents = f.read()
    for ln in contents.splitlines():
        lns = ln.strip()
        if lns:
            yield lns


# Use the README.md content for the long description:
with io.open("README.md", encoding="utf-8") as fo:
    long_description = fo.read()

setup(
    name="list_gh_contributions",
    version="0.1.0",
    url="https://github.com/seanbreckenridge/list_gh_contributions",
    author="Sean Breckenridge",
    author_email="seanbrecke@gmail.com",
    description=("""Script to list all of your contributions to all repositories"""),
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(include=["list_gh_contributions"]),
    test_suite="tests",
    install_requires=list(read_requirements()),
    keywords="github api",
    entry_points={
        "console_scripts": [
            "list_gh_contributions = list_gh_contributions.__main__:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
