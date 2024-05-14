from setuptools import setup, find_packages

# Parse requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='config-cobra',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'config-cobra=src.app:main',
        ],
    },
)