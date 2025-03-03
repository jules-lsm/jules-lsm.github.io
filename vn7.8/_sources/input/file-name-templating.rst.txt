File name templating
====================

If the names of input files follow particular patterns, JULES can use a substitution template rather than requiring a potentially long list of file names. Templating comes in two forms, time templating and variable name templating, which can be used separately or together.

Substitution strings are 3-character strings, starting with ``%``. JULES will automatically detect the use of either form of templating by checking for the presence of the substitution strings in file names.


Time templating
---------------

If any of the time templating substitution strings are present in a file name, then JULES assumes time-templating is to be used. The valid substitution strings for time templating are:

+-----------------------+------------------------------------------------------------------------------------------------+
| Substitution string   | Replaced with                                                                                  |
+=======================+================================================================================================+
| ``%y4``               | 4-digit year                                                                                   |
+-----------------------+------------------------------------------------------------------------------------------------+
| ``%y2``               | 2-digit year                                                                                   |
+-----------------------+------------------------------------------------------------------------------------------------+
| ``%m2``               | 2-digit month                                                                                  |
+-----------------------+------------------------------------------------------------------------------------------------+
| ``%m1``               | 1- or 2-digit month                                                                            |
+-----------------------+------------------------------------------------------------------------------------------------+
| ``%mc``               | 3-character month abbreviation                                                                 |
+-----------------------+------------------------------------------------------------------------------------------------+
| ``%d2``               | 2-digit day of month                                                                           |
+-----------------------+------------------------------------------------------------------------------------------------+

JULES will automatically detect the period (or frequency) of files based on the specific substitution strings in the following manner:

.. figure:: time_templating_flow_diagram.png
   :alt: Time templating flow diagram
   
   Flow diagram showing detection of file period from time templated string

This means that monthly files must also have a year substitution string present, and daily files must have both month and year substitution strings present. Only yearly, monthly and daily files are allowed with time templating, with each file containing a single period (year, month or day respectively) of data. For yearly files, the first data in each file must apply from 00:00:00 on 1st January for each year. For monthly files, the first data in the file must apply from 00:00:00 on the 1st of the month. For daily files, the first data in the file must apply from 00:00:00 on the given day. Other configurations can be specified using a list of files with their respective start times.


Variable name templating
------------------------

Variable name templating can be used when related variables are stored in separate files with file names that are identical apart from a section that indicates what variable is in each file. Examples of the use of this are given in the next section. JULES will automatically detect if the variable name substitution string - ``%vv`` - is present in a file name, and apply variable name templating if appropriate.


Examples of file name templating
--------------------------------

Time templating only
~~~~~~~~~~~~~~~~~~~~

Data is in monthly files with all related variables in the same file.

Template:

.. code-block:: none

    /data/met_data_%y4%m2.nc

Example filenames:

.. code-block:: none

    /data/met_data_199001.nc
    /data/met_data_199002.nc
    ...
    /data/met_data_200410.nc
    
Variable name templating only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ancillary (non-time-varying) data with each variable in similarly named but separate files.

Template:
    
.. code-block:: none

    /ancil/soil_%vv.nc
        
Example filenames:
    
.. code-block:: none

    /data/soil_satcon.nc
    /data/soil_sathh.nc

Time and variable name templating together
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data is in monthly files with each variable in similarly named but separate files.

Template:

.. code-block:: none

    /data/%vv_%y4%mc.nc
    
Example filenames:

.. code-block:: none

    /data/Rain_1990jan.nc
    /data/Wind_1990jan.nc
    ...
    /data/Rain_2000oct.nc
    /data/Wind_2000oct.nc
    
Variable name templating with a list of files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data in 6-monthly files with each variable in similarly named but separate files.
    
Since the time templating cannot handle 6-monthly files, the files and their start times must be specified as a list. However, variable name templating can still be used.
    
Also note that it is possible to use a substitution string more than once in a template.

Template list:

.. code-block:: none

    ./%vv/met_%vv_199001.nc
    ./%vv/met_%vv_199007.nc
    ...
    ./%vv/met_%vv_199801.nc

Example filenames:

.. code-block:: none

    ./Rain/met_Rain_199001.nc
    ./Wind/met_Wind_199001.nc
    ./Rain/met_Rain_199007.nc
    ./Wind/met_Wind_199007.nc
    ...
    ./Rain/met_Rain_199801.nc
    ./Wind/met_Wind_199801.nc
