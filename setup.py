import setuptools, os, sys, platform, shutil

pkgname = "delphimodule"
  
def get_release_version():
    lcals = locals()
    gbals = globals()
    with open(os.path.join(os.getcwd(), pkgname, "__version__.py"), "rt") as opf:
        opffilecontents = opf.read()
        retvalue = exec(opffilecontents, gbals, lcals)
    versorigstr = lcals["__version__"]
    return versorigstr     

versnewstr = get_release_version()   

with open("README.md", "r") as fh:
  long_description = fh.read()     

setuptools.setup(
  name=pkgname,
  version=versnewstr,
  description="Delphi FMX for Python",
  author="Lucas Belo, Jim McKeeth",
  author_email="lucas.belo@live.com",
  long_description=long_description,
  long_description_content_type="text/markdown",
  license="Other/Proprietary License",
  license_files=["LICENSE.md"],
  url = "https://github.com/Embarcadero/DelphiFMX4Python",
  python_requires=">=3.3<=3.10",
  packages=[pkgname],
  classifiers=[            
            'Intended Audience :: Developers',
            'Topic :: Software Development',
            'License :: Other/Proprietary License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3 :: Only',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'Operating System :: Unix',
            'Operating System :: MacOS',
            'Operating System :: Android',                        
        ]
)
