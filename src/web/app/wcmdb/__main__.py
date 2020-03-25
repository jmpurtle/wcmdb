# Enable the use of cinje templates.
__import__('cinje') # Doing it this way prevents an "imported but unused" warning.

from web.core import Application

# Get references to web framework extensions.
from web.ext.annotation import AnnotationExtension
from web.ext.debug import DebugExtension
from web.ext.serialize import SerializationExtension
from web.ext.db import DatabaseExtension

# Get a reference to our database connection adapter.
from web.db.mongo import MongoDBConnection

# Get a reference to our WCMDB root object.
from web.app.wcmdb.root import Wcmdb

app = Application(Wcmdb, extensions=[
		AnnotationExtension(),
		DebugExtension(),
		SerializationExtension(),
		DatabaseExtension(MongoDBConnection("mongodb://localhost/test")),
	])

if __name__ == "__main__":
	app.serve('wsgiref')