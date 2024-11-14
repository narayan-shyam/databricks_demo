from setuptools import setup, find_packages

setup(
    name="data-processor",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas>=1.3.0",
        "pyspark>=3.0.0",
        "databricks-cli>=0.17.0"
    ],
    python_requires=">=3.8",
)
