from pathlib import Path

from setuptools import find_packages, setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="grn-thresholding",
    packages=find_packages(exclude=[]),
    version="0.0.1",
    license="MIT",
    description="A collection of thesholding methods for GRNs",
    long_description="GRN - Thresholding",
    author="Soel Micheletti",
    author_email="msoel@ethz.ch",
    url="https://github.com/soelmicheletti/grn-thresholding",
    keywords=[
        "statistics",
        "causality",
    ],
    install_requires=["mixem>=0.1.4", "scikit-learn"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
)
