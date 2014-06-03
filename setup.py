from distutils.core import setup
setup(name='GReader',
	url='http://cuarentaydos.com/',
	author='Luis Lopez',
	author_email='luis@cuarentaydos.com',
	version='0.0.1',
	packages = ['GReader'],
	package_dir = {'GReader': 'GReader'},
	description = 'Small library to access a subset of Google Reader API',
	license = 'GPL-2'
	)
