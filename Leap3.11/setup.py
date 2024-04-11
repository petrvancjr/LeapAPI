from setuptools import setup, find_packages

setup(
    name='Leap',
    version='3.11.0',
    description='Leap Motion for Python 3.11',
    url='',
    author='Petr Vanc',
    author_email='petr.vanc@cvut.cz',
    license='BSD 2-clause',
    packages=[''],
    py_modules=['Leap'],
    install_requires=['numpy',
                      ],
    package_data={'': ['libLeap.so', 'LeapPython.so']},
    include_package_data=True,
    entry_points='''
        [console_scripts]
        Leap=Leap:Leap
    ''',

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.11',
    ],
)
