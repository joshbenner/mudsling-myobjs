from setuptools import setup, find_packages


setup(
    name='mudsling-myobjs',
    license='MIT',
    author='Josh Benner',
    author_email='josh@bennerweb.com',

    packages=find_packages(),
    include_package_data=True,
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    install_requires=['mudsling'],

    entry_points={
        'mudsling.plugin': [
            'myobjs = myobjs:MyObjsPlugin'
        ]
    }
)
