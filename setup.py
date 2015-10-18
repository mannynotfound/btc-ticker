try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='clockr',
      description='Simple curses clock written in Python',
      long_description=open('README.md').read(),
      version='0.9',
      author='Johnathan "ShaggyTwoDope" Jenkins',
      author_email='twodopeshaggy@gmail.com',
      url='https://github.com/shaggytwodope/clockr',
      keywords='clock terminal time curses',
      data_files=[
          ("share/man/man1", ["clockr.1"]),
          ("share/doc/clockr", ["LICENSE"])
      ],
      packages=['clockr'],
      entry_points={'console_scripts': ['clockr=clockr.__main__:main']},
      classifiers=['Intended Audience :: End Users/Desktop',
                   'Programming Language :: Python :: 3'],
      license='MIT')
