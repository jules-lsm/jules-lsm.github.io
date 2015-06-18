``initial_conditions.nml``
==========================


This file contains a single namelist called :nml:lst:`JULES_INITIAL` that is used to set up the initial state of prognostic variables.


``JULES_INITIAL`` namelist members
----------------------------------

.. nml:namelist:: JULES_INITIAL

The values of all prognostic variables must be set at the start of a run. This initial state, or initial condition, can be read from a "dump" from an earlier run of the model, or may be read from a different file. Another option is to prescribe a simple or idealised initial state by giving constant values for the prognostic variables directly in the namelist. It is also possible to set some fields using values from a file (e.g. a dump) but to set others to constants given in the namelist.


.. nml:member:: dump_file

   :type: logical
   :default: F

   Indicates whether the given :nml:mem:`file` is a dump from a previous run of JULES.

   TRUE
       The file is a JULES dump file.

   FALSE
       The file is not a JULES dump file.


.. nml:member:: total_snow

   :type: logical
   :default: T

   Switch controlling simplified initialisation of snow variables.

   TRUE
       Only the total mass of snow on each tile (see ``snow_tile`` in :ref:`list-of-initial-condition-variables`) is required to be input, and all related variables will be calculated from this or simple assumptions made. All the snow is assumed to be on the ground (not in the canopy).

   FALSE
       All snow variables required for the current configuration must be input separately (see :ref:`list-of-initial-condition-variables`).


.. nml:group:: Members used to set up spacially varying properties

   .. nml:member:: file
   
      :type: character
      :default: None
   
      The file to read initial conditions from.
      
      If :nml:mem:`use_file` (see below) is FALSE for every variable, this will not be used.

      If :nml:mem:`dump_file` = TRUE, this should be a JULES dump file.
      
      If :nml:mem:`dump_file` = FALSE, this should be a file conforming to the :doc:`JULES input requirements </input/overview>`. This file name may use :doc:`variable name templating </input/file-name-templating>`.    
   
   
   .. nml:member:: nvars
   
      :type: integer
      :permitted: >= 0
      :default: 0
   
      The number of initial condition variables that will be provided.
   
      See :ref:`list-of-initial-condition-variables` for those required for a particular configuration.
   
      .. note:: If :nml:mem:`dump_file` = TRUE and :nml:mem:`nvars` = 0, then the model will attempt to initialise all required variables from the given dump file.
   
   
   .. nml:member:: var
   
      :type: character(nvars)
      :default: None
   
      List of initial condition variable names as recognised by JULES (see :ref:`list-of-initial-condition-variables`). Names are case sensitive.
   
      .. note:: For ASCII files, variable names must be in the order they appear in the file.
   
   
   .. nml:member:: use_file
   
      :type: logical(nvars)
      :default: T
   
      For each JULES variable specified in :nml:mem:`var`, this indicates if it should be read from the specified file or whether a constant value is to be used.
   
      TRUE
          The variable will be read from the file.
   
      FALSE
          The variable will be set to a constant value everywhere using :nml:mem:`const_val` below.
   
   
   .. nml:member:: var_name
   
      :type: character(nvars)
      :default: None
   
      For each JULES variable specified in :nml:mem:`var` where :nml:mem:`use_file` = TRUE, this is the name of the variable in the file containing the data.
   
      This is not used for variables where :nml:mem:`use_file` = FALSE, but a placeholder must still be given.
   
      .. note:: For ASCII files, this is not used - only the order in the file matters, as described above.
   
   
   .. nml:member:: tpl_name
   
      :type: character(nvars)
      :default: None
   
      For each JULES variable specified in :nml:mem:`var`, this is the string to substitute into the file name in place of the variable name substitution string.
   
      If the file name does not use variable name templating, this is not used.
   
   
   .. nml:member:: const_val
   
      :type: real(nvars)
      :default: None
   
      For each JULES variable specified in :nml:mem:`var` where :nml:mem:`use_file` = FALSE, this is a constant value that the variable will be set to at every point in every layer.
   
      This is not used for variables where :nml:mem:`use_file` = TRUE, but a placeholder must still be given.


.. _list-of-initial-condition-variables:

List of initial condition variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All input to the model must be on the same grid (see :doc:`/input/overview`), and initial conditions are no different. Even when the variable is only required for land points, values must be provided for the full input grid. Variables read as initial conditions must have no time dimension.

The variables it is possible to specify as initial conditions can be grouped into 'types' depending on the number and size of the levels dimensions they are required to have. For NetCDF files, the dimension names are those specified in the :nml:lst:`JULES_INPUT_GRID` namelist. For variables with no type specified, no levels dimensions should be used.

The required levels dimensions for each initial condition 'type' are given in the following table:

.. tabularcolumns:: |p{2.5cm}|p{2cm}|p{4cm}|p{6.5cm}|

+-------------+------------------+----------------------------------------------+--------------------------------------------------------+
| Type        | Number of levels | Levels dimension name(s)                     | Levels dimension size(s)                               |
|             | dimensions       |                                              |                                                        |
+=============+==================+==============================================+========================================================+
| soil        |                1 | :nml:mem:`JULES_INPUT_GRID::soil_dim_name`   | :nml:mem:`JULES_MODEL_LEVELS::sm_levels`               |
+-------------+------------------+----------------------------------------------+--------------------------------------------------------+
| pft         |                1 | :nml:mem:`JULES_INPUT_GRID::pft_dim_name`    | :nml:mem:`JULES_MODEL_LEVELS::npft`                    |
+-------------+------------------+----------------------------------------------+--------------------------------------------------------+
| type        |                1 | :nml:mem:`JULES_INPUT_GRID::type_dim_name`   | ``ntype`` (:nml:mem:`JULES_MODEL_LEVELS::npft` +       |
|             |                  |                                              | :nml:mem:`JULES_MODEL_LEVELS::nnvg`)                   |
+-------------+------------------+----------------------------------------------+--------------------------------------------------------+
| tile        |                1 | :nml:mem:`JULES_INPUT_GRID::tile_dim_name`   | ``ntiles`` (1 if :nml:mem:`JULES_SWITCHES::l_aggregate`|
|             |                  |                                              | = TRUE, ``ntype`` otherwise)                           |
+-------------+------------------+----------------------------------------------+--------------------------------------------------------+
| sc_pool     |                1 | :nml:mem:`JULES_INPUT_GRID::scpool_dim_name` | Number of soil carbon pools (1 if                      |
|             |                  |                                              | :nml:mem:`JULES_SWITCHES::l_triffid` = FALSE, 4        |
|             |                  |                                              | otherwise)                                             |
+-------------+------------------+----------------------------------------------+--------------------------------------------------------+
| snow        |                2 | :nml:mem:`JULES_INPUT_GRID::tile_dim_name`,  | ``ntiles`` (see above),                                |
|             |                  | :nml:mem:`JULES_INPUT_GRID::snow_dim_name`   | :nml:mem:`JULES_MODEL_LEVELS::nsmax`                   |
|             |                  |                                              |                                                        |
|             |                  |                                              | Only applicable if ``nsmax > 0``                       |
+-------------+------------------+----------------------------------------------+--------------------------------------------------------+

The required variables for a particular configuration, along with their 'type' as specified above, are given in the following table.

.. tabularcolumns:: |p{2.5cm}|p{9cm}|p{3.5cm}|

+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| Name            | Description                                                                            | Type                          |
+=================+========================================================================================+===============================+
| Always required                                                                                                                          |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| ``canopy``      | Amount of intercepted water that is held on each tile (kg m\ :sup:`-2`).               | tile                          |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| ``cs``          | Soil carbon (kg m\ :sup:`-2`).                                                         | sc_pool                       |
|                 |                                                                                        |                               |
|                 | If TRIFFID is not being used (:nml:mem:`JULES_SWITCHES::l_triffid` = FALSE), this is   |                               |
|                 | the total soil carbon.                                                                 |                               |
|                 |                                                                                        |                               |
|                 | If TRIFFID is being used, this is the carbon in each of the 4 pools of the RothC model.|                               |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| ``gs``          | Stomatal conductance for water vapour (m s\ :sup:`-1`).                                | None                          |
|                 |                                                                                        |                               |
|                 | This is used to start the iterative calculation of gs for the first timestep only.     |                               |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| ``snow_tile``   | If :nml:mem:`JULES_SWITCHES::can_model` >= 4, this is the total snow on the tile       | tile                          |
|                 | (since there is a single store which doesn't distinguish between snow on canopy and    |                               |
|                 | under canopy).                                                                         |                               |
|                 |                                                                                        |                               |
|                 | If :nml:mem:`JULES_SWITCHES::can_model` = 4 (and then only at tiles where              |                               |
|                 | :nml:mem:`JULES_SNOW_PARAM::cansnowpft` = TRUE), ``snow_tile`` is interpreted as the   |                               |
|                 | snow on the canopy, except as overridden by :nml:mem:`JULES_INITIAL::total_snow`       |                               |
|                 | = TRUE.                                                                                |                               |
|                 |                                                                                        |                               |
|                 | If :nml:mem:`JULES_INITIAL::total_snow` = TRUE, ``snow_tile`` is used to hold the      |                               |
|                 | total snow on the tile (and is subsequently put onto the ground at tiles that          |                               |
|                 | distinguish between ground and canopy stores).                                         |                               |
|                 |                                                                                        |                               |
|                 | Further details of snow initialisation are given below.                                |                               |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| ``sthuf``       | Soil wetness for each soil layer. This is the mass of soil water (liquid and frozen),  | soil                          |
|                 | expressed as a fraction of the water content at saturation.                            |                               |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| ``t_soil``      | Temperature of each soil layer (K).                                                    | soil                          |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| ``tstar_tile``  | Temperature of each tile (K). This is the surface or skin temperature.                 | tile                          |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| Required if :nml:mem:`JULES_SWITCHES::l_phenol` = TRUE                                                                                   |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| ``lai``         | Leaf area index of each PFT.                                                           | pft                           |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| Required if :nml:mem:`JULES_SWITCHES::l_triffid` = TRUE                                                                                  |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| ``canht``       | Height (m) of each PFT.                                                                | pft                           |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| Required if :nml:mem:`JULES_SWITCHES::l_veg_compete` = TRUE                                                                              |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| ``frac``        | The fraction of land area of each gridbox that is covered by each surface type.        | type                          |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| Required if :nml:mem:`JULES_SWITCHES::l_top` = TRUE                                                                                      |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| ``sthzw``       | Soil wetness in the deep ("water table") layer beneath the standard soil column.       | None                          |
|                 |                                                                                        |                               |
|                 | This is the mass of soil water (liquid and frozen), expressed as a fraction of the     |                               |
|                 | water content at saturation.                                                           |                               |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| ``zw``          | Depth from the surface to the water table (m).                                         | None                          |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| Required if :nml:mem:`JULES_SWITCHES::l_snow_albedo` = TRUE                                                                              |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| ``rgrain``      | Snow surface grain size (\ |mu|\ m) on each tile.                                      | None                          |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| All variables from here onwards are only required if :nml:mem:`total_snow` = FALSE.                                                      |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| ``rho_snow``    | Bulk density of lying snow (kg m\ :sup:`-3`).                                          | tile                          |
|                 |                                                                                        |                               |
|                 | If :nml:mem:`JULES_INITIAL::total_snow` = TRUE then this is set as follows:            |                               |
|                 |                                                                                        |                               |
|                 | * If :nml:mem:`JULES_MODEL_LEVELS::nsmax` = 0, it is set to                            |                               |
|                 |   :nml:mem:`JULES_SNOW_PARAM::rho_snow_const`.                                         |                               |
|                 | * If :nml:mem:`JULES_MODEL_LEVELS::nsmax` > 0 and there is an existing snow pack, it   |                               |
|                 |   is set to :nml:mem:`JULES_SNOW_PARAM::rho_snow_const`.                               |                               |
|                 | * If :nml:mem:`JULES_MODEL_LEVELS::nsmax` > 0 and there is no snow pack, it is set to  |                               |
|                 |   :nml:mem:`JULES_SNOW_PARAM::rho_snow_fresh`.                                         |                               |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| ``snow_depth``  | Depth of snow (kg m).                                                                  | tile                          |
|                 |                                                                                        |                               |
|                 | If :nml:mem:`JULES_INITIAL::total_snow` = TRUE, this is calculated from mass and       |                               |
|                 | density of snow.                                                                       |                               |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| Required if :nml:mem:`total_snow` = FALSE and :nml:mem:`JULES_SWITCHES::can_model` = 4                                                   |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| ``snow_grnd``   | Amount of snow on the ground, beneath the canopy (kg m\ :sup:`-2`), on each tile.      | tile                          |
|                 |                                                                                        |                               |
|                 | If :nml:mem:`JULES_INITIAL::total_snow` = TRUE this is set to ``snow_tile`` at tiles   |                               |
|                 | where :nml:mem:`JULES_SWITCHES::can_model` = 4 is active, and to zero at all other     |                               |
|                 | tiles.                                                                                 |                               |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| Required if :nml:mem:`total_snow` = FALSE and :nml:mem:`JULES_MODEL_LEVELS::nsmax` > 0                                                   |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| ``nsnow``       | The number of snow layers on each tile.                                                | tile                          |
|                 |                                                                                        |                               |
|                 | If :nml:mem:`JULES_INITIAL::total_snow` = TRUE this is calculated from the snow depth. |                               |
|                 |                                                                                        |                               |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| ``snow_ds``     | Depth of snow in each layer (kg m).                                                    | snow                          |
|                 |                                                                                        |                               |
|                 | If :nml:mem:`JULES_INITIAL::total_snow` = TRUE this is calculated from the snow depth  |                               |
|                 | and the number of snow layers.                                                         |                               |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| ``snow_ice``    | Mass of frozen water in each snow layer (kg m\ :sup:`-2`).                             | snow                          |
|                 |                                                                                        |                               |
|                 | If :nml:mem:`JULES_INITIAL::total_snow` = TRUE all snow is assumed to be ice.          |                               |
|                 |                                                                                        |                               |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| ``snow_liq``    | Mass of liquid water in each snow layer (kg m\ :sup:`-2`).                             | snow                          |
|                 |                                                                                        |                               |
|                 | If :nml:mem:`JULES_INITIAL::total_snow` = TRUE this is set to zero.                    |                               |
|                 |                                                                                        |                               |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| ``tsnow``       | Temperature of each snow layer (K).                                                    | snow                          |
|                 |                                                                                        |                               |
|                 | If :nml:mem:`JULES_INITIAL::total_snow` = TRUE this is set to the temperature of the   |                               |
|                 | top soil layer.                                                                        |                               |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| Required if :nml:mem:`total_snow` = FALSE, :nml:mem:`JULES_MODEL_LEVELS::nsmax` > 0 and :nml:mem:`JULES_SWITCHES::l_snow_albedo` = TRUE  |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+
| ``rgrainl``     | Snow grain size (\ |mu|\ m) on each tile in each snow layer.                           | snow                          |
|                 |                                                                                        |                               |
|                 | If :nml:mem:`JULES_INITIAL::total_snow` = TRUE this is set to ``rgrain``.              |                               |
|                 |                                                                                        |                               |
+-----------------+----------------------------------------------------------------------------------------+-------------------------------+

.. |mu| unicode:: &#x03BC; .. u


Examples of specification of initial state
------------------------------------------

Specification of initial state at a single point
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This assumes that :nml:mem:`JULES_SWITCHES::l_phenol` = FALSE, :nml:mem:`JULES_SWITCHES::l_triffid` = FALSE and :nml:mem:`JULES_MODEL_LEVELS::nsmax` = 0.

::

    &JULES_INITIAL
      file = "initial_conditions.dat",

      nvars = 8,
      var       = 'canopy'  'tstar_tile'   'cs'  'gs'  'rgrain'  'snow_tile'  'sthuf'  't_soil',
      use_file  =       F             F      F     F         F            F        T         T ,
      const_val =     0.0        276.78   12.1   0.0      50.0          0.0
    /

Or using the alternative list syntax (see :doc:`intro`)::

    &JULES_INITIAL
      file = "initial_conditions.dat",

      nvars = 8,
      var(1) = 'canopy',      use_file(1) = F,  const_val(1) = 0.0 ,
      var(2) = 'tstar_tile',  use_file(2) = F,  const_val(2) = 276.78,
      var(3) = 'cs',          use_file(3) = F,  const_val(3) = 12.1,
      var(4) = 'gs',          use_file(4) = F,  const_val(4) = 0.0,
      var(5) = 'rgrain',      use_file(5) = F,  const_val(5) = 50.0,
      var(6) = 'snow_tile',   use_file(6) = F,  const_val(6) = 0.0,
      var(7) = 'sthuf',       use_file(7) = T,
      var(8) = 't_soil',      use_file(8) = T,
    /

This shows how a mixture of constant values and initial state from a file can be used. In this case, the first 6 variables will be set to constant values everywhere (:nml:mem:`JULES_INITIAL::use_file` = FALSE) with the last 2 read from the specified file (:nml:mem:`JULES_INITIAL::use_file` = TRUE).

:nml:mem:`JULES_INITIAL::file` specifies an ASCII file to read the variables for which :nml:mem:`JULES_INITIAL::use_file` = TRUE from.

Since the variables are arranged such that all those with :nml:mem:`JULES_INITIAL::use_file` = FALSE are first, we need only supply constant values for those variables that require them.

The contents of ``initial_conditions.dat`` should look similar to::

    # sthuf(1:4)                    t_soil(1:4)
      0.749  0.743  0.754  0.759    276.78  277.46  278.99  282.48

The data for each soil layer is given in consecutive columns. A comment line is used to indicate which columns comprise which variable (see :doc:`/input/overview` for more details).

Specifying initial state for gridded data using NetCDF files is similar, except that:

* :nml:mem:`JULES_INITIAL::var_name` is required for each variable read from file.
* If variable name templating is used, :nml:mem:`JULES_INITIAL::tpl_name` is required for each variable read from file.


Specification of initial state from an existing dump file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example, we use an existing dump file (from a previous run) to set the initial values of all required variables.

::

    &JULES_INITIAL
      total_snow = F,
      dump_file = T,
      file = "jules_dump.nc"
    /

:nml:mem:`JULES_INITIAL::total_snow` = FALSE indicates that we want to initialise all the snow variables directly from the dump.

:nml:mem:`JULES_INITIAL::dump_file` = TRUE indicates that the given file should be interpreted as a JULES dump file.

:nml:mem:`JULES_INITIAL::file` specifies the dump file to read (in this case a NetCDF dump file).

Since it is not specified, :nml:mem:`JULES_INITIAL::nvars` takes its default value of 0, which indicates that JULES should attempt to read all required variables from the given dump file.

