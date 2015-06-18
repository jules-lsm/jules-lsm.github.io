Running JULES
=============

The user interface of JULES consists of several files with the extension ``.nml`` containing Fortran namelists. These files and the namelist members are documented in more detail in :doc:`/namelists/contents`. These namelists are grouped together in a single directory. That directory is referred to as the *namelist directory* for a JULES run.

Once a :doc:`JULES executable is compiled <building-jules>` and the :doc:`namelists </namelists/contents>` are set up, JULES can be run in one of two ways:

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
   
   To allow runs to be portable across different machines, it is common to specify data files relative to the namelist directory (e.g. in the ``point_loobos_*`` examples supplied with JULES). In this case, JULES must be run using the first method to allow the relative paths to be resolved correctly.


Running the Loobos example from a fresh download of JULES
---------------------------------------------------------

#. Move into the JULES root directory (the directory containing ``includes``, ``src`` etc.):

   .. code-block:: bash

       $ cd /jules/root/dir
    
#. Build JULES, either using FCM:

   .. code-block:: bash

       $ fcm make -f etc/fcm-make/make-local.cfg

   Or make:

   .. code-block:: bash

       $ make COMPILER=gfortran BUILD=run CDFDUMMY=true

#. Move into the example directory:

   .. code-block:: bash

       $ cd examples/point_loobos/

#. Run the JULES executable (location depends on build method):

   * FCM make:
    
     .. code-block:: bash

         $ ../../build/bin/jules.exe
    
   * GNU make:
    
     .. code-block:: bash

         $ ../../jules.exe
