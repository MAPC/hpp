from setuptools import setup

setup(
    name     = 'hpp',
    version  = '0.0.0',
    packages = ['src', 'config'],

    install_requires = [
        'Jinja2==3.1.2',
        'munch==3.0.0',
        'pandas==1.3.5',
        'python-dotenv==0.21.1',
        'requests==2.31.0',
        'XlsxWriter==3.1.2',
    ],

    entry_points = {
        'console_scripts': [
            'hpp = src.__main__:main',
        ],
    }
)
