from setuptools import find_packages,setup

setup(
    name="genaimcq",
    version='0.0.1',
    author="sujeet kumar",
    author_email='kumar.sujeet132@gmail.com',
    install_requires=['openai','langchain,','streamlit','python-dotenv','PyPDF2'],
    package_dir={"":"src"},
    package_data=find_packages(where="src")
)