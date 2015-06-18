``ancillaries.nml``
===================


This file sets up the values for tile fractional coverage, soil properties, PDM and TOPMODEL parameters and agricultural fraction. It contains six namelists - :nml:lst:`JULES_FRAC`, :nml:lst:`JULES_SOIL_PARAM`, :nml:lst:`JULES_SOIL_PROPS`, :nml:lst:`JULES_PDM`, :nml:lst:`JULES_TOP` and :nml:lst:`JULES_AGRIC`.


``JULES_FRAC`` namelist members
-------------------------------

.. nml:namelist:: JULES_FRAC

This namelist specifies the fraction of the land area in each gridbox that is covered by each of the surface types. If :nml:mem:`JULES_SWITCHES::l_veg_compete` = TRUE, then the fraction of each surface type is modelled and the initial state should be specified in :nml:lst:`JULES_INITIAL`. In all other cases, it must be read here.

Note that all land points must be either soil points (indicated by values > 0 of the saturated soil moisture content), or land ice points (indicated by the fractional coverage of the ice surface type - if used - being one). The fractional cover of the ice surface type in each gridbox must be either zero or one - there cannot be partial coverage of ice within a gridbox.

If using either URBAN-2T or MORUSES then the total urban fraction should be entered in the :nml:mem:`JULES_MODEL_LEVELS::urban_canyon` or :nml:mem:`JULES_MODEL_LEVELS::urban` tile, whichever is specified. This is partitioned into canyon and roof fractions using the canyon fraction (W/R). The canyon fraction is set in :doc:`urban.nml` and can either be prescribed by the user or calculated by an empirical formula.


.. nml:member:: file

   :type: character
   :default: None

   The name of the file to read surface type fractional coverage data from.


.. nml:member:: frac_name

   :type: character
   :default: None

   The name of the variable containing the surface type fractional coverage data.

   .. note::
       This is only used for NetCDF files.
       For ASCII files, the surface type fractional coverage data is expected to be the first (ideally only) variable in the file.

   In the file, the variable must have a single levels dimension of size ``ntype`` called :nml:mem:`JULES_INPUT_GRID::type_dim_name`, and should not have a time dimension.


``JULES_SOIL_PARAM`` namelist members
-------------------------------------

.. nml:namelist:: JULES_SOIL_PARAM

This namelist is responsible for setting soil parameters that are not spacially varying.

.. nml:member:: zsmc

   :type: real
   :permitted: > 0
   :default: 1.0

   If a depth-averaged soil moisture diagnostic is requested, the average is calculated from the surface to this depth (m).


.. nml:member:: zst

   :type: real
   :permitted: > 0
   :default: 1.0

   If a depth-averaged soil temperature diagnostic is requested, the average is calculated from the surface to this depth (m).


.. nml:member:: confrac

   :type: real
   :permitted: 0 <= confrac <= 1
   :default: 0.3

   The fraction of the gridbox covered by convective precipitation.


.. nml:member:: dzsoil_io

   :type: real(sm_levels)
   :default: None

   The soil layer depths (m), starting with the uppermost layer.

   Note that the soil layer depths (and hence the total soil depth) are constant across the domain.

   In all the examples, JULES uses layer depths of 0.1, 0.25, 0.65 and 2.0m, giving a total depth of 3.0m. It is recommended that this is used unless there is good reason not to.



``JULES_SOIL_PROPS`` namelist members
-------------------------------------

.. nml:namelist:: JULES_SOIL_PROPS

This namelist specifies how spacially varying soil properties should be set.


.. nml:member:: const_z

   :type: logical
   :default: F

   Switch indicating if soil properties are to be uniform with depth.

   TRUE
       Soil characteristics do not vary with depth.

   FALSE
       Soil characteristics vary with depth.


.. nml:member:: file

   :type: character
   :default: None

   The file to read soil properties from.

   If :nml:mem:`use_file` is FALSE for every variable, this will not be used.

   This file name can use :doc:`variable name templating </input/file-name-templating>`.


.. nml:member:: nvars

   :type: integer
   :permitted: >= 0
   :default: 0

   The number of soil property variables that will be provided. At present, all variables are required for all runs.


.. nml:member:: var

   :type: character(nvars)
   :default: None

   List of soil variable names as recognised by JULES (see :ref:`list-of-soil-params`). Names are case sensitive.

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


.. _list-of-soil-params:

List of soil parameters
~~~~~~~~~~~~~~~~~~~~~~~

If :nml:mem:`const_z` = FALSE, variables read from file must have a single levels dimension of size :nml:mem:`JULES_MODEL_LEVELS::sm_levels` called :nml:mem:`JULES_INPUT_GRID::soil_dim_name`.

If :nml:mem:`const_z` = TRUE, variables read from file must have no levels dimensions.

In both cases, the variables must have no time dimension. Some examples of the setup of soil properties can be found in the ``examples`` directory.

.. tabularcolumns:: |p{2.5cm}|L|

+----------------------------+-----------------------------------------------------------------------------------------------------------+
| Name                       | Description                                                                                               |
+============================+===========================================================================================================+
| ``albsoil``                | Soil albedo. A single (averaged) waveband is used.                                                        |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``b``                      | Exponent in soil hydraulic characteristics.                                                               |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``hcap``                   | Dry heat capacity (J m\ :sup:`-3` K\ :sup:`-1`).                                                          |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``hcon``                   | Dry thermal conductivity (W m\ :sup:`-1` K\ :sup:`-1`).                                                   |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``satcon``                 | Hydraulic conductivity at saturation (kg m\ :sup:`-2` s\ :sup:`-1`).                                      |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``sathh``                  | If :nml:mem:`JULES_SWITCHES::l_vg_soil` = TRUE (using van Genuchten model),                               |
|                            | sathh = 1 / |alpha| (m\ :sup:`-1`), where |alpha| is a parameter of the van Genuchten model.              |
|                            |                                                                                                           |
|                            | .. |alpha| unicode:: &#x03B1; .. alpha                                                                    |
|                            |                                                                                                           |
|                            | If :nml:mem:`JULES_SWITCHES::l_vg_soil` = FALSE (using Brooks and Corey model), ``sathh`` is              |
|                            | the absolute value of the soil matric suction at saturation (m). The suction at saturation is generally   |
|                            | less than zero, but JULES uses the absolute value.                                                        |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``sm_crit``                | Volumetric soil moisture content at the critical point (m\ :sup:`3` water per m\ :sup:`3` soil). The      |
|                            | critical point is that at which soil moisture stress starts to restrict transpiration.                    |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``sm_sat``                 | Volumetric soil moisture content at saturation (m\ :sup:`3` water per m\ :sup:`3` soil).                  |
|                            |                                                                                                           |
|                            | .. note::                                                                                                 |
|                            |    This field is used to distinguish between soil points and land ice points.                             |
|                            |                                                                                                           |
|                            |    ``sm_sat > 0`` indicates a soil point.                                                                 |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``sm_wilt``                | Volumetric soil moisture content at the wilting point (m\ :sup:`3` water per m\ :sup:`3` soil). The       |
|                            | wilting point is that at which soil moisture stress completely prevents transpiration.                    |
+----------------------------+-----------------------------------------------------------------------------------------------------------+



``JULES_PDM`` namelist members
------------------------------

.. nml:namelist:: JULES_PDM

This namelist reads parameter values for the PDM-type parameterisation of surface runoff. The values are only used if :nml:mem:`JULES_SWITCHES::l_pdm` = TRUE. These parameters are held constant across the model domain. For further details of PDM, see references under :nml:mem:`JULES_SWITCHES::l_pdm`.


.. nml:member:: dz_pdm

   :type: real
   :default: 1.0

   The depth of soil considered by PDM (m).

   A value of ~1m can be used.


.. nml:member:: b_pdm

   :type: real
   :default: 1.0

   Shape factor for the pdf.



``JULES_TOP`` namelist members
------------------------------

.. nml:namelist :: JULES_TOP

This namelist reads parameter values for the TOPMODEL-type parameterisation of runoff. The values are only used if :nml:mem:`JULES_SWITCHES::l_top` = TRUE. The description below is very brief. For further details, see the references under :nml:mem:`JULES_SWITCHES::l_top`.


.. nml:member:: zw_max

   :type: real
   :default: 15.0

   The maximum allowed depth to the water table (m).

   This is the depth to the bottom of an additional layer below the :nml:mem:`JULES_MODEL_LEVELS::sm_levels` soil layers and hence should be set to a value greater than ``SUM(dzsoil)``.

   Values of 10 to 15m have been used.


.. nml:member:: ti_max

   :type: real
   :default: 10.0

   The maximum possible value of the topographic index.

   A value of 10 has been used successfully.


.. nml:member:: ti_wetl

   :type: real
   :default: 2.0

   A calibration parameter used in the calculation of the wetland fraction.

   It is used to increment the "critical" value of the topographic index that is used to calculate the saturated fraction of the gridbox. It excludes locations with large values of the topographic index from the wetland fraction.
   
   See Gedney and Cox (2003).
   
   A value of 2 has been used.


.. nml:group:: Members used to set up spacially varying properties

   .. nml:member:: file
   
      :type: character
      :default: None
   
      The file to read TOPMODEL properties from.
   
      If :nml:mem:`use_file` is FALSE for every variable, this will not be used.
  
      This file name can use :doc:`variable name templating </input/file-name-templating>`.
   
    
   .. nml:member:: nvars
   
      :type: integer
      :permitted: >= 0
      :default: 0
   
      The number of TOPMODEL property variables that will be provided. At present, all variables are required for runs using TOPMODEL.
   
   
   .. nml:member:: var
   
      :type: character(nvars)
      :default: None
   
      List of TOPMODEL variable names as recognised by JULES (see :ref:`list-of-topmodel-params`). Names are case sensitive.
   
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


.. _list-of-topmodel-params:

List of TOPMODEL parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~

All of the TOPMODEL variables listed below are expected to have no levels dimensions and no time dimension.

.. tabularcolumns:: |p{2.5cm}|L|

+----------------------------+-----------------------------------------------------------------------------------------------------------+
| Name                       | Description                                                                                               |
+============================+===========================================================================================================+
| ``fexp``                   | Decay factor describing how the saturated hydraulic conductivity decreases with depth below the standard  |
|                            | soil column (m\ :sup:`-1`).                                                                               |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``ti_mean``                | Mean value of the topographic index in each gridbox.                                                      |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``ti_sig``                 | Standard deviation of the topographic index in each gridbox.                                              |
+----------------------------+-----------------------------------------------------------------------------------------------------------+



``JULES_AGRIC`` namelist members
--------------------------------

.. nml:namelist:: JULES_AGRIC

If the TRIFFID vegetation model is used, the fractional area of agricultural land in each gridbox is specified using this namelist. Otherwise, the values in this namelist are not used.


.. nml:member:: zero_agric

   :type: logical
   :default: T

   Switch used to simplify the initialisation of agricultural fraction.

   TRUE
       Set agricultural fraction at all points to zero.

   FALSE
       Set agricultural fraction using specified data.


.. nml:group:: Used if :nml:mem:`zero_agric` = FALSE and the input grid consists of a single location

   .. nml:member:: frac_agr
   
      :type: real
      :default: None
   
      The agricultural fraction for the single location.


.. nml:group:: Used if :nml:mem:`zero_agric` = FALSE and the input grid consists of more than one location

   .. nml:member:: file
   
      :type: character
      :default: None
   
      The name of the file to read agricultural fraction data from.
   
   
   .. nml:member:: agric_name
   
      :type: character
      :default: None
   
      The name of the variable containing the agricultural fraction data.
   
      In the file, the variable must have no levels dimensions and no time dimension.


