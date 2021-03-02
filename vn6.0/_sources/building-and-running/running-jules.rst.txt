Running JULES
=============

The user interface of JULES consists of several files with the extension ``.nml`` containing Fortran namelists. These files and the namelist members are documented in more detail in :doc:`/namelists/contents`. These namelists are grouped together in a single directory. That directory is referred to as the *namelist directory* for a JULES run. In most use cases, this is practically abstracted away by the use of the rose/cylc workflow. This provides a GUI and rich ecosystem for integration of JULES into a larger workflow (eg compile-run-analyse).

Once a :doc:`JULES executable is compiled <fcm>` and the :doc:`namelists </namelists/contents>` are set up, JULES can be run in one of two ways:

1. Run the JULES executable in the namelist directory with no arguments:

   .. code-block:: bash
   
      cd /path/to/namelist/dir
      /path/to/jules.exe
      
2. Run the JULES executable with the namelist directory as an argument:

   .. code-block:: bash
   
      /path/to/jules.exe  /path/to/namelist/dir
      
      
.. warning::
   Any relative paths given to JULES via the namelists (e.g. :nml:mem:`JULES_FRAC::file` in :nml:lst:`JULES_FRAC`) will be interpreted *relative to the current working directory*.
   
   This means that if the user plans to use the second method to run JULES (e.g. in a batch environment), it is advisable to use fully-qualified path names for all files specified in the namelists.
   
   To allow runs to be portable across different machines, it is common to specify data files relative to the namelist directory. In this case, JULES must be run using the first method to allow the relative paths to be resolved correctly.


General example of running JULES from the command line
---------------------------------------------------------

#. Move into the JULES root directory (the directory containing ``includes``, ``src`` etc.):

   .. code-block:: bash

       $ cd /jules/root/dir
    
#. Build JULES:

   .. code-block:: bash

       $ fcm make -f etc/fcm-make/make.cfg

#. Move into the namelist directory:

   .. code-block:: bash

       $ cd /path/to/namelist/dir

#. Run the JULES executable:

   .. code-block:: bash

       $ /path/to/jules.exe


Running JULES with OpenMP
-------------------------

If JULES is compiled with OpenMP, then it must be told how many OpenMP threads to use. This is done using the environment variable ``OMP_NUM_THREADS``:

.. code-block:: bash

    $ export OMP_NUM_THREADS=4  # Use 4 threads for OpenMP parallel regions
    $ /path/to/jules.exe
    
    
Running JULES with MPI
----------------------

When running JULES using MPI, JULES attempts to find a suitable decomposition of the grid depending on how many MPI tasks are made available to it. Each MPI task can then be thought of as its own independent version of JULES, with each task being responsible for a portion of the grid. Each task reads its portion of the input file(s), performs calculations on those points and outputs its portion of the output file(s). Tasks only communicate in order to read and write dump files - this ensures that dump files are consistent regardless of decomposition, i.e. a dump from any run (MPI or not; different numbers of MPI tasks), can be used to (re-)start any other run and produce identical results, providing the overall model grids are the same.

None of the namelists or namelist members are parallel-specific - the same :doc:`JULES namelists </namelists/contents>` can be used to run JULES with or without MPI, and the final results will be identical.

If JULES is compiled with MPI, then it must be run using commands from your MPI distribution (usually called ``mpiexec`` and/or ``mpirun``):

.. code-block:: bash

    $ mpirun -n 4 /path/to/jules.exe  # Run JULES using 4 MPI tasks
    
Detailed discussion of ``mpiexec``/``mpirun`` is beyond the scope of this document - please refer to the documentation for your chosen MPI distribution for the available options and features.
