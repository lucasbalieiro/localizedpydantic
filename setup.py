from setuptools import setup, find_packages

setup(
    name='localizedpydantic',
    version='0.1.0',
    description='Library to validate localized data with pydantic',
    packages=find_packages(),
    install_requires=[
        'pydantic',
        'requests'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
