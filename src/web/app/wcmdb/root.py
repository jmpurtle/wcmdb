from webob.exc import HTTPFound
from datetime import datetime # Python's standard date + time object.

from pymongo.errors import DuplicateKeyError

# Get a reference to our Film resource class.
from .movie.controller import MoviesController
from .movie.model import MovieDetail as D

class Wcmdb:
	"""Basic IMDB clone"""

	# Object Dispatching
	movies = MoviesController

	def __init__(self, context):
		"""Executed when the root of the site (or children) are accessed, on each request."""
		self._ctx = context # Store the "request context" for later use.

	def __call__(self):
		return "I am the root"

	def get(self):
		"""Called to handle direct requests to the web root itself."""
		return HTTPFound(location=str(self._ctx.path.current / 'Home')) # Issue the redirect
