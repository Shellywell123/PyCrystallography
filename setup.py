from setuptools import setup, find_packages

# with open("README.md", "r") as f:
#     README = f.read()

setup(
    name='PyCrystallography',
    version='0.1.1',
    description='Python 3 package being written to illustrate crystallography',
    long_description='Python 3 package being written to illustrate crystallography', # fix readme import
    long_description_content_type='text/markdown',
    author='Shellywell123',
    url='https://github.com/Shellywell123/PyCrystallography',
    packages=find_packages(),
    install_requires=[
        'matplotlib>=3.3.2',
        'numpy>=1.19.2',
        'imageio>=2.9.0'
    ],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    zip_safe=False
)