import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="boiga", # Replace with your own username
    version="0.0.1",
    author="Wytamma Wirth",
    author_email="wytamma.wirth@me.com",
    description="A simple bioinformatics package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Wytamma/boiga",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)