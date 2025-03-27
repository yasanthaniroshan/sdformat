from setuptools import setup, find_packages

setup(
    name="sdformat15",
    version="1.0.0",
    description="Python wrapper for sdformat15",
    author="Yasantha Niroshan",
    author_email="yasantha.21@cse.mrt.ac.lk",
    license="MIT",
    packages=find_packages(),
    package_data={
        # Include all .so and .pyi files in the sdformat15 package
        "sdformat15": ["*.so", "*.pyi","__init__.py"],
    },
    include_package_data=True,  # This ensures that package data is included
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)