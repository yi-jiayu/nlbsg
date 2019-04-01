from setuptools import setup

setup(name='nlblg',
      version='0.1.1',
      description='Python SDK for the NLB Open Web Services',
      url='https://github.com/yi-jiayu/nlbsg',
      author='Jiayu Yi',
      author_email='yijiayu@gmail.com',
      license='MIT',
      packages=['nlbsg'],
      install_requires=[
          'zeep',
      ],
      zip_safe=False)
