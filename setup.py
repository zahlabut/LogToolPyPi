from setuptools import setup, find_packages
import pathlib
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')
setup(
    name='LogTool',  # Required
    version='0.0.2.8',  # Required
    description='Extract unique Errors from logs using provided "start time" timestamp',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/zahlabut/LogToolPyPi",
    author='Arkady Shtempler',
    author_email='arkadysh@gmail.com',
    keywords='log files, log, analyze log, statistics, zahlabut, openstack, redhat',
    package_dir={'': 'src'},  # Optional
    packages=find_packages(where='src'),  # Required
    python_requires='>=3.5, <4',
    package_data={  # Optional
        'conf_file': ['conf.ini'],
    },
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/zahlabut/LogToolPyPi/issues',
        'Articles': 'https://opensource.com/article/20/1/logtool-root-cause-identification',
        'Source': 'https://github.com/zahlabut/LogToolPyPi/',
    },
)