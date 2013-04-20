import os
from setuptools import setup

def read(fname1, fname2):
    if os.path.exists(fname1):
        fname = fname1
    else:
        fname = fname2
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "django_ip_authn",
    version = "0.3.0.1",
    author = "Kirit Saelensminde",
    author_email = "kirit@felspar.com",
    url = 'https://github.com/Felspar/django-ip-authn',
    description = ("IP number based authentication for Django"),
    long_description = read('README','README.markdown'),
    license = "Boost Software License - Version 1.0 - August 17th, 2003",
    keywords = "django authn authentication ip",
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved",
    ],
    packages = ['django_ip_authn'],
)
