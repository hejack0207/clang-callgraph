# vim: sts=-1 sw=4 fdm=marker

from setuptools import setup

setup(name='clang-callgraph',
    version='0.0.1',
    description='clang call graph',
    keywords='tools clang',
    author='hejack0207',
    author_email='hejack0207@gmail.com',
    license='MIT',
    url='https://github.com/hejack0207/clang-callgraph',
    python_requires=">=3.7",
    install_requires=["clang==6.0.0.2"],
    packages=['lib'],
    entry_points={
        'console_scripts': [
            'clang-callgraph = lib.clang_callgraph:main'
        ]
    }
)
