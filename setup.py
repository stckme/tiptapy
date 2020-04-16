
from setuptools import setup, find_packages


setup(
    name="tiptapy",
    version="0.5.1",
    url="https://github.com/scrolltech/tiptapy",
    description="Library that generates HTML output from JSON export of tiptap editor",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    author="Shekhar Tiwatne",
    author_email="pythonic@gmail.com",
    license="http://www.opensource.org/licenses/mit-license.php",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
