``urban.nml``
=============


This file contains three namelists called :nml:lst:`URBAN_SWITCHES`, :nml:lst:`URBAN2T_PARAM` and :nml:lst:`URBAN_PROPERTIES`.

This section reads in model configuration choices, geometry & material characteristics data for the urban schemes URBAN-2T and MORUSES. Both these schemes must have an :nml:mem:`JULES_MODEL_LEVELS::urban_roof` tile and an :nml:mem:`JULES_MODEL_LEVELS::urban_canyon` tile. Values from this section are only used if either of the two-tile urban schemes are enabled by specifying an :nml:mem:`JULES_MODEL_LEVELS::urban_roof` tile.

For parameters that MORUSES does not parameterise, and for any MORUSES parametrisations that are turned off, values from :doc:`nveg_params.nml` will be used. See the switches below for more information.

Further information on MORUSES, including references, can be found in the technical documentation and under :nml:mem:`URBAN_SWITCHES::l_moruses`.



``URBAN_SWITCHES`` namelist members
-----------------------------------

.. nml:namelist:: URBAN_SWITCHES


.. nml:member:: l_moruses

   :type: logical
   :default: F

   .. note:: Not used unless an :nml:mem:`JULES_MODEL_LEVELS::urban_roof` tile is present.

   Switch for turning on MORUSES.

   TRUE
       Use MORUSES parameterisations.

   FALSE
       Do not use MORUSES parameterisations. Use urban tile parameters, set in :doc:`nveg_params.nml`, instead.

   .. seealso::
      References:
   
      *   Porson, A., et al. (2010), Implementation of a new urban energy budget scheme in the MetUM. Part I: Description and idealized simulations, Quarterly Journal of the Royal Meteorological Society, 136: 1514-1529. doi: 10.1002/qj.668
      *   Porson, A., et al. (2010), Implementation of a new urban energy budget scheme into MetUM. Part II: Validation against observations and model Intercomparison, Quarterly Journal of the Royal Meteorological Society, 136: 1530-1542. doi: 10.1002/qj.572


.. nml:member:: l_urban_empirical

   :type: logical
   :default: T

   Switch to use empirical relationships for urban geometry, based on total urban fraction. Dimensions calculated are W/R, H/W & H.

   URBAN-2T uses W/R only.

   Used in calculation of the canyon and roof fractions and also to distribute anthropogenic heat between roof and canyon if :nml:mem:`JULES_SWITCHES::l_anthrop_heat_src` = TRUE.

   TRUE
       Use empirical relationships for urban geometry.

   FALSE
       Appropriate data needs to be supplied instead.

   .. warning:: These are only valid for high resolutions (~1 km).

   .. seealso::
      References:
   
      *   Bohnenstengel SI, Evans S, Clark P, Belcher SE (2010). Simulations of the London urban heat island, Quarterly Journal of the Royal Meteorological Society (submitted)


.. nml:member:: l_moruses_macdonald

   :type: logical
   :default: T

   MORUSES switch for using MacDonald et al. (1998) to calculate effective roughness length of urban areas and displacement height from urban geometry.

   TRUE
       Use MacDonald et al. (1998) formulations.

   FALSE
       Appropriate data needs to be supplied instead.

   .. note:: If :nml:mem:`l_urban_empirical` = TRUE then :nml:mem:`l_moruses_macdonald` = TRUE, which the code enforces.

   .. seealso::
      References:
   
      *   Macdonald RW, Griffiths RF, Hall D. 1998. An improved method for the estimation of surface roughness of obstacle arrays. Atmos. Env. 32: 1857-1864


.. nml:member:: l_moruses_albedo

   :type: logical
   :default: T

   MORUSES switch for effective canyon albedo parameterisation.

   TRUE
       Use MORUSES parameterisation. Requires that :nml:mem:`JULES_SWITCHES::l_cosz` = TRUE, which the code automatically enables.

   FALSE
       The canyon albedo is taken from :nml:mem:`JULES_NVEGPARM::albsnf_nvg_io` and :nml:mem:`JULES_NVEGPARM::albsnc_nvg_io`.

   In all cases, the roof albedo is taken from :nml:mem:`JULES_NVEGPARM::albsnf_nvg_io` and :nml:mem:`JULES_NVEGPARM::albsnc_nvg_io`.


.. nml:member:: l_moruses_emissivity

   :type: logical
   :default: F

   MORUSES switch for effective canyon emissivity parameterisation.

   TRUE
       Use MORUSES parameterisation.

   FALSE
       The canyon emmissivity is taken from :nml:mem:`JULES_NVEGPARM::emis_nvg_io`.

   In all cases, the roof emissivity is taken from :nml:mem:`JULES_NVEGPARM::emis_nvg_io`.


.. nml:member:: l_moruses_rough

   :type: logical
   :default: T

   MORUSES switch for effective roughness length for heat parameterisation.

   TRUE
       Use MORUSES parameterisation for canyon and roof.

   FALSE
       Values for canyon and roof are taken from :nml:mem:`JULES_NVEGPARM::z0_nvg_io` and :nml:mem:`JULES_NVEGPARM::z0hm_nvg_io`.


.. nml:member:: l_moruses_storage

   :type: logical
   :default: T

   MORUSES switch for thermal inertia and coupling with underlying soil parameterisation.

   TRUE
       Use MORUSES parameterisation.

   FALSE
       Values are taken from :nml:mem:`JULES_NVEGPARM::ch_nvg_io` and :nml:mem:`JULES_NVEGPARM::vf_nvg_io`.


.. nml:member:: l_moruses_storage_thin

   :type: logical
   :default: T

   MORUSES switch to use a thin roof to simulate the effects of insulation.

   Only used if :nml:mem:`l_moruses_storage` = TRUE.

   TRUE
       Use thin, insulated roof.

   FALSE
       Use damping depth diffusivity of roofing materials.




``URBAN2T_PARAM`` namelist members
----------------------------------

.. nml:namelist:: URBAN2T_PARAM


.. nml:member:: anthrop_heat_scale

   :type: real
   :default: 1.0

   Distribution scaling factor, which allows the anthropogenic heat flux to be spread between the :nml:mem:`JULES_MODEL_LEVELS::urban_canyon` and :nml:mem:`JULES_MODEL_LEVELS::urban_roof` tiles such that:

   *   ``H_roof = anthrop_heat_scale x H_canyon``
   *   ``H_canyon x (W/R) + H_roof x ( 1.0 - W/R ) = anthrop_heat``

   Has a value between 0.0 and 1.0 where the extremes correspond to:

   *   0.0 = all released within the canyon.
   *   1.0 = evenly spread between canyon and roof.

   Only used if :nml:mem:`JULES_SWITCHES::l_anthrop_heat_src` = TRUE.




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


.. _list-of-urban-properties:

List of urban properties
~~~~~~~~~~~~~~~~~~~~~~~~

All of the urban property variables listed below are expected to have no levels dimensions and no time dimension.

+---------------+----------------------------------+-------------------------------------------------------------------------------------+
| Variable name | Decription [*]_                  | Notes                                                                               |
+===============+==================================+=====================================================================================+
| ``wrr``       | Repeating width ratio (or canyon | If :nml:mem:`URBAN_SWITCHES::l_urban_empirical` = TRUE then this is updated with    |
|               | fraction, W/R)                   | calculated values.                                                                  |
+---------------+----------------------------------+-------------------------------------------------------------------------------------+
| **The following apply to MORUSES only**                                                                                                |
+---------------+----------------------------------+-------------------------------------------------------------------------------------+
| ``hwr``       | Height-to-width ratio (H/W)      | See for ``wrr`` above.                                                              |
+---------------+----------------------------------+-------------------------------------------------------------------------------------+
| ``hgt``       | Building height (H)              | See for ``wrr`` above.                                                              |
+---------------+----------------------------------+-------------------------------------------------------------------------------------+
| ``ztm``       | Effective roughness length of    | If :nml:mem:`URBAN_SWITCHES::l_moruses_macdonald` = TRUE (or                        |
|               | urban areas                      | :nml:mem:`URBAN_SWITCHES::l_urban_empirical` = TRUE), then this is updated with     |
|               |                                  | calculated values.                                                                  |
|               |                                  |                                                                                     |
|               |                                  |                                                                                     |
|               |                                  |                                                                                     |
|               |                                  |                                                                                     |
|               |                                  |                                                                                     |
|               |                                  |                                                                                     |
|               |                                  |                                                                                     |
|               |                                  |                                                                                     |
|               |                                  |                                                                                     |
+---------------+----------------------------------+-------------------------------------------------------------------------------------+
| ``disp``      | Displacement height              | See for ``ztm`` above.                                                              |
+---------------+----------------------------------+-------------------------------------------------------------------------------------+
| ``albwl``     | Wall albedo                      | Data only used if :nml:mem:`URBAN_SWITCHES::l_moruses_albedo` = TRUE.               |
+---------------+----------------------------------+-------------------------------------------------------------------------------------+
| ``albrd``     | Road albedo                      | See for ``albwl`` above.                                                            |
+---------------+----------------------------------+-------------------------------------------------------------------------------------+
| ``emisw``     | Wall emissivity                  | Data only used if :nml:mem:`URBAN_SWITCHES::l_moruses_emissivity` = TRUE.           |
+---------------+----------------------------------+-------------------------------------------------------------------------------------+
| ``emisr``     | Road emissivity                  | See for ``emisw`` above.                                                            |
+---------------+----------------------------------+-------------------------------------------------------------------------------------+



.. rubric:: Footnotes

.. [*]  For more information on the urban geometry used please see the JULES technical documentation.