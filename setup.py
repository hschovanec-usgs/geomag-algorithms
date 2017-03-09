from distutils.core import setup

setup(
    name='geomag-algorithms',
    version='0.2.2',
    description='USGS Geomag IO Library',
    url='https://github.com/usgs/geomag-algorithms',
    packages=[
        'geomagio',
        'geomagio.algorithm',
        'geomagio.binlog',
        'geomagio.edge',
        'geomagio.iaga2002',
        'geomagio.imfv122',
        'geomagio.imfv283',
        'geomagio.metadata',
        'geomagio.metadata.observatory',
        'geomagio.pcdcp',
        'geomagio.temperature',
        'geomagio.vbf'
    ],
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy',
        'obspy',
        'pycurl'
    ],
    scripts=[
        'bin/geomag.py',
        'bin/make_cal.py'
    ]
)
