from setuptools import find_packages, setup
setup(
    name='bibgrafo',
    packages=find_packages(include=['bibgrafo', 'multipledispatch']),
    version='0.9.5',
    description='Biblioteca para ensino de Teoria dos Grafos',
    author='Henrique do Nascimento Cunha',
    license='MIT',
)