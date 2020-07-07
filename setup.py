from setuptools import setup

setup(name="literal_dice",
      version="0.1",
      description="Word shuffler",
      author="Stefan Walluhn",
      author_email="stefan@walluhn.de",
      license="MIT",
      packages=["literal_dice"],
      install_requires=[
          'click',
      ],
      test_suite='nose.collector',
      tests_require=[
          'nose'
      ],
      entry_points = {
          'console_scripts': ['l_dice=literal_dice.cli:dice'],
      },
      zip_safe=False)
