from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_desc = f.read()

setup(
    name="vflask",
    author="VickySuraj",
    author_email="vigneshwaranjheyaraman@gmail.com",
    version=1.0,
    description="Flask CLI for deployment at once",
    long_description= long_desc,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    entry_points={
        "console_scripts":[
            "vflask=vflaskcli:vflask_cli"
        ],
    },
)