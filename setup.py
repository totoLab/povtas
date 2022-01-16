import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='povtas',  
    version='0.1',
    scripts=['povtas'] ,
    author="Antonio Labate",
    author_email="totolab@gmail.com",
    description="Turns every r of a word in a v.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/totolab/povtas",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)