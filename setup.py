import sys
from setuptools import setup
main = 'ezrp.py'

if (sys.platform == 'darwin'):
	extra_options = dict(
		setup_requires=["py2app"],
		options=dict(py2app=dict(argv_emulation=True))
	)
elif (sys.platform == 'win32'):
	from cx_Freeze import setup, Executable
	extra_options = dict(
		setup_requires=["cx_Freeze"],
		options = {"build_exe": build_exe_options},
		executables = [Executable(main, base="Win32GUI")]
	)
else:
	extra_options = dict(
		scripts=[main]
	)
setup(
	name = "ezrp",
	version = "1.0.0-alpha2",
    app=[main],
	**extra_options
)