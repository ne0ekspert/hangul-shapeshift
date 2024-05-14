import setuptools

with open("README.md", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="hangul-shapeshift",
    author="ne0ekspert",
    description="Hangul character transition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.1.0",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",
    install_requires=[
        "jamo",
        "networkx"
    ],
)