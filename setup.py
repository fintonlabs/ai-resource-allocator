from setuptools import setup, find_packages

setup(
    name='ai-resource-allocation',
    version='0.1.0',
    description='AI-powered tool for analyzing workload data and dynamically allocating computing resources.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'numpy==1.21.2',
        'pandas==1.3.3',
        'scikit-learn==0.24.2',
        'tensorflow==2.6.0',
        'requests==2.26.0'
    ],
)