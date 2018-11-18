from setuptools import find_packages, setup

setup(
    name="zergling",
    version="0.1.0-beta",
    description="RESTful API performance testing",
    classifiers=[
        "License :: MIT License",
        "Programming Launcuage :: Python 3.7"
    ],
    author="Radu Pluta",
    license="MIT",
    install_requires=["gevent>=1.2.2", "flask>=0.10.1", "requests>=2.9.1", "msgpack>=0.4.2", "six>=1.10.0", "pyzmq>=16.0.2"],
    test_suite='zergling.test',
    test_require=["mock"]
)
