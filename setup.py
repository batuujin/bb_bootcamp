import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='bb_bootcamp',
    version='0.0.1',
    author='Batuujin Burendei',
    author_email='bburendei@scripps.edu',
    description='Utilities for use in bootcamp. BB edited',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
