from setuptools import setup, find_packages

requirements = [
    'torch',
    'numpy',
    'opencv-python',
]

setup(
    name='pytorch_retinaface',
    version='1.0',

    description="Python package for Pytorch_Retinaface implementation by biubug6 (https://github.com/biubug6/Pytorch_Retinaface)",

    url='https://github.com/ReneLutz/Pytorch_Retinaface',
    author='Rene Lutz',

    packages=find_packages(),

    python_requires='>=3',
    install_requires=requirements,

    classifiers=[
        'Intended Audience :: Developers',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
    ]
)