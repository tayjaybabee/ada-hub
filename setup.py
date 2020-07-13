from setuptools import setup, find_namespace_packages
import toml
import os

toml_file = 'pyproject.toml'

this_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_dir, 'README.md'), encoding='utf8') as f:
    long_desc = f.read()

if os.path.exists(toml_file) and os.path.isfile(toml_file):
    setup_data = toml.load(toml_file)
    version = setup_data['tool']['poetry']['version']
else:
    version = None

setup(
    install_requires=[
        "sense-hat",
        "inspy-logger",
        "sense-emu",
        "pysimpleguiqt",
    ],
    name="ada-hub",
    version=version,
    packages=find_namespace_packages(),
    url="https://softworks.inspyre.tech/ada-hub",
    license="MIT",
    author="Taylor-Jayde Blackstone",
    author_email="t.blackstone@inspyre.tech",
    description="An application that allows one to monitor their environment.",
    long_description=long_desc,
    long_description_content_type='text/markdown',
    scripts=["scripts/ada-hub"],
    keywords="temperature humidity",
)
