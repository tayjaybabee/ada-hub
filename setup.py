from setuptools import setup


setup(
        name='ada-hub',
        version='0.2.0',
        packages=[ 'ada_hub' ],
        url='https://softworks.inspyre.tech/ada-hub',
        license='MIT',
        author='Taylor-Jayde Blackstone',
        author_email='t.blackstone@inspyre.tech',
        description='An application that allows one to monitor their environment.',
        entry_points={
                'console_scripts': [
                        'ada_hub=ada_hub:main',
                ],
        },
        keywords='temperature humidity'
)
