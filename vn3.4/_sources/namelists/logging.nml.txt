``logging.nml``
===============


This file provides control over the log output from JULES. It contains a single namelist called :nml:lst:`LOGGING`.


``LOGGING`` namelist members
----------------------------

.. nml:namelist:: LOGGING

.. nml:member:: log_dir

   :type: character
   :default: ""
   
   The directory that log files will be created in.
   
   If no log directory is given (i.e. the empty string ``""`` is given as :nml:mem:`log_dir`), then log output will be written to ``stdout``. If the user is running multiple tasks using MPI (see :doc:`/building-and-running/parallel`), lines written to ``stdout`` will be prefixed with the MPI task number, e.g.:
   
   .. code-block:: text
   
       {MPI Task 4} [INFO] jules: Run completed successfully
   
   If a log directory is given and JULES is running in serial mode, a single log file called ``task0.stdout`` will be created. If JULES is running in parallel using MPI, a log file will be created for each MPI task. The log files will have names like ``task<n>.stdout`` where ``<n>`` is the MPI task number.
   
   
.. nml:member:: log_print_level

   :type: integer
   :permitted: 0-31
   :default: 31
   
   Determines which levels of log messages are written to the log files (or ``stdout``).
   
   The default is to write all levels of log messages.
   
   :nml:mem:`log_print_level` is a bitwise combination of the following:
   
   =========  =====  ======================================================================================
   Level      Value  Meaning
   =========  =====  ======================================================================================
   ``INFO``   1      Informational messages.
   ``DEBUG``  2      Debugging messages.
   ``WARN``   4      Warning messages indicating that something may be wrong.
   ``ERROR``  8      Error messages indicating that something is wrong but program execution can continue.
   ``FATAL``  16     Error messages indicating that program execution must be halted.
   =========  =====  ======================================================================================
   
   For example, to print all log levels (the default), ``31 = 1 + 2 + 4 + 8 + 16`` is used. To print only debug messages and fatal errors, ``18 = 2 + 16`` would be used.
   
   
.. nml:member:: log_stop_level

   :type: integer
   :permitted: 0-15
   :default: 0
   
   Determines which levels of log messages cause the program to terminate.
   
   .. note:: Fatal errors will always cause the program to terminate, regardless of this setting.
   
   The default is to only terminate the program if a fatal error is encountered.
   
   :nml:mem:`log_stop_level` is a bitwise combination of the following:
   
   =========  =====  ======================================================================================
   Level      Value  Meaning
   =========  =====  ======================================================================================
   ``INFO``   1      Informational messages.
   ``DEBUG``  2      Debugging messages.
   ``WARN``   4      Warning messages indicating that something may be wrong.
   ``ERROR``  8      Error messages indicating that something is wrong but program execution can continue.
   =========  =====  ======================================================================================
   
   For example, to stop execution at warning and error messages as well as fatal errors, ``12 = 4 + 8`` would be used.
   