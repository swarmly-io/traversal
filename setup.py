import os
import requests
from setuptools import setup, find_packages

lib_name = 'traversal'

def get_version_from_url(service_name):
    """
    Fetch version information from a URL specified in an environment variable.
    """
    version_url = os.environ.get('VERSION_URL') or 'https://versioning.azurewebsites.net'
    if not version_url:
        raise ValueError("VERSION_URL environment variable is not set.")

    response = requests.get(f'{version_url}/{service_name}')
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch version from {version_url}")

    new_version = str(response.text.strip().replace('"', ''))
    return f'v{new_version}'

version=get_version_from_url(lib_name)

def get_requirements():
    """
    Parse dependencies from 'requirements.in' file.

    Collecting dependencies from 'requirements.in' as a list,
    this list will be used by 'install_requires' to specify minimal dependencies
    needed to run the application.
    """
    with open('requirements.txt') as fd:
        return [l.split("==")[0] for l in fd.read().splitlines()]

install_requires = get_requirements()

setup(
    name=lib_name,
    version=version,
    description='Algorithms for traversing domain graphs',
    author='Adrian Plani',
    author_email='adrian@swarmly.io',
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)