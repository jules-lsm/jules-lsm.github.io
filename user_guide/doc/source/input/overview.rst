Input files for JULES
=====================


The recommended file format for use with JULES is NetCDF, although an ASCII format is also supported for data at a single location only. NetCDF is recommended since in this format, the metadata are provided in a standardised manner that many other tools and applications can interpret. The file handling code of JULES is written in a modular way that aims to make it easy for the user to add support for other file formats if they desire. Any user that does this is strongly encouraged to contribute their code back to the community.


.. toctree::
   principles
   ascii
   netcdf
   file-name-templating
   temporal-interpolation
