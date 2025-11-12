"""
Setup script for LisezMoiCreator
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="LisezMoiCreator",
    version="2.0.0",
    author="Confrérie des Traducteurs",
    description="Générateur de fichier README pour la Confrérie des Traducteurs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Doezer/LisezMoiCreator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Text Editors :: Text Processing",
    ],
    python_requires=">=3.8",
    install_requires=[
        "PyQt6>=6.0.0",
    ],
    entry_points={
        "gui_scripts": [
            "lisezmoi-creator=main:main",
        ],
    },
)
