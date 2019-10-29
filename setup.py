import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rosbackup",
    version="1.1.0",
    author="Mario Harjac",
    author_email="m@harja.ch",
    description="RouterOS config backup tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mharjac/rosbackup",
    packages=setuptools.find_packages(),
    install_requires=['netmiko'],
    entry_points={
        'console_scripts': [
            'rosbackup = rosbackup.main:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
