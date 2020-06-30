from setuptools import setup

setup(
    name='fiveDayForecast',
    version='0.1',
    pymodules=['fiveDayForecast'],
    install_requires=[
        'Click', 'Requests'
    ],
    entry_points='''
    [console_scripts]
    fiveDayForecast=fiveDayForecast:cli
    '''
)