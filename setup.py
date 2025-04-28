import os
from typing import List

from setuptools import find_packages
from distutils.core import setup

__version__ = "1.53.0.6"

dependencies = [
    'grpcio',
]


def find_stub_files(name: str) -> List[str]:
    result = []
    for root, dirs, files in os.walk(name):
        for file in files:
            if file.endswith('.pyi') or file == 'py.typed':
                if os.path.sep in root:
                    sub_root = root.split(os.path.sep, 1)[-1]
                    file = os.path.join(sub_root, file)
                result.append(file)
    return result


with open('README.md', 'r') as f:
    readme = f.read()

package_data = {
    'grpc-stubs': find_stub_files('grpc-stubs'),
    'grpc_channelz-stubs': find_stub_files('grpc_channelz-stubs'),
    'grpc_health-stubs': find_stub_files('grpc_health-stubs'),
    'grpc_reflection-stubs': find_stub_files('grpc_reflection-stubs'),
    'grpc_status-stubs': find_stub_files('grpc_status-stubs'),
}

setup(
    name="grpc-stubs",
    version=__version__,
    description='Mypy stubs for gRPC',
    long_description=readme,
    long_description_content_type='text/x-rst',
    license='MIT',
    url="https://github.com/shabbyrobe/grpc-stubs",
    author="Blake Williams",
    author_email="code@shabbyrobe.org",
    py_modules=[],
    python_requires='>=3.6',
    install_requires=dependencies,
    packages=[
        'grpc-stubs',
        'grpc_channelz-stubs',
        'grpc_health-stubs',
        'grpc_reflection-stubs',
        'grpc_status-stubs',
        *find_packages(exclude=['scripts']),
    ],
    package_data=package_data,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ]
)
