from setuptools import setup, find_packages

setup(
    name='diabetes_prediction_project',
    version='0.1',
    packages=find_packages(include=['src', 'src.*']),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'pyyaml'
    ],
    entry_points={
        'console_scripts': [
            'diabetes-predict=main:main'
        ]
    },
    author='Your Name',
    description='Diabetes prediction using machine learning',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    license='MIT'
)