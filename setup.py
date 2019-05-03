import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='flask-ssl',
    version='0.0.0.1c1',
    author="Standart AG, LLC",
    author_email="it@standart.lv",
    description="Flask SSL require and redirect helper decorator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/standart-ag/flask-ssl",
    packages=setuptools.find_packages(),
    install_requires=[
        'flask'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
