from setuptools import setup, find_packages

app_name = "enphaseai"
app_version = "0.0.1"
license_filename = "LICENSE.txt"
readme_md_file = "readme.md"
description_package = "Enphase coding challenge."

with open('_version.txt') as f:
    app_version = f.read()

setup(
    name=app_name,
    version=app_version,
    author="Jimmy Leroux",
    author_email="jim.leroux1@gmail.com",
    license=license_filename,
    description=description_package,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "matplotlib",
        "sklearn",
        "pytest"
    ],
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: license_filename',
    ],
)
