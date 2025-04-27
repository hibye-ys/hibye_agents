from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# setup.py 상단에
with open("requirements.txt") as f:
    install_requires = [l.strip() for l in f if l and not l.startswith("#")]

setup(
    name="hibye_agents",
    version="0.1.0",
    author="hibye",
    author_email="dldudtjr88@gmail.com",
    description="agent packages for personal use",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hibye-ys/hibye_agents",
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
    entry_points={
        "console_scripts": [
            "hibye_agents=main:main",
        ],
    },
)
