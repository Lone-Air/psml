#!/usr/bin/python3
from setuptools import find_packages
from distutils.core import setup
import os

with open("README.md") as r:
    README=r.read()

with open("VERSION") as v:
    _v=v.read()

_v.replace("\n","")

setup(
        author="Lone_air",
        author_email="Lone_air_Use@outlook.com",
        name="psmlc",
        packages=["psmlc"],
        package_data={"psmlc":os.listdir("psmlc")},
        version=_v,
        license="GPLv2.0",
        url="https://github.com/lone-air/psml",
        description="A simpile python server markup language",
        long_description=README,
        long_description_content_type="text/markdown",
        python_requires=">=3.6",
        install_requires=[
            "flask",
            "bottle"
            ],
        entry_points={
            "console_scripts":[
                "psml=psmlc.psml:_start",
                "psmlweb=psmlc.psml_web:run_server"
                ]
            }
        )
