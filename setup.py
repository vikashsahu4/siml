from setuptools import setup

setup(
		name='siml',
		version='0.1',
		description='Machine Learning algorithms implemented from scratch',
		url='https://github.com/taspinar/siml',
		author='Ahmet Taspinar',
		author_email='taspinar@gmail.com',
		license='MIT',
		packages=['twitterscraper'],
		install_requires=[
          'numpy', 
		  'math'
      ],
		zip_safe=False
		)