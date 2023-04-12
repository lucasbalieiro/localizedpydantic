from setuptools import setup

setup(
    name='localizedpydantic',
    version='0.1.0',
    packages=['localizedpydantic'],
    install_requires=[
        'pydantic',
        'requests',
    ],
    tests_require=[
        'pytest',
    ],
    author='Lucas Balieiro Matos && Chat GPT-4',
    author_email='lucasbalieirom@hotmail.com',
    description='Library to validate localized data with pydantic',
    url='https://github.com/lucasbalieiro/localizedpydantic',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.7',
)
