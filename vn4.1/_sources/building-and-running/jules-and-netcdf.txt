JULES and NetCDF
================

JULES can be built with or without the NetCDF libraries, however building JULES without NetCDF limits the functionality of JULES.

If JULES is built without NetCDF libraries, it will use a dummy NetCDF library which allows the program to build but provides no functionality. Any attempt to use NetCDF files as input with this option will result in a runtime error. All input files must be columnar ASCII, meaning that the user is restricted to running at a single point only. Output files will automatically use a columnar ASCII format with headers. File formats are discussed in more details in :doc:`/input/overview`.

To build JULES with NetCDF, it must be told where to find the NetCDF library files. JULES needs two pieces of information - the directory containing the NetCDF archive files, ``netcdf.a`` and ``netcdff.a`` (the *'NetCDF library path'*), and the directory containing the NetCDF Fortran 90 module file, ``netcdf.mod`` (the *'NetCDF include path'*). In a standard NetCDF install, these are often ``/usr/lib`` and ``/usr/include`` or ``/usr/local/lib`` and ``/usr/local/include`` respectively.

If the ``nc-config`` program is installed on your system (run ``which nc-config`` to find out), this can be used to determine values for the NetCDF library path (``nc-config --flibs``) and NetCDF include path (``nc-config --includedir``). When JULES is built with NetCDF, users can supply either ASCII or NetCDF input files, and all output will be NetCDF.
