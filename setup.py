from setuptools import setup, find_packages

VERSION = '0.0.1'


setup(
    name="winterbloom-mkdocs-theme",
    version="0.0.1",
    url='https://github.com/theacodes/winterbloom_mkdocs_theme',
    license='MIT',
    description='',
    author='Alethea Flowers',
    author_email='thea@winterbloom.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'winterbloom = winterbloom_mkdocs_theme',
        ]
    },
    zip_safe=False
)