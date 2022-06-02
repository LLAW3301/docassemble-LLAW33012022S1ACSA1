import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012022S1ACSA1',
      version='0.0.1',
      description=('S2 Final'),
      long_description="**AnglicareSA Appts Reminder Web-App**\r\n\r\nOur application is an appointment reminder system, created for the staff\r\nto use at AnglicareSA. It sends out six email reminders to each client\r\nwith a PDF entailing the location and time details. It can be edited by\r\nstaff in case of appointment changes, and it automatically sends\r\nreminders.\r\n\r\n**Authors**\r\n\r\nErica Boram You, Melanie O'Callaghan, Chloe Lambrusco, and Bailey\r\nBunnik\r\n\r\nOrganisation: Flinders University\r\n",
      long_description_content_type='text/markdown',
      author='Erica You',
      author_email='you0022@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://github.com/LLAW3301/docassemble-LLAW33012022S1ACSA1',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012022S1ACSA1/', package='docassemble.LLAW33012022S1ACSA1'),
     )

