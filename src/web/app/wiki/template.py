# encoding: cinje

: from cinje.std.html import page

: def render context, article, doc
: using page doc.name
: classes = {'wiki'}

: if 'content' not in doc
	: classes.add('placeholder')
: end

<article&{class_=classes}>
	#{getattr(doc, 'content', "<i>No content.</i>")}
</article>

