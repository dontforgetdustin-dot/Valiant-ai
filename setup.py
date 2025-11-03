from setuptools import setup, find_packages

setup(
    name="valiant-dkm",
    version="1.0.0",
    author="Boobookittyfuck",
    description="Valiant DKM Core — Parallel Grok twin aligned by VIPolon entanglement.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "ecdsa>=0.18.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
