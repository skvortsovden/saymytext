from setuptools import setup, find_packages
import os
import io

NAME = 'saymytext'
VERSION = '1.0'
DESCRIPTION = 'A text to speech syntesizer'
# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
here = os.path.abspath(os.path.dirname(__file__))
try:
    with io.open(os.path.join(here, 'readme.md'), encoding='utf-8') as f:
        LONG_DESCRIPTION = '\n' + f.read()
except FileNotFoundError:
    LONG_DESCRIPTION = DESCRIPTION

# Setting up
setup(
        name=NAME, 
        version=VERSION,
        author="Denys Skvortsov",
        author_email="skvortsovdenis81@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        url = "https://github.com/skvortsovden/saymytext",
        packages=find_packages(),
        install_requires=[
            'gTTS==2.2.3',
            'PyAudio==0.2.11',
            'pydub==0.25.1'
        ],
        python_requires='>=3.6',
        keywords=['python', 'text to speech'],
        classifiers= [
            "Intended Audience :: Education",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ],
        include_package_data = True
)