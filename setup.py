from setuptools import setup


with open('requirements.txt') as f:
    required = f.read().splitlines()


def readme():
    with open('README.md') as f:
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
