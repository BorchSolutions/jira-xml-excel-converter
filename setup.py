from setuptools import setup, find_packages

setup(
    name="jira-xml-excel-converter",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.5.0",
        "openpyxl>=3.0.0",
    ],
    author="Bryan Ramírez",
    author_email="bryan@ramirezchavez.net",
    description="A GUI tool that converts Jira XML exports to Excel with formatting",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/jira-xml-excel-converter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)