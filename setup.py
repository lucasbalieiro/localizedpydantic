from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="localizedpydantic",
    version="0.1.2",
    author="Lucas Balieiro Matos",
    author_email="lucasbalieirom@hotmail.com",
    description="Library to validate localized data with pydantic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lucasbalieiro/localizedpydantic",
    packages=find_packages(),
    install_requires=[
        "pydantic",
        "requests",
    ],
    tests_require=[
        "pytest",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
)
