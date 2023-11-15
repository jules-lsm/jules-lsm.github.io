Building JULES using FCM
========================

FCM is a code management and build system developed by the Met Office with a particular focus on simplifying the process of building large Fortran programs. In this section, we will be using the build tool - FCM make.

As part of the build process, FCM make will analyse the dependencies of every Fortran file and automatically compile them in the correct order.

FCM make must be given a configuration file that it uses to determine how to build the source code. Extensive documentation on FCM make configuration files is `available online <http://metomi.github.io/fcm/doc/user_guide/make.html>`_.

Help pages for the FCM make command itself (rather than the configuration file) can be accessed using the command:

.. code-block:: bash

    fcm help make
    
The FCM configuration file for building JULES is ``etc/fcm-make/make.cfg``. This file uses the environment variables below to determine the settings to use when compiling JULES.

Running FCM make with this configuration file will create some files and directories in the specified build directory (see the ``-C`` option of ``fcm make``; defaults to the current working directory). The JULES executable will be produced in the specified build directory at ``build/bin/jules.exe``.


.. _fcm-make-environment-variables:

Environment variables used when building JULES using FCM make
-------------------------------------------------------------

``JULES_PLATFORM``
    Used to select settings for a pre-defined platform. The default values of other variables may depend on the choice of this setting; differences from the generic defaults are included in the descriptions below.
    
    .. note::
        If you have many users using the same platform to run JULES, you may want to contribute a suitable platform configuration.
    
    +----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Permitted value            | Purpose                                                                                                                                                      |
    +============================+==============================================================================================================================================================+
    | ``custom``                 | **Default.** Use a custom configuration entirely determined by the other environment                                                                         |
    |                            | variables. The default values of those variables are set in this platform's configuration file.                                                              |
    +----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``vm``                     | Use settings for the `JULES development virtual machine`.                                                                                                    |
    |                            |                                                                                                                                                              |
    +----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``ceh``                    | Use settings for the GFortran compiler on the CEH Linux systems.                                                                                             |
    |                            |                                                                                                                                                              |
    +----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``jasmin-lotus-intel``     | Use settings for the Intel compiler on the Lotus system at JASMIN.                                                                                           |
    |                            |                                                                                                                                                              |
    +----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``jasmin-gcc-nompi``       | Use settings for the gfortran compiler on the JASMIN Cylc server.                                                                                            |
    |                            |                                                                                                                                                              |
    +----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``jasmin-intel-nompi``     | Use settings for the intel compiler on the JASMIN Cylc server.                                                                                               |
    |                            |                                                                                                                                                              |
    +----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``meto-linux-gfortran``    | Use settings for the GFortran compiler on Met Office Linux systems.                                                                                          |
    |                            |                                                                                                                                                              |
    +----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``meto-linux-nagfor``      | Use settings for the NAG compiler on Met Office Linux systems.                                                                                               |
    |                            |                                                                                                                                                              |
    |                            | **Warning:** This build configuration is intended for correctness checking only, not production runs.                                                        |
    +----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``meto-linux-intel-nompi`` | Use settings for the Intel compiler *without* MPI on Met Office Linux systems.                                                                               |
    |                            |                                                                                                                                                              |
    +----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``meto-linux-intel-mpi``   | Use settings for the Intel compiler *with* MPI on Met Office Linux systems.                                                                                  |
    |                            |                                                                                                                                                              |
    +----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``meto-xc40-cce``          | Use settings for the Cray Compiler Environment on the Met Office Cray XC40 system.                                                                           |
    |                            |                                                                                                                                                              |
    +----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ``uoe-linux-gfortran``     | Use settings for the GFortran compiler on University of Exeter Linux system (SL7).                                                                           |
    |                            |                                                                                                                                                              |
    +----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    
``JULES_REMOTE``, ``JULES_REMOTE_HOST``, ``JULES_REMOTE_PATH``
    .. warning:: Advanced users only

    Used to determine whether the build will happen on a local or remote machine.
    
    +-----------------+----------------------------------------------------------------------------------+
    | Permitted value | Purpose                                                                          |
    +=================+==================================================================================+
    | ``local``       | **Default.** All compilation occurs on the local machine.                        |
    +-----------------+----------------------------------------------------------------------------------+
    | ``remote``      | Code is extracted on the local machine and mirrored to                           |
    |                 | ``${JULES_REMOTE_HOST}@${JULES_REMOTE_PATH}``, where ``JULES_REMOTE_HOST`` is    |
    |                 | the name of the remote machine and ``JULES_REMOTE_PATH`` is the path on the      |
    |                 | remote machine.                                                                  |
    |                 |                                                                                  |
    |                 | The compilation can then be completed on the remote machine. See below for an    |
    |                 | example.                                                                         |
    +-----------------+----------------------------------------------------------------------------------+
    
``JULES_COMPILER``
    Used to select compiler specific settings.
    
    +-----------------+----------------------------------------------------------------------------------+
    | Permitted value | Purpose                                                                          |
    +=================+==================================================================================+
    | ``gfortran``    | **Default.** Use settings for the `GNU Fortran compiler`_.                       |
    +-----------------+----------------------------------------------------------------------------------+
    | ``intel``       | Use settings for the `Intel Fortran compiler`_.                                  |
    +-----------------+----------------------------------------------------------------------------------+
    | ``nagfor``      | Use settings for the `NAG Fortran compiler`_.                                    |
    +-----------------+----------------------------------------------------------------------------------+
    | ``cray``        | Use settings for the `Cray Compiler Environment`_.                               |
    +-----------------+----------------------------------------------------------------------------------+

``JULES_BUILD``
    Used to select the type of build.

    +-----------------+----------------------------------------------------------------------------------+
    | Permitted value | Purpose                                                                          |
    +=================+==================================================================================+
    | ``normal``      | **Default.** Compile JULES normally.                                             |
    +-----------------+----------------------------------------------------------------------------------+
    | ``debug``       | Compile JULES with additional settings for debugging.                            |
    +-----------------+----------------------------------------------------------------------------------+
    | ``fast``        | Compile JULES with additional settings for faster execution.                     |
    +-----------------+----------------------------------------------------------------------------------+
    
``JULES_OMP``
    Used to determine whether to build with OpenMP or not.
    
    +-----------------+----------------------------------------------------------------------------------+
    | Permitted value | Purpose                                                                          |
    +=================+==================================================================================+
    | ``noomp``       | **Default.** Compile JULES with OpenMP off.                                      |
    +-----------------+----------------------------------------------------------------------------------+
    | ``omp``         | Compile JULES with OpenMP on.                                                    |
    +-----------------+----------------------------------------------------------------------------------+

``JULES_MPI``
    Used to determine whether to build with MPI enabled or not.
    
    +-----------------+----------------------------------------------------------------------------------+
    | Permitted value | Purpose                                                                          |
    +=================+==================================================================================+
    | ``nompi``       | **Default.** Compile JULES without MPI support.                                  |
    +-----------------+----------------------------------------------------------------------------------+
    | ``mpi``         | Compile JULES with MPI support.                                                  |
    +-----------------+----------------------------------------------------------------------------------+

``JULES_NETCDF``
    Indicates whether to use a dummy NetCDF library or a 'real' NetCDF library.
    
    +-----------------+----------------------------------------------------------------------------------+
    | Permitted value | Purpose                                                                          |
    +=================+==================================================================================+
    | ``nonetcdf``    | **Default.** Use a dummy NetCDF library.                                         |
    +-----------------+----------------------------------------------------------------------------------+
    | ``netcdf``      | Use a 'real' NetCDF library.                                                     |
    |                 |                                                                                  |
    |                 | The NetCDF installation to use is specified using one of:                        |
    |                 |                                                                                  |
    |                 | * ``JULES_NETCDF_PATH``                                                          |
    |                 | * ``JULES_NETCDF_INC_PATH`` and ``JULES_NETCDF_LIB_PATH``                        |
    +-----------------+----------------------------------------------------------------------------------+

``JULES_NETCDF_PATH``
    Path to NetCDF installation.
    
    This sets ``JULES_NETCDF_INC_PATH = $JULES_NETCDF_PATH/include`` and ``JULES_NETCDF_LIB_PATH = $JULES_NETCDF_PATH/lib``. These can be overridden by setting the variables directly.
    
``JULES_NETCDF_INC_PATH``
    Path to NetCDF include directory (i.e. directory containing ``netcdf.mod``).
    
``JULES_NETCDF_LIB_PATH``
    Path to NetCDF library directory (i.e. directory containing ``libnetcdff.a`` and ``libnetcdf.a``).
    
.. note::
    When compiled in parallel mode, NetCDF must be statically linked. This means the compiler must be able to find all required library and include files (i.e. for NetCDF, HDF5, curl and zlib) in ``JULES_NETCDF_INC_PATH``, ``JULES_NETCDF_LIB_PATH`` or the default search path.

``JULES_FFLAGS_EXTRA``
    Any additional compiler flags you wish to add to the build. For example, to activate additional compiler checks.

``JULES_LDFLAGS_EXTRA``
    Any additional library flags you wish to add to the build. This may need to include both the linker flags themselves and, if you are linking in a new library, the flags specifying the path to the new library object.

.. note::
    When adding a completely new external dependency it is likely you will need to edit or override the FCM make build configuration files. The FCM make tool performs a dependency analysis on the JULES source tree to ensure all of the required files are present. Any new external sources must be added to the list of exclusions from this analysis or the build will fail when the external files cannot be found in the JULES working copy.

``JULES_SOURCE``
    The full path to the copy of JULES being compiled. This could be a directory path or an FCM/Subversion/file URL to a repository location. This variable is used by the configuration file contained in many Rose fcm_make apps, but is not read by JULES itself.


Example FCM make commands
-------------------------

To create a normal JULES executable without NetCDF using the GFortran compiler (taking advantage of the default values for the environment variables):

.. code-block:: bash

    $ fcm make -j 2 -f etc/fcm-make/make.cfg --new

To create a fast JULES executable with NetCDF using the Intel compiler:

.. code-block:: bash

    $ export JULES_COMPILER=intel
    $ export JULES_BUILD=fast
    $ export JULES_NETCDF=netcdf
    $ export JULES_NETCDF_PATH=/path/to/netcdf  # Replace this with the correct path
    $ fcm make -j 2 -f etc/fcm-make/make.cfg --new
    
To create a fast JULES executable with NetCDF using the GFortran compiler on a Met Office Linux system (making use of the platform setting):

.. code-block:: bash

    $ export JULES_PLATFORM=meto-linux-gfortran
    $ export JULES_BUILD=fast
    $ export JULES_NETCDF=netcdf  # Note that we don't need to specify paths
    $ fcm make -j 2 -f etc/fcm-make/make.cfg --new
    
To create a normal JULES executable with NetCDF and OpenMP using the Intel compiler on a remote machine:

.. code-block:: bash

    localhost $ export JULES_REMOTE=remote
    localhost $ export JULES_REMOTE_HOST=my-host
    localhost $ export JULES_REMOTE_PATH=/path/on/remote/host
    localhost $ export JULES_COMPILER=intel
    localhost $ export JULES_OMP=omp
    localhost $ export JULES_NETCDF=netcdf
    localhost $ export JULES_NETCDF_PATH=/path/to/netcdf  # Replace this with the path ON THE REMOTE MACHINE
    localhost $ fcm make -f etc/fcm-make/make.cfg --new  # This does the extract and mirror steps
    localhost $ ssh -Y my-host
    my-host $ cd /path/on/remote/host
    my-host $ fcm make -j 4 --new  # This does the preprocess and build steps

To create a normal JULES executable with MPI enabled, using the Intel compiler with array bounds checking turned on:

.. code-block:: bash
   
    $ export JULES_COMPILER=intel
    $ export JULES_MPI=mpi
    $ export JULES_NETCDF=netcdf  # We have to use NetCDF for distributed simulations
    $ export JULES_NETCDF_PATH=/path/to/parallel/netcdf  # NetCDF must be compiled with parallel I/O enabled
    $ export JULES_FFLAGS_EXTRA="-check bounds"  # Must be quoted because of the space
    $ fcm make -j 2 -f etc/fcm-make/make.cfg --new
    

Tips for effective use of FCM make
----------------------------------

* To check the current values of the environment variables JULES will use to build, use the command ``env | grep JULES``

* If you always use the same compilation options for JULES, consider adding the export lines to the ``.profile`` file in your ``$HOME`` directory. Commands in the ``.profile`` file are automatically executed in any shell that you open, so defining environment variables there ensures your build environment remains consistent across shells and restarts of your computer. The definitions can still be overridden on the command line if required.
    

.. _JULES development virtual machine: https://code.metoffice.gov.uk/trac/jules/wiki/JULESVirtualMachine
.. _GNU Fortran compiler: http://www.gnu.org/software/gcc/fortran/
.. _Intel Fortran compiler: http://software.intel.com/en-us/articles/fortran-compilers/
.. _NAG Fortran compiler: https://www.nag.co.uk/nag-compiler
.. _Cray Compiler Environment: http://docs.cray.com/cgi-bin/craydoc.cgi?mode=SiteMap;f=xc_sitemap
