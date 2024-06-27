from setuptools import setup, find_packages

setup(
    name="cv_automator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'PyQt5==5.15.4',
        'python-docx==0.8.11',
    ],
    entry_points={
        'console_scripts': [
            'cv_automator=src.main:main',
        ],
    },
)