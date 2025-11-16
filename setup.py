from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements.txt file and returns a clean list of dependencies.
    Removes '-e .' if present.
    """
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            req = line.strip()              # removes \n and spaces
            if req and req != HYPHEN_E_DOT: # ignore empty lines + -e .
                requirements.append(req)

    return requirements


setup(
    name="ml_project",
    version="0.0.1",
    author="Somesh",
    author_email="biradarsomesh52@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
