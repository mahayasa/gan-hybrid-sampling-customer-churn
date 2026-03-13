
from setuptools import setup, find_packages

setup(
    name='ctganenn',
    version='1.0.7',
    packages=find_packages(),
    install_requires=[
        'scikit-learn==1.6.1',
        'sdv==1.18.0',
        'pandas==2.0.3',
        # Add any dependencies your package needs
    ],
    author='Mahayasa Adiputra',
    author_email='mahayasa.a@kkumail.com',
    description='CTGAN-ENN : Tabular GAN-based Hybrid sampling method',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    license='',
)