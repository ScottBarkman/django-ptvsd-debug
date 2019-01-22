import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-ptvsd-debug",
    version="1.0.3",
    author="Scott Barkman",
    author_email="scottbarkman@gmail.com",
    description="Multithreaded django hook for PTVSD debugging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scottbarkman/django-ptvsd-debug",
    packages=setuptools.find_packages(),
    install_requires=[
          'ptvsd==4.*',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)