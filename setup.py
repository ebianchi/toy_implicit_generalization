from setuptools import setup

setup(
   name='toy_implicit_generalization',
   version='1.0',
   description=f'Toy examples of the generalizability of implicit methods ' \
               + 'in building accurate dynamics models.',
   author='Bibit Bianchini',
   author_email='bibit@seas.upenn.edu',
   packages=['toy_implicit_generalization'],
   install_requires=[
      'matplotlib',
      'numpy'
   ],
)
