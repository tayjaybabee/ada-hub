from setuptools import setup, find_namespace_packages
import toml
import os

toml_file = 'pyproject.toml'

if os.path.exists(toml_file) and os.path.isfile(toml_file):
    setup_data = toml.load(toml_file)
    version = setup_data['tool']['poetry']['version']
else:
    version = None

setup(
    install_requires=[
        "sense-hat==2.2.0",
        "inspy-logger==1.0.3",
        "sense-emu==1.1",
        "pysimpleguiqt==0.35.0",
    ],
    name="ada-hub",
    version=version,
    packages=find_namespace_packages(),
    url="https://softworks.inspyre.tech/ada-hub",
    license="MIT",
    author="Taylor-Jayde Blackstone",
    author_email="t.blackstone@inspyre.tech",
    description="An application that allows one to monitor their environment.",
    scripts=["scripts/ada-hub"],
    keywords="temperature humidity",
)
