#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import codecs

from setuptools import setup, find_packages


# Used to load the `README.rst` file from disk later.
here = os.path.abspath(os.path.dirname(__file__))

tests_require = [  # We require these packages when running tests.
		'coverage',  # Capture code execution coverage.
		'pytest',  # The main test runner.
		'pytest-cov',  # Coverage reporting integration.
		'pytest-flakes',  # Code linting integration.
		'pytest-capturelog',  # Python logging capture, for display with test failures.
	]


setup(
		name = "web.app.wiki",
		version = "1.0",
		
		# Additional project metadata.
		
		description = "An example portable Wiki application and add-on for WebCore.",
		long_description = codecs.open(os.path.join(here, 'README.rst'), 'r', 'utf8').read(),  # Load from file.
		url = "https://github.com/marrow/tutorial/tree/wiki",  # Primary site address is on GitHub.
		download_url = "https://github.com/marrow/tutorial/releases",  # Downloads are available here.
		author = "Alice Bevan-McGregor",
		author_email = "alice@gothcandy.com",
		license = "MIT",
		keywords = ['web.app', 'WebCore', 'marrow'],  # Make our package discoverable using keywords.
		classifiers = [  # "Trove Classifiers", ref: https://pypi.python.org/pypi?%3Aaction=list_classifiersA
				"Development Status :: 5 - Production/Stable",
				"Environment :: Console",
				"Environment :: Web Environment",
				"Intended Audience :: Developers",
				"License :: OSI Approved :: MIT License",
				"Natural Language :: English",
				"Operating System :: OS Independent",
				"Programming Language :: Python",
				"Programming Language :: Python :: 3",
				"Programming Language :: Python :: 3 :: Only",
				"Programming Language :: Python :: 3.3",
				"Programming Language :: Python :: 3.4",
				"Programming Language :: Python :: 3.5",
				"Programming Language :: Python :: Implementation :: CPython",
				"Topic :: Internet :: WWW/HTTP :: Dynamic Content",
				"Topic :: Software Development :: Libraries",
				"Topic :: Software Development :: Libraries :: Python Modules",
			],
		
		# Code-related settings.
		
		packages = find_packages(exclude=['test']),  # Our test modules aren't installable.
		include_package_data = True,  # Include additional files in the bundled package.
		package_data = {'': [  # Include these files in bundled packages, like .egg files.
				'README.rst',
				'LICENSE.txt'
			]},
		
		namespace_packages = [  # We include our own package under `web.app`, also list parents.
				'web',
				'web.app',
			],
		
		setup_requires = [  # Conditionally include the test runner if asked to run tests.
				'pytest-runner',
			] if {'pytest', 'test', 'ptr'}.intersection(sys.argv) else [],
		
		tests_require = tests_require,  # Include our test helper packages.
		
		install_requires = [
				'WebCore>=2.0.3,<3',  # The underlying web framework.
				'web.db',  # Database connectivity layer for WebCore.
				'marrow.mongo',  # Database connectivity and schema + query system for MongoDB.
				'web.dispatch.object',  # Object (class-based filesystem-like) dispatch for endpoint discovery.
				'web.dispatch.resource',  # Resource (based on REQUEST_METHOD) dispatch for endpoint discovery.
				'cinje',  # Template engine, an importable Python domain-specific code transformer / language.
			],
		
		extras_require = dict(
				development = tests_require,  # Also include our test helper packages, in development.
			),
		
		entry_points = {  # Plugins we define.
				}
	)
