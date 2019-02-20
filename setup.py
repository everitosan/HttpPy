import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE/"README.md").read_text()

setup(
    name="HttpPy",
    version="0.0.5",
    description="More comfortable requests with python",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/everitosan/HttpClient/",
    author="everitosan",
    author_email="eve.san.dev@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(exclude=("test", "env", ".git")),
    include_package_data=True,
    install_requires=[
        "colorama",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "HttpPy=HttpPy.__main__:main"
        ]
    }
)
