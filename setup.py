from setuptools import setup, find_packages

setup(
    name='dev-scripts',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # your dependencies
    ],
    entry_points={
        'console_scripts': [
            'fl-create-page=scripts.flutter.create_page:main',
            # add other scripts here
        ],
    },
    include_package_data=True,
    package_data={
        '': ['templates/**/*'],
    },
)