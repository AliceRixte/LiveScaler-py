from setuptools import setup

setup(
    
    name = 'livescaler', 
    
    version = '0.0.0',
    
    description = 'A python library implementing the affine transformations of LiveScaler, aiming to transform live the harmony of an electronic music piece',
    
    py_modules = ["LiveScaler"],
    
    package_dir = {'':'src'},
    
    # If you have many modules included in your package, you want to use the following parameter instead of py_modules.
#     packages = ['ThePackageName1',
#                 'ThePackageName2',
#                 ...
#  ],
    

    author = 'Alice Rixye',
    author_email = 'alice.rixte@u-bordeaux.fr',
    
    long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    long_description_content_type = "text/markdown",
    
    url='https://github.com/autonym8/LiveScaler-py',
    
    include_package_data=True,
    

    # Here is a full list of what you can put here:
    
    # https://pypi.org/classifiers/

    classifiers  = [
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "License :: OSI Approved :: BSD License",
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Topic :: Multimedia :: Sound/Audio :: MIDI ',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: OS Independent',
    ],
    
    
    # This part specifies all the dependencies of your package. 
    # "~=" means the users will need a minimum version number of the dependecies to run the package.
    # If you specify all the dependencies here, you do not need to write a requirements.txt separately like many others do.
    
    install_requires = [
    ],
    
    keywords = ['Live Music'],
    
)
