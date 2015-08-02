from setuptools import setup
from setuptools import find_packages


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name="ulit",
      version="0.2.0",
      author="Amanjeev Sethi",
      author_email="aj@amanjeev.com",
      description="Translate a bunch of times and then see it become funny, almost.",
      long_description=readme(),
      url="https://github.com/amanjeev/ulit",
      license="MIT",
      packages=find_packages(),
      package_dir={'ulit': 'ulit'},
      provides=['ulit'],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.4',
      ],
      test_suite='ulit.tests',
      tests_require=['nose'],
      platforms=['All'],
      install_requires=[
          'google-api-python-client==1.4.1',
          'yandex.translate==0.3.5'
      ],
      )
