from setuptools import setup, find_packages


setup(
    name="pytest-lineno",
    version="0.0.1",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=["pytest"],
    extras_require={"dev": ["black", "flake8", "wheel"]},
    entry_points={"pytest11": ["lineno = pytest_lineno"]},
    author="harupy",
    description="A pytest plugin to show the line numbers of test functions",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    python_requires=">=3.5",
)
