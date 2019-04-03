from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

version = {}
with open("nlbsg/__version__.py") as f:
    exec(f.read(), version)

setup(name='nlbsg',
      version=version['__version__'],
      description='Python SDK for the NLB Open Web Services',
      long_description_content_type='text/markdown',
      long_description=long_description,
      url='https://github.com/yi-jiayu/nlbsg',
      author='Jiayu Yi',
      author_email='yijiayu@gmail.com',
      license='MIT',
      classifiers=[
          "Programming Language :: Python :: 3.7",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      project_urls={
          'Documentation': 'https://nlbsg.readthedocs.io/en/latest/',
          'Source code': 'https://github.com/yi-jiayu/nlbsg',
          'Builds': 'https://travis-ci.com/yi-jiayu/nlbsg',
          'Coverage': 'https://codecov.io/gh/yi-jiayu/nlbsg',
      },
      packages=['nlbsg'],
      install_requires=[
          'zeep',
      ],
      python_requires=">=3.7",
      zip_safe=False)
