"""Sphinx configuration file for a Rubin Telescope and Site package

This configuration only affects single-package Sphinx documentation builds.
"""

from documenteer.conf.pipelinespkg import *  # noqa

project = "ts_opensplics_rpm"
html_theme_options["logotext"] = project  # noqa
html_title = project
html_short_title = project
doxylink = {}  # Avoid warning: Could not find tag file _doxygen/doxygen.tag
intersphinx_mapping["ts_opensplice_rpm"] = ("https://ts-opensplice_rpm.lsst.io", None)
