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
   :default: F

   Switch controlling simplified initialisation of snow variables.

   TRUE
       Only the total mass of snow on each surface tile (see ``snow_tile`` in :ref:`list-of-initial-condition-variables`) is required to be input, and all related variables will be calculated from this or simple assumptions made. All the snow is assumed to be on the ground (not in the canopy).

   FALSE
       All snow variables required for the current configuration must be input separately (see :ref:`list-of-initial-condition-variables`).


.. nml:group:: Members used to set up spatially varying properties

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
      :default: '' (empty string)
   
      For each JULES variable specified in :nml:mem:`var` where :nml:mem:`use_file` = TRUE, this is the name of the variable in the file containing the data.

      If the empty string (the default) is given for any variable, then the corresponding value from :nml:mem:`var` is used instead.
   
      This is not used for variables where :nml:mem:`use_file` = FALSE, but a placeholder must still be given in that case.
   
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

   .. nml:member:: l_broadcast_soilt
   
      :type: logical
      :default: False
   
      Switch to allow non-soil tiled initial condition data to be broadcast to all soil tiles. This is only used when :nml:mem:`JULES_SOIL::l_tile_soil` is enabled. This helps distribute the model state, for example from a non-soil tiled run into a new run with soil tiling. Spin up of the model state should be considered when using this option.

      Note that if :nml:mem:`JULES_SOIL::l_tile_soil` = TRUE and values on soil tiles are available to define the initial state (e.g. from a previous run with soil tiling), :nml:mem:`l_broadcast_soilt` should be set to FALSE. Setting it to TRUE will result in the run failing because it will attempt to read a non-tiled variable.

.. _list-of-initial-condition-variables:

List of initial condition variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All input to the model must be on the same grid (see :doc:`/input/overview`), and initial conditions are no different. Even when the variable is only required for land points, values must be provided for the full input grid. Variables read as initial conditions must have no time dimension.

The variables it is possible to specify as initial conditions can be grouped into 'types' depending on the number and size of the levels dimensions they are required to have. For NetCDF files, the dimension names are those specified in the :nml:lst:`JULES_INPUT_GRID` namelist. For variables with no type specified, no levels dimensions should be used.

The required levels dimensions for each initial condition 'type' are given in the following table:

.. tabularcolumns:: |p{2.5cm}|p{2cm}|p{4cm}|p{6.5cm}|

+---------+------------------+-----------------------------------------------+--------------------------------------------------------+
| Type    | Number of levels | Levels dimension name(s)                      | Levels dimension size(s)                               |
|         | dimensions       |                                               |                                                        |
+=========+==================+===============================================+========================================================+
| soil    | 1                | :nml:mem:`JULES_INPUT_GRID::soil_dim_name`    | :nml:mem:`JULES_SOIL::sm_levels`                       |
+---------+------------------+-----------------------------------------------+--------------------------------------------------------+
| pft     | 1                | :nml:mem:`JULES_INPUT_GRID::pft_dim_name`     | :nml:mem:`JULES_SURFACE_TYPES::npft`                   |
+---------+------------------+-----------------------------------------------+--------------------------------------------------------+
| cpft    | 1                | :nml:mem:`JULES_INPUT_GRID::cpft_dim_name`    | :nml:mem:`JULES_SURFACE_TYPES::ncpft`                  |
+---------+------------------+-----------------------------------------------+--------------------------------------------------------+
| type    | 1                | :nml:mem:`JULES_INPUT_GRID::type_dim_name`    | ``ntype`` (:nml:mem:`JULES_SURFACE_TYPES::npft` +      |
|         |                  |                                               | :nml:mem:`JULES_SURFACE_TYPES::nnvg`)                  |
+---------+------------------+-----------------------------------------------+--------------------------------------------------------+
| surft   | 1                | :nml:mem:`JULES_INPUT_GRID::tile_dim_name`    | ``nsurft`` (1 if :nml:mem:`JULES_SURFACE::l_aggregate` |
|         |                  |                                               | = TRUE, ``ntype`` otherwise)                           |
+---------+------------------+-----------------------------------------------+--------------------------------------------------------+
| sclayer | 1                | :nml:mem:`JULES_INPUT_GRID::sclayer_dim_name` | Number of soil biogeochemistry layers.                 |
|         |                  |                                               |                                                        |
|         |                  |                                               | If using the single-pool moodel                        |
|         |                  |                                               | (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 1 )|
|         |                  |                                               | this is 1.                                             |
|         |                  |                                               |                                                        |
|         |                  |                                               | If using the 4-pool model                              |
|         |                  |                                               | (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2) |
|         |                  |                                               | with                                                   |
|         |                  |                                               | :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_layeredc` = FALSE   |
|         |                  |                                               | this is 1, else with                                   |
|         |                  |                                               | :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_layeredc` = TRUE    |
|         |                  |                                               | this is equal to :nml:mem:`JULES_SOIL::sm_levels`.     |
|         |                  |                                               |                                                        |
|         |                  |                                               | If using the ECOSSE model                              |
|         |                  |                                               | (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 3) |
|         |                  |                                               | this is equal to                                       |
|         |                  |                                               | :nml:mem:`JULES_SOIL_ECOSSE::dim_cslayer`.             |
+---------+------------------+-----------------------------------------------+--------------------------------------------------------+
| scpool  | 2                | :nml:mem:`JULES_INPUT_GRID::scpool_dim_name`, | number of soil carbon pools (1 if                      |
|         |                  | :nml:mem:`JULES_INPUT_GRID::sclayer_dim_name` | :nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 1,  |
|         |                  |                                               | 4 otherwise) and number of soil biogeochemistry layers |
|         |                  |                                               | (see ``sclayer`` above)                                |
+---------+------------------+-----------------------------------------------+--------------------------------------------------------+
| bedrock | 1                | :nml:mem:`JULES_INPUT_GRID::bedrock_dim_name` | :nml:mem:`JULES_SOIL::ns_deep`                         |
|         |                  |                                               |                                                        |
|         |                  |                                               | Only applicable if :nml:mem:`JULES_SOIL::l_bedrock` =  |
|         |                  |                                               | TRUE                                                   |
+---------+------------------+-----------------------------------------------+--------------------------------------------------------+
| snow    | 2                | :nml:mem:`JULES_INPUT_GRID::tile_dim_name`,   | ``nsurft`` (see above), :nml:mem:`JULES_SNOW::nsmax`   |
|         |                  | :nml:mem:`JULES_INPUT_GRID::snow_dim_name`    |                                                        |
|         |                  |                                               |                                                        |
|         |                  |                                               | Only applicable if ``nsmax > 0``                       |
+---------+------------------+-----------------------------------------------+--------------------------------------------------------+


The required variables for a particular configuration, along with their 'type' as specified above, are given in the following table.

.. tabularcolumns:: |p{3cm}|p{9cm}|p{3.5cm}|

+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Name                             | Description                                                                             | Type    |
+==================================+=========================================================================================+=========+
| Always required                                                                                                                      |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``canopy``                       | Amount of intercepted water that is held on each surface tile (kg m\ :sup:`-2`).        | surft   |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``cs``                           | Soil carbon (kg m\ :sup:`-2`).                                                          | scpool  |
|                                  |                                                                                         |         |
|                                  | If using the single-pool model (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 1),  |         |
|                                  | this is the total soil carbon.                                                          |         |
|                                  |                                                                                         |         |
|                                  | Otherwise, this is the carbon in each of the 4 pools of the 4-pool or ECOSSE models.    |         |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``snow_tile``                    | If :nml:mem:`JULES_VEGETATION::can_model` /= 4, this is the total snow on the surface   | surft   |
|                                  | tile (since there is a single store which doesn't distinguish between snow on canopy    |         |
|                                  | and under canopy).                                                                      |         |
|                                  |                                                                                         |         |
|                                  | If :nml:mem:`JULES_VEGETATION::can_model` = 4 (and then only at surface tiles where     |         |
|                                  | :nml:mem:`JULES_SNOW::cansnowpft` = TRUE), ``snow_tile`` is interpreted as the          |         |
|                                  | snow on the canopy, except when overridden by :nml:mem:`JULES_INITIAL::total_snow`      |         |
|                                  | = TRUE.                                                                                 |         |
|                                  |                                                                                         |         |
|                                  | If :nml:mem:`JULES_INITIAL::total_snow` = TRUE, ``snow_tile`` is used to hold the       |         |
|                                  | total snow on the surface tile (and is subsequently put onto the ground at tiles that   |         |
|                                  | distinguish between ground and canopy stores).                                          |         |
|                                  |                                                                                         |         |
|                                  | Further details of snow initialisation are given below.                                 |         |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``t_soil``                       | Temperature of each soil layer (K).                                                     | soil    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``tstar_tile``                   | Temperature of each surface tile (K). This is the surface or skin temperature.          | surft   |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if :nml:mem:`JULES_VEGETATION::can_rad_mod` = 1                                                                             |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``gs``                           | Surface conductance for water vapour (m s\ :sup:`-1`).                                  | None    |
|                                  |                                                                                         |         |
|                                  | This is used to start the iterative calculation of gs for the first timestep only.      |         |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if ``sthuf`` is not prescribed for all levels in :nml:lst:`JULES_PRESCRIBED`                                                |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``sthuf``                        | Soil wetness for each soil layer. This is the mass of soil water (liquid and frozen),   | soil    |
|                                  | expressed as a fraction of the water content at saturation.                             |         |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if :nml:mem:`JULES_VEGETATION::l_phenol` = TRUE                                                                             |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``lai``                          | Leaf area index of each PFT.                                                            | pft     |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if :nml:mem:`JULES_VEGETATION::l_triffid` = TRUE                                                                            |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``canht``                        | Height (m) of each PFT.                                                                 | pft     |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if :nml:mem:`JULES_VEGETATION::l_trif_biocrop` = TRUE                                                                       |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``years_since_harvest``          | Number of years since the previous harvest.                                             | pft     |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if :nml:mem:`JULES_VEGETATION::l_veg_compete` = TRUE                                                                        |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``frac``                         | The fraction of land area of each gridbox that is covered by each surface type.         | type    |
|                                  | N.B. values specified here will override those at :nml:lst:`JULES_FRAC`                 |         |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if :nml:mem:`JULES_IRRIG::l_irrig_dmd` = TRUE                                                                               |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``sthu_irr``                     | Unfrozen soil wetness of each layer as a fraction of saturation in irrigated fraction.  | soil    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if :nml:mem:`JULES_SURFACE_TYPES::ncpft` > 0                                                                                |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``cropdvi``                      | Development index for each crop pft.                                                    | cpft    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``croprootc``                    | Root carbon pool for each crop pft (kg m\ :sup:`-2`).                                   | cpft    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``cropharvc``                    | Carbon in 'harvest parts' pool for each crop pft (kg m\ :sup:`-2`) .                    | cpft    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+ 
| ``cropreservec``                 | Carbon in stem reserves pool for each crop pft (kg m\ :sup:`-2`).                       | cpft    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+ 
| ``croplai``                      | Leaf area index of each crop pft.                                                       | cpft    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``cropcanht``                    | Height (m) of each crop pft.                                                            | cpft    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if :nml:mem:`JULES_HYDROLOGY::l_top` = TRUE                                                                                 |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``sthzw``                        | Soil wetness in the deep LSH/TOPMODEL layer beneath the standard soil column.           | None    |
|                                  |                                                                                         |         |
|                                  | This is the mass of soil water (liquid and frozen), expressed as a fraction of the      |         |
|                                  | water content at saturation.                                                            |         |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``zw``                           | Depth from the surface to the water table (m).                                          | None    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if :nml:mem:`JULES_SOIL::l_bedrock` = TRUE                                                                                  |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``tsoil_deep``                   | Temperature of each bedrock layer (K)                                                   | bedrock |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if :nml:mem:`JULES_RADIATION::l_snow_albedo` = TRUE                                                                         |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``rgrain``                       | Snow surface grain size (\ |mu|\ m) on each surface tile.                               | None    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if :nml:mem:`total_snow` = FALSE                                                                                            |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``rho_snow``                     | Bulk density of lying snow (kg m\ :sup:`-3`).                                           | surft   |
|                                  |                                                                                         |         |
|                                  | If :nml:mem:`JULES_INITIAL::total_snow` = TRUE then this is set as follows:             |         |
|                                  |                                                                                         |         |
|                                  | * If :nml:mem:`JULES_SNOW::nsmax` = 0, it is set to                                     |         |
|                                  |   :nml:mem:`JULES_SNOW::rho_snow_const`.                                                |         |
|                                  | * If :nml:mem:`JULES_SNOW::nsmax` > 0 and there is an existing snow pack, it is set to  |         |
|                                  |   :nml:mem:`JULES_SNOW::rho_snow_const`.                                                |         |
|                                  | * If :nml:mem:`JULES_SNOW::nsmax` > 0 and there is no snow pack, it is set to           |         |
|                                  |   :nml:mem:`JULES_SNOW::rho_snow_fresh`.                                                |         |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``snow_depth``                   | Depth of snow (kg m).                                                                   | surft   |
|                                  |                                                                                         |         |
|                                  | If :nml:mem:`JULES_INITIAL::total_snow` = TRUE, this is calculated from mass and        |         |
|                                  | density of snow.                                                                        |         |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if :nml:mem:`total_snow` = FALSE and :nml:mem:`JULES_VEGETATION::can_model` = 4                                             |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``snow_grnd``                    | Amount of snow on the ground, beneath the canopy (kg m\ :sup:`-2`), on each surface     | surft   |
|                                  | tile.                                                                                   |         |
|                                  |                                                                                         |         |
|                                  | If :nml:mem:`JULES_INITIAL::total_snow` = TRUE this is set to ``snow_tile`` at tiles    |         |
|                                  | where :nml:mem:`JULES_VEGETATION::can_model` = 4 is active, and to zero at all other    |         |
|                                  | tiles.                                                                                  |         |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if :nml:mem:`total_snow` = FALSE and :nml:mem:`JULES_SNOW::nsmax` > 0                                                       |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``nsnow``                        | The number of snow layers on each surface tile.                                         | surft   |
|                                  |                                                                                         |         |
|                                  | If :nml:mem:`JULES_INITIAL::total_snow` = TRUE this is calculated from the snow depth.  |         |
|                                  |                                                                                         |         |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``snow_ds``                      | Depth of snow in each layer (kg m).                                                     | snow    |
|                                  |                                                                                         |         |
|                                  | If :nml:mem:`JULES_INITIAL::total_snow` = TRUE this is calculated from the snow depth   |         |
|                                  | and the number of snow layers.                                                          |         |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``snow_ice``                     | Mass of frozen water in each snow layer (kg m\ :sup:`-2`).                              | snow    |
|                                  |                                                                                         |         |
|                                  | If :nml:mem:`JULES_INITIAL::total_snow` = TRUE all snow is assumed to be ice.           |         |
|                                  |                                                                                         |         |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``snow_liq``                     | Mass of liquid water in each snow layer (kg m\ :sup:`-2`).                              | snow    |
|                                  |                                                                                         |         |
|                                  | If :nml:mem:`JULES_INITIAL::total_snow` = TRUE this is set to zero.                     |         |
|                                  |                                                                                         |         |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``tsnow``                        | Temperature of each snow layer (K).                                                     | snow    |
|                                  |                                                                                         |         |
|                                  | If :nml:mem:`JULES_INITIAL::total_snow` = TRUE this is set to the temperature of the    |         |
|                                  | top soil layer.                                                                         |         |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if :nml:mem:`total_snow` = FALSE, :nml:mem:`JULES_SNOW::nsmax` > 0 and :nml:mem:`JULES_RADIATION::l_snow_albedo` = TRUE     |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``rgrainl``                      | Snow grain size (\ |mu|\ m) on each surface tile in each snow layer.                    | snow    |
|                                  |                                                                                         |         |
|                                  | If :nml:mem:`JULES_INITIAL::total_snow` = TRUE this is set to ``rgrain``.               |         |
|                                  |                                                                                         |         |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if :nml:mem:`JULES_VEGETATION::l_triffid` = TRUE and :nml:mem:`JULES_VEGETATION::l_landuse` = TRUE                          |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``frac_agr_prev``                | Gridbox agricultural/crop fraction from previous TRIFFID timestep.                      | none    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``wood_prod_fast``               | Carbon content of the wood products pool with a fast decay rate.                        | none    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``wood_prod_med``                | Carbon content of the wood products pool with a medium decay rate.                      | none    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``wood_prod_slow``               | Carbon content of the wood products pool with a slow decay rate.                        | none    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if :nml:mem:`JULES_VEGETATION::l_triffid` = TRUE and :nml:mem:`JULES_VEGETATION::l_landuse` = TRUE and                      |
| :nml:mem:`JULES_VEGETATION::l_trif_crop` = TRUE                                                                                      |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``frac_past_prev``               | Gridbox pasture fraction from previous TRIFFID timestep.                                | none    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if :nml:mem:`JULES_VEGETATION::l_triffid` = TRUE and :nml:mem:`JULES_VEGETATION::l_landuse` = TRUE and                      |
| :nml:mem:`JULES_VEGETATION::l_trif_biocrop` = TRUE                                                                                   |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``frac_biocrop_prev``            | Gridbox bioenergy fraction from previous TRIFFID timestep.                              | none    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if using 4-pool model (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2) with                                 |         |
| :nml:mem:`JULES_VEGETATION::l_nitrogen` = TRUE., or if using ECOSSE                                                        |         |
| (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 3) with :nml:mem:`JULES_SOIL_ECOSSE::l_soil_n` = TRUE.                 |         |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``ns``                           | Soil nitrogen (kg m\ :sup:`-2`).                                                        | scpool  |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if using 4-pool model (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2) and                                  |         |
| :nml:mem:`JULES_VEGETATION::l_nitrogen` = TRUE.                                                                            |         |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``n_inorg``                      | Soil inorganic nitrogen  (kg m\ :sup:`-2`).                                             | sclayer |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if using ECOSSE (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 3) and                                        |         |
| :nml:mem:`JULES_SOIL_ECOSSE::l_soil_n` = TRUE.                                                                             |         |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``n_amm``                        | Soil ammonium  (kg m\ :sup:`-2`).                                                       | sclayer |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``n_nit``                        | Soil nitrate  (kg m\ :sup:`-2`).                                                        | sclayer |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if :nml:mem:`JULES_RIVERS::l_rivers` = TRUE, :nml:mem:`JULES_RIVERS::i_river_vn` = '2' and                                  |
| :nml:mem:`JULES_INITIAL::dump_file` = TRUE                                                                                           |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``rfm_surfstore_rp``             | Surface water storage on river routing points (m3)                                      | none    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``rfm_substore_rp``              | Sub-surface water storage on river routing points (m3)                                  | none    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``rfm_flowin_rp``                | Surface flow into a grid box on river routing points (m3)                               | none    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``rfm_bflowin_rp``               | Sub-surface flow into a grid box on river routing points (m3)                           | none    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if :nml:mem:`JULES_RIVERS::l_rivers` = TRUE, :nml:mem:`JULES_RIVERS::i_river_vn` = '1,3' and                                |
| :nml:mem:`JULES_INITIAL::dump_file` = TRUE                                                                                           |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``rivers_sto_rp``                | Water storage (kg)                                                                      | none    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if :nml:mem:`JULES_RIVERS::l_rivers` = TRUE, :nml:mem:`JULES_RIVERS::i_river_vn` = '3',                                     |
| :nml:mem:`JULES_INITIAL::dump_file` = TRUE and :nml:mem:`OASIS_RIVERS::send_fields` or                                               |
| :nml:mem:`JULES_OUTPUT_PROFILE::var` contains 'outflow_per_river'                                                                    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``rivers_outflow_rp``            | River outflow on river routing points (kg s\ :sup:`-1`)                                 | none    | 
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| Required if :nml:mem:`JULES_VEGETATION::photo_acclim_model` = 2 or 3                                                                 |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+
| ``t_growth_gb``                  | Running mean air temperature (K)                                                        | none    |
+----------------------------------+-----------------------------------------------------------------------------------------+---------+


.. warning::
  if :nml:mem:`JULES_RIVERS::l_rivers` = TRUE, :nml:mem:`JULES_RIVERS::i_river_vn` = '2' and :nml:mem:`JULES_INITIAL::dump_file` = FALSE,
    rfm_surfstore_rp, rfm_substore_rp, rfm_flowin_rp and rfm_bflowin are initialised to zero.

.. warning::
  if :nml:mem:`JULES_RIVERS::l_rivers` = TRUE, :nml:mem:`JULES_RIVERS::i_river_vn` = '1,3' and :nml:mem:`JULES_INITIAL::dump_file` = FALSE, 
  rivers_sto_rp is initialised to zero.

.. |mu| unicode:: &#x03BC; .. u


Examples of specification of initial state
------------------------------------------

Specification of initial state at a single point
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This assumes that :nml:mem:`JULES_VEGETATION::l_phenol` = FALSE, :nml:mem:`JULES_VEGETATION::l_triffid` = FALSE, :nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 1 and :nml:mem:`JULES_SNOW::nsmax` = 0.

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
      dump_file = T,
      file = "jules_dump.nc"
    /

:nml:mem:`JULES_INITIAL::dump_file` = TRUE indicates that the given file should be interpreted as a JULES dump file.

:nml:mem:`JULES_INITIAL::file` specifies the dump file to read (in this case a NetCDF dump file).

Since it is not specified, :nml:mem:`JULES_INITIAL::nvars` takes its default value of 0, which indicates that JULES should attempt to read all required variables from the given dump file.

