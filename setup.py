  
from setuptools import setup, find_packages


setup(
    name='mkdocs-pagenav-generator',
    version='1.0.0',
    description='Generates a navigation for pages within same subdirectory for the page itself.',
    long_description='mkdocs-pagenav-generator is a very simplistic plugin, which allows you to generate a navigation '
                     'inside a page which will list all other pages within the same directory and any subdirectory of '
                     'it. This plugin requires the awesome-pages plugin for MkDocs to work and uses any ``.pages.yml`` '
                     'used in the directory to generate the nav according to its settings.',
    keywords='mkdocs python markdown wiki',
    url='https://github.com/andre/mkdocs-pagenav-generator/',
    author='Lukas Geiter',
    license='MIT',
    python_requires='>=3.5',
    install_requires=[
        'mkdocs>=1',
        'wcmatch>=7',
        'mkdocs-awesome-pages-plugin>=2.5.0'
    ],
    packages=find_packages(exclude=['*.tests', '*.tests.*']),
    entry_points={
        'mkdocs.plugins': [
            'pagenav-generator = mkdocs_pagenav_generator.plugin:NavGeneratorPlugin'
        ]
    }
)
