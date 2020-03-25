WebCore Wiki Tutorial / Example
===============================

This is a sample Wiki application for WebCore, using marrow.mongo and RESTful Resource Dispatch.

In order to run the example, you will want to:

1. Create a virtual environment to house the project by running::

      python3.5 -m venv wiki

2. Activate the virtual environment::

      cd wiki
      source bin/activate

3. Check out a copy of this code into the environment::

      git clone -b wiki https://github.com/amcgregor/WebCore-Tutorial.git src

4. Install the project, which will pull in any required dependencies::

      cd src
      python setup.py develop

5. Make sure you have MongoDB running locally.

6. Run the example in the development web server::

      python -m web.app.wiki

That's about it.  To follow the tutorial, `browse the commit history on GitHub`_, starting at the oldest commit and working your way up.  Each commit is generally accompanied by an extensive commit message describing what changed and providing any further instructions related to that change.

Happy hacking!


Embedding a Wiki in your own Application
----------------------------------------

As of commit `78ccad1`_ the example wiki implementation is relocatable to paths other than the root, and as of commit `e163ee4`_ the collection used to store articles is configurable. Being entirely reusable, now, you can embed a wiki in your own application very easily:

.. code:: python

   from web.app.wiki.root import Wiki
   
   class YourApplicationRoot:
       wiki = Wiki

This will attach a wiki to your application, accessible as ``/wiki``. If you wish to override the name of the collection used to store articles you can subclass ``Wiki`` and override the ``__collection__`` attribute:

.. code:: python

   from web.app.wiki.root import Wiki
   
   class YourApplicationRoot:
       class wiki(Wiki):
           __collection__ = 'articles'

.. _browse the commit history on GitHub: https://github.com/amcgregor/WebCore-Tutorial/commits/wiki

.. _78ccad1: https://github.com/amcgregor/WebCore-Tutorial/commit/78ccad1ffbbf84295d74b151534eb9f9383c5bc5
.. _e163ee4: https://github.com/amcgregor/WebCore-Tutorial/commit/e163ee44a3256eed906bbe4b7109a8f8c1c074f0

