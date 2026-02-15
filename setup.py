from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="people-name-cleaner",
    version="1.0.0",
    author="deng-peng",
    description="A Python library for cleaning and parsing people's names from various formats",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deng-peng/people-name-cleaner",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
)
