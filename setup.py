import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='inmagik-drf-auth',
    version='0.1.1',
    packages=['inmagik_drf_auth'],
    include_package_data=True,
    license='BSD License',  # example license
    description='Additional views and helpers for django-rest-framework authentication',
    long_description=README,
    url='https://github.com/INMAGIK/inmagik-drf-auth/',
    author='Mauro Bianchi',
    author_email='bianchimro@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires = [
        'djangorestframework'
    ]
)