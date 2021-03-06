from setuptools import setup, find_packages

VERSION = '0.2.3'
PKG_KEYWORDS = ('NoSQL', 'persistent', 'storage', 'key-value',
                'store', 'redis', 'leveldb', 'lmdb', 'database')
PKG_LONG_DESCRIPTION = """
Cupboard is an abstracted interface to a variety of 
key-value storage systems. Cupboard can serve as a drop-in 
replacement for a dictionary under most usages and can 
be backed by a variety of key-value storage systems. Fine 
grained control over marshalling and lower level 
features specific to different backends are 
configurable in contexts. Cupboard reduces cognitive overhead while enforcing 
best practices in key-value store usage. In addition, Cupboard provides an 
easy-to-use function memoization decorator that, once again, is backend 
agnostic.
"""


setup(
    name='Cupboard',
    version=VERSION,
    description=('Abstracted interface for a variety '
                 'of key-value storage systems.'),
    author='Luke de Oliveira',
    author_email='lukedeo@vaitech.io',
    url='https://github.com/vaitech/Cupboard',
    license='Apache 2.0',
    install_requires=['future'],
    download_url='https://github.com/vaitech/Cupboard/archive/{}.tar.gz'.format(
        VERSION),
    long_description=PKG_LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=' '.join(PKG_KEYWORDS),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    extras_require={
        'all': ['redis', 'lmdb', 'plyvel'],
        'lmdb': ['lmdb'],
        'redis': ['redis'],
        'leveldb': ['plyvel'],
        'tests': ['numpy', 'pytest', 'pytest-cov', 'pytest-pep8',
                  'pytest-xdist', 'python-coveralls']
    }
)
