# Python's standard date + time object.
from datetime import datetime

# HTTP status code exception for "302 Found" redirection.
from webob.exc import HTTPFound

# MongoDB exceptions that may be raised when manipulating data.
from pymongo.errors import DuplicateKeyError

# Get a reference to our Article resource class and data model.
from .article import Article
from .model import WikiArticle as D  # Shortened due to to repeated use.


class Wiki:
	"""Basic multi-article editable wiki."""
	
	__dispatch__ = 'resource'  # The Wiki is a collection of pages, so use resource dispatch.
	__resource__ = Article  # Declare the type of resource we contain.
	__collection__ = 'articles'  # The default collection name to use when bound.
	__home__ = 'Home'  # The default homepage users are directed to if requesting the root.
	
	def __init__(self, context, collection=None, record=None):
		"""Executed when the root of the site (or children) are accessed, on each request."""
		
		self._ctx = context  # Store the "request context" for later use.
		self.__collection__ = context.db[self.__collection__]  # Get a reference to the collection we use.
	
	def __getitem__(self, name):
		"""Load data for the Article with the given name."""
		
		# Attempt to locate a document by that name.
		data = self.__collection__.find_one(D.name == name)
		
		if not data:  # If no record was found, populate some default data.
			data = D(name)  # Creation and modification times are constructed for us.
		else:
			data = D.from_mongo(data)  # Otherwise, wrap in our model object.
		
		return data
	
	def get(self):
		"""Called to handle direct requests to the web root itself."""
		
		# Redirect users to the default home page.
		return HTTPFound(location=str(self._ctx.path.current / self.__home__))
	
	def post(self, name, content):
		"""Save a new article to the database."""
		
		try:
			# Insert an article with the given name and content.
			result = self.__collection__.insert_one(D(name, content))
		
		except DuplicateKeyError:
			return {
					'ok': False,
					'reason': 'duplicate',
					'message': "An article with that name already exists.",
					'name': name,
				}
		
		# All is well, so we inform the client.
		return {
				'ok': True,
				'acknowledged': result.acknowledged,
				'name': result.inserted_id
			}

