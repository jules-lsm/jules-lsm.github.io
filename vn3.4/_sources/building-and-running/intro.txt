==========================
Building and running JULES
==========================


Building a JULES executable requires a Fortran 95 compiler with a preprocessor (i.e. any modern Fortran compiler) and either FCM or a version of the make utility. The Fortran 90 NetCDF interface library is required to use gridded data (i.e. data for more than a single location). All of this software is freely available:

* GFortran, the GNU GCC Fortran compiler - http://www.gnu.org/software/gcc/fortran/.
* FCM - http://www.metoffice.gov.uk/research/collaboration/fcm.
* GNU make - http://www.gnu.org/software/make/.
* NetCDF libraries - http://www.unidata.ucar.edu/software/netcdf/.

.. note::
   To build JULES with the ability to run multiple points in parallel, there are additional software requirements. These are discussed in more detail in :doc:`parallel`.

JULES has only been tested on Linux but, given a suitable Fortran compiler, should run on any Unix-like system with minimal changes. The recommended way to attempt to run JULES on Windows is via the Linux compatability layer `Cygwin <http://www.cygwin.com/>`_, although this is untested.

For more information, see the following sections:

.. toctree::
   :maxdepth: 2
   
   jules-and-netcdf
   building-jules
   running-jules
   parallel

