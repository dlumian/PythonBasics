from setuptools import setup, find_packages

setup(
    name='examplepackage',
    version='0.0.0',
    author='Your Name',
    author_email='myemail@mail.com',
    description='Brief description of package.',
    long_description=open('PackageGuide.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/username/package_repo',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'seaborn',
        'matplotlib',
        'scikit-learn',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
