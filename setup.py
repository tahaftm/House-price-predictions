from setuptools import find_packages, setup

HYPHEN_E_DOT = '-e .'
def find_requirements(file):
    with open(file) as f:
        requirements = f.readlines()
    requirements = [req.replace("\n","") for req in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements 


setup(
    name="HousePricePredictions",
    author="TahaTariq",
    author_email="tahatariqf@gmail.com",
    version="0.0.1",
    packages=find_packages(),
    install_requires=find_requirements('requirements.txt')
)