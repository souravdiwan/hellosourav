from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='souravtools',
    version='0.1.2',
    description='Useful tools to work with Elastic stack in Python',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Sourav Diwan',
    author_email='soura_diwan@rediffmail.com',
    keywords=['HELLO'],
    url='https://github.com/souravdiwan/hellosoureav',
    download_url='https://pypi.org/project/souravdiwan/'
)

# install_requires = [
#     'elasticsearch>=6.0.0,<7.0.0',
#     'jinja2'
# ]

if __name__ == '__main__':
    setup(**setup_args)