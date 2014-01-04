mempy.org
=========
This is the website for the Memphis Python User group. It's
generated with pelican_.

deploy
------

This site is hosted in cloud files. To generate the site and deploy:

::

    # Generate any new content
	pelican -s settings.py content

    # upload to the correct container
	swiftcontainer mempy
    cd output && swiftupload .


.. _`pelican`: http://alexis.notmyidea.org/pelican/
