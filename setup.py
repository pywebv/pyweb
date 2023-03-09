# PyWeb - Python add-on extension to Pyrogram
# Copyright (C) 2023-2024 PyWebV <https://github.com/pywebv>
#
# This file is part of PyWeb.
#
# PyWeb is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyStark is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyWeb. If not, see <https://www.gnu.org/licenses/>.

import os
import re
from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    long_description = "\n".join([x for x in f.read().split("\n") if not x.startswith('>')])

with open("requirements.txt", encoding="utf-8") as r:
    install_requires = [i.strip() for i in r if not i.startswith('#')]

with open("pyweb/constants.py", "r", encoding="utf-8") as f:
    text = f.read()
    pat = r"['\"]([^'\"]+)['\"]"
    version = re.search("__version__ = "+pat, text).group(1)
    # beta_version = re.search("__beta_version__ = "+pat, text).group(1)
    description = re.search("__description__ = "+pat, text).group(1)


def get_packages():
    return [path.replace("\\", ".").replace("/", ".") for path, _, _ in os.walk("pyweb") if "__" not in path]


setup(
    name='PyWeb',
    packages=get_packages(),
    version=version,
    license='GPLv3+',
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='TheHamkerXD',
    author_email='pywebv@gmail.com',
    url='https://github.com/pywebv/pyweb',
    keywords=['telegram', 'bot', 'pyrogram', 'python', 'telegram-bot'],
    install_requires=install_requires,
    zip_safe=False,
    python_requires=">=3.9",
    dependency_links=['https://github.com/pyrogram/pyrogram/tarball/master'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Natural Language :: English',
        'Topic :: Communications :: Chat',
        'Topic :: Education :: Testing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    project_urls={
        "Support": "https://t.me/pyweb_chat",
        "Community": "https://t.me/pywebv",
        "Updates": "https://t.me/pywebv",
        "Documentation": "pywebv.github.io",
    },
    entry_points={
        'console_scripts': [
            'pyweb = pyweb.cli:main',
        ],
    },
)
