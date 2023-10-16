``jules_prnt_control.nml``
==========================


This file contains one namelist called :nml:lst:`JULES_PRNT_CONTROL`.

This namelist sets options for output of diagnostic and informative messages.

``JULES_PRNT_CONTROL`` namelist members
---------------------------------------

.. nml:namelist:: JULES_PRNT_CONTROL

.. nml:member:: prnt_writers

   :type: integer
   :permitted: 1,2
   :default: 1

   Selects which tasks in a parallel job will write informative
   output.

   = ==========================================
   1 All tasks write output
   2 Only the first task (Task 0) writes output
   = ==========================================

