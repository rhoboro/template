from setuptools import setup, find_packages


def main():
    setup(
        name='template',
        version='0.1',
        author='rhoboro',
        author_email='rhoboro@gmail.com',
        maintainer='rhoboro',
        maintainer_email='rhoboro@gmail.com',
        py_modules=['template'],
        install_requires=[
            'Click',
        ],
        entry_points='''
            [console_scripts]
            template=template:cmd
        ''',
        classifiers=[
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
        ],
    )


if __name__ == '__main__':
    main()
