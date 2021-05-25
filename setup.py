import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="bopt",
    version="0.1.0",
    author="Jakub Arnold",
    author_email="darthdeus@gmail.com",
    description="Bayesian Optimization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/darthdeus/bopt",
    packages=setuptools.find_packages(),

    package_data={
        "": ["LICENSE"],
        "bopt": ["templates/*"]
    },

    python_requires=">=3.6, <4",
    install_requires=[
        "numpy>=1.17.4",
        "scipy>=1.1.0",
        "pyyaml>=5.1",
        "tqdm>=4.39,<4.62",
        "flask~=1.0.2",
        "psutil~=5.6.3",
        "jsonpickle~=1.0",
        "GPy[plotting]~=1.9.9",
        "filelock~=3.0.10",
        "ipdb~=0.11",
        "livereload==2.5.1",
        "colored==1.4.2"
    ],

    extras_require={
        "plotting": [
            "matplotlib~=3.2.0",
        ],
        "dev": [
            "pylint",
            "coverage",
            "deepdiff",
            "Cython",
            "pytest",
            "mypy",
            "radon",
        ]
    },

    entry_points={
        "console_scripts": [
            "bopt=bopt.cli.cli:main"
        ]
    },

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
