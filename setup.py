from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

version = {}
with open("nlbsg/__version__.py") as f:
    exec(f.read(), version)

setup(name='nlbsg',
      version=version['__version__'],
      description='Python SDK for the NLB Open Web Services',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/yi-jiayu/nlbsg',
      author='Jiayu Yi',
      author_email='yijiayu@gmail.com',
      license='MIT',
      packages=['nlbsg'],
      install_requires=[
          'zeep',
      ],
      python_requires=">=3.7",
      zip_safe=False)
