from setuptools import setup

setup(
    name     = 'hpp',
    version  = '0.0.0',
    packages = ['src', 'config'],

    install_requires = [
        'munch',
        'pandas',
        'pyqt5',
        'pyinstaller',
        'python-dotenv',
        'requests',
        'xlsxwriter',
    ],

    entry_points = {
        'console_scripts': [
            'hpp = src.__main__:main',
        ],
    }
)
