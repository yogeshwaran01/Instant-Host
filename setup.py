from setuptools import setup

with open("README.md", "r") as file_obj:
    des = file_obj.read()

setup(
    name="instanthost",
    version="1.1",
    license="MIT",
    url="https://github.com/yogeshwaran01/Instant-Host",
    description="A cli tool to host any non-binary files",
    long_description=des,
    long_description_content_type="text/markdown",
    author="Yogeshwaran R",
    author_email="yogeshin247@gmail.com",
    py_modules=["instanthost"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    download_url="https://raw.githubusercontent.com/yogeshwaran01/Instant-Host/master/instanthost.py",
    entry_points="""
        [console_scripts]
        instanthost=instanthost:main
    """,
)
