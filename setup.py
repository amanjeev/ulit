from setuptools import setup
from setuptools import find_packages



with open('README.rst') as f:
    readme = f.read()


setup(name="ulit",
      version="0.2.2",
      author="Amanjeev Sethi",
      author_email="aj@amanjeev.com",
      description="Start with some text in a langauge. Translate it stepwise using a number of intermediate langauges, and back to the one you started with. See how the original text changes.",
      long_description=readme,
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
      keywords=['translate', 'cascade', 'repeated translations',
                'lost in translation', 'translations', 'languages'],
      install_requires=[
          'google-api-python-client==1.4.1',
          'yandex.translate==0.3.5'
      ],
      )
