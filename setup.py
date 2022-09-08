from setuptools import find_packages, setup
setup(
    name='bibgrafo',
    packages=find_packages(include=['bibgrafo']),
    version='1.0.4',
    description='Biblioteca para ensino de Teoria dos Grafos',
    author='Henrique do Nascimento Cunha',
    install_requires=[
          'multipledispatch',
    ],
    license='MIT',
)