import re
from setuptools import setup

requirements = [
    "discord.py>=1.0.0"
]

version = ""
with open("discord_argparse/__init__.py") as fp:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fp.read(), re.MULTILINE).group(1)

readme = ""
with open("README.md") as fp:
    readme = fp.read()

setup(
    name="discord_argparse",
    version=version,
    author="lukeciel",
    url="https://github.com/lukeciel/discord-argparse",
    packages=["discord_argparse"],
    license="MIT",
    description="Arbitrarily ordered arguments for commands in discord.py",
    install_requires=requirements,
    long_description=readme,
    long_description_content_type="text/markdown"
)