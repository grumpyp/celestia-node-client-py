from setuptools import setup, find_packages

setup(
    name='celestia_node',
    version='0.0.3',
    author='Patrick Gerard',
    author_email='hallo@patrickgerard.de',
    description='Celestia Node Python SDK',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/grumpyp/celestia-node-client-py',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    keywords='blockchain celestia node sdk client',
    install_requires=[
        'requests>=2.26.0',
        'loguru>=0.7.0'
    ],
    python_requires='>=3.8',
)
