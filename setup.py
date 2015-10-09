from setuptools import setup

setup(
    name='Flask-ABTester',
    version='1.0',
    url='https://github.com/arjpuriCMU/ABTester',
    license='',
    author='Arjun Puri',
    author_email='arjunpur@andrew.cmu.edu',
    description='ab tests',
    long_description=__doc__,
    # if you would be using a package instead use packages instead
    # of py_modules:
    packages=['flask-abtester'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'Redis>=2.4.13'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
