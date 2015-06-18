Building and running JULES in parallel mode
===========================================


.. warning::
   This section is for advanced users only.
   
.. note::
   Before reading this section, users should be familiar with how to build and run JULES in serial (i.e. non-parallel) mode (see :doc:`building-jules` and :doc:`running-jules`).
   
   Currently, building JULES in parallel mode is only supported with the :doc:`FCM make build system <fcm>` (i.e. JULES *cannot* be built in parallel mode with GNU make).
   

Overview
--------

From version 3.3 onwards, in order to reduce processing time, JULES is able to run multiple points in parallel. This parallel processing can use multiple cores on the same machine, a cluster of machines, or both. To achieve this, JULES uses `MPI (Message Passing Interface) <http://en.wikipedia.org/wiki/Message_Passing_Interface>`_, a standardised message passing interface. MPI coordinates the running of multiple 'tasks' in parallel, and provides mechanisms for these tasks to communicate with each other when required (e.g. for sharing results).

JULES takes advantage of the parallel I/O features available in `HDF5 <http://www.hdfgroup.org/HDF5/>`_/`NetCDF4 <http://www.unidata.ucar.edu/software/netcdf/>`_, which themselves use MPI 'under the hood'. These features enable multiple MPI tasks to read from and write to the same NetCDF file(s) at the same time.

When running JULES in parallel, each MPI task can be thought of as its own independent version of JULES, with each task being responsible for a portion of the grid. Each task reads its portion of the input file(s), performs calculations on those points and outputs its portion of the output file(s). Tasks only communicate with each other in order to read and write dump files - this ensures that the dump files produced with different numbers of tasks are compatible with each other. This means that you can use a dump from a serial (i.e. non-parallel) run to (re-)start a parallel run, providing the overall model grids are the same (and vice versa).

None of the namelists or namelist members are parallel-specific - the same :doc:`JULES namelists </namelists/contents>` can be used to run JULES in serial or parallel mode, and the final results will be identical. The only difference is that, when compiled and run in parallel mode, JULES is able to utilise multiple cores and/or machines.

To compile and run JULES in parallel, MPI-specific commands must be used. The configuration of the MPI tasks available to JULES (number of tasks, which machines to use, etc.) is specified at run-time using these commands (see :ref:`running-jules-in-parallel-mode`). JULES will then attempt to find a suitable decomposition of the grid depending on how many MPI tasks are made available to it.

.. note::
   For running JULES at a single point, compiling and running JULES in parallel mode provides no advantage.
   
   However, if JULES is already compiled in parallel mode, it is still possible to run a single point by simply specifying the number of MPI tasks to be 1.


Required software
-----------------

In order to build and run JULES in parallel mode, three pieces of software are required:

1. A Fortran compiler (and associated C compiler). This will be referred to as the *underlying compiler*.

2. An implementation of MPI compiled using that compiler.

   Several implementations of MPI are available, the most commonly used being `MPICH2 <http://www.mpich.org/>`_ and `OpenMPI <http://www.open-mpi.org/>`_.
   
   .. note::
      The ``bin`` directory of your MPI installation must be in your ``$PATH`` to allow FCM make to find the MPI utilities required to build JULES in parallel mode.
      
      Specifically, FCM make must be able to find ``mpif90``. ``mpif90`` is a wrapper around the *underlying compiler* (see above) that 'injects' the MPI dependencies automatically.

3. A version of HDF5/NetCDF4 compiled *with parallel I/O enabled*, using the MPI implementation installed above.

   This is *not* the default way to compile NetCDF, and must be explicitly enabled. More information on how to do this can be found on the `NetCDF website <https://www.unidata.ucar.edu/software/netcdf/docs/build_parallel.html>`_.
   
   
Building JULES in parallel mode
-------------------------------

.. note::
   Building JULES in parallel mode can only be done using FCM. Make sure you have read and understood the section on :doc:`building JULES in serial mode using FCM <fcm>` first.
   
Building JULES in parallel mode uses the same FCM make configuration file as building in serial mode, i.e. ``etc/fcm-make/make-local.cfg``. This means that the same environment variables used when building JULES in serial mode (see :ref:`fcm-make-environment-variables`), *plus one additional environment variable*, are used to determine how JULES should be built in parallel mode:

``JULES_CFG_COMP``
    Used to select settings for the *underlying compiler*.
    
    The permitted values are the same as those for building in serial mode.
    
``JULES_CFG_BLD``
    Used to select the type of build.
    
    Again, the permitted values are the same as those for building in serial mode.
    
``JULES_CFG_ARCH``
    As when building in serial mode, this can override ``JULES_CFG_COMP`` and ``JULES_CFG_BLD`` to provide compiler related settings if the *underlying compiler* is not one of the common compilers.
    
``JULES_CFG_NCDF``
    Path to a file containing NetCDF related settings.
    
    Like building in serial mode, this file must update ``$fflags`` and ``$ldflags`` to enable JULES to compile and link with the NetCDF libraries. However, compiling HDF5 with parallel I/O enabled means that shared libraries cannot be built - this means that all the libraries that NetCDF is dependent on must also be specified at link time.
    
    For example, assuming all the libraries (zlib, HDF5, NetCDF4) have been installed in ``/home/jblogs/utils``, the NetCDF configuration file would like something like:
    
    .. code-block:: fcm_make
    
       $fflags = $fflags -I/home/jblogs/utils/include     
       $ldflags = $ldflags -L/home/jblogs/utils/lib -lnetcdff -lnetcdf -lhdf5_hl -lhdf5 -lz -lm
       
    Notice that we must explicitly declare all the libraries we are dependent on - the NetCDF Fortran library (``-lnetcdff``), the NetCDF C library (``-lnetcdf``), HDF5 (``-lhdf5_hl -lhdf5``) and zlib (``-lz``). On some systems, the math library must also be included (``-lm``).
    
    .. note::
       Note that, as when building in serial mode, this still defaults to ``etc/fcm-make/ncdf/netcdf-dummy.cfg`` meaning a dummy NetCDF library will be used.
   
``JULES_CFG_MPI``
    Used to determine the MPI settings to use.
    
    .. note::
        Defaults to ``etc/fcm-make/mpi/mpi-dummy.cfg``. This will build JULES using a dummy MPI library, and parallel runs will not be possible.
        
        This is exactly how building JULES in serial mode works. 
        
    To compile JULES with MPI enabled, this should be set to ``$HERE/mpi/use-mpi.cfg``.
    
    
Example of building JULES in parallel mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here, we build a JULES executable with MPI enabled, using the Intel compiler as our underlying compiler:

.. code-block:: bash
   
   export JULES_CFG_COMP=intel
   export JULES_CFG_NCDF=/path/to/netcdf-config.cfg
   # '\' must be used to escape the $ to prevent the shell expanding $HERE as a variable
   export JULES_CFG_MPI=\$HERE/mpi/use-mpi.cfg       
   
   fcm make -f etc/fcm-make/make-local.cfg
   
where ``/path/to/netcdf-config.cfg`` looks like:

.. code-block:: fcm_make

   $fflags = $fflags -I/path/to/netcdf/include     
   $ldflags = $ldflags -L/path/to/netcdf/lib -lnetcdff -lnetcdf -lhdf5_hl -lhdf5 -lz -lm
   
This will create an MPI-enabled JULES executable at ``build/bin/jules.exe``.


.. _running-jules-in-parallel-mode:

Running JULES in parallel mode
------------------------------

Once JULES has been compiled with MPI enabled, it can be run in parallel mode. To do this, the commands ``mpiexec`` and ``mpirun`` should be used. For example, to run JULES using 4 tasks on the current machine, with namelists in ``/path/to/namelist/dir``, the following command could be used:

.. code-block:: bash

   mpirun -n 4 /path/to/jules.exe /path/to/namelist/dir

Detailed discussion of ``mpiexec`` and ``mpirun`` is beyond the scope of this document - please refer to the documentation for your chosen MPI implementation for the available options and features.
