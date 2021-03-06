from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.2'
DESCRIPTION = 'CNN architecture for Image Classification'

# Setting up
setup(
    name="Fas14MNet",
    version=VERSION,
    author="Sonali Saha, Diganta Dutta",
    author_email="sonalisaha2310@gmail.com, diganta.aimlos@gmail.com",
    url="https://github.com/DigantaD/Fas14MNet/tree/main/src",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['torch'],
    keywords=['image classification', 'cnn'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)