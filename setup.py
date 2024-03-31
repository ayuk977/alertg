from setuptools import setup, find_packages


setup(
    name="alertg",
    version="1.0.2",
    license="MIT",
    url="https://github.com/ayuk977/alertg",
    author="Zackzonexx",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author_email="ayuk977@gmail.com",
    packages=find_packages(),
    keywords="alertg",
    classifiers=[
        "License :: OSI Approved :: MIT License",  # Specify your license type
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Natural Language :: English",
    ],
    install_requires=[
        "opsgenie-sdk",
        "requests",
        "urllib3",
        "dmacheck",
    ],
    entry_points={
        "console_scripts": [
            "alertg=alertg.app:main",
        ],
    },
    project_urls={
        "Source": "https://github.com/ayuk977/alertg",
    },
    zip_safe=False,
)
