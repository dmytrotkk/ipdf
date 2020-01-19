from setuptools import (
    find_packages,
    setup,
)


extras_require = {
    'linter': [
        "flake8==3.7.8"
    ],
    'dev': [
        "pytest==5.2.1",
        "twine==1.12.1",
        "wheel==0.33.6",
    ]
}


setup(
    name='ipdframework',
    version='0.1',
    description='Library for the iterated evolutionary tournaments between memory-based agents',
    long_description_markdown_filename='README.md',
    author='Dmytro Tkachyk',
    author_email='dmitry.tkk@gmail.com',
    url='https://github.com/dmitry-tk/ipdf',
    include_package_data=True,
    install_requires=[
        "colorful==0.5.4",
        "numpy==1.18.1"
    ],
    python_requires='>=3.6,<4',
    extras_require=extras_require,
    keywords=['game-theory', 'strategy'],
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ]
)
