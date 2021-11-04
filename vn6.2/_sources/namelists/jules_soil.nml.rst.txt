``jules_soil.nml``
==================


This file sets the soil options and parameters. It contains one namelist called :nml:lst:`JULES_SOIL`.



``JULES_SOIL`` namelist members
-------------------------------

.. nml:namelist:: JULES_SOIL

.. nml:member:: sm_levels

   :type: integer
   :permitted: >= 1
   :default: 4

   Number of soil layers.

   A value of 4 is often used, with soil layer depths that have been tuned using this.
   
   .. warning::
      If :nml:mem:`JULES_SURFACE_TYPES::ncpft` > 0, ``sm_levels >= 3`` is required.

   
.. nml:member:: l_vg_soil

   :type: logical
   :default: F

   Switch for van Genuchten soil hydraulic model.

   TRUE
       Use van Genuchten model.

   FALSE
       Use Brooks and Corey model [#]_.

   .. seealso::
      References:
   
      * Brooks, R.H. and A.T. Corey, 1964, Hydraulic properties of porous media. Colorado State University Hydrology Papers 3.
      * van Genuchten, M.T., 1980, A Closed-form Equation for Predicting the Hydraulic Conductivity of Unsaturated Soils. Soil Science Society of America Journal, 44:892-898.


.. nml:member:: l_dpsids_dsdz

   :type: logical
   :default: F

   Switch to calculate vertical gradient of soil suction with the assumption of linearity only for fractional saturation (consistent with the calculation of hydraulic conductivity).
   
   
.. nml:member:: l_soil_sat_down

   :type: logical
   :default: F

   Switch for dealing with supersaturated soil layers. If a soil layer becomes supersaturated, the water in excess of saturation will be put into the layer below or above according to this switch.

   TRUE (Down)
       Any excess is put into the layer below. Any excess from the bottom
       layer becomes subsurface runoff.

   FALSE (Up)
       Any excess is put into the layer above. Any excess from the top layer becomes surface runoff. This option was used in JULES2.0.

.. nml:member:: l_holdwater

   :type: logical
   :default: F

   This switch fixes a problem in soil hydrology, whereby if a layer goes supersaturated during the implicit calulation, the excess water is pushed out of the soil column (``l_holdwater = FALSE``) instead of into an adjacent layer (``l_holdwater = TRUE``).

   TRUE
       Supersaturated soil moisture from implicit calculation goes into an adjacent layer
       (above or below depending on :nml:mem:`l_soil_sat_down`). This option was added in JULES 5.1.

   FALSE
       Supersaturated soil moisture from implicit calculation goes out of the base of the soil column.


.. nml:member:: soilhc_method

   :type: integer
   :permitted: 1, 2 or 3
   :default: 1

   Switch for soil thermal conductivity model.

   1. | Use approach of Cox et al (1999), as in JULES2.0.
      | This is likely to predict values of soil thermal conductivity that are too low (Dharssi et al, 2009).

   2. | Use approach of Dharssi et al (2009), which was adapted from Johansen (1975) and described by Peters-Lidard et al. (1998).
      | This is not recommended for organic soils.

   3. | Use approach of Chadburn et al (2015).
      | This is recommended when using organic soils, which can have a much lower saturated thermal conductivity than mineral soils.

   .. seealso::
      References:
   
      * Chadburn et al (2015). An improved representation of physical permafrost dynamics in a global land-surface scheme. Geoscientific Model Development
      * Dharssi et al (2009). New soil physical properties implemented in the Unified Model at PS18. Met Office Technical note 528
      * Johansen (1975). Thermal conductivity of soils. PhD thesis. University of Trondheim, Norway 
      * Peters-Lidard et al (1998). The effect of soil thermal conductivity parameterisation on surface energy fluxes and temperatures. J. Atmos. Sci. 55:1209-1224


.. nml:member:: l_bedrock

   :type: logical
   :default: F

   Switch for using a thermal bedrock column beneath the soil column. The bedrock has no hydrological processes - diffusion of heat is the only process represented.
   
   Properties of the bedrock can be set using :nml:mem:`ns_deep`, :nml:mem:`hcapdeep`, :nml:mem:`hcondeep` and :nml:mem:`dzdeep`.
   
   TRUE
       An additional bedrock column is used below the soil column.
       
   FALSE
       No effect.
   
   .. seealso::
      For full details see Chadburn et al. (2015)


.. nml:group:: Bedrock parameters (only used if :nml:mem:`l_bedrock` = TRUE)

   .. nml:member:: ns_deep

      :type: integer
      :permitted: >= 1
      :default: 100

      The number of levels in the thermal-only bedrock.


   .. nml:member:: hcapdeep

      :type: real
      :default: 2100000.0

      The heat capacity of the bedrock (J K\ :sup:`-1` m\ :sup:`-3` ).


   .. nml:member:: hcondeep

      :type: real
      :default: 8.6

      The heat conductivity of the bedrock (W m\ :sup:`-2` K\ :sup:`-1` ).


   .. nml:member:: dzdeep

      :type: real
      :default: 0.5

      The thickness of the bedrock layers (m).


.. nml:member:: cs_min

   :type: real
   :default: 1.0e-6

   Minimum allowed soil carbon (kg m\ :sup:`-2`).


.. nml:member:: zsmc

   :type: real
   :permitted: > 0
   :default: 1.0

   If a depth-averaged soil moisture diagnostic is requested, the average is calculated from the surface to this depth (m).


.. nml:member:: zst

   :type: real
   :permitted: > 0
   :default: 1.0

   The depth (0.0->zst) to which the soil temperature is averaged for use in the calculation of wetland methane emissions (m).


.. nml:member:: confrac

   :type: real
   :permitted: 0 <= confrac <= 1
   :default: 0.3

   The fraction of the gridbox assumed to be covered by convective precipitation.


.. nml:member:: dzsoil_io

   :type: real(sm_levels)
   :default: None

   The soil layer depths (m), starting with the uppermost layer.

   Note that the soil layer depths (and hence the total soil depth) are constant across the domain.

   It is recommended that JULES uses layer depths of 0.1, 0.25, 0.65 and 2.0m, giving a total depth of 3.0m, unless there is good reason not to.

.. nml:member:: dzsoil_elev

   :type: real
   :default: None

   Depth of the tiled solid-ice bedrock-type layer used underneath individual ice tiles if :nml:mem:`JULES_SURFACE::l_elev_land_ice` is TRUE. 
   Effectively this sets the amount of thermal buffering each surface tile has to heat fluxes penetrating through the snowpack.

.. nml:member:: l_tile_soil

   :type: logical
   :default: False

   Switch to set the number of soil tiles to equal the number of surface tiles. Each soil tile has independent properties.

   See also :nml:mem:`l_broadcast_ancils` and :nml:mem:`JULES_INITIAL::l_broadcast_soilt`.

   .. note::
      Setting :nml:mem:`l_tile_soil` = TRUE means a separate soil tile exists for each surface tile (rather than all surface tiles using the same, single soil tile). This also alters the names of many of the soil prognostic and ancillary variables that are used (see elsewhere), with the suffix "_soilt'' being added to indicate the presence of soil tiling. The switches :nml:mem:`l_broadcast_ancils` and :nml:mem:`JULES_INITIAL::l_broadcast_soilt` allow soil tiling to be used with input files that do not contain soil tile information. Setting :nml:mem:`l_broadcast_ancils` = TRUE means that a soil ancillary file that does not contain soil tiles can be used in a tiled run. Setting :nml:mem:`JULES_INITIAL::l_broadcast_soilt` = TRUE means an initital state file that does not contain soil tiles can be used to initialise a run with soil tiles.

.. nml:member:: l_broadcast_ancils

   :type: logical
   :default: False

   Switch to allow non-soil tiled ancillary files to be broadcast to all soil tiles. Only active when :nml:mem:`l_tile_soil` is True. When reading ancillaries from the dump file, use :nml:mem:`JULES_INITIAL::l_broadcast_soilt` instead.

.. rubric:: Footnotes

.. [#] In the JULES2.0 User Manual this was described as the 'Clapp and Hornberger' model and the JULES code still refers to 'Clapp and Hornberger' rather than 'Brooks and Corey'. In fact there are important differences between these two hydraulic models (Marthews et al. 2014,GMD). There has been confusion in the literature and in past documentation of MOSES/JULES, but JULES uses the Brooks and Corey model when :nml:mem:`JULES_SOIL::l_vg_soil` = FALSE .

      References:
      * Brooks RH & Corey AT (1964). Hydraulic properties of porous media. Colorado State University Hydrology Papers 3.
      * Clapp RB & Hornberger GM (1978). Empirical Equations for Some Soil Hydraulic Properties. Water Resources Research 14:601-604.
