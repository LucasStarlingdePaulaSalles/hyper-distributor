import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyqif",
    version="0.0.5",
    author="Lucas Starling",
    author_email="lucastarling1@gmail.com",
    description="A tool for calculating the hyper distribution from pushing a prior into a channel. Quantitative Information Flow.",
    long_description=long_description,
    url="https://github.com/LucasStarlingdePaulaSalles/hyper-distributor",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    py_modules=["pyqif"], 
    requires=['numpy'],
    install_requires=['numpy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'pyqif=pyqif:main',
        ],
    },
)