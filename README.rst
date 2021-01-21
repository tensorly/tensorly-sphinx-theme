=====================
TensorLy Sphinx Theme
=====================

This is the `TensorLy <tensorly.org>`_ theme for `Sphinx <https://www.sphinx-doc.org/en/master/>`_ documentations,
based on `Bulma <https://bulma.io>`_.

Installation
============

After cloning this repository, simply run:

.. code:: bash

    pip install -e .


Usage 
=====

To use the theme in your project, add the following to the `conf.py` file of your sphinx documentation:

.. code:: python

   html_theme = "tensorly_sphinx_theme"


Configuration
=============

Project logo
------------
The logo of your project will be used in the navigation bar. You can specify the path to it in your `conf.py`:

.. code:: rst

    html_logo = '_static/image.png'


Navigation and main options
---------------------------

You can set most of the parameters in your sphinx configuration file (`conf.py`). 

The options are:

* `'google_analytics'` : str, your Google analytics ID, if any.
* `'nav_links'` :  tuple list, a list of ('Link display name', 'local.file'), contains the links to the local documentation, in the top navigation bar.
* `'external_nav_links'` : same as above but contains external links.

Example:

.. code:: rst

    html_theme_options = {
        'google_analytics' : 'YOUR_GOOGLE_ANALYTICS_ID',
        'nav_links' : [('Install', 'installation'), 
                    ('User Guide', 'user_guide/index')]
        'external_nav_links' : [('TensorLy', 'https://github.com/tensorly/tensorly'),
                                ('TensorLy-Torch', 'https://github.com/tensorly/torch')]
    }


In rst files
------------

In your documentation itself, you can use `no-toc`, :no-localtoc: and `no-pagination` 
to remove the side-menu's table of content (toc), local toc ("on this page") 
and pagination buttons, respectively.
For instance, if you don't want `file.rst` to have a toc, simply add in the file:

.. code::

    :no-toc:
