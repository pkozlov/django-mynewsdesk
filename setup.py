import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-mynewsdesk',
    version='0.4',
    packages=['mynewsdesk'],
    include_package_data=True,
    license='MIT License',
    description='Django package for MyNewsDesk API',
    long_description=README,
    url='https://github.com/pkozlov/django-mynewsdesk',
    author='Pavel Kozlov',
    author_email='mail@pkozlov.ru',
    install_requires=[
        'Django >= 1.4.3',
        'requests >= 1.0.3'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)