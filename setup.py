from setuptools import find_packages, setup

setup(
    name="the-littlest-jupyterhub",
    version="1.0.0.dev0",
    description="A small JupyterHub distribution",
    url="https://github.com/jupyterhub/the-littlest-jupyterhub",
    author="Jupyter Development Team",
    author_email="jupyter@googlegroups.com",
    license="3 Clause BSD",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "ruamel.yaml==0.17.*",
        "jinja2",
        "pluggy==1.*",
        "passlib",
        "backoff",
        "requests",
        "bcrypt",
        "jupyterhub-traefik-proxy==0.3.*",
    ],
    entry_points={
        "console_scripts": [
            "tljh-config = tljh.config:main",
        ]
    },
)
