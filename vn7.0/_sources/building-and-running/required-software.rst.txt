Required software
=================

Building a JULES executable requires FCM and one of the supported Fortran compilers (see :doc:`fcm`). The Fortran 90 NetCDF interface library is required to use gridded data (i.e. data for more than a single location).

To be able to automatically upgrade namelists between JULES versions or use a GUI to configure JULES runs, Rose is required.

All of this software is freely available:

*   GFortran, the GNU GCC Fortran compiler - http://www.gnu.org/software/gcc/fortran
*   FCM - http://metomi.github.io/fcm/doc
*   Rose - http://metomi.github.io/rose/doc/html/index.html
*   NetCDF libraries - http://www.unidata.ucar.edu/software/netcdf

JULES has only been tested on Linux but, given a suitable Fortran compiler, should run on any Unix-like system with minimal changes. The recommended way to attempt to run JULES on Windows is via the Linux compatability layer `Cygwin <http://www.cygwin.com/>`_, although this is untested.


Building JULES with NetCDF
--------------------------

To build JULES with NetCDF, it must be told where to find the NetCDF library files. JULES needs two pieces of information - the directory containing the NetCDF archive files, ``netcdf.a`` and ``netcdff.a`` (the *'NetCDF library path'*), and the directory containing the NetCDF Fortran 90 module file, ``netcdf.mod`` (the *'NetCDF include path'*). In a standard NetCDF install, these are often ``/usr/lib`` and ``/usr/include`` or ``/usr/local/lib`` and ``/usr/local/include`` respectively.

If the ``nc-config`` program is installed on your system (run ``which nc-config`` to find out), this can be used to determine values for the NetCDF library path (``nc-config --flibs``) and NetCDF include path (``nc-config --includedir``). When JULES is built with NetCDF, users can supply either ASCII or NetCDF input files, and all output will be NetCDF.


Building and running JULES with MPI
-----------------------------------

.. warning:: For advanced users only

In order to build and run JULES with MPI, additional software is required:

#.  An implementation of MPI compiled using the same compiler you will be using to compile JULES. Several implementations of MPI are available, the most commonly used being `MPICH2 <http://www.mpich.org/>`_ and `OpenMPI <http://www.open-mpi.org/>`_.

    .. note:: The ``bin`` directory of your MPI installation must be in your ``$PATH``

#.  A version of HDF5/NetCDF4 compiled *with parallel I/O enabled*, using the MPI implementation installed above. This is *not* the default way to compile NetCDF, and must be explicitly enabled. More information on how to do this can be found on the `NetCDF website <http://www.unidata.ucar.edu/software/netcdf/docs/getting_and_building_netcdf.html#build_parallel>`_.
