import sys
from setuptools import setup
main = 'ezrp.py'

if (sys.platform == 'darwin'):
	extra_options = dict(
		setup_requires=["py2app"],
		options=dict(py2app=dict(argv_emulation=True))
	)
elif (sys.platform == 'win32'):
	extra_options = dict(
		setup_requires=["py2exe"]
	)
else:
	extra_options = dict(
		scripts=[main]
	)
setup(
    app=[main],
	**extra_options
)