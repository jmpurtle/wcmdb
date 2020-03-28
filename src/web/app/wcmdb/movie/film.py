from .view.template import render
from .model import FilmDetail as D

class Film:
	"""A film."""

	__dispatch__ = 'resource'

	def __init__(self, context, wcmdb, page):
		self._ctx = context # The "request context" we were constructed for.
		self._wcmdb = wcmdb # The parent (containing) Wcmdb instance
		self._page = page # The data associated with our current Wcmdb page.

	def get(self):
		"""Retrieve the film data or render an HTML page containing the film."""

		candidates = ['text/html'] + list(self._ctx.serialize.types)
		match = self._ctx.request.accept.best_match(candidates, default_match='text/html')

		if match == 'text/html':
			return render(self._ctx, self, self._page) # Render an HTML page for the content.

		return self._page # Let the serialization extension handle this for us.

	def post(self, content):
		"""Update the in-database content for the current film.

		This will create the film if one by this name doesn't already exist.
		"""
		result = self._wcmdb.__collection__.update_one(
			D.name == self._page.name, # a query identifying the document to update.
			{ # The following are the MongoDB update operations to apply to the document.
				'$set': { 'content': content}, # Update the page content.
				'$currentDate': {'modified': True} # Also update the last-modified time.
			})

		if not result.matched_count: # Nothing was updated... so let's create instead.
			return self._wcmdb.post(self._page['_id'], content)

		return {
			'ok': True,
			'acknowledged': result.acknowledged,
			'name': self._page['_id'],
		}

	def delete(self):
		"""Delete this page from the wiki."""

		result = self._wcmdb.__collection__.delete_one(D.name == self._page.name)

		if not result.deleted_count: # Nothing was deleted? We probably didn't exist!
			return {
				'ok': False,
				'reason': 'missing',
				'message': "Cowardly refusing to delete something which does not exist.",
				'name': self._page['_id'],
			}

		return {
			'ok': True,
			'acknowledged': result.acknowledged,
			'name': self._page['_id'],
		}
