from setuptools import find_packages
from setuptools import setup

setup(
    name="autoWord",
    version="0.0.1",
    license="GNU General Public License v2.0",
    author="Sajor Dino",
    author_email="sajor@foxmail.com",
    description="auto generator word file",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=["autoWord"],
    url="https://github.com/Sajor-X/autoWord",
    install_requires=[
        "python-docx",
    ],
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "autoWord = autoWord.__main__:cli",
        ]
    },
)