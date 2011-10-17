import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "django_ip_authn",
    version = "0.1",
    author = "Kirit Saelensminde",
    author_email = "kirit@felspar.com",
    description = ("IP number based authentication for Django"),
    license = "Boost Software License - Version 1.0 - August 17th, 2003",
    keywords = "django authn authentication ip",
    packages = ['django_ip_authn'],
    long_description = read('README.markdown'),
    install_requires = ['simplejson', 'httplib2'],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Boost Software License - Version 1.0 - August 17th, 2003",
    ],
)
