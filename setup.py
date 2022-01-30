from setuptools import setup

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name='airignis',
	version='0.0.1',
	url="https://github.com/Subvael/Airignis",
	author="Subvael",
	author_email="Subvael@gmail.com",
	description='Looking for a C# familiar package to handle events or looking for a very practical and '
				'intuitive way to schedule periodically launching auto event? Then this package is for you.',
	py_modules=["airignis/autoevent",
				"airignis/duetime",
				"airignis/event"],
	package_dir={'': 'src'},
	classifiers=[
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10",
		"License :: OSI Approved :: MIT",
		"Operating System :: OS Independent",
	],
	long_description=long_description,
	long_description_content_type="text/markdown",
	extras_require={
		"dev":[
			"alabaster==0.7.12"
			"attrs==21.4.0"
			"Babel==2.9.1"
			"certifi==2021.10.8"
			"cffi==1.15.0"
			"charset-normalizer==2.0.10"
			"coverage==6.3"
			"cryptography==36.0.1"
			"docutils==0.17.1"
			"entrypoints==0.3"
			"idna==3.3"
			"imagesize==1.3.0"
			"importlib-metadata==4.10.1"
			"iniconfig==1.1.1"
			"jeepney==0.7.1"
			"Jinja2==3.0.3"
			"keyring==18.0.1"
			"MarkupSafe==2.0.1"
			"packaging==21.3"
			"pluggy==1.0.0"
			"py==1.11.0"
			"pycparser==2.21"
			"Pygments==2.11.2"
			"pyparsing==3.0.7"
			"pytest==6.2.5"
			"pytest-cov==3.0.0"
			"python-dateutil==2.7.5"
			"pytz==2019.3"
			"requests==2.27.1"
			"SecretStorage==3.3.1"
			"six==1.16.0"
			"snowballstemmer==2.2.0"
			"Sphinx==4.4.0"
			"sphinx-rtd-theme==1.0.0"
			"sphinxcontrib-applehelp==1.0.2"
			"sphinxcontrib-devhelp==1.0.2"
			"sphinxcontrib-htmlhelp==2.0.0"
			"sphinxcontrib-jsmath==1.0.1"
			"sphinxcontrib-qthelp==1.0.3"
			"sphinxcontrib-serializinghtml==1.1.5"
			"toml==0.10.2"
			"tomli==2.0.0"
			"urllib3==1.26.8"
			"zipp==3.7.0"
		],
	},
)
