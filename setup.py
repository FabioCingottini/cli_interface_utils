# http://python-packaging.readthedocs.io/en/latest/minimal.html#picking-a-name

from setuptools import setup

setup(
    name='cli_utils',
    version='0.1',
    description='create a CliInterface, extends AbstractCliWorker, now you have a working cli application',
    url='http://github.com/',
    author='Fabio Cingottini',
    author_email='fabio.cingottini@gmail.com',
    license='MIT',
    packages=['cli_utils'],
    zip_safe=False
)
