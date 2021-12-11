import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pam_ingestion",
    version="1.0.0",
    author="Hossein Akhlaghpour",
    author_email="hossein.akhlaghpour@autogrid.com",
    description="A small demo package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/demopackage",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: Private :: MIT License",
        "Operating System :: OS Independent",
    ),
)
