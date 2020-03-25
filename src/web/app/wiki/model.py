from datetime import datetime

from marrow.mongo import Document
from marrow.mongo.field import String, Date


class WikiArticle(Document):
	name = String('_id')  # The primary key is the URL accessible name of the page, often called a "slug".
	content = String()  # The HTML (currently), Markdown (in the future) content of the article.
	created = Date(default=datetime.utcnow, assign=True)  # The creation time of the document.
	modified = Date(default=datetime.utcnow, assign=True)  # The last modification time of the document.
	
	def __repr__(self):
		"""The "programmer's representation" of this document.
		
		Used in logging and interactive debugger contexts.
		"""
		
		return "{self.__class__.__name__}({self.name}, created={created}, modified={modified})".format(
				self = self,
				created = self.created.isoformat(),
				modified = self.modified.isoformat(),
			)
