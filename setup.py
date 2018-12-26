from setuptools import find_packages, setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='django-coverage',
    version='0.1.0',
    license='MIT',
    description='Adds coverage reporting to Django test command',
    long_description=readme(),
    keywords='django test coverage',
    author='Vacasa, LLC',
    author_email='opensource@vacasa.com',
    url='https://github.com/vacasa/django-coverage',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=[
        'django',
        'coverage'
    ],
    zip_safe=False
)
