from .template import render
from .model import WikiArticle as D


class Article:
	"""A wiki article."""
	
	__dispatch__ = 'resource'
	
	def __init__(self, context, wiki, page):
		"""Prepare an article for manipulation."""
		
		self._ctx = context  # The "request context" we were constructed for.
		self._wiki = wiki  # The parent (containing) Wiki instance.
		self._page = page  # The data associated with the page we represent.
	
	def get(self):
		"""Retrieve the article data or render an HTML page containing the article."""
		
		candidates = ['text/html'] + list(self._ctx.serialize.types)  # Allowable mime types.
		match = self._ctx.request.accept.best_match(candidates, default_match='text/html')
		
		if match == 'text/html':  # If the client wants HTML, we render the template.
			return render(self._ctx, self, self._page)  # Render an HTML page for the content.
		
		return self._page  # Let the serialization extension handle other cases for us.
	
	def post(self, content):
		"""Update the in-database content for the current article.
		
		This will create the article if one by this name doesn't already exist.
		"""
		
		# Update a page with our name.
		result = self._wiki.__collection__.update_one(
				D.name == self._page.name,  # A query identifying the document to update.
				{  # The following are the MongoDB update operations to apply to the document.
					'$set': {'content': content},  # Update the page content.
					'$currentDate': {'modified': True}  # Also update the last-modified time.
				}
			)
		
		if not result.matched_count:  # Nothing was updated... so let's create instead.
			return self._wiki.post(self._page['_id'], content)  # You are totally allowed to do this.
		
		return {
				'ok': True,
				'acknowledged': result.acknowledged,
				'name': self._page['_id'],
			}
	
	def delete(self):
		"""Delete this page from the wiki."""
		
		# Attempt to delete a page with our name.
		result = self._wiki.__collection__.delete_one(D.name == self._page.name)
		
		if not result.deleted_count:  # Nothing was deleted?  We probably didn't exist!
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

