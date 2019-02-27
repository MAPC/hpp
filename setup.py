from setuptools import setup

setup(
    name     = 'hpp',
    version  = '0.0.0',
    packages = ['src'],

    install_requires = [
        'pyqt5',
    ],

    entry_points = {
        'console_scripts': [
            'hpp = src.__main__:main',
        ],
    }
)
