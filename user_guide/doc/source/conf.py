# -*- coding: utf-8 -*-
#
# Joint UK Land Environment Simulator (JULES) User Guide build configuration file, created by
# sphinx-quickstart on Thu Mar 21 11:40:02 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# Add the sphinxext directory to the Python search path
# Remember that when this script is executed, the current working directory is the directory containing this file
sys.path.insert(0, os.path.abspath('../sphinxext'))


# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    # Sphinx extensions
    'sphinx.ext.todo', 'sphinx.ext.imgmath', 'sphinx.ext.mathjax',
    # Custom extensions
    'sphinx_nml_domain', 'pygments_fortran_nml_lexer', 'pygments_fcm_make_conf_lexer'
]

# Use nitpicky mode so that bad cross-references are flagged
nitpicky = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Joint UK Land Environment Simulator (JULES)'
copyright = u'2023'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '7.4'
# The full version, including alpha/beta/rc tags.
release = '7.4'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

highlight_language = 'nml'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'nature'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "%s v%s User Guide" % (project, version)

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "jules_logo_html.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add extra CSS files here to remove the need for a layout.html
# template override file
html_css_files = [
    'jules-tweaks.css',
]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'JULES_User_Guide'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
  'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
  'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
  'fontenc' : '\\usepackage[LGR,T1]{fontenc}',

# Remove the blank pages that result from formatting for double sided printing
  'classoptions': ',openany,oneside',
  'babel' : '\\usepackage[english]{babel}'
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'JULES_User_Guide.tex', u'Joint UK Land Environment Simulator (JULES) User Guide',
   u'Met Office', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "jules_logo_pdf.png"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'JULES_User_Guide', u'Joint UK Land Environment Simulator (JULES) User Guide',
     [u'Met Office'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'JULES_User_Guide', u'Joint UK Land Environment Simulator (JULES) User Guide',
   u'Met Office', 'JULES', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# Linkcheck options
# Initially, ignore all broken links
linkcheck_ignore = [
    r"https://code.metoffice.gov.uk/.*",
    r"https://www.nag.co.uk/nag-compiler",
    r"https://doi.org/10.3354/cr00899",
    r"https://puma.nerc.ac.uk/trac/JULES",
    r"https://doi.org/10.1007/BF0038623",
    r"http://docs.cray.com/.*",
    r"http://cylc.github.io/cylc/",
    r"http://jules.jchmr.org/content/.*",
    r"http://nora.nerc.ac.uk/10890/1/dadson_etal_2010_g2gtrip.pdf",
    r"http://www.borenv.net/BER/pdfs/ber15/ber15-501.pdf",
    r"http://www.unidata.ucar.edu/software/netcdf/docs/.*",
    r"https://.*wiley.com/.*",
    r"https://www.liebertpub.com/.*",
    r"https://royalsocietypublishing.org/.*",
    ]

# Bump the limit up a bit
linkcheck_retries = 3

