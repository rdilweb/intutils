import setuptools

setuptools.setup(
    name="intutils",
    version="3.1.0",
    author="Reece Dunham",
    author_email="me@rdil.rocks",
    license="MIT",
    packages=setuptools.find_packages(),
    include_package_data=True,
    url="https://github.com/rdilweb/intutils",
    description="Basic integer manipulation library.",
    python_requires=">3.3",
    project_urls={
        "Documentation": "https://docs.rdil.rocks/libraries/intutils/"
    },
    keywords=[
        "int",
        "integer",
        "utils",
        "util",
        "utilities"
    ],
    package_data={
        'intutils': ['py.typed'],
    },
    zip_safe=False,
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown"
)
