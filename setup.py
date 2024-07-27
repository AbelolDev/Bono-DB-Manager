from setuptools import setup, find_packages

setup(
    name='Bono-DB-Manager',
    version='0.1.0',
    author='AbelolDev',
    author_email='aaravenaortiz4@gmail.com',
    description='Una librería para gestionar bases de datos SQLite de manera sencilla',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AbelolDev/Bono-DB-Manager',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[],
    include_package_data=True,
    package_data={},
)
