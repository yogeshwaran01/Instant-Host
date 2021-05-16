from setuptools import setup

setup(
    name="instanthost",
    version="0.1",
    url="https://github.com/yogeshwaran01/Instant-Host",
    description="Host pages from the Terminal",
    author="Yogeshwaran R",
    author_email="yogeshin247@gmail.com",
    license="MIT",
    install_requires=["Click", "requests"],
    py_modules=["instanthost"],
    entry_points="""
        [console_scripts]
        instanthost=instanthost:run
    """,
)
