from setuptools import setup, find_packages

setup(
    name="orm-package",  # Le nom que vous utiliserez pour pip install
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "sqlalchemy>=1.4.0",
        # Ajoutez ici vos autres dépendances
    ],
    python_requires=">=3.7",
    author="Votre Nom",
    author_email="votre@email.com",
    description="Une description courte de votre package",
)
