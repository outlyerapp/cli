from setuptools import setup, find_packages
from outlyer import __version__, __title__

if __name__ == "__main__":
    setup(
        name=__title__,
        description = 'Outlyer Command line Utility',
        version=__version__,
        license='MIT',
        url='https://github.com/outlyerapp/cli',
        download_url='https://github.com/outlyerapp/cli/archive/0.1.tar.gz',
        author='Colin Hemmings',
        author_email='colin.hemmings@outlyer.com',
        keywords=['outlyer', 'cli'],
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Natural Language :: English",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: Implementation :: CPython",
            "Programming Language :: Python :: Implementation :: PyPy",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
        install_requires=[
            'click==6.7'
        ],
        entry_points={
            'console_scripts': ['outlyer=outlyer.cli:main'],
        },
        packages=find_packages(exclude=['tests']),
    )
