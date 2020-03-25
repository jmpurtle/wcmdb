# Enable the use of cinje templates.
__import__('cinje')  # Doing it this way prevents an "imported but unused" warning.

# Get a reference to the Application class.
from web.core import Application

# Get references to web framework extensions.
from web.ext.annotation import AnnotationExtension  # Built-in to WebCore.
from web.ext.debug import DebugExtension
from web.ext.serialize import SerializationExtension  # New in 2.0.3!
from web.ext.db import DatabaseExtension  # From external dependency: web.db

# Get a reference to our database connection adapter.
from web.db.mongo import MongoDBConnection  # From extenral dependency: marrow.mongo

# Get a reference to our Wiki root object.
from web.app.wiki.root import Wiki


# This is our WSGI application instance.
app = Application(Wiki, extensions=[
		# Extensions that are always enabled.
		AnnotationExtension(),  # Allows us to use Python 3 function annotations.
		SerializationExtension(),  # Allows the return of mappings from endpoints, transformed to JSON.
		DatabaseExtension(MongoDBConnection("mongodb://localhost/test")),
	] + ([
		# Extensions that are only enabled in development or testing environments.
		DebugExtension()  # Interactive traceback debugger, but gives remote code execution access.
	] if __debug__ else []))


# If we're run as the "main script", serve our application over HTTP.
if __name__ == "__main__":
	app.serve('wsgiref')

