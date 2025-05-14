# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'cntmosaic'
copyright = '2025, sss'
author = 'xxx'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  'sphinx.ext.napoleon',
  'sphinx.ext.autodoc',
  'sphinx.ext.viewcode',
  'sphinx-copybutton',
  'myst_parser',
  'nbsphinx'
]
# Support notebook files
nbsphinx_execute = 'never'  # Use pre-executed notebooks
nbsphinx_allow_errors = True
autoclass_content = 'both'

source_suffix = {
  '.rst': 'restructuredtext',
  '.txt': 'markdown',
  '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_title = 'Contact Mosaic documentation'
html_theme_options = {
  'repository_url': 'https://github.com/ShozenD/high_res_brc',
  'use_repository_button': True
}
html_static_path = ['_static']

import sys
from pathlib import Path

sys.path.insert(0, str(Path('../../').resolve()))

