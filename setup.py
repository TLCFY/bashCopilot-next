from setuptools import setup, find_packages

setup(
    name='bashcopilot',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Dependencies will be added here
    ],
    entry_points={
        'console_scripts': [
            'bcopilot = bashcopilot.cli:main',
        ],
    },
    author='Your Name', # Replace with actual author name
    author_email='your.email@example.com', # Replace with actual email
    description='Linux command line intelligent assistant application',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/TLCFY/bashCopilot-next', # Replace with actual URL if different
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
