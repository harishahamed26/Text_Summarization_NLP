from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

__version__ = "0.0.0"

REPO_NAME       = "Text_Summarization_NLP"
AUTHOR_NAME     = "harishahamed26"
SRC_REPO        = "TEXT_SUMMARIZATION_NLP"
AUTHOR_EMAIL    = "harishahamed26@gmail.com"

setup(
    name                             = SRC_REPO,
    version                          = __version__,
    author                           = AUTHOR_NAME,
    author_email                     = AUTHOR_EMAIL,
    description                      = "A python package for text summarization using NLP techniques.",
    long_description                 = description,
    long_description_content_type    = "text/markdown",
    url                              =   f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls                     =   {
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues"
    },
    package_dir                      = {"": "src"},
    packages                         = setuptools.find_packages(where="src")
)