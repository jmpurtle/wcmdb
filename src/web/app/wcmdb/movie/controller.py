
class MoviesController:
	"""Endpoints for a movie."""

	__collection__ = 'movies'

	def __init__(self, context):
		self._ctx = context # The "request context" we were constructed for.

	def __call__(self):
		return "Delivering the collection"

	def __getattr__(self, slug='foo'):
		""" Return the collection """
		if not slug:
			return "Delivering the collection in getattr"

		""" Return an individual instance of a movie """
		return "I am a movie named {slug}".format(slug=slug)

	def get(self):
		return 'hi'

	def post(self, name, content):
		pass

	def delete(self):
		pass
