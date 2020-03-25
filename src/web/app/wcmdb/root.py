from webob.exc import HTTPFound
from datetime import datetime # Python's standard date + time object.

from pymongo.errors import DuplicateKeyError

# Get a reference to our Movie resource class.
from .movie import Movie
from .model import MovieDetail as D

class Wcmdb:
	"""Basic movie information database"""

	__dispatch__ = 'resource' # The WCMDB is a collection of pages, so use resource dispatch.
	__resource__ = Movie # Declare the type of resource we contain.
	__collection__ = 'movies'

	def __init__(self, context, collection=None, record=None):
		"""Executed when the root of the site (or children) are accessed, on each request."""
		self._ctx = context # Store the "request context" for later use.
		self.__collection__ = context.db[self.__collection__] # Get a reference to the collection we use.

	def __getitem__(self, name):
		"""Load data for the Movie with the given name."""

		data = self.__collection__.find_one(D.name == name)

		if not data: # If no record was found, populate some default data.
			data = D(name)
		else:
			data = D.from_mongo(data) # Otherwise, wrap in our model object

		return data

	def get(self):
		"""Called to handle direct requests to the web root itself."""
		return HTTPFound(location=str(self._ctx.path.current / 'Home')) # Issue the redirect

	def post(self, name, content):
		"""Save a new movie to the database."""

		try:
			result = self.__collection__.insert_one(D(name, content))

		except DuplicateKeyError:
			return {
				'ok': False,
				'reason': 'duplicate',
				'message': "A movie with that name already exists.",
				'name': name,
			}

		# All is well so we inform the client.
		return {
			'ok': True,
			'acknowledged': result.acknowledged,
			'name': result.inserted_id
		}
