Considerations
==============

Depending on your use case, there are two main things that you need to consider:

Do I need NetCDF?
-----------------

`NetCDF <http://www.unidata.ucar.edu/software/netcdf/>`_ is a data format (and associated software libraries) specifically designed for large-scale scientific data. It has two major benefits over raw binary data:
    
1.  It is machine-independent, so `endianness <http://en.wikipedia.org/wiki/Endianness>`_ is not an issue when moving datasets between machines
2.  It is self-describing, so as well as containing raw data, NetCDF files also contain metadata describing the data (e.g. variable names, units, origin). Many tools are capable of exploiting this metadata to simplify processing.

JULES can be built with or without NetCDF, however *building JULES without NetCDF limits the functionality of JULES*. Without NetCDF, JULES will use a dummy NetCDF library which allows the program to build but provides no functionality. Any attempt to use NetCDF files as input with this option will result in a runtime error. All input files must be columnar ASCII, meaning that the user is restricted to running at a single point only. Output files will automatically use a columnar ASCII format with headers. File formats are discussed in more detail in :doc:`/input/overview`.


Do I need parallel processing?
------------------------------

.. note::
    For running JULES at a single point, parallel processing provides no advantage. However, if JULES is already compiled with OpenMP or MPI enabled, it is still possible to run a single point by simply specifying the number of OpenMP threads and/or MPI tasks to be 1.
        
JULES is capable of exploiting parallel processing techniques to reduce processing time for distributed/gridded simulations. There are two different methods JULES can use:
    
OpenMP
    `OpenMP <http://en.wikipedia.org/wiki/OpenMP>`_ is a form of compiler-assisted parallelisation that uses directives for shared-memory, loop-level parallelism across multiple cores on a machine (OpenMP is *not* capable of utilising a cluster of machines).
        
    This form of parallelism is not as effective as MPI, but may provide some speedup and does not require a specially compiled NetCDF library.
    
MPI
    `MPI (Message Passing Interface) <http://en.wikipedia.org/wiki/Message_Passing_Interface>`_ is a standardised message passing interface. MPI coordinates the running of multiple 'tasks' in parallel, potentially on several machines (or nodes), and provides mechanisms for these tasks to communicate with each other.
        
    JULES takes advantage of the parallel I/O features available in `HDF5 <http://www.hdfgroup.org/HDF5/>`_ and `NetCDF4 <http://www.unidata.ucar.edu/software/netcdf/>`_, which enable multiple MPI tasks to read from and write to the same NetCDF file(s) at the same time. These features must be explicitly enabled when NetCDF is compiled (see :doc:`required-software`).

It is also possible to use MPI and OpenMP together, where each MPI task has a number of OpenMP threads, however this is very advanced and beyond the scope of this document.
