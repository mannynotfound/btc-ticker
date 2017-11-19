from version import __version__ as version
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='clockr',
      description='Simple curses clock written in Python',
      long_description=open('README.md').read(),
      version=version,
      author='Johnathan "ShaggyTwoDope" Jenkins',
      author_email='twodopeshaggy@gmail.com',
      url='https://github.com/shaggytwodope/clockr',
      keywords='clock terminal time curses',
      data_files=[
          ("share/man/man1", ["clockr.1"]),
          ("share/doc/clockr", ["LICENSE"])
      ],
      packages=['clockr'],
      entry_points={'console_scripts': ['clockr=clockr.clockr:main']},
      classifiers=['Intended Audience :: End Users/Desktop',
                   'Programming Language :: Python :: 3'],
      license='MIT')
