import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example_qifhdc",
    version="0.0.1",
    author="Lucas Starling",
    author_email="lucastarling1@gmail.com",
    description="A tool for calculating the hyper distribution from pushing a prior into a channel. Quantitative Information Flow.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LucasStarlingdePaulaSalles/hyper-distributor",
    project_urls={
        "Bug Tracker": "https://github.com/LucasStarlingdePaulaSalles/hyper-distributor/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)