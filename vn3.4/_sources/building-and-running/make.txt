Building JULES using make
=========================


The ``Makefile`` supplied with the JULES code should be compliant with most versions of make, but is only guaranteed to work with GNU Make.

The JULES ``Makefile`` uses architecture- and compiler-specific variables that must be set by the user to the appropriate values for their system. Architecture-specific variables, such as the remove command and archiving utility to use, are specified in ``Makefile.common.mk``. Compiler-specific variables are given in files named ``Makefile.comp.*``. These files are provided for a number of common compilers, e.g. ``Makefile.comp.gfortran``. To use a compiler for which a file has not been provided, the user should replace the ``@@`` strings in the blank compiler file ``Makefile.comp.misc`` with values appropriate to their compiler.

Once the ``Makefile`` is set up for the user's system, JULES is built by issuing a ``make`` command at the command prompt while in the directory containing the ``Makefile``. The user must specify some options to make that will determine how JULES is built - valid values for these options are given below, and additional information is given in the comments at the head of the ``Makefile``.

Running make will produce a JULES executable (either ``jules.exe``, ``jules_debug.exe`` or ``jules_fast.exe`` depending on the value of ``BUILD``) in the JULES root directory, i.e. the directory containing ``Makefile``, ``src``, etc.


Options that can be passed to make when building JULES
------------------------------------------------------

``COMPILER``
    Determines which version of ``Makefile.comp.*`` to use for compiler specific options.
    
    +--------------------+--------------------------------------------------------------------------------+
    | Permitted values   | Purpose                                                                        |
    +====================+================================================================================+
    | ``gfortran``       | Use options for the `GNU Fortran compiler`_.                                   |
    +--------------------+--------------------------------------------------------------------------------+
    | ``intel``          | Use options for the `Intel Fortran compiler`_.                                 |
    +--------------------+--------------------------------------------------------------------------------+
    | ``nag``            | Use options for the `NAGWare compiler`_.                                       |
    +--------------------+--------------------------------------------------------------------------------+
    | ``pgf``            | Use options for the `Portland Group compiler`_.                                |
    +--------------------+--------------------------------------------------------------------------------+
    | ``g95``            | Use options for the `G95 compiler`_.                                           |
    +--------------------+--------------------------------------------------------------------------------+
    | ``sun``            | Use options for the `Oracle (previously Sun) Studio compiler`_.                |
    +--------------------+--------------------------------------------------------------------------------+
    | ``misc``           | Use options for an unsupported compiler.                                       |
    +--------------------+--------------------------------------------------------------------------------+
    
``BUILD``
    Allows different compiler flags to be used without changing the ``Makefile`` s.
    
    +--------------------+--------------------------------------------------------------------------------+
    | Permitted values   | Purpose                                                                        |
    +====================+================================================================================+
    | ``run``            | **Default.**  Compile JULES normally.                                          |
    +--------------------+--------------------------------------------------------------------------------+
    | ``debug``          | Switch on compiler debug flags.                                                |
    +--------------------+--------------------------------------------------------------------------------+
    | ``fast``           | Switch on compiler optimisation flags for faster execution.                    |
    +--------------------+--------------------------------------------------------------------------------+

``CDFDUMMY``
    Determines whether to use a 'real' NetCDF library or the dummy NetCDF library provided with JULES.

    +--------------------+--------------------------------------------------------------------------------+
    | Permitted values   | Purpose                                                                        |
    +====================+================================================================================+
    | ``true``           | Use the dummy NetCDF library provided with JULES.                              |
    +--------------------+--------------------------------------------------------------------------------+
    | ``false``          | **Default.** Use a 'real' NetCDF library.                                      |
    +--------------------+--------------------------------------------------------------------------------+

``CDF_LIB_PATH``
    .. note:: Only used if ``CDFDUMMY=false``.

    The NetCDF library path (see :doc:`jules-and-netcdf`).

``CDF_MOD_PATH``
    .. note:: Only used if ``CDFDUMMY=false``.

    The NetCDF include path (see :doc:`jules-and-netcdf`).


Example make commands
---------------------

To create a normal JULES executable without NetCDF using the GFortran compiler:

.. code-block:: bash

    make COMPILER=gfortran BUILD=run CDFDUMMY=true

To create a fast JULES executable with the Intel compiler using a NetCDF library:

.. code-block:: bash

    make COMPILER=intel BUILD=fast CDF_LIB_PATH=/path/to/netcdf/lib CDF_MOD_PATH=/path/to/netcdf/include


.. _GNU Fortran compiler: http://www.gnu.org/software/gcc/fortran/
.. _Intel Fortran compiler: http://software.intel.com/en-us/articles/fortran-compilers/
.. _NAGWare compiler: http://www.nag.co.uk/nagware/np.asp
.. _Portland Group compiler: http://www.pgroup.com/
.. _G95 compiler: http://www.g95.org/
.. _Oracle (previously Sun) Studio compiler: http://www.oracle.com/us/products/servers-storage/solaris/studio/overview/index.html
