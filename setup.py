import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LogTool", # Replace with your own username
    version="0.0.1",
    author="Arkady Shtempler",
    author_email="arkadysh@gmail.com",
    description='Extract unique Errors from logs using provided "start time" timestamp',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zahlabut/LogToolPyPi",
    #packages=setuptools.find_packages(),
    packages=['LogTool'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords='logs, analyzing log, LogTool, zahlabut, openstack, redhat',
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
        'GitHub': 'https://github.com/zahlabut/LogTool',
        'Article': 'https://opensource.com/article/20/1/logtool-root-cause-identification',
        'Source': 'https://github.com/zahlabut/LogToolPyPi'}
)



