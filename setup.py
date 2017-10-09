from setuptools import setup, find_packages

setup(
    name='cdm',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cdm= cdm.main:cdm_main',
            'cdc= cdc.main:cdc_main',
        ]
    },
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
)
