import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qifhdc",
    version="0.0.3",
    author="Lucas Starling",
    author_email="lucastarling1@gmail.com",
    description="A tool for calculating the hyper distribution from pushing a prior into a channel. Quantitative Information Flow.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # packages=['qifhdc'],
    packages=setuptools.find_packages(),
    # package_dir={'':'src'},
    py_modules=["qifhdc"], 
    requires=['numpy'],
    install_requires=['numpy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={  # Optional
        'console_scripts': [
            'qifhdc=qifhdc:main',
        ],
    },
)