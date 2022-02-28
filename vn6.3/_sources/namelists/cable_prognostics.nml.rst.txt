``cable_prognostics.nml``
==========================


This file contains a single namelist called :nml:lst:`CABLE_PROGS` that is used to set up the initial state of prognostic variables.


``CABLE_PROGS`` namelist members
----------------------------------

.. nml:namelist:: CABLE_PROGS

The values of all prognostic variables must be set at the start of a run. This initial state, or initial condition, can be read from a file. Another option is to prescribe a simple or idealised initial state by giving constant values for the prognostic variables directly in the namelist. It is also possible to set some fields using values from a file but to set others to constants given in the namelist.


.. nml:member:: file

   :type: character
   :default: None

   The file to read initial values for CABLE prognostic variables from.

   If :nml:mem:`use_file` is FALSE for every variable, this will not be used.

   This file name can use :doc:`variable name templating </input/file-name-templating>`.


.. nml:member:: nvars

   :type: integer
   :permitted: >= 0
   :default: 0

   The number of prognostic variables that will be provided (see :ref:`list-of-cable-prognostic-variables`).


.. nml:member:: var

   :type: character(nvars)
   :default: None

   List of CABLE prognostic variable names as recognised by CABLE (see :ref:`list-of-cable-prognostic-variables`). Names are case sensitive.

   .. note:: For ASCII files, variable names must be in the order they appear in the file.


.. nml:member:: tpl_name

   :type: character(nvars)
   :default: None

   For each CABLE variable specified in :nml:mem:`var`, this is the string to substitute into the file name in place of the variable name substitution string.

   If the file name does not use variable name templating, this is not used.


.. nml:member:: use_file

   :type: logical(nvars)
   :default: T

   For each CABLE variable specified in :nml:mem:`var`, this indicates if it should be read from the specified file or whether a constant value is to be used.

   TRUE
      The variable will be read from the file.

   FALSE
      The variable will be set to a constant value everywhere using :nml:mem:`const_val` below.


.. nml:member:: var_name

   :type: character(nvars)
   :default: '' (empty string)

   For each CABLE variable specified in :nml:mem:`var` where :nml:mem:`use_file` = TRUE, this is the name of the variable in the file containing the data.

   If the empty string (the default) is given for any variable, then the corresponding value from :nml:mem:`var` is used instead.

   This is not used for variables where :nml:mem:`use_file` = FALSE, but a placeholder must still be given in that case.

   .. note:: For ASCII files, this is not used - only the order in the file matters, as described above.


.. nml:member:: const_val

   :type: real(nvars)
   :default: None

   For each CABLE variable specified in :nml:mem:`var` where :nml:mem:`use_file` = FALSE, this is a constant value that the variable will be set to at every point in every layer.

   This is not used for variables where :nml:mem:`use_file` = TRUE, but a placeholder must still be given in that case.


.. _list-of-cable-prognostic-variables:

List of CABLE prognostic variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Values are set for each tile of each grid point and for each layer of soil or snow.

.. tabularcolumns:: |p{5cm}|p{10cm}|

+-------------------------------+-------------------------------------------------------------------------------+
| Name                          | Description                                                                   |
+===============================+===============================================================================+
| ``SoilTemp_CABLE``            | Temperature of each soil layer (K).                                           |
+-------------------------------+-------------------------------------------------------------------------------+
| ``SoilMoisture_CABLE``        | Soil moisture content of each soil layer (kg m\ :sup:`-2`).                   |
+-------------------------------+-------------------------------------------------------------------------------+
| ``FrozenSoilFrac_CABLE``      | Frozen soil moisture content of each soil layer as a fraction of saturation.  |
+-------------------------------+-------------------------------------------------------------------------------+
| ``SnowDepth_CABLE``           | Depth of each snow level (m).                                                 |
+-------------------------------+-------------------------------------------------------------------------------+
| ``SnowMass_CABLE``            | Mass of each each snow level (kg).                                            |
+-------------------------------+-------------------------------------------------------------------------------+
| ``SnowTemp_CABLE``            | Temperature for each snow layer (K).                                          |
+-------------------------------+-------------------------------------------------------------------------------+
| ``SnowDensity_CABLE``         | Density for each snow layer (kg m\ :sup:`-3`).                                |
+-------------------------------+-------------------------------------------------------------------------------+
| ``SnowAge_CABLE``             | Age of each snow layer                                                        |
+-------------------------------+-------------------------------------------------------------------------------+
| ``OneLyrSnowDensity_CABLE``   | Snow density when all snow treated as one layer. (kg m\ :sup:`-3`)            |
+-------------------------------+-------------------------------------------------------------------------------+
| ``ThreeLayerSnowFlag_CABLE``  | Flag for 3 layer snow pack (0 - false, 1 - true)                              |
+-------------------------------+-------------------------------------------------------------------------------+