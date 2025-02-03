from setuptools import setup, find_packages

setup(
    name="Kipito-orm",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["SQLAlchemy", "psycopg2-binary"],
)
