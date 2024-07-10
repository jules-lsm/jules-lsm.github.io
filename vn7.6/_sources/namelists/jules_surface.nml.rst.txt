``jules_surface.nml``
=====================


This file sets the surface options. It contains one namelist called :nml:lst:`JULES_SURFACE`.



``JULES_SURFACE`` namelist members
----------------------------------

.. nml:namelist:: JULES_SURFACE

.. nml:member:: all_tiles

   :type: integer
   :permitted: 0,1
   :default: 0

   Perform calculations of tile properties on all tiles (except land ice) for all gridpoints even when the tile fraction is zero.

   0. Off
   1. On

.. nml:member:: cor_mo_iter

   :type: integer
   :permitted: 1-4
   :default: 1

   Corrections to Monin-Obukhov surface exchange calculation. Please see also `UMDP24 "The Parametrization of Boundary Layer Processes" (section 8.4.1) <https://code.metoffice.gov.uk/doc/um/latest/papers/umdp_024.pdf>`_.

   1. Correct convective gustiness in low winds
   2. Correct U* in dust scheme,
   3. Limit Obukhov length in low winds
   4. Improve the initialisation of the iteration

   .. note::
       Option 4 should be the preferred option.

.. nml:member:: beta_cnv_bl

   :type: real
   :permitted: >=0.0

   Dimensionless coefficient scaling the boundary layer convective
   gustiness contribution to surface exchange.  Historically this was
   set to 0.08 but is recommended to be reduced to 0.04 when gustiness
   from convective downdraughts is included, either from the
   convection parametrization or when convection is resolved (so
   resolutions ~1km or finer). Please see also `UMDP24 "The
   Parametrization of Boundary Layer Processes" (section 8.1)
   <https://code.metoffice.gov.uk/doc/um/latest/papers/umdp_024.pdf>`_.

.. nml:member:: l_aggregate

   :type: logical
   :default: F

   Switch controlling number of surface tiles for each gridbox.

   This is used to set the number of surface energy balances that are solved for each gridbox (``nsurft``).

   TRUE
       Aggregate parameter values are used to solve a single energy balance per gridbox. This option sets ``nsurft = 1``.

   FALSE
       A separate energy balance is calculated for each surface type. This option sets ``nsurft = ntype``.


.. nml:member:: i_aggregate_opt

   :type: integer
   :permitted: 0-1
   :default: 0

   Option for aggregating surface properties to surface tiles:

   0. Aggregate momentum roughness lengths and set the thermal roughness length as a given fraction of this (in practice the ratio of roughness lengths for the first surface type).
   1. Aggregate the thermal roughness lengths separately from the momentum roughness lengths using an analogous algorithm.

   .. note::
       This option is ignored unless :nml:mem:`l_aggregate` is true.


.. nml:member:: l_epot_corr

   :type: logical
   :default: F

   TRUE
       Use correction to the calculation of potential evaporation.

   FALSE
       No effect.


.. nml:member:: l_point_data

   :type: logical
   :default: F

   Flag indicating if driving data are point or area-average values. This affects the treatment of precipitation input and how snow affects the albedo.

   TRUE
       Driving data are point data. Precipitation is not distributed in space (see FALSE below) and is all assumed to be large-scale in origin. The albedo formulation is suitable for a point.

   FALSE
       Driving data are area averages. The precipitation inputs are assumed to be exponentially distributed in space, as in UMDP25, and can include convective and large-scale components. The albedo formulation is suitable for a gridbox.


.. nml:member:: l_land_ice_imp

   :type: logical
   :default: F

   Switch to control the use of implicit numerics to update land ice temperatures.

   TRUE
       Use implicit numerics to update land ice temperatures.

   FALSE
       Use explicit numerics to update land ice temperatures.


.. nml:member:: l_anthrop_heat_src

   :type: logical
   :default: F

   Switch for inclusion of anthropogenic contribution to the surface heat flux from *urban* surface types. If :nml:mem:`JULES_SURFACE::l_urban2t` then the anthropogenic heat will be distributed between the :nml:mem:`JULES_SURFACE_TYPES::urban_canyon` and :nml:mem:`JULES_SURFACE_TYPES::urban_roof` according to :nml:mem:`JULES_URBAN::anthrop_heat_scale`, otherwise it is added to :nml:mem:`JULES_SURFACE_TYPES::urban` only.

   TRUE
       Add anthropogenic effect.

   FALSE
       No effect.


.. nml:member:: iscrntdiag

   :type: integer
   :permitted: 0-3 (standalone: 0 or 1 only)
   :default: 0

   Switch controlling method for diagnosing screen temperature.

   0. Use surface similarity theory (no decoupling).
   1. Use surface similarity theory but allow decoupling in very
      stable conditions based on the quasi-equilibrium radiative
      solution.
   2. Diagnose the screen temperature including transient effects and
      radiative cooling.
   3. Diagnose the screen temperature and humidity including transient
      effects and radiative cooling. The diagnosis of the screen
      temperature follows option 2. This is an experimental option and
      is undergoing development and additional testing.

   .. note::
       Option 0 should be the preferred option in standalone i.e. no decoupling until the decoupled options are fully tested in standalone scenarios.


.. nml:member:: l_elev_lw_down

      :type: logical
      :default: false

      If surface tiles are set to be at an elevation offset from the gridbox mean altitude (see :nml:lst:`JULES_SURF_HGT`) this switch controls
      whether downwelling longwave radiation is adjusted along with surface air temperature and relative humidity.

      If true, the downwelling longwave for each surface tile not at the gridbox mean height is adjusted by an amount
      proportional to the fourth power of the adjustment that has been made to the surface air temperature. The adjustments are then
      scaled such that the sum over all surface tiles conserves the gridbox mean energy in the original forcing.


.. nml:member:: l_elev_land_ice

      :type: logical
      :default: false

      Allows multiple ice surface tiles to exist in an ice gridbox, usually with each representing a different elevation (:nml:lst:`JULES_SURF_HGT`)
      band on in icesheet areas so that a sub-gridscale surface mass balance term (a strong function of altitude) can be derived for forcing
      icesheet/glacier models.  When enabled, ice tiles in a gridbox do not use the usual (gridbox mean) JULES soil/ice subsurface model,
      but each tile has an independent single layer bedrock-type solid ice boundary condition under the snowpack.

      In addition, when selected, dense snowpacks on elevated ice gridboxes are parameterised to behave more like firn in two ways:
      1) The meltwater-holding capacity of snow layers reduces as a linear function of their density, becoming zero
      above the pore-closure density of 850 kg/m^2 so as to restrict retention of melt within the snowpack.
      2) Where the top few centimetres of the pack has a density appropriate to firn/bare ice
      and the grain-size physics otherwise used for snow albedo become less appropriate,
      surface albedo becomes a function of density, tending towards that of bare ice as density increases
      (see :nml:mem:`JULES_SNOW::rho_firn_albedo`, :nml:mem:`JULES_SNOW::amax`, :nml:mem:`JULES_SNOW::aicemax`).

      If this scheme is enabled, a depth for the bedrock layer must be provided (:nml:mem:`JULES_SOIL::dzsoil_elev`) and the new tile
      numbers must be specified (:nml:lst:`JULES_SURFACE_TYPES`) as either type :nml:mem:`JULES_SURFACE_TYPES::elev_ice` (for fully glaciated areas) or :nml:mem:`JULES_SURFACE_TYPES::elev_rock` (for
      non-glaciated areas where the bedrock may become exposed under a thin snow layer). The total number of non-vegetated surface tiles, and
      their surface properties (:nml:lst:`JULES_NVEGPARM`, usually set to be the same as the normal ice tile) must be set accordingly,
      as with any surface tile.

.. nml:member:: l_flake_model

      :type: logical
      :default: false

      Switch for using the freshwater lake model 'FLake' on the lake/inland-water surface tile. More information on the FLake model can be found on `the FLake website <http://www.flake.igb-berlin.de/>`_. A description of how FLake is coupled to JULES can be found in `Rooney and Jones 2010 <http://www.borenv.net/BER/pdfs/ber15/ber15-501.pdf>`_.

      When using FLake, it is not necessary to use a canopy representation of lake properties so :nml:mem:`JULES_NVEGPARM::catch_nvg_io`,
      :nml:mem:`JULES_NVEGPARM::ch_nvg_io` and :nml:mem:`JULES_NVEGPARM::vf_nvg_io` should all be set to zero for the lake tile.

.. nml:member:: l_urban2t

      :type: logical
      :default: false

      Switch for using the two-tile urban schemes (including MORUSES). This allows two urban surface tiles (:nml:mem:`JULES_SURFACE_TYPES::urban_canyon` and :nml:mem:`JULES_SURFACE_TYPES::urban_roof`) to be used instead of one.
      Additional parameters must be supplied via :nml:lst:`JULES_NVEGPARM`, with some able to be provided by MORUSES (see :nml:lst:`JULES_URBAN`).

.. nml:member:: l_mo_buoyancy_calc

      :type: logical
      :default: false

      Default JULES (l_mo_buoyancy_flux = false) uses the buoyancy from the previous timestep to calculate the surface transfer coefficients. In coupled simulations this can lead to unrealistic surface temperatures if the stability suddenly
      switches from stable to unstable, due to the low turbulence determined by the stable buoyancy flux.

      With the interactive buoyancy flux option (l_mo_buoyancy_flux = true) the surface energy balance and buoyancy flux are calculated within the iterative calculation for the Monin-Obukhov similarity theory for the surface exchange
      coefficients. On occations when the stability is around neutral it is possible that the iterative calculation does not converge. In this case the larger of the last two calculated transfer coefficients is then used to prevent
      any unrealistic surface temperatures.

.. nml:group:: Surface parameters

   .. nml:member:: hleaf

      :type: real
      :default: 5.7e4

      Specific heat capacity of leaves (J K\ :sup:`-1` per kg carbon).

      See Hadley Centre Technical Note 30, p6, available from `the Met Office Library <http://www.metoffice.gov.uk/learning/library/publications/science/climate-science-technical-notes>`_.


   .. nml:member:: hwood

      :type: real
      :default: 1.1e4

      Specific heat capacity of wood (J K\ :sup:`-1` per kg carbon).

      See Hadley Centre Technical Note 30, p6, available from `the Met Office Library <http://www.metoffice.gov.uk/learning/library/publications/science/climate-science-technical-notes>`_.


   .. nml:member:: beta1

      :type: real
      :default: 0.83

      Coupling coefficient for co-limitation in photosynthesis model.

      See Cox et al. (1999), Eq.61.


   .. nml:member:: beta2

      :type: real
      :default: 0.93

      Coupling coefficient for co-limitation in photosynthesis model.

      See Cox et al. (1999), Eq.61.


   .. nml:member:: fwe_c3

      :type: real
      :default: 0.5

      Constant in expression for limitation of photosynthesis by transport of products, for C3 plants.

      See Cox et al. (1999) Eq.60.


   .. nml:member:: fwe_c4

      :type: real
      :default: 20000.0

      Constant in expression for limitation of photosynthesis by transport of products, for C4 plants.

      See Cox et al. (1999) Eq.60.
