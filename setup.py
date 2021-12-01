"""Setup for the binance_candles package."""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Alexander Marinov",
    author_email="amarinov@gmail.com",
    name='binance-candles',
    license="MIT",
    description='Provides python generator for crypto currency 1 min candles via Binance Socket API',
    version='v0.0.1',
    long_description=README,
    url='https://github.com/shaypal5/chocobo',
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=['python-binance==1.0.15'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry'
    ],
)