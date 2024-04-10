``ancillaries.nml``
===================


This file sets up spatially varying ancillary values. It contains the following namelists: :nml:lst:`JULES_FRAC`, :nml:lst:`JULES_VEGETATION_PROPS`, :nml:lst:`JULES_SOIL_PROPS`, :nml:lst:`JULES_TOP`, :nml:lst:`JULES_PDM`, :nml:lst:`JULES_AGRIC`, :nml:lst:`JULES_CROP_PROPS`, :nml:lst:`JULES_IRRIG_PROPS`, :nml:lst:`JULES_RIVERS_PROPS`, :nml:lst:`JULES_OVERBANK_PROPS`, :nml:lst:`JULES_WATER_RESOURCES_PROPS`, :nml:lst:`URBAN_PROPERTIES` , :nml:lst:`JULES_CO2` and :nml:lst:`JULES_FLAKE`.

Data associated with each of these namelists can optionally be read from the dump file (if present) by setting ``read_from_dump`` to true. This functionality provides closer alignment with UM functionality and can help ensure that the correct ancillary data remain associated with the model state.

``JULES_FRAC`` namelist members
-------------------------------

.. nml:namelist:: JULES_FRAC

This namelist specifies the fraction of the land area in each gridbox that is covered by each of the surface types. If :nml:mem:`JULES_VEGETATION::l_veg_compete` = TRUE, then the fraction of each surface type is modelled and the initial state should be specified in :nml:lst:`JULES_INITIAL`. In all other cases, it must be read here.

Note that all land points must be either soil points (indicated by values > 0 of the saturated soil moisture content), or land ice points (indicated by the fractional coverage of the ice surface type - if used - being one). The fractional cover of the ice surface type in each gridbox must be either zero or one - there cannot be partial coverage of ice within a gridbox.

If using either URBAN-2T or MORUSES then the total *urban* fraction can be specified instead of the separate :nml:mem:`JULES_SURFACE_TYPES::urban_canyon` and :nml:mem:`JULES_SURFACE_TYPES::urban_roof` contributions. When initialising, if the roof fraction is zero, the canyon fraction will be interpreted as the total *urban* fraction and be partitioned according to canyon fraction (W/R, see :nml:lst:`URBAN_PROPERTIES`).

.. note::    For runs with dynamic vegetation (TRIFFID, :nml:mem:`JULES_VEGETATION::l_triffid` = TRUE) and :nml:mem:`JULES_VEGETATION::l_veg_compete` = TRUE, then the fraction of each surface type is being modelled and the initial state should be specified in :nml:lst:`JULES_INITIAL` (which will override any settings given in this section). In all other cases, frac must be read here.

.. nml:member:: read_from_dump

   :type: logical
   :default: F

   TRUE
      Populate variables associated with this namelist from the dump file. All other namelist members are ignored.

   FALSE
      Use the other namelist members to determine how to populate variables.


.. nml:member:: file

   :type: character
   :default: None

   The name of the file to read surface type fractional coverage data from.


.. nml:member:: frac_name

   :type: character
   :default: 'frac'

   The name of the variable containing the surface type fractional coverage data.

   .. note::
       This is only used for NetCDF files.
       For ASCII files, the surface type fractional coverage data is expected to be the first (ideally only) variable in the file.



   .. note::
       The open water fraction of this array (given by :nml:mem:`JULES_SURFACE_TYPES::lake`) should contain permanent water, and wetland extents that are not being otherwise simulated.
       If groundwater inundation is being simulated (i.e. TOPMODEL is active :nml:mem:`JULES_HYDROLOGY::l_top` = TRUE and therefore fsat is being calculated) then all groundwater-maintained wetlands must be excluded from :nml:mem:`JULES_FRAC::frac_name`.
       If overbank inundation is being simulated (i.e. :nml:mem:`JULES_RIVERS::l_riv_overbank` = TRUE) then all fluvial wetlands must be excluded from :nml:mem:`JULES_FRAC::frac_name`.
       Finally, note that simulation of a potential future climate scenario with greatly reduced areas for lakes that are currently 'permanent' would require suitable modification of the ancillary provided here.

   In the file, the variable must have a single levels dimension of size ``ntype`` called :nml:mem:`JULES_INPUT_GRID::type_dim_name`, and should not have a time dimension.



``JULES_VEGETATION_PROPS`` namelist members
-------------------------------------------

.. nml:namelist:: JULES_VEGETATION_PROPS


This namelist specifies how spatially-varying  properties of vegetation should be set.

At present only one variable - ``t_home_gb`` - can be specified via this namelist, and this is only required if thermal adaptation of photosynthetic capacity is selected (:nml:mem:`JULES_VEGETATION::photo_acclim_model` = 1 or 3).

Note that Leaf Area Index and vegetation height are specified elsewhere - see :nml:lst:`JULES_PRESCRIBED`.


.. nml:member:: read_from_dump

   :type: logical
   :default: F

   TRUE
      Populate variables associated with this namelist from the dump file. All other namelist members are ignored.

   FALSE
      Use the other namelist members to determine how to populate variables.


.. nml:member:: file

   :type: character
   :default: None

   The file to read vegetation properties from.

   If :nml:mem:`use_file` is FALSE for every variable, this will not be used.

   This file name can use :doc:`variable name templating </input/file-name-templating>`.


.. nml:member:: nvars

   :type: integer
   :permitted: >= 0
   :default: 0

   The number of vegetation property variables that will be provided (see :ref:`list-of-vegetation-params`).


.. nml:member:: var

   :type: character(nvars)
   :default: None

   List of vegetation variable names as recognised by JULES (see :ref:`list-of-vegetation-params`). Names are case sensitive.

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

   For each JULES variable specified in :nml:mem:`var` where :nml:mem:`use_file` = FALSE, this is a constant value that the variable will be set to at every point.

   This is not used for variables where :nml:mem:`use_file` = TRUE, but a placeholder must still be given in that case.


.. _list-of-vegetation-params:

List of vegetation parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabularcolumns:: |p{2cm}|p{9cm}|

+-----------------+--------------------------------------------------------------------------------------+
| Name            | Description                                                                          |
+=================+======================================================================================+
| ``t_home_gb``   | Average temperature (home temperature) for thermal adaptation of photosynthetic      |
|                 | capacity (K), e.g. a multi-decadal average or pre-industrial temperature.            |
|                 | Suggestions as to how to calculate a suitable temperature can be found in            |
|                 | :ref:`Kattge and Knorr (2007)<References_ancillaries>` or                            |
|                 | :ref:`Kumarathunge et al (2019)<References_ancillaries>`. This variable should not   |
|                 | have a time dimension nor any "levels" dimension.                                    |
+-----------------+--------------------------------------------------------------------------------------+




``JULES_SOIL_PROPS`` namelist members
-------------------------------------

.. nml:namelist:: JULES_SOIL_PROPS

This namelist specifies how spatially varying soil properties should be set.

.. nml:member:: read_from_dump

   :type: logical
   :default: F

   TRUE
      Populate variables associated with this namelist from the dump file. All other namelist members are ignored.

   FALSE
      Use the other namelist members to determine how to populate variables.


.. nml:member:: const_z

   :type: logical
   :default: F

   Switch indicating if soil properties are to be uniform with depth.

   TRUE
       Soil characteristics do not vary with depth.

   FALSE
       Soil characteristics vary with depth. For any variable this is ignored if a constant value is to be used (see :nml:mem:`const_val`).


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

   The number of soil property variables that will be provided (see :ref:`list-of-soil-params`).


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

   For each JULES variable specified in :nml:mem:`var` where :nml:mem:`use_file` = FALSE, this is a constant value that the variable will be set to at every point in every layer (overriding :nml:mem:`const_z` = FALSE).

   This is not used for variables where :nml:mem:`use_file` = TRUE, but a placeholder must still be given in that case.


.. _list-of-soil-params:

List of soil parameters
~~~~~~~~~~~~~~~~~~~~~~~

If :nml:mem:`const_z` = FALSE, variables read from file must have a single levels dimension. For most variables this dimension must be of size :nml:mem:`JULES_SOIL::sm_levels` and called :nml:mem:`JULES_INPUT_GRID::soil_dim_name`; exceptions to this rule are indicated in the table below.

If :nml:mem:`const_z` = TRUE, variables read from file must have no levels dimensions.

If soil tiling is selected (:nml:mem:`JULES_SOIL::l_tile_soil` = TRUE), ancillary fields can be specified for each soil tile (:nml:mem:`JULES_SOIL::l_broadcast_ancils` = FALSE), or values can be read for one soil tile and copied to all tiles (:nml:mem:`JULES_SOIL::l_broadcast_ancils` = TRUE).

In all cases, the variables must have no time dimension.

.. tabularcolumns:: |p{2cm}|p{9cm}|p{3.5cm}|

+-----------------+--------------------------------------------------------------------------------------+--------------------------------------------------+
| Name            | Description                                                                          | Levels name                                      |
+=================+======================================================================================+==================================================+
| ``albsoil``     | Soil albedo. A single (averaged) waveband is used.                                   | None                                             |
+-----------------+--------------------------------------------------------------------------------------+--------------------------------------------------+
| ``b``           | Exponent in soil hydraulic characteristics.                                          | :nml:mem:`JULES_INPUT_GRID::soil_dim_name`       |
|                 |    n.b. Related to the Brooks & Corey parameter lambda by b=1/lambda                 |                                                  |
|                 |    and to the van Genuchten-Mualem parameter n by b=1/(n-1)                          |                                                  |
+-----------------+--------------------------------------------------------------------------------------+--------------------------------------------------+
| ``hcap``        | Dry heat capacity (J m\ :sup:`-3` K\ :sup:`-1`).                                     | :nml:mem:`JULES_INPUT_GRID::soil_dim_name`       |
+-----------------+--------------------------------------------------------------------------------------+--------------------------------------------------+
| ``hcon``        | Dry thermal conductivity (W m\ :sup:`-1` K\ :sup:`-1`).                              | :nml:mem:`JULES_INPUT_GRID::soil_dim_name`       |
+-----------------+--------------------------------------------------------------------------------------+--------------------------------------------------+
| ``satcon``      | Hydraulic conductivity at saturation (kg m\ :sup:`-2` s\ :sup:`-1`).                 | :nml:mem:`JULES_INPUT_GRID::soil_dim_name`       |
+-----------------+--------------------------------------------------------------------------------------+--------------------------------------------------+
| ``sathh``       | If :nml:mem:`JULES_SOIL::l_vg_soil` = TRUE (i.e. using van Genuchten model),         | :nml:mem:`JULES_INPUT_GRID::soil_dim_name`       |
|                 | ``sathh`` = 1 / ``alpha``, where ``alpha`` (m\ :sup:`-1`) is a parameter of the van  |                                                  |
|                 | Genuchten model.                                                                     |                                                  |
|                 |                                                                                      |                                                  |
|                 | If :nml:mem:`JULES_SOIL::l_vg_soil` = FALSE (using Brooks and Corey model), ``sathh``|                                                  |
|                 | is the soil matric suction at saturation (in pressure head units, m), i.e. the       |                                                  |
|                 | absolute value of the soil matric potential at saturation.                           |                                                  |
+-----------------+--------------------------------------------------------------------------------------+--------------------------------------------------+
| ``sm_crit``     | Volumetric soil moisture content at the critical point (m\ :sup:`3` water per        | :nml:mem:`JULES_INPUT_GRID::soil_dim_name`       |
|                 | m\ :sup:`3` soil). If :nml:mem:`JULES_VEGETATION::l_use_pft_psi` = F,                |                                                  |
|                 | the point at which soil moisture stress starts to restrict                           |                                                  |
|                 | transpiration is a function of ``sm_crit``, ``sm_sat`` and the pft-dependent         |                                                  |
|                 | parameter :nml:mem:`JULES_PFTPARM::fsmc_p0_io` .                                     |                                                  |
|                 |                                                                                      |                                                  |
|                 | ``sm_crit`` is also used to calculate the surface conductance of bare soil.          |                                                  |
+-----------------+--------------------------------------------------------------------------------------+--------------------------------------------------+
| ``sm_sat``      | Volumetric soil moisture content at saturation (m\ :sup:`3` water per m\ :sup:`3`    | :nml:mem:`JULES_INPUT_GRID::soil_dim_name`       |
|                 | soil).                                                                               |                                                  |
|                 |                                                                                      |                                                  |
|                 | .. note::                                                                            |                                                  |
|                 |    This field is used to distinguish between soil points and land ice points.        |                                                  |
|                 |                                                                                      |                                                  |
|                 |    ``sm_sat > 0`` indicates a soil point.                                            |                                                  |
+-----------------+--------------------------------------------------------------------------------------+--------------------------------------------------+
| ``sm_wilt``     | Volumetric soil moisture content at the wilting point (m\ :sup:`3` water             | :nml:mem:`JULES_INPUT_GRID::soil_dim_name`       |
|                 | per m\ :sup:`3` soil). If :nml:mem:`JULES_VEGETATION::l_use_pft_psi` = F,            |                                                  |
|                 | ``sm_wilt`` is the limit where soil moisture stress                                  |                                                  |
|                 | completely prevents transpiration.                                                   |                                                  |
|                 |                                                                                      |                                                  |
|                 | ``sm_wilt`` is also used to calculate soil respiration.                              |                                                  |
+-----------------+--------------------------------------------------------------------------------------+--------------------------------------------------+
| ``clay``        | Soil clay content (g clay per g soil). Only required for the 4-pool and ECOSSE soil  | :nml:mem:`JULES_INPUT_GRID::sclayer_dim_name`    |
|                 | carbon models (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2 or 3).           |                                                  |
|                 |                                                                                      |                                                  |
|                 | .. note::                                                                            |                                                  |
|                 |    To allow backwards compatibility when using the 4-pool model                      |                                                  |
|                 |    (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2), if the clay content is    |                                                  |
|                 |    not available it is set to 0.0 in the code.                                       |                                                  |
|                 |                                                                                      |                                                  |
|                 |    However, this is wrong - if it is not available it should be set to 0.23.         |                                                  |
+-----------------+--------------------------------------------------------------------------------------+--------------------------------------------------+
| ``soil_ph``     | Soil pH. Only required for the ECOSSE soil carbon model                              | :nml:mem:`JULES_INPUT_GRID::sclayer_dim_name`    |
|                 | (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 3).                              |                                                  |
+-----------------+--------------------------------------------------------------------------------------+--------------------------------------------------+


``JULES_TOP`` namelist members
------------------------------

.. nml:namelist :: JULES_TOP

This namelist reads spatially varying parameter values for the TOPMODEL-type parameterisation of runoff. The values are only used if :nml:mem:`JULES_HYDROLOGY::l_top` = TRUE. The description below is very brief. For further details, see the references under :nml:mem:`JULES_HYDROLOGY::l_top`.


.. nml:member:: read_from_dump

   :type: logical
   :default: F

   TRUE
      Populate variables associated with this namelist from the dump file. All other namelist members are ignored.

   FALSE
      Use the other namelist members to determine how to populate variables.


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

   The number of TOPMODEL property variables that will be provided. At present, all variables are required for runs using TOPMODEL (see :ref:`list-of-topmodel-params`).


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

   This is not used for variables where :nml:mem:`use_file` = TRUE, but a placeholder must still be given in that case.


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
|                            |                                                                                                           |
|                            | Routinely set between 2 and 3 m\ :sup:`-1`. Gedney & Cox (2003, J Hydromet) used value 0.5 m\ :sup:`-1`;  |
|                            | Niu & Yang (2003, Global & Planet. Change) suggested a global mean value of 2.0 m\ :sup:`-1`.             |
|                            |                                                                                                           |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``ti_mean``                | (Spatial, not temporal) mean value of the topographic index in each gridbox.                              |
|                            | Value 5.99 is the global mean given in Marthews et al. (2015, HESS)                                       |
|                            |                                                                                                           |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``ti_sig``                 | (Spatial, not temporal) standard deviation of the topographic index in each gridbox.                      |
|                            | Values <0.5 are updated to =0.5 internally to allow at least some variability                             |
|                            |                                                                                                           |
+----------------------------+-----------------------------------------------------------------------------------------------------------+


``JULES_PDM`` namelist members
------------------------------

.. nml:namelist :: JULES_PDM

This namelist reads spatially varying parameter values for the PDM-type parameterisation of runoff. The values are only used if :nml:mem:`JULES_HYDROLOGY::l_pdm` = TRUE. The description below is very brief. For further details, see the references under :nml:mem:`JULES_HYDROLOGY::l_pdm`.


.. nml:member:: file

   :type: character
   :default: None

   The file to read PDM properties from.

   If :nml:mem:`use_file` is FALSE for every variable, this will not be used.

   This file name can use :doc:`variable name templating </input/file-name-templating>`.


.. nml:member:: nvars

   :type: integer
   :permitted: >= 0
   :default: 0

   The number of PDM property variables that will be provided (see :ref:`list-of-pdm-params`). At present, only the topographic slope can be provided.


.. nml:member:: var

   :type: character(nvars)
   :default: None

   List of PDM variable names as recognised by JULES (see :ref:`list-of-pdm-params`). Names are case sensitive.

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
   make html
   This is not used for variables where :nml:mem:`use_file` = TRUE, but a placeholder must still be given.


.. _list-of-pdm-params:

List of PDM parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~

All of the PDM variables listed below are expected to have no levels dimensions and no time dimension.

.. tabularcolumns:: |p{2.5cm}|L|

+----------------------------+-----------------------------------------------------------------------------------------------------------+
| Name                       | Description                                                                                               |
+============================+===========================================================================================================+
| ``slope``                  | Mean value of the topographic slope in the gridbox (deg).                                                 |
+----------------------------+-----------------------------------------------------------------------------------------------------------+


``JULES_AGRIC`` namelist members
--------------------------------

.. nml:namelist:: JULES_AGRIC

If the TRIFFID vegetation model is used, the fractional area of agricultural land in each gridbox is specified using this namelist. Otherwise, the values in this namelist are not used.


.. nml:member:: read_from_dump

   :type: logical
   :default: F

   TRUE
      Populate frac_agr, frac_past, and frac_biocrop from the dump file. All other namelist members are ignored.

   FALSE
      Use the other namelist members to determine how to populate variables.


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
      :default: 'frac_agr'

      The name of the variable containing the agricultural fraction data.

      In the file, the variable must have no levels dimensions and no time dimension.


.. nml:member:: zero_past

   :type: logical
   :default: T

   Switch used to simplify the initialisation of pasture fraction. Pasture fraction can only be used if :nml:mem:`JULES_VEGETATION::l_trif_crop` is TRUE.

   TRUE
       Set pasture fraction at all points to zero.

   FALSE
       Set pasture fraction using specified data.


.. nml:group:: Used if :nml:mem:`zero_past` = FALSE and the input grid consists of a single location

   .. nml:member:: frac_past

      :type: real
      :default: None

      The pasture fraction for the single location.


.. nml:group:: Used if :nml:mem:`zero_past` = FALSE and the input grid consists of more than one location

   .. nml:member:: file_past

      :type: character
      :default: None

      The name of the file to read pasture fraction data from.


   .. nml:member:: pasture_name

      :type: character
      :default: 'frac_past'

      The name of the variable containing the pasture fraction data.

      In the file, the variable must have no levels dimensions and no time dimension.


.. nml:member:: zero_biocrop

   :type: logical
   :default: T

   Switch used to simplify the initialisation of bioenergy fraction. Bioenergy fraction can only be used if :nml:mem:`JULES_VEGETATION::l_trif_biocrop` is TRUE.

   TRUE
       Set bioenergy fraction at all points to zero.

   FALSE
       Set bioenergy fraction using specified data.


.. nml:group:: Used if :nml:mem:`zero_biocrop` = FALSE and the input grid consists of a single location

   .. nml:member:: frac_biocrop

      :type: real
      :default: None

      The bioenergy fraction for the single location.


.. nml:group:: Used if :nml:mem:`zero_biocrop` = FALSE and the input grid consists of more than one location

   .. nml:member:: file_biocrop

      :type: character
      :default: None

      The name of the file to read bioenergy fraction data from.


   .. nml:member:: biocrop_name

      :type: character
      :default: 'frac_biocrop'

      The name of the variable containing the bioenergy fraction data.

       In the file, the variable must have no levels dimensions and no time dimension.


.. nml:group:: Specify the day of year on which harvesting occurs. Only used if :nml:mem:`JULES_VEGETATION::l_trif_biocrop` = TRUE. A placeholder value must be set for all PFTs, though will only be used for PFTs with :nml:mem:`JULES_TRIFFID::harvest_type_io` = 2.


  .. nml:member:: read_harvest_doy_from_dump

     :type: logical
     :default: F

     TRUE
        Populate harvest_doy from the dump file. All other namelist members are ignored.

     FALSE
        Use the other namelist members to determine how to populate variables.


  .. nml:member:: file_harvest_doy

     :type: character
     :default: None

     The name of the file to read harvest day-of-year data from.


  .. nml:member:: harvest_doy_name

     :type: character
     :default: 'harvest_doy'

     The name of the variable containing the harvest day-of-year data.

     .. note::
         This is only used for NetCDF files.
         For ASCII files, the harvest day-of-year data is expected to be the first (ideally only) variable in the file.


``JULES_CROP_PROPS`` namelist members
-------------------------------------

.. nml:namelist:: JULES_CROP_PROPS


.. nml:member:: read_from_dump

   :type: logical
   :default: F

   TRUE
      Populate variables associated with this namelist from the dump file. All other namelist members are ignored.

   FALSE
      Use the other namelist members to determine how to populate variables.


.. nml:member:: file

   :type: character
   :default: None

   The file from which crop properties are read.

   If :nml:mem:`use_file` is FALSE for every variable, this will not be used.

   This file name can use :doc:`variable name templating </input/file-name-templating>`.


.. nml:member:: nvars

   :type: integer
   :permitted: >= 0
   :default: 0

   The number of crop property variables that will be provided (see :ref:`list-of-spatially-varying-crop-properties`).


.. nml:member:: var

   :type: character(nvars)
   :default: None

   List of variable names for spatially-varying crop properties as recognised by JULES (see :ref:`list-of-spatially-varying-crop-properties`). Names are case sensitive.

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

   This is not used for variables where :nml:mem:`use_file` = TRUE, but a placeholder must still be given in that case.


.. _list-of-spatially-varying-crop-properties:

List of spatially-varying crop properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All of the crop variables listed below are expected to have a single levels dimension of size :nml:mem:`JULES_SURFACE_TYPES::ncpft` called :nml:mem:`JULES_INPUT_GRID::cpft_dim_name`.

.. tabularcolumns:: |p{3.75cm}|p{11cm}|

+----------------------------+-----------------------------------------------------------------------------------------------------------+
| Name                       | Description                                                                                               |
+============================+===========================================================================================================+
| ``cropsowdate``            | The sowing date for each crop.                                                                            |
|                            |                                                                                                           |
|                            | The sowing date should be a real number, with ``0 < nint(sowing_date) < number of days in year``.         |
|                            | For example, for a 365 day year, sow_date = 1.0 is Jan 1st and sow_date = 365.0 is Dec 31st.              |
|                            |                                                                                                           |
|                            | If a crop requires two sowing dates per year, it should be treated as two separate crops with identical   |
|                            | parameters apart from the sowing date.                                                                    |
|                            |                                                                                                           |
|                            |                                                                                                           |
|                            | .. note:: Only required if :nml:mem:`JULES_VEGETATION::l_prescsow` = TRUE.                                |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``cropttveg``              | Thermal time between emergence and flowering (degree days).                                               |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``cropttrep``              | Thermal time between flowering and maturity/harvest (degree days).                                        |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``croplatestharvdate``     | The latest possible harvest date for each crop.                                                           |
|                            | croplatestharvdate is only a required variable when                                                       |
|                            | :nml:mem:`JULES_VEGETATION::l_croprotate` = TRUE and                                                      |
|                            | :nml:mem:`JULES_VEGETATION::l_prescsow` = TRUE.                                                           |
|                            |                                                                                                           |
|                            | croplatestharvdate is not a required variable when                                                        |
|                            | :nml:mem:`JULES_VEGETATION::l_croprotate` = FALSE and                                                     |
|                            | :nml:mem:`JULES_VEGETATION::l_prescsow` = TRUE but will be used if provided in the ancillary file         |
|                            |                                                                                                           |
|                            | croplatestharvdate is not a required variable and is only used if provided as an ancillary when           |
|                            | :nml:mem:`JULES_VEGETATION::l_prescsow` = TRUE.                                                           |
|                            |                                                                                                           |
+----------------------------+-----------------------------------------------------------------------------------------------------------+

.. seealso::
   References:

   * Osborne et al, `JULES-crop: a parametrisation of crops in the Joint UK Land Environment Simulator <http://www.geosci-model-dev.net/8/1139/2015/gmd-8-1139-2015.html>`_, Geosci. Model Dev., 8, 1139-1155, 2015.
   * Mathison et al, 'Developing a sequential cropping capability in the JULESvn5.2 land–surface model', Geosci. Model Dev. Discuss., https://doi.org/10.5194/gmd-2019-85, in review, 2019


``JULES_IRRIG_PROPS`` namelist members
--------------------------------------

.. nml:namelist:: JULES_IRRIG_PROPS

This namelist specifies the options available for initialising irrigated fraction.

.. nml:member:: read_from_dump

   :type: logical
   :default: F

   TRUE
      Populate variables associated with this namelist from the dump file. All other namelist members are ignored.

   FALSE
      Use the other namelist members to determine how to populate variables.


.. nml:member:: read_file

   :type: logical
   :default: T

   Indicates if irrigated fraction is to be read from file.

   TRUE
       Irrigated fraction is read from the file specified in :nml:mem:`irrig_frac_file`.

   FALSE
       Irrigated fraction is set to the constant value specified in :nml:mem:`const_frac_irr`.


.. nml:member:: irrig_frac_file

   :type: character
   :default: None

   The file from which irrigation fractions are read, including path.


.. nml:member:: var_name

   :type: character
   :default: 'frac_irig'

   The name of the variable containing the irrigated fraction data.

   .. note::
       This is only used for NetCDF files.
       For ASCII files, the irrigated fraction data is expected to be the first (ideally only) variable in the file.

   In the file, the variable must have no levels or time dimensions.


.. nml:member:: const_frac_irr

   :type: real
   :default: none

   The constant irrigated fraction to be applied to all grid points.

.. nml:member:: const_irrfrac_irrtiles

   :type: real
   :default: none

   The constant irrigated fraction to be applied to specific surface tiles given in :nml:mem:`JULES_IRRIG::irrigtiles`.



``JULES_RIVERS_PROPS`` namelist members
---------------------------------------

.. nml:namelist:: JULES_RIVERS_PROPS

This namelist specifies how spatially varying river routing properties should be set.

.. note:: ``read_from_dump`` is not currently implemented for this namelist, meaning that river ancillary variables cannot be read from a dump file. Initial values of river prognostic variables can however be read from a dump file (see :nml:lst:`JULES_INITIAL`).

.. note::
   The grid on which the river routing will run, and on which river routing ancillaries must be provided, could potentially differ from the input/model grid specified in :doc:`model_grid.nml`.

   For the duration of this section, the following nomenclature will be used:

   *  **Model input grid** - The full JULES input grid specified in :nml:lst:`JULES_INPUT_GRID`.
   *  **Land grid** - The grid that JULES runs on (not rivers) - this is the grid that includes land points. If JULES is using a 1-D grid internally, the land grid is the notional 2D grid across which the points can be scattered.
   *  **River routing input grid** - The grid on which river routing ancillaries are provided.
   *  **River domain** - That part of the river input grid that is selected for modelling.
     
   Information about the river routing input grid and its relationship to the land grid is specified in this namelist. In all cases river routing is only possible if the land and river grids are regular, in that they have a constant spacing between rows and columns (but see note below about 1D model input grids).

   The river routing input grid must always be defined on a 2D grid, as defined through the x and y dimensions of the rivers ancillary file (see :nml:mem:`x_dim_name` and :nml:mem:`y_dim_name` for further details). If the model input is defined on a 1D grid, those points must be a subset of a regular grid (meaning one with constant spacing of points in each of the 2 dimensions) if river routing is to be activated. 

   JULES calculates runoff on the land grid and this information is then transferred to the river grid by either regridding (when the grids are not coincident) or remapping (between coincident grids). Here coincident means grids of the same resolution and for which points in each grid coincide. Hence land and river grids of different resolution are linked through regridding (interpolation), while a simpler remapping can be used when the gridboxes coincide. Note that functionality to regrid only currently exists for grids that are defined by latitude and longitude coordinates; all other coordinate systems have to be handled through remapping.

   Internally JULES converts the river routing input grid to a 1D river routing model grid, with length ``np_rivers``, which is the number of valid routing points in the domain of interest. All river routing output is either defined on the 1D river routing model grid or is regridded to the land grid.

   The most satisfactory situation is one in which the areas covered by land and river gridboxes are identical (though the resolutions can differ). In that case all the runoff that is generated on the land is correctly captured by the river network, and each river length has a well-defined input of local runoff. However there are situations in which the user might be prepared to allow other configurations - e.g. if studying a particular catchment, land in headwaters of surrounding catchments might not be covered by the river ancillary.



.. nml:group:: Members used to define the river routing input grid


   .. nml:member:: coordinate_file

      :type: character
      :default: None

      The file from which to read coordinate information for the river routing input grid. This is only used when :nml:mem:`file` includes :doc:`variable-name templating </input/file-name-templating>`, i.e. it is only used when ancillary variables will come from multiple files, in which case this variable is used to provide clarity as to where the coordinates are read from.


   .. nml:member:: x_dim_name

      :type: character
      :default: None

      The name of the x dimension for the river routing input grid (it may, but does not have to, be the same as :nml:mem:`JULES_INPUT_GRID::x_dim_name`). The coordinate system used to define the river input grid must be the same as that used for the main model grid - see :nml:mem:`JULES_LATLON::l_coord_latlon`.

      .. note:: For ASCII files, this can be anything. For NetCDF files, it should be the name of the dimension in :nml:mem:`file` (if that does not include :doc:`variable-name templating </input/file-name-templating>`) or in :nml:mem:`coordinate_file` (if :nml:mem:`file` includes templating).
      .. note:: Values for the coordinates along the x dimension of the river routing input grid will be read from the input file to define the river grid, and it is assumed that the file contains a variable with the same name as the dimension (x_dim_name).


   .. nml:member:: y_dim_name

      :type: character
      :default: None

      The name of the y dimension for the river routing input grid (it may, but does not have to, be the same as :nml:mem:`JULES_INPUT_GRID::y_dim_name`). The coordinate system used to define the river input grid must be the same as that used for the main model grid - see :nml:mem:`JULES_LATLON::l_coord_latlon`.

      .. note:: For ASCII files, this can be anything. For NetCDF files, it should be the name of the dimension in :nml:mem:`file` (if that does not include :doc:`variable-name templating </input/file-name-templating>`) or in :nml:mem:`coordinate_file` (if :nml:mem:`file` includes templating).
      .. note:: Values for the coordinates along the y dimension of the river routing input grid will be read from the input file to define the river grid, and it is assumed that the file contains a variable with the same name as the dimension (y_dim_name).

   .. nml:member:: nx_rivers

      :type: integer
      :permitted: >= 2
      :default: None

      The size of the x dimension of the river routing input grid.

   .. nml:member:: ny_rivers

      :type: integer
      :permitted: >= 2
      :default: None

      The size of the y dimension of the river routing input grid.


.. nml:member:: l_find_grid

   :type: logical
   :default: none

   Switch controlling how characteristics of the land grid and the river domain are determined.

   FALSE
      Use namelist values for the variables :nml:mem:`nx_land_grid`, :nml:mem:`ny_land_grid`, :nml:mem:`x1_land_grid` and :nml:mem:`y1_land_grid` to describe the land grid. This value is required so as to recreate some historical results but necessarily requires that the input values are correct and, for some configurations, has deficencies such as producing a river domain that is larger than required.

   TRUE
      Calculate details of the land grid from the known coordinates of land points. This also triggers differences in how the river domain is set up, including better treatment of cases in which the resolutions of the land and river grids differ and/or land points (e.g. from a regional domain) straddle the longitudinal edges of a global river input grid (a smaller river domain can be identified).


.. nml:group:: Members used to describe the land grid

   .. nml:member:: land_dx

      :type: real
      :default: None
      :permitted: > 0

      The gridbox size in the x direction of the 2D land grid. The units of this are the same as for the model grid - see :nml:mem:`JULES_LATLON::l_coord_latlon`.

   .. nml:member:: land_dy

      :type: real
      :default: None
      :permitted: > 0

      The gridbox size in the y direction of the 2D land grid. The units of this are the same as for the model grid - see :nml:mem:`JULES_LATLON::l_coord_latlon`.

   .. nml:group:: Only used with l_find_grid = FALSE

      .. nml:member:: nx_land_grid

         :type: integer
         :permitted: >= 1
         :default: none

         The size of the x dimension of the 2D land grid. This should be large enough to include all land points that are being modelled.

      .. nml:member:: ny_land_grid

         :type: integer
         :permitted: >= 1
         :default: none

      .. nml:member:: x1_land_grid

         :type: real
         :default: none

         The x coordinate of the "western-most" (i.e. first) column of gridpoints in the land grid. The units of this are the same as for the model grid - see :nml:mem:`JULES_LATLON::l_coord_latlon`.

      .. nml:member:: y1_land_grid

         :type: real
         :default: none

         The y coordinate of the "southern-most" (i.e. first) row of gridpoints in the land grid. The units of this are the same as for the model grid - see :nml:mem:`JULES_LATLON::l_coord_latlon`.

   .. note:: With :nml:mem:`l_find_grid` = F, although :nml:mem:`nx_land_grid`, :nml:mem:`ny_land_grid`, :nml:mem:`land_dx`, :nml:mem:`land_dy`, :nml:mem:`x1_land_grid` and :nml:mem:`y1_land_grid` describe the land grid, they are also used to calculate the area that will be searched for river points (the river domain). The area to be searched is the rectangle defined by x=x1_land_grid to x1_land_grid+(nx_land_grid*land_dx) and y=y1_land_grid to y1_land_grid+(ny_land_grid*land_dy). With :nml:mem:`l_find_grid` = T the model internally seeks to define a river domain that includes all land gridboxes.


.. nml:member:: rivers_regrid

   :type: logical
   :default: F

   Flag indicating if variables on the land grid need to be regridded (interpolated) to the river routing grid. This is currently only possible for grids that are regular in latitude and longituide. We distinguish between regridding (which is used between land and river grids of different resolution, or the same resolution but staggered relative to one another) and remapping (between consistent grids of the same resolution).

Grids are considered consistent (and therefore regridding is not required) if they are of the same resolution and points on one coincide with points on the other. We do not require that all locations have to be in both grids (though that is desirable), nor do the points need to be presented in the same order in both grids.

   TRUE
      River routing and land grids differ and regridding is required.

   FALSE
      River routing and land grids are consistent and regridding is not required.

.. note::
   In principle consistent grids with the same resolution can be handled via regridding, but the recommended approach in that case is to use the simpler remapping.

.. warning::
   Currently, regridding between land and river routing grids must only be used with regular lat/lon grids.

   If a 1D model input grid is specified in :nml:lst:`JULES_INPUT_GRID`, it must be possible to define a 2D regular lat/lon grid containing all the points in the model input grid.

   An example with the GSWP2 (land points only) forcing data is given below.


.. nml:member:: rivers_length

   :type: real
   :default: None

   The constant size of the rivers grid (m). This value is used in several ways, as explained below.

   If the coordinate system used is not latitude and longitude (:nml:mem:`JULES_LATLON::l_coord_latlon` = F) river_length must be provided and its value must be >0. This is used to calculate gridbox areas, assuming square gridboxes.

   If the coordinate system used is latitude and longitude, and a run is using RFM (:nml:mem:`JULES_RIVERS::i_river_vn` = 2) and/or overbank inundation without hypsometry (:nml:mem:`JULES_OVERBANK::l_riv_overbank` = T and :nml:mem:`JULES_OVERBANK::overbank_model` = 1 or 2), rivers_length is again required, but in this case a value <= 0 can be used to trigger calculation of a value based on the latitudinal size of gridboxes (this is so as to mimic the behaviour of older versions of the code). In these cases rivers_length is used as a length scale (the distance between points) for RFM and as a length scale (relative to a gridbox) for overbank inundation.


.. nml:group:: Members only used with RFM (:nml:mem:`JULES_RIVERS::i_river_vn` = 2).

   .. nml:member:: l_use_area

   :type: logical
   :default: F

   Switch to control whether a drainage area ancillary field is used to distinguish between land and river points (for the purpose of setting routing parameter values).

   TRUE
     An ancillary field will be used to define the area draining to each point. See "area" in :ref:`list-of-rivers-params`.

   FALSE
     No ancillary field will be used and all points will be given river parameter values.


.. nml:group:: Members used to determine how river routing variables are set

   .. nml:member:: file

      :type: character
      :default: None

      The file to read river routing properties from.

      If :nml:mem:`use_file` is FALSE for every variable, this will not be used.

      This file name can use :doc:`variable name templating </input/file-name-templating>`.


   .. nml:member:: nvars

      :type: integer
      :permitted: >= 0
      :default: 0

      The number of river routing property variables that will be provided (see :ref:`list-of-rivers-params`).


   .. nml:member:: var

      :type: character(nvars)
      :default: None

      List of river routing variable names as recognised by JULES (see :ref:`list-of-rivers-params`). Names are case sensitive.

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

      For each JULES variable specified in :nml:mem:`var` where :nml:mem:`use_file` = FALSE, this is a constant value that the variable will be set to at every point.

      This is not used for variables where :nml:mem:`use_file` = TRUE, but a placeholder must still be given in that case.


.. nml:group:: Additional ancillaries, which may be required depending on requested options
 	
   .. nml:member:: riv_number_file
	
      :type: character
      :default: ''
	
      Ancillary file containing river numbers, which assign each river mouth on the Rivers grid, to the river which discharges into it. The river number is used in the calculation of 'outflow_per_river' (River outflow into the ocean for each river; kg s\ :sup:`-1`), when it is requested either as a JULES output (:nml:mem:`JULES_OUTPUT_PROFILE::var`) or as a send field when coupled to OASIS (:nml:mem:`OASIS_RIVERS::send_fields`). The river outflow for each river is calculated as the sum of the river outflows corresponding to that river. When passed to the ocean model via OASIS the river outflow is distributed over the corresponding river outflow points on the ocean grid. This is to ensure that water is conserved and rivers discharge into the correct ocean grid points.


.. _list-of-rivers-params:

List of rivers properties
~~~~~~~~~~~~~~~~~~~~~~~~~

The following table summarises river routing properties required to run RFM or TRIP river routing algorithms, specified from an ancillary file if :nml:mem:`JULES_RIVERS_PROPS::use_file` = TRUE.

.. tabularcolumns:: |p{2.5cm}|L|

+----------------------------+-----------------------------------------------------------------------------------------------------------+
| Name                       | Description                                                                                               |
+============================+===========================================================================================================+
| ``area``                   | Drainage area (in number of grid boxes) draining into a given grid box.                                   |
|                            |                                                                                                           |
|                            | This is used with RFM (:nml:mem:`JULES_RIVERS::i_river_vn` = ``2``) to distinguish between river and land |
|                            | points using the :nml:mem:`JULES_RIVERS::a_thresh` parameter. Points with drainage area >                 |
|                            | :nml:mem:`JULES_RIVERS::a_thresh` are treated as rivers, all others as land. These two classes of points  |
|                            | use different wave speeds (e.g. :nml:mem:`JULES_RIVERS::cland` and :nml:mem:`JULES_RIVERS::criver`).      |
|                            | Note that these "river" and "land" classes together comprise the total number of river routing points.    |
|                            |                                                                                                           |
|                            | If this field is not available, all points are treated as rivers.                                         |
|                            |                                                                                                           |
|                            | The drainage area does not include the grid point itself, and so an extra point must be added where       |
|                            | catchment area calculations are required.                                                                 |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``direction``              | Flow direction for each river routing grid box, defining the next grid box into which surface or          |
|                            | sub-surface water will be routed.                                                                         |
|                            |                                                                                                           |
|                            | This is specified as an integer according to ``[1 = N, 2 = NE, 3 = E, 4 = SE, 5 = S, 6 = SW, 7 = W,       |
|                            | 8 = NW]``.                                                                                                |
|                            |                                                                                                           |
|                            | Although these are referred to via compass directions, they are used as "grid-relative" directions.       |
|                            | e.g. "N" means "same column, one row up", "E" means "one column over, same row".                          |
|                            | Thus for a rotated grid (columns do not run S-N on the Earth), the point "same column, one row up" does   |
|                            | does not lie immediately N.                                                                               |
|                            |                                                                                                           |
|                            | Additionally,                                                                                             |
|                            |                                                                                                           |
|                            | 9: river mouth (outflow to sea)                                                                           |
|                            |                                                                                                           |
|                            | 10: inland drainage point (an endorheic catchment; no outflow from grid box)                              |
|                            |                                                                                                           |
|                            | All other values (<1 or >10) are excluded from the river calculations (effectively treated as sea).       |
|                            |                                                                                                           |
|                            | Note that at present any river flow at an inland drainage point is NOT added to the soil moisture (in     |
|                            | standalone JULES).                                                                                        |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``sequence``               | River routing network pathway number.                                                                     |
|                            |                                                                                                           |
|                            | Used by TRIP river routing only (i.e. :nml:mem:`JULES_RIVERS::i_river_vn` = ``1,3``).                     |
|                            | See Oki et al. (1999) for details.                                                                        |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``latitude_2d``            | The latitude of each river grid point must be specified. This field is required only if the model         |
|                            | coordinates are latitude and longitude, i.e. if :nml:mem:`JULES_LATLON::l_coord_latlon` = FALSE.          |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``longitude_2d``           | The longitude of each river grid point must be specified. This field is required only if the model        |
|                            | coordinates are latitude and longitude, i.e. if :nml:mem:`JULES_LATLON::l_coord_latlon` = FALSE.          |
+----------------------------+-----------------------------------------------------------------------------------------------------------+



Example of how to set up the river grid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following gives an example of how you would set up the namelists to use routing with the GSWP2 forcing data.

The model input grid is the GSWP2 grid, i.e. a land-points-only, 1D grid where points lie on a 1\ |deg| x 1\ |deg| grid. The river routing input grid is a 2D 1\ |deg| x 1\ |deg| grid.

Since both grids are 1\ |deg| x 1\ |deg|, we define the 2D regular lat-lon grid containing the land points to be the river routing input grid, which means we don't need any regridding of variables. ::

    &JULES_INPUT_GRID
      grid_is_1d    = T,
      npoints       = 15238,
      grid_dim_name = "land"
      # ...
    /

    &JULES_LATLON
      l_coord_latlon = T,
    /

    &JULES_RIVERS_PROPS
      # Define the river routing input grid
      x_dim_name = "longitude",
      nx_rivers  = 360,
      y_dim_name = "latitude",
      ny_rivers  = 180,

      # Define the 2D regular lat-lon grid containing the model input grid to be a 2D 1\ |deg| x 1\ |deg| grid
      nx_land_grid = 360,
      ny_land_grid = 180,
      x1_land_grid = -179.5,
      y1_land_grid = -89.5,
      land_dx      = 1.0,
      land_dy      = 1.0,

      # No regridding required since the river routing input grid and the land grid are consistent grids with the same resolution
      rivers_regrid = F
    /


.. |deg| unicode:: U+00B0



.. seealso::
      References:

      * Bell, V.A. et al. (2007) Development of a high resolution grid-based river flow model for use with regional climate model output. Hydrology and Earth System Sciences. 11 532-549
      * Oki, T., et al (1999) Assessment of annual runoff from land surface models using Total Runoff Integrating Pathways (TRIP). Journal of the Meteorological Society of Japan. 77 235-255

``JULES_OVERBANK_PROPS`` namelist members
-----------------------------------------

.. nml:namelist:: JULES_OVERBANK_PROPS

This namelist specifies how the river overbank inundation properties should be set.

.. note:: ``read_from_dump`` is not currently implemented for this namelist.

.. note::
   The grid here MUST coincide exactly with the river routing input grid specified in :nml:lst:`JULES_RIVERS_PROPS`.

.. nml:group:: Members used to determine how overbank inundation variables are set

   .. nml:member:: file

      :type: character
      :default: None

      The file to read overbank inundation properties from (can be the same file as specified in :nml:lst:`JULES_RIVERS_PROPS`).

      If :nml:mem:`use_file` is FALSE for every variable, this will not be used.

      This file name can use :doc:`variable name templating </input/file-name-templating>`.

   .. nml:member:: nvars

      :type: integer
      :permitted: >= 0
      :default: 0

      The number of overbank inundation property variables that will be provided (see :ref:`list-of-overbank-params`).


   .. nml:member:: var

      :type: character(nvars)
      :default: None

      List of overbank inundation variable names as recognised by JULES (see :ref:`list-of-overbank-params`). Names are case sensitive.

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

      For each JULES variable specified in :nml:mem:`var` where :nml:mem:`use_file` = FALSE, this is a constant value that the variable will be set to at every point.

      This is not used for variables where :nml:mem:`use_file` = TRUE, but a placeholder must still be given in that case.

.. _list-of-overbank-params:

List of overbank inundation properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following table summarises overbank inundation grid properties, specified from an ancillary file if :nml:mem:`JULES_OVERBANK_PROPS::use_file` = TRUE.

.. tabularcolumns:: |p{2.5cm}|L|

+----------------------------+-----------------------------------------------------------------------------------------------------------+
| Name                       | Description                                                                                               |
+============================+===========================================================================================================+
| ``logn_mean``              | Mean of ln(elevation-elev_min) for each grid cell (in units ln(m))                                        |
|                            |                                                                                                           |
|                            | This is only used if :nml:mem:`JULES_OVERBANK::overbank_model` = 3.                                       |
|                            |                                                                                                           |
|                            | Note that elev_min is DEM minimum, not river/lake bed level (therefore large values close to water        |
|                            | bodies can occur in floodplain gridcells).                                                                |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``logn_stdev``             | Standard deviation of ln(elevation-elev_min) for each grid cell (in units ln(m))                          |
|                            |                                                                                                           |
|                            | This is only used if :nml:mem:`JULES_OVERBANK::overbank_model` = 3.                                       |
|                            |                                                                                                           |
+----------------------------+-----------------------------------------------------------------------------------------------------------+

.. seealso::
      References:

      * Appx B of Lewis HW, Castillo Sanchez JM, Graham J, Saulter A, Bornemann J, Arnold A, Fallmann J, Harris C, Pearson D, Ramsdale S, Martínez de la Torre A, Bricheno L, Blyth E, Bell VA, Davies H, Marthews TR, O'Neill C, Rumbold H, O'Dea E, Brereton A, Guihou K, Hines A, Butenschon M, Dadson SJ, Palmer T, Holt J, Reynard N, Best M, Edwards J & Siddorn J (2018). The UKC2 regional coupled environmental prediction system. Geoscientific Model Development 11:1-42.



``JULES_WATER_RESOURCES_PROPS`` namelist members
------------------------------------------------

.. nml:namelist:: JULES_WATER_RESOURCES_PROPS

This namelist specifies how the water resource ancillary properties should be set.

.. nml:group:: Members used to determine how water resource variables are set


   .. nml:member:: read_from_dump

      :type: logical
      :default: F

      TRUE
         Populate variables associated with this namelist from the dump file. All other namelist members are ignored.

      FALSE
         Use the other namelist members to determine how to populate variables.

   .. nml:member:: file

      :type: character
      :default: None

      The file to read water resource ancillary properties from.

      If :nml:mem:`use_file` is FALSE for every variable, this will not be used.

      This file name can use :doc:`variable name templating </input/file-name-templating>`.

   .. nml:member:: nvars

      :type: integer
      :permitted: >= 0
      :default: 0

      The number of water resource property variables that will be provided (see :ref:`list-of-water-resources-params`).


   .. nml:member:: var

      :type: character(nvars)
      :default: None

      List of water resource variable names as recognised by JULES (see :ref:`list-of-water-resources-params`). Names are case sensitive.

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

      For each JULES variable specified in :nml:mem:`var` where :nml:mem:`use_file` = FALSE, this is a constant value that the variable will be set to at every point.

      This is not used for variables where :nml:mem:`use_file` = TRUE, but a placeholder must still be given in that case.

.. _list-of-water-resources-params:

List of water resources properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following table summarises ancillary fields for the water resources code, specified from an ancillary file if :nml:mem:`JULES_WATER_RESOURCES_PROPS::use_file` = TRUE.

.. tabularcolumns:: |p{3cm}|L|

+----------------------------+-----------------------------------------------------------------------------------------------------------+
| Name                       | Description                                                                                               |
+============================+===========================================================================================================+
| ``conveyance_loss``        | Fraction of water that is lost during conveyance from source to user.                                     |
|                            |                                                                                                           |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``irrig_eff``              | Irrigation efficiency.                                                                                    |
|                            | This is only used if :nml:mem:`JULES_WATER_RESOURCES::l_water_irrigation` = TRUE.                         |
|                            |                                                                                                           |
+----------------------------+-----------------------------------------------------------------------------------------------------------+
| ``sfc_water_frac``         | Target for the fraction of demand that will be met from surface water (rather than groundwater).          |
|                            |                                                                                                           |
+----------------------------+-----------------------------------------------------------------------------------------------------------+



``URBAN_PROPERTIES`` namelist members
-------------------------------------

.. nml:namelist:: URBAN_PROPERTIES


.. nml:member:: file

   :type: character
   :default: None

   The file to read urban properties from.

   If :nml:mem:`use_file` (see below) is FALSE for every variable, this will not be used.

   This file name can use :doc:`variable name templating </input/file-name-templating>`.


.. nml:member:: nvars

   :type: integer
   :permitted: >= 0
   :default: 0

   The number of urban property variables that will be provided.

   The required variables depend on whether MORUSES is used or not:

   * If MORUSES is on, all variables must be given. However, depending on the configuration of MORUSES, not all given variables will be used. Those that will not be used could be set to constant values to avoid setting them from file.
   * If MORUSES is *not* on, only ``wrr`` is required.


.. nml:member:: var

   :type: character(nvars)
   :default: None

   List of urban property variable names as recognised by JULES (see :ref:`list-of-urban-properties`). Names are case sensitive.

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


.. _list-of-urban-properties:

List of urban properties
~~~~~~~~~~~~~~~~~~~~~~~~

All of the urban property variables listed below are expected to have no levels dimensions and no time dimension.

+---------------+----------------------------------+-------------------------------------------------------------------------------------+
| Variable name | Description [#]_                 | Notes                                                                               |
+===============+==================================+=====================================================================================+
| ``wrr``       | Repeating width ratio (or canyon | If :nml:mem:`JULES_URBAN::l_urban_empirical` = TRUE                                 |
|               | fraction, W/R)                   | then this is updated with calculated values.                                        |
+---------------+----------------------------------+-------------------------------------------------------------------------------------+
| **The following apply to MORUSES only**                                                                                                |
+---------------+----------------------------------+-------------------------------------------------------------------------------------+
| ``hwr``       | Height-to-width ratio (H/W)      | See for ``wrr`` above.                                                              |
+---------------+----------------------------------+-------------------------------------------------------------------------------------+
| ``hgt``       | Building height (H)              | See for ``wrr`` above.                                                              |
+---------------+----------------------------------+-------------------------------------------------------------------------------------+
| ``ztm``       | Effective roughness length of    | If :nml:mem:`JULES_URBAN::l_moruses_macdonald` = TRUE                               |
|               | urban areas                      | then this is updated with calculated values.                                        |
+---------------+----------------------------------+-------------------------------------------------------------------------------------+
| ``disp``      | Displacement height              | See for ``ztm`` above.                                                              |
+---------------+----------------------------------+-------------------------------------------------------------------------------------+
| ``albwl``     | Wall albedo                      | Data only used if :nml:mem:`JULES_URBAN::l_moruses_albedo` = TRUE.                  |
+---------------+----------------------------------+-------------------------------------------------------------------------------------+
| ``albrd``     | Road albedo                      | See for ``albwl`` above.                                                            |
+---------------+----------------------------------+-------------------------------------------------------------------------------------+
| ``emisw``     | Wall emissivity                  | Data only used if :nml:mem:`JULES_URBAN::l_moruses_emissivity` = TRUE.              |
+---------------+----------------------------------+-------------------------------------------------------------------------------------+
| ``emisr``     | Road emissivity                  | See for ``emisw`` above.                                                            |
+---------------+----------------------------------+-------------------------------------------------------------------------------------+



.. rubric:: Footnotes

.. [#]  For more information on the urban geometry used please see the JULES technical documentation.



``JULES_CO2`` namelist members
------------------------------

.. nml:namelist:: JULES_CO2

.. nml:member:: read_from_dump

   :type: logical
   :default: F

   TRUE
      Populate variables associated with this namelist from the dump file. All other namelist members are ignored.

   FALSE
      Use the other namelist members to determine how to populate variables.


.. nml:member:: co2_mmr

   :type: real
   :default: 5.241e-4

   Concentration of atmospheric CO2, expressed as a mass mixing ratio.


``JULES_FLAKE`` namelist members
--------------------------------

.. nml:namelist:: JULES_FLAKE

.. nml:member:: read_from_dump

   :type: logical
   :default: F

   TRUE
      Populate variables associated with this namelist from the dump file. All other namelist members are ignored.

   FALSE
      Use the other namelist members to determine how to populate variables.

.. nml:member:: file

   :type: character
   :default: None

   The file to read the FLake parameters from.

.. nml:member:: nvars

   :type: integer
   :permitted: >= 0
   :default: 0

   The number of FLake variables that will be provided.
   (At the moment lake depth is the only variable that needs to be provided).

.. nml:member:: var

   :type: character(nvars)
   :default: None

   List of FLake parameter variable names as recognised by JULES (see :ref:`list-of-FLake-params`). Names are case sensitive.

   .. note:: For ASCII files, variable names must be in the order they appear in the file.

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

.. nml:member:: use_file

   :type: logical(nvars)
   :default: T

   For each JULES variable specified in :nml:mem:`var`, this indicates if it should be read from the specified file or whether a constant value is to be used.

   TRUE
       The variable will be read from the file.

   FALSE
       The variable will be set to a constant value everywhere using :nml:mem:`const_val` below.

.. nml:member:: const_val

   :type: real(nvars)
   :default: 5.0m

   For each JULES variable specified in :nml:mem:`var` where :nml:mem:`use_file` = FALSE, this is a constant value that the variable will be set to for every point or gridbox.

   This is not used for variables where :nml:mem:`use_file` = TRUE, but a placeholder must still be given.


.. _list-of-FLake-params:

List of FLake parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabularcolumns:: |p{2.5cm}|L|

+----------------+---------------------------------------------------------------------------------------+
| Name           | Description                                                                           |
+================+=======================================================================================+
| ``lake_depth`` | For each gridbox, the depth of the lakes should be provided in meters.                |
|                |                                                                                       |
|                | Note that for deep lakes FLake will assume an artificial lake bottom at 50m depth.    |
+----------------+---------------------------------------------------------------------------------------+


.. _References_ancillaries:

References for ancillaries
--------------------------

* Kattge, J. and Knorr, W., 2007,
  Temperature acclimation in a biochemical model of photosynthesis:
  a reanalysis of data from 36 species,
  Plant, Cell and Environment, 30: 1176--1190,
  https://doi.org/10.1111/j.1365-3040.2007.01690.x.
