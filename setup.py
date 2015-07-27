from setuptools import setup
import os


PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))

with open(PROJECT_DIR + '/requirements.txt') as f:
    required = f.read().splitlines()


def readme():
    with open(PROJECT_DIR + '/README.md') as f:
        return f.read()


setup(name="ulit",
      version="0.1",
      description="Translate a bunch of times and then see it become funny, almost.",
      long_description=readme(),
      url="",
      author="Amanjeev Sethi",
      author_email="aj@amanjeev.com",
      license="MIT",
      package=["ulit"],
      install_requires=required,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      )
