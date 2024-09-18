# setup.py
from setuptools import setup, find_packages

setup(
    name='zucchini',
    version='0.1.0',
    description='Zucchini: A lightweight, Celery-like task queue for local development and trialing.',
    author='Zacchaeus',
    author_email='zacchaeuschok2014@gmail.com',
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'zucchini-example=examples.example:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
