from setuptools import setup

URL = "https://unit8co.github.io/darts/"
PROJECT_URLS = {
    "Bug Tracker": "https://github.com/unit8co/darts/issues",
    "Documentation": URL,
    "Source Code": "https://github.com/unit8co/darts",
}


setup(
    name="darts",
    version="0.16.1",
    description="A python library for easy manipulation and forecasting of time series.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    project_urls=PROJECT_URLS,
    url=URL,
    maintainer="Unit8 SA",
    maintainer_email="darts@unit8.co",
    license="Apache License 2.0",
    packages=find_packages(),
    install_requires=all_reqs,
    package_data={
        "darts": ["py.typed"],
    },
    zip_safe=False,
    python_requires=">=3.7",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    keywords="time series forecasting",
)
