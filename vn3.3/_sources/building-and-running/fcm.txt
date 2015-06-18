Building JULES using FCM
========================


FCM is a suite of tools for managing and building source code. In this section, we will be using the build tool - FCM make. FCM make must be given a configuration file that it uses to determine how to build the source code. Extensive documentation on FCM make configuration files is `available online <http://collab.metoffice.gov.uk/twiki/pub/Support/FCM/doc/user_guide/make.html>`_.

Help pages for the FCM make command itself (rather than the configuration file) can be accessed using the command:

.. code-block:: bash

    fcm help make
    
The FCM configuration file for building JULES is ``etc/fcm-make/make-local.cfg``. This file uses the environment variables below to determine the compiler settings and NetCDF settings to use.

Running FCM make with this configuration file will create 4 new directories in your JULES root directory (i.e. the directory containing ``docs``, ``src`` etc.):

``.fcm-make``
    Used by FCM to store information about the build process.

``extract``
    Contains a copy of the code that FCM will build.

``preprocess``
    Contains the code after preprocessing but before compilation.

``build``
    Contains the results of the compilation.
  
The JULES executable will be produced at ``build/bin/jules.exe``.


.. _fcm-make-environment-variables:

Environment variables used when building JULES using FCM make
-------------------------------------------------------------

``JULES_CFG_COMP``
    Used to select compiler specific settings.
    
    +--------------------+--------------------------------------------------------------------------------+
    | Permitted value    | Purpose                                                                        |
    +====================+================================================================================+
    | ``gfortran``       | **Default.** Use settings for the `GNU Fortran compiler`_.                     |
    +--------------------+--------------------------------------------------------------------------------+
    | ``intel``          | Use settings for the `Intel Fortran compiler`_.                                |
    +--------------------+--------------------------------------------------------------------------------+
    | ``nag``            | Use settings for the `NAGWare compiler`_.                                      |
    +--------------------+--------------------------------------------------------------------------------+
    | ``pgf``            | Use settings for the `Portland Group compiler`_.                               |
    +--------------------+--------------------------------------------------------------------------------+
    | ``sun``            | Use settings for the `Oracle (previously Sun) Studio compiler`_ series.        |
    +--------------------+--------------------------------------------------------------------------------+

``JULES_CFG_BLD``
    Used to select the type of build.

    +--------------------+--------------------------------------------------------------------------------+
    | Permitted value    | Purpose                                                                        |
    +====================+================================================================================+
    | ``normal``         | **Default.** Compile JULES normally.                                           |
    +--------------------+--------------------------------------------------------------------------------+
    | ``debug``          | Compile JULES with debug flags.                                                |
    +--------------------+--------------------------------------------------------------------------------+
    | ``fast``           | Compile JULES with optimisation flags for faster execution.                    |
    +--------------------+--------------------------------------------------------------------------------+

``JULES_CFG_NCDF``
    Path to a file defining NetCDF related settings.

    .. note::
        Defaults to ``etc/fcm-make/ncdf/netcdf-dummy.cfg``. This will build JULES using a dummy NetCDF library.

    If this variable points to any file other than the default, that file must do the following:

    * Update ``$fflags`` with the flags required to add the NetCDF include path to the compiler's module search path, e.g.:
    
      .. code-block:: fcm_make

          $fflags = $fflags -I<NetCDF include path>

    * Update ``$ldflags`` with the flags required to add the NetCDF library path to the compiler's library search path, and the flags to tell the compiler it needs to link the NetCDF libraries, e.g.:
    
      .. code-block:: fcm_make

          $ldflags = $ldflags -L<NetCDF library path> -lnetcdf -lnetcdff

    The file ``etc/fcm-make/ncdf/netcdf.cfg`` is provided as an example of how to set these variables, and should work with most compilers once the correct paths are inserted.

``JULES_CFG_ARCH``
    Path to the file defining compiler related options.

    If you use a common compiler, you should never have to set this directly - ``JULES_CFG_COMP`` and ``JULES_CFG_BLD`` should be used instead.

    The default value of this variable is determined by ``JULES_CFG_COMP`` and ``JULES_CFG_BLD``. This can be overridden by setting it as an environment variable itself. This way, options for compilers other than those listed above can be specified.

    This file must do the following:

    * Set ``build.prop{fc}`` to the compiler name.
    * Update ``$fflags`` with the compiler flags to use at compile-time.
    * Update ``$ldflags`` with the compiler flags to use at link-time.

    The files in ``etc/fcm-make/arch`` can be used as examples of how to do this.


Example FCM make commands
-------------------------

To create a normal JULES executable without NetCDF using the GFortran compiler (taking advantage of the default values for the environment variables):

.. code-block:: bash

    fcm make -f etc/fcm-make/make-local.cfg

To create a fast JULES executable with NetCDF using the Intel compiler:

.. code-block:: bash

    export JULES_CFG_COMP=intel
    export JULES_CFG_BLD=fast
    export JULES_CFG_NCDF=/path/to/ncdf/config.cfg
    fcm make -f etc/fcm-make/make-local.cfg

Where ``/path/to/ncdf/config.cfg`` looks like:

.. code-block:: fcm_make

    $fflags = $fflags -I/path/to/netcdf/include
    $ldflags = $ldflags -L/path/to/netcdf/lib -lnetcdf -lnetcdff


Tips for effective use of FCM make (Unix-like systems only)
-----------------------------------------------------------

To check the current values of the environment variables JULES will use to build, use the command:

.. code-block:: bash

    env | grep JULES

If you always use the same compilation options for JULES, consider adding the export lines to the ``.profile`` file in your ``$HOME`` directory. Commands in the ``.profile`` file are automatically executed in any shell that you open, so defining environment variables there ensures your build environment remains consistent across shells and restarts of your computer. The definitions can still be
overridden on the command line if required. For example, to always create a fast JULES executable with NetCDF using the Intel compiler (as above), add the following lines to your ``.profile``:

.. code-block:: bash

    export JULES_CFG_COMP=intel
    export JULES_CFG_BLD=fast
    export JULES_CFG_NCDF=/path/to/ncdf/config.cfg

Then to build JULES with those settings, run:

.. code-block:: bash

    fcm make -f etc/fcm-make/make-local.cfg

    

.. _GNU Fortran compiler: http://www.gnu.org/software/gcc/fortran/
.. _Intel Fortran compiler: http://software.intel.com/en-us/articles/fortran-compilers/
.. _NAGWare compiler: http://www.nag.co.uk/nagware/np.asp
.. _Portland Group compiler: http://www.pgroup.com/
.. _Oracle (previously Sun) Studio compiler: http://www.oracle.com/us/products/servers-storage/solaris/studio/overview/index.html