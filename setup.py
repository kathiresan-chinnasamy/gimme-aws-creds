from setuptools import setup, find_packages

import gimme_aws_creds

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='gimme aws creds',
    version=gimme_aws_creds.version,
    install_requires=requirements,
    author='kathiresan chinnasamy',
    author_email='kchinnasamy@ghx.com',
    description="A CLI to get temporary AWS credentials from Okta",
    url='https://github.com/kathiresan-chinnasamy/gimme-aws-creds',
    license='Apache License, v2.0',
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite="tests",
    scripts=['bin/gimme-aws-creds', 'bin/gimme-aws-creds.cmd'],
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: Apache Software License'
    ]
)
