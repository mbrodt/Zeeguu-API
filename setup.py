#!/usr/bin/env python
# coding: utf8 -*-

import setuptools

setuptools.setup(
    name="zeeguu_api",
    version="0.2",
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    author="The Zeeguu Team",
    author_email="zeeguu.team@gmail.com",
    description="API for Zeeguu, a project that aims to accelerate vocabulary acquisition in a second language",
    keywords=" API, second language acquisition",
    dependency_links=[
            "git+https://github.com/mircealungu/zeeguu-core.git#egg=zeeguu",
            "git+https://github.com/mircealungu/python-translators.git#egg=python_translators",
            "git+https://github.com/mircealungu/automatic-monitoring-dasboard/tree/development.git#egg=dashboard",
        ],
    install_requires=("flask>=0.10.1",
                      "Flask-SQLAlchemy",
                      "Flask-Assets",
                      "flask_cors",
                      "mysqlclient",
                      "regex",
                      "beautifulsoup4",
                      "feedparser",
                      'zeeguu',
                      'python_translators',
                      'dashboard')
)
