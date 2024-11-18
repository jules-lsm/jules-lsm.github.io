``jules_vegetation.nml``
========================


This file sets the vegetation options. It contains one namelist called :nml:lst:`JULES_VEGETATION`.


``JULES_VEGETATION`` namelist members
-------------------------------------

.. nml:namelist:: JULES_VEGETATION

.. nml:member:: l_trait_phys

   :type: logical
   :default: F

   Switch for using trait-based physiology.

   TRUE
       Vcmax is calculated based on observed leaf traits. Leaf
       nitrogen (nmass: kgN kgLeaf\ :sup:`-1`) and leaf mass (LMA:
       kgLeaf m\ :sup:`-2`) can be based on observations from the TRY
       database. Vcmax (umol CO\ :sub:`2` m\ :sup:`-2` s\ :sup:`-1`) is based
       on linear regressions as in :ref:`Kattge et al. 2009<References_vegetation>`. Two additional
       parameters are needed: vint and vsl - the intercept and slope,
       respectively, that relate the leaf nitrogen to vcmax. Sigl is
       replaced with LMA (sigl=LMA*Cmass, where Cmass is the
       kgC kgLeaf\ :sup:`-1` and is 0.4).

   FALSE
       Vcmax is calculated based on parameters nl0 (kgN kgC\ :sup:`-1`) and neff.


.. nml:member:: l_phenol

   :type: logical
   :default: F

   Switch for vegetation phenology model.

   TRUE
       Use phenology model.

   FALSE
       Do not use phenology model.


.. nml:member:: l_triffid

   :type: logical
   :default: F

   Switch for dynamic vegetation model (TRIFFID) except for competition.

   TRUE
       Use TRIFFID. In this case soil carbon is modelled using four pools
       (biomass, humus, decomposable plant material, resistant plant material).

   FALSE
       Do not use TRIFFID. A single soil carbon pool is used.


.. nml:member:: l_veg_compete

   :type: logical
   :default: T

   Switch for competing vegetation.

   Only used if :nml:mem:`l_triffid` = TRUE.

   TRUE
       TRIFFID will let the different PFTs compete against each other and modify the vegetation fractions.

   FALSE
       Vegetation fractions do not change.


.. nml:member:: l_ht_compete

   :type: logical
   :default: F

   Only used if :nml:mem:`l_triffid` = TRUE.

   TRUE
      Use height-based vegetation competition (recommended).

      This allows for a generic number of PFTs. When
      :nml:mem:`l_trif_eq` = TRUE, this is implemented by
      ``lotka_eq_jls.F90``. When :nml:mem:`l_trif_eq` = FALSE, it is
      implemented in ``lotka_noeq_jls.F90`` when
      :nml:mem:`l_trif_crop` = FALSE and in
      ``lotka_noeq_subset_jls.F90`` when :nml:mem:`l_trif_crop` =
      TRUE.

   FALSE
      Use the vegetation competition described in :ref:`HCTN24<References_vegetation>`.

      This is hard-wired for 5 PFTs (BT, NT, C3, C4, SH, in that
      order) with co-competition for grasses and trees in
      ``lokta_jls.F90``.

.. nml:member:: l_nitrogen

   :type: logical
   :default: F

   Only used if :nml:mem:`l_triffid` = TRUE.

   TRUE
      Enable Nitrogen limitation of carbon uptake. A nitrogen
      deposition field should be provided otherwise no N deposition is
      assumed.

   FALSE
      No Nitrogen limitation. Nitrogen fluxes are calculated as diagnostics only.

.. nml:member:: l_trif_eq

   :type: logical
   :default: T

   Switch for equilibrium vegetation model (i.e., an equilibrium solution of TRIFFID).

   Only used if :nml:mem:`l_triffid` = TRUE.

   TRUE
       Use equilibrium TRIFFID.

   FALSE
       Do not use equilibrium TRIFFID.


.. nml:member:: phenol_period

   :type: integer
   :permitted: >= 1
   :default: None

   Period for calls to phenology model in *days*. Only relevant if :nml:mem:`l_phenol` = TRUE.


.. nml:member:: triffid_period

   :type: integer
   :permitted: >= 1
   :default: None

   Period for calls to TRIFFID model in *days*. Only relevant if one of :nml:mem:`l_triffid` or :nml:mem:`l_trif_eq` is TRUE.


.. nml:member:: l_gleaf_fix

   :type: logical
   :default: T

   Switch for fixing a bug in the accumulation of ``g_leaf_phen_acc``.

   This bug occurs because ``veg2`` is called on TRIFFID timesteps and
   ``veg1`` is called on phenol timesteps, but ``veg1`` did not
   previously accumulate ``g_leaf_phen_acc`` in the same way as
   ``veg2``.

   TRUE
       ``veg1`` accumulates ``g_leaf_phen_acc`` between calls to
       TRIFFID. This is important if :nml:mem:`triffid_period` >
       :nml:mem:`phenol_period`.

   FALSE
       ``veg1`` does not accumulate ``g_leaf_phen_acc`` between calls to TRIFFID.


.. nml:member:: l_bvoc_emis

   :type: logical
   :default: F

   Switch to enable calculation of BVOC emissions.

   TRUE
       BVOC emissions diagnostics will be calculated.

   FALSE
       BVOC emissions diagnostics will not be calculated.


.. nml:member:: l_o3_damage

   :type: logical
   :default: F

   Switch for ozone damage.

   TRUE
       Ozone damage is on.

       .. note:: Ozone concentration in ppb must be prescribed in :doc:`prescribed_data.nml`.

   FALSE
       No effect.

.. nml:member:: l_stem_resp_fix

   :type: logical
   :default: F

   Switch for bug fix for stem respiration to use balanced LAI to
   derive respiring stem mass. The switch is included for backwards
   compatibility with existing configurations. Future updates should
   include this change.

   TRUE
       Respiring stem mass is derived allometrically.

   FALSE
       Respiring stem mass varies with seasonal LAI.

       In the case of a Broadleaf tree in the winter (no leaves) this
       would mean stem respiration is scaled to 0.


.. nml:member:: l_scale_resp_pm

   :type: logical
   :default: F

   Scale whole plant maintenance respiration by the soil moisture
   stress factor, instead of only scaling leaf respiration.

   TRUE
       Soil moisture stress reduces leaf, root, and stem maintenance respiration.

   FALSE
       Soil moisture stress only reduces leaf maintenance respiration.


.. nml:member:: fsmc_shape

   :type: integer
   :permitted: 0,1
   :default: 0

   Shape of soil moisture stress function on vegetation (fsmc).

   0. Piece-wise linear in vol. soil moisture.

   1. Piece-wise linear in soil potential. Currently only allowed when
      :nml:mem:`JULES_SOIL_PROPS::const_z` = T and
      :nml:mem:`JULES_VEGETATION::l_use_pft_psi` = T.

   .. note:: The option :nml:mem:`JULES_VEGETATION::fsmc_shape` = 1 is
	     still in development. Users should ensure that results
	     are as expected, and provide feedback where deficiencies
	     are identified.

.. nml:member:: l_use_pft_psi

   :type: logical
   :default: F

   Switch for parameters in the soil moisture stress on vegetation function (fsmc).

   TRUE
       Fsmc is calculated from :nml:mem:`JULES_PFTPARM::psi_close_io`
       and :nml:mem:`JULES_PFTPARM::psi_open_io`.

   FALSE
       Fsmc is calculated from ``sm_wilt`` and ``sm_crit`` in
       :nml:lst:`JULES_SOIL_PROPS` and
       :nml:mem:`JULES_PFTPARM::fsmc_p0_io`.

   .. note:: Soil respiration and surface conductance of bare soil
	     respectively will depend on ``sm_wilt`` and ``sm_crit``
	     in :nml:lst:`JULES_SOIL_PROPS`, regardless of the setting
	     of :nml:mem:`JULES_VEGETATION::fsmc_shape`.

   .. note:: The option :nml:mem:`JULES_VEGETATION::l_use_pft_psi` = T
	     is still in development. Users should ensure that results
	     are as expected, and provide feedback where deficiencies
	     are identified.


.. nml:member:: l_vegcan_soilfx

   :type: logical
   :default: F

   Switch for enhancement to canopy model to allow for conduction in
   the soil below the vegetative canopy, reducing coupling between the
   soil and the canopy.

   TRUE
       Allow for conduction in the soil.

   FALSE
       No effect.

.. nml:member:: l_leaf_n_resp_fix

   :type: logical
   :default: F

   Switch for bug fix for leaf nitrogen content used in the
   calculation of plant maintenance respiration. The switch is
   included for backwards compatibility with existing
   configurations. Runs with :nml:mem:`can_rad_mod` = 1, 4 or 5 are
   affected.

   TRUE
       Use correct forms for canopy-average leaf N content.

   FALSE
       No effect.

.. nml:member:: l_landuse

   :type: logical
   :default: F

   Switch for using landuse change in conjunction with TRIFFID

   Only used if :nml:mem:`l_triffid` = TRUE.

   TRUE
       Land use change is implemented within TRIFFID. Litter fluxes
       are split between soil and wood product pools. Requires
       additional prognostics covering the product pools and the
       agricultural fraction from the previous TRIFFID call.

   FALSE
       All litter fluxes enter the soil


.. nml:member:: l_recon

   :type: logical
   :default: T

   Switch for reconfiguring vegetation fractions. Also initialises
   vegetation and soil biogeochemistry at land ice points. With the
   ECOSSE soil model this switch also ensures that the initial
   condition for soil biogeochemistry is internally consistent.

   TRUE
       For soil points (land points with no ice) ensure vegetation
       fractions are at least a minimum value and reduce other
       fractions accordingly.

   FALSE
       Do not apply the minimum vegetation fractions. This is useful
       when some points are 100% lake and urban, in which case
       reconfiguration leads to a total surface tile fraction of greater
       than 1.


.. nml:member:: l_prescsow

   :type: logical
   :default: F

   Switch that determines how crop sowing dates are defined. Only used
   if :nml:mem:`JULES_SURFACE_TYPES::ncpft` > 0.

   TRUE
       Sowing dates prescribed in :nml:lst:`JULES_CROP_PROPS` are used.

   FALSE
       Sowing dates are determined by the model.


.. nml:member:: l_trif_crop

   :type: logical
   :default: F

   Switch controlling the treatment of agricultural PFTs. Where
   agricultural PFTs are defined by the
   :nml:mem:`JULES_TRIFFID::crop_io` parameter.

   TRUE
       In the non-agricultural area natural PFT competition is
       calculated by a call to a new version of the lotka routine and
       in each agricultural area agricultural-PFT competition is
       calculated by an additional call to the new version of the
       lotka routine. Crop and pasture areas are defined by the
       :nml:mem:`JULES_AGRIC::frac_agr` and
       :nml:mem:`JULES_AGRIC::frac_past` variables
       respectively. Additionally, to represent harvesting, a fraction
       of crop litter is added to the fast wood products pool instead
       of the soil carbon pools.

   FALSE
       Vegetation competition is calculated for natural and crop PFTs
       together, with natural PFTs excluded from the agricultural area
       that is defined by the :nml:mem:`JULES_AGRIC::frac_agr`
       variable. Agricultural PFTs can also grow in natural areas
       where they are interpreted as natural grasses.


.. nml:member:: l_trif_biocrop

   :type: logical
   :default: F

   Allows for representation of bioenergy crops with continuous or periodic harvesting of agricultural PFTs at prescribed intervals. Requires :nml:mem:`JULES_VEGETATION::l_trif_crop` = TRUE.

   TRUE
       Crop, pasture, and bioenergy crop areas are defined by the :nml:mem:`JULES_AGRIC::frac_agr`, :nml:mem:`JULES_AGRIC::frac_past`, :nml:mem:`JULES_AGRIC::frac_biocrop` variables respectively. Harvests are permitted from any land class and enabled for each PFT separately using the :nml:mem:`JULES_TRIFFID::harvest_type_io` variable. Harvesting may be continuous (as per the existing scheme in  :nml:mem:`JULES_VEGETATION::l_trif_crop`, when :nml:mem:`JULES_TRIFFID::harvest_type_io` is 1), or performed at prescribed intervals defined using the :nml:mem:`JULES_TRIFFID::harvest_freq_io` and :nml:mem:`JULES_TRIFFID::harvest_ht_io` variables (when :nml:mem:`JULES_TRIFFID::harvest_type_io` is 2). 

   FALSE
       Land use classes, PFT partitioning, and harvests are as defined by the :nml:mem:`JULES_VEGETATION::l_trif_crop` switch.

  .. seealso::
     References:

     * Littleton et al., 2020, JULES-BE: representation of bioenergy crops and harvesting in the Joint UK Land Environment Simulator vn5.1, Geosci. Model Dev., https://doi.org/10.5194/gmd-13-1123-2020


.. nml:member:: l_ag_expand

   :type: logical
   :default: F

   Allows for assisted expansion of agricultural crop areas. Requires :nml:mem:`JULES_VEGETATION::l_landuse` = TRUE.

   TRUE
       Automatically plant out new crop areas with target PFTs.

   FALSE
       No automatic increase of PFT fraction when land class fraction increases.


.. nml:member:: can_model

   :type: integer
   :permitted: 1-4
   :default: 4

   Choice of canopy model for vegetation:

   1. No distinct canopy (i.e. surface is represented as a single entity for radiative processes).
   2. Radiative canopy with no heat capacity.
   3. Radiative canopy with heat capacity. This option is deprecated, with 4 preferred.
   4. As 3 but with a representation of snow beneath the canopy. This option is preferred to 3.

   .. note::
       :nml:mem:`can_model` = 1 does not mean that there is no
	    vegetation canopy. It means that the surface is
	    represented as a single entity, rather than having
	    distinct surface and canopy levels for the purposes of
	    radiative processes.


.. nml:member:: can_rad_mod

   :type: integer
   :permitted: 1, 4, 5, 6
   :default: 4

   Options for treatment of canopy radiation.

   1. A single canopy layer for which radiation absorption is
      calculated using Beer's law. Leaf-level photosynthesis is scaled
      to the canopy level using the 'big leaf' approach. Leaf
      nitrogen, photosynthetic capacity, i.e the Vcmax parameter, and
      leaf photosynthesis vary exponentially through the canopy with
      radiation.

   4. Multi-layer approach for radiation interception following the
      two-stream approach of :ref:`Sellers et
      al. (1992)<References_vegetation>`. This approach takes into account leaf
      angle distribution, zenith angle, and differentiates absorption
      of direct and diffuse radiation. It has an exponential decline
      of leaf N through the canopy and includes inhibition of leaf
      respiration in the light. Canopy photosynthesis and conductance
      are calculated as the sum over all layers.

   5. This is an improvement of option 4, including:

      * Sunfleck penetration though the canopy.
      * Division of sunlit and shaded leaves within each canopy level.
      * A modified version of inhibition of leaf respiration in the light.

   6. This is an improvement of option 5, including an exponential
      decline of leaf N with canopy height proportional to LAI,
      following Beer's law.

   .. note:: :nml:mem:`can_rad_mod` = 1 and 6 are recommended.

   .. note:: When using :nml:mem:`can_rad_mod` = 4, 5 or 6 it is
	     recommended to use driving data that contains direct and
	     diffuse radiation separately rather than a constant
	     diffuse fraction.

   .. seealso:: Descriptions of option 1 can be found in
		:ref:`Jogireddy et al. (2006)<References_vegetation>`, and an
		application of option 4 can be found in :ref:`Mercado
		et al. (2007)<References_vegetation>`. Options 1 to 5 are
		described in :ref:`Clark et al (2011)<References_vegetation>`.


.. nml:member:: ilayers

   :type: integer
   :permitted: >= 0
   :default: 10

   Number of layers for canopy radiation model. Only used for :nml:mem:`can_rad_mod` = 4, 5 or 6.

   These layers are used for the calculations of radiation interception and photosynthesis.


.. nml:member:: photo_model

   :type: integer
   :permitted: 1 or 2
   :default: none

   Choice for model of leaf photosynthesis.

   Possible values are:

   1. | C\ :sub:`3` and C\ :sub:`4` plants use the models of Collatz et al., 1991 and 1992, respectively. These were used in the original JULES model.

   2. | C\ :sub:`3` plants use the model of Farquhar et al. (1980); C\ :sub:`4` plants use the model of Collatz et al. (1992).

   .. warning::
      The Farquhar model can only be used if :nml:mem:`can_rad_mod` = 1, 5 or 6. Code has not been written for other values of :nml:mem:`can_rad_mod`.

   .. seealso::
      References:

      * Collatz et al., 1991, Physiological and environmental regulation of stomatal conductance, photosynthesis, and transpiration – a model that includes a laminar boundary layer, Agricultural and Forest Meteorology, https://doi.org/10.1016/0168-1923(91)90002-8.
      * Collatz et al., 1992, Coupled Photosynthesis-Stomatal Conductance Model for Leaves of C\ :sub:`4` Plants, Australian Journal of Plant Physiology, https://doi.org/10.1071/PP9920519.
      * Farquhar et al., 1980, A biochemical model of photosynthetic CO\ :sub:`2` assimilation in leaves of C\ :sub:`3` species, Planta, https://doi.org/10.1007/BF0038623.


.. nml:member:: stomata_model

   :type: integer
   :permitted: 1, 2, OR 3
   :default: 1

   Choice for model of stomatal conductance.

   Possible values are:

   1. The original JULES model, including the Jacobs closure - see
      Eqn.9 of :ref:`Best et al. (2011)<References_vegetation>`.

   2. The model of :ref:`Medlyn et al. (2011)<References_vegetation>` - see
      Eqn.11 of that paper, and :ref:`Medlyn et al
      (2012)<References_vegetation>`. Note that as implemented the model uses a
      single parameter (g\ :sub:`1`, assuming that g\ :sub:`0` = 0).
   3. The SOX model of :ref:`Eller et al. (2020)<References_vegetation>`

   .. warning::

      Only the original (Jacobs) model can currently be used with the
      UM (Option 1).


.. nml:member:: frac_min

   :type: real
   :default: 1.0e-6

   Minimum fraction that a PFT is allowed to cover if TRIFFID is used.


.. nml:member:: frac_seed

   :type: real
   :default: 0.01

   Seed fraction for TRIFFID.


.. nml:member:: pow

   :type: real
   :default: 5.241e-4

   Power in sigmodial function used to get competition coefficients.

   See Hadley Centre Technical Note 24, Eq.3.


.. nml:member:: l_inferno

   :type: logical
   :default: F

   Switch that determines whether interactive fires (INFERNO) is
   used. This allows for the diagnostic of burnt area, burnt carbon
   and a variety of fire emissions.

   TRUE
       INFERNO is used to provide diagnostic fire variables

   FALSE
       INFERNO is not used.

.. nml:member:: ignition_method

   :type: integer
   :permitted: 1, 2, 3
   :default: 1

   Switch to determine the type of ignition used (ubiquitous or prescribed with population and lightning)

   1.  INFERNO uses ubiquitous (constant) ignitions, of 1.67 fires km\
       :sup:`-2` s\ :sup:`-1` (1.5 from humans, 0.17 from lightning).

   2.  INFERNO uses prescribed lightning ignitions, either from an ancillary or the UM.
       Meanwhile humans are assumed to ignite 1.5 fires km\ :sup:`-2` s\ :sup:`-1`.

   3.  INFERNO uses prescribed ignition using Population Density and Lightning Frequency (Cloud-to-Ground).
       These must be provided as prescribed data to the JULES run.

.. nml:member:: l_trif_fire

   :type: logical
   :default: F

   Switch that determines whether interactive fire is used. This allows for burnt area to link with dynamic
   vegetation.

   Only used if :nml:mem:`l_triffid` = TRUE.

   TRUE
       Burnt area is calculated in INFERNO and passed to TRIFFID to
       calculate vegetation dynamics. Carbon is also removed from DPM
       and RPM pools in SOILCARB.
   FALSE
       Burnt area is zero unless prescribed via an ancillary file.

.. nml:member:: l_vegdrag_pft

   :type: logical(npft)
   :default: F

   Switch for using vegetation canopy drag scheme on each PFT.

   TRUE
       Use a vegetative drag scheme. This is based on :ref:`Harman and Finnigan (2007)<References_vegetation>`.

   FALSE
       Do not use vegetative drag scheme.

.. nml:member:: l_rsl_scalar

   :type: logical
   :default: F

   Switch for using a roughness sublayer correction scheme in scalar
   variables. This is based on :ref:`Harman and Finnigan
   (2008)<References_vegetation>`.

   Only use if any :nml:mem:`l_vegdrag_pft` = TRUE.

   TRUE
       Use a roughness sublayer correction scheme in scalar variables.

   FALSE
       Do not use a roughness sublayer correction scheme in scalar variables.

.. nml:member:: c1_usuh

   :type: real
   :permitted: >= 0
   :default: None

   u*/U(h) at the top of dense canopy. See :ref:`Massman (1997)<References_vegetation>`.

   Only use if any :nml:mem:`l_vegdrag_pft` = TRUE.

.. nml:member:: c2_usuh

   :type: real
   :permitted: >= 0
   :default: None

   u*/U(h) at substrate under canopy. See :ref:`Massman (1997)<References_vegetation>`.

   Only use if any :nml:mem:`l_vegdrag_pft` = TRUE.

.. nml:member:: c3_usuh

   :type: real
   :permitted: >= 0
   :default: None

   This is used in the exponent of equation weighting dense and sparse
   vegetation to get u*/U(h) in neutral condition. See :ref:`Massman
   (1997)<References_vegetation>`. The default value is taken from :ref:`Wang
   (2012)<References_vegetation>`.

   Only use if any :nml:mem:`l_vegdrag_pft` = TRUE.

.. nml:member:: cd_leaf

   :type: real
   :permitted: 0:1
   :default: None

   Leaf level drag coefficient.

   Only use if any :nml:mem:`l_vegdrag_pft` = TRUE.

.. nml:member:: stanton_leaf

   :type: real
   :permitted: 0:1
   :default: None

   Leaf-level Stanton number

   Only use if :nml:mem:`l_rsl_scalar` = TRUE.

.. nml:member:: l_spec_veg_z0

   :type: logical
   :default: F

   Switch for using specified values of the vegetation roughness
   length rather than being determined by the canopy height.

   TRUE
       Vegetation roughness lengths are specified for each PFT in
       :nml:mem:`JULES_PFTPARM::z0v_io`.

   FALSE
       Vegetation roughness lengths are calculated using canopy
       heights and parameter :nml:mem:`JULES_PFTPARM::dz0v_dh_io`.

.. nml:member:: l_limit_canhc

   :type: logical
   :default: F

   Switch for limiting the canopy heat capacity for vegetation, which
   is calculated from the canopy height.

   Using the SIMARD canopy height ancillary gives very large heat
   capacities in the Amazon, so this switch limits the areal heat
   capacity to 1.15e5 J kg\ :sup:`-1` m\ :sup:`-2`, which is the value
   calculated by the default broadleaf tree height of 19.01 m.

   TRUE
       Vegetation areal heat capacity limited.

   FALSE
       Vegetation areal heat capacity unlimited.

.. nml:member:: l_sugar

   :type: logical
   :default: F

   Switch for using the SUGAR carbohydrate model (:ref:`Jones et al., (2020)<References_vegetation>`)

   TRUE
       Respiration is calculated using the SUGAR carbohydrate model

   FALSE
       SUGAR is not used

   .. note:: The option :nml:mem:`JULES_VEGETATION::l_sugar` = T
             is still in development. Users should ensure that results
             are as expected, and provide feedback where deficiencies
             are identified.


.. nml:group:: Only used with the Farquhar model of leaf photosynthesis (:nml:mem:`photo_model` = 2).

   .. nml:member:: photo_acclim_model

      :type: integer
      :permitted: 0, 1, 2, or 3
      :default: None

      Choice for model of thermal response of photosynthetic capacity.
      Possible values are:

      0. | No adaptation or acclimation.

      1. | Thermal adaptation - plant response to temperature varies geographically in response to a static "home" temperature.

      2. | Thermal acclimation - plant response to temperature varies geographically and temporally in response to a dynamic "growth" temperature.

      3. | Thermal adaptation and acclimation - plant response to temperature varies geographically and temporally in response to a static "home" temperature and a dynamic "growth" temperature.

      .. note:: When :nml:mem:`photo_acclim_model` = 1 or 3 is used, the user must supply the long-term home temperature as ancillary field ``t_home_gb`` in :nml:lst:`JULES_VEGETATION_PROPS`.  When :nml:mem:`photo_acclim_model` = 2 or 3 is used, the user must supply the running mean growth temperature as initial condition ``t_growth_gb`` in :nml:lst:`JULES_INITIAL`.


   .. nml:member:: photo_act_model

      :type: integer
      :permitted: 1 or 2
      :default: None

      Choice of model for the activation energies of J\ :sub:`max` and V\ :sub:`cmax`.

      1. | Activation energies vary by PFT but not by land point, and are NOT subject to acclimation.

      2. | Activation energies vary by land point but not by PFT, and are subject to acclimation.

      .. note:: When :nml:mem:`photo_act_model` = 1 is used, activation energies are calculated using :nml:mem:`JULES_PFTPARM::act_jmax_io` and :nml:mem:`JULES_PFTPARM::act_vcmax_io`.  When :nml:mem:`photo_act_model` = 2 is used, activation energies are calculated using :nml:mem:`act_j_coef` and :nml:mem:`act_v_coef`.

      .. warning::
        A value of 1 (PFT-dependent) must be used if :nml:mem:`photo_acclim_model` = 0 (no adaptation or acclimation).


   .. nml:member:: photo_jv_model

      :type: integer
      :permitted: 1 or 2
      :default: None

      Choice for model of for the variation of J\ :sub:`25`/V\ :sub:`25`.

      1. | J\ :sub:`25` is found by scaling V\ :sub:`25` by the given ratio J\ :sub:`25`/V\ :sub:`25`, that is, all the variation in the ratio comes from varying J\ :sub:`25` (while V\ :sub:`25` remains fixed).

      2. | J25 and V25 are calculated assuming that the total amount of nitrogen allocated to photosynthesis remains constant, thus any change in J25 requires a compensatory change in V25 - as used in :ref:`Mercado et al. (2018)<References_vegetation>`.

      .. warning::
        A value of 1 (simple scaling) must be used if :nml:mem:`photo_acclim_model` = 0 (no adaptation or acclimation).



.. nml:group:: Only used with :nml:mem:`photo_jv_model` = 2.


   .. nml:member:: n_alloc_jmax

      :type: real
      :default: None

      Constant relating nitrogen allocation to J\ :sub:`max` (mol CO\ :sup:`2` m\ :sup:`-2` s\ :sup:`-1` [kg m\ :sup:`-2`]\ :sup:`-1`). This is 5.3 in Eq.5 of :ref:`Mercado et al. (2018)<References_vegetation>`.


   .. nml:member:: n_alloc_vcmax

      :type: real
      :default: None

      Constant relating nitrogen allocation to V\ :sub:`cmax` (mol CO\ :sup:`2` m\ :sup:`-2` s\ :sup:`-1` [kg m\ :sup:`-2`]\ :sup:`-1`). This is 3.8 in Eq.5 of :ref:`Mercado et al. (2018)<References_vegetation>`.



.. nml:group:: Only used with thermal adaptation or acclimation of photosynthesis (:nml:mem:`photo_acclim_model` = 1, 2 or 3).

   The thermal adaptation/acclimation scheme in JULES is structured following Eq. 13 of :ref:`Kumarathunge et al. (2019)<References_vegetation>`, in which C3 photosynthetic capacity is allowed to vary at each land point as a function of a static home temperature (T\ :sub:`h`) and a dynamic growth temperature (T\ :sub:`g`).  This is achieved by calculating five parameters used in the Farquhar photosynthesis scheme as functions of those temperature fields, rather than using fixed parameters from :nml:lst:`JULES_PFTPARM`.  Each parameter, Q, is calculated as a linear function of T\ :sub:`h` and T\ :sub:`g`:

   Q(T\ :sub:`h`, T\ :sub:`g`) = Q\ :sub:`coef`\ (0) + Q\ :sub:`coef`\ (1) T\ :sub:`h` + Q\ :sub:`coef`\ (2) T\ :sub:`g`.

   The following namelist members specify the coefficients, Q\ :sub:`coef`, used for each parameter.  Note that, in each case, the units for Q\ :sub:`coef`\ (1) and Q\ :sub:`coef`\ (2) have an extra factor K\ :sup:`-1` relative to the units for Q\ :sub:`coef`\ (0).  This structure can be configured to represent the acclimation scheme of :ref:`Kattge and Knorr (2007)<References_vegetation>`, as used by :ref:`Mercado et al. (2018)<References_vegetation>`, and the scheme of :ref:`Kumarathunge et al. (2019)<References_vegetation>`.

   .. note:: If :nml:mem:`photo_acclim_model` = 1 is used all Q\ :sub:`coef`\ (2) must equal 0.0, and if :nml:mem:`photo_acclim_model` = 2 is used all Q\ :sub:`coef`\ (1) must equal 0.0.

   .. nml:member:: act_j_coef

      :type: real(3)
      :default: None

      Coefficients for the activation energy for J\ :sub:`max` (J mol\ :sup:`-1` and J mol\ :sup:`-1` K\ :sup:`-1`).  Replaces the use of :nml:mem:`JULES_PFTPARM::act_jmax_io`.


   .. nml:member:: act_v_coef

      :type: real(3)
      :default: None

      Coefficients for the activation energy for V\ :sub:`cmax` (J mol\ :sup:`-1` and J mol\ :sup:`-1` K\ :sup:`-1`).  Replaces the use of :nml:mem:`JULES_PFTPARM::act_vcmax_io`.


   .. nml:member:: dsj_coef

      :type: real(3)
      :default: None

      Coefficients for entropy factor for J\ :sub:`max` (J mol\ :sup:`-1` K\ :sup:`-1` and J mol\ :sup:`-1` K\ :sup:`-2`).  Replaces the use of :nml:mem:`JULES_PFTPARM::deact_jmax_io`.


   .. nml:member:: dsv_coef

      :type: real(3)
      :default: None

      Coefficients for the entropy factor for V\ :sub:`cmax` (J mol\ :sup:`-1` K\ :sup:`-1` and J mol\ :sup:`-1` K\ :sup:`-2`).  Replaces the use of :nml:mem:`JULES_PFTPARM::deact_vcmax_io`.


   .. nml:member:: jv25_coef

      :type: real(3)
      :default: None

      Coefficients for the ratio J\ :sub:`25`/V\ :sub:`25` (mol electrons [mol\ :sup:`-1` CO\ :sub:`2`] and (mol electrons [mol\ :sup:`-1` CO\ :sub:`2`] K\ :sup:`-1`).  Replaces the use of :nml:mem:`JULES_PFTPARM::jv25_ratio_io`.


.. nml:group:: Only used with thermal acclimation of photosynthesis (:nml:mem:`photo_acclim_model` = 2 or 3).

   .. nml:member:: n_day_photo_acclim

      :type: real
      :default: None

      Time constant (days) for the exponential moving average of temperature that is used as the growth temperature. Given a step function as input, the smoothed output has fallen to 1/e (approx. 37%) of the initial value after this number of days.


.. nml:member:: l_croprotate

   :type: logical
   :default: F

   Switch that enables sequential cropping (crop rotations). 
   Only used
   if :nml:mem:`JULES_SURFACE_TYPES::ncpft` > 0 and
   if :nml:mem:`JULES_VEGETATION::l_prescsow` = T.

   TRUE
       Sowing dates and latest harvest dates prescribed in
       :nml:lst:`JULES_CROP_PROPS` are used. The method is implemented in
       :ref:`Mathison et al. (2019)<References_vegetation>`.

   FALSE
       The crop model is used in its standard form with a single crop per year

.. _References_vegetation:

``JULES_VEGETATION`` references
-------------------------------

* Best et al., 2011, The Joint UK Land Environment Simulator (JULES),
  model description – Part 1: Energy and water fluxes, Geosci. Model
  Dev., https://doi.org/10.5194/gmd-4-677-2011.
* Clark et al., 2011, The Joint UK Land Environment Simulator (JULES)
  model description – Part 2: Carbon fluxes and vegetation dynamics,
  Geosci. Model Dev., 4, 701-722,
  https://doi.org/10.5194/gmd-4-701-2011
* Eller et al. (2020), Stomatal optimization based on xylem hydraulics
  (SOX) improves land surface model simulation of vegetation responses
  to climate. New Phytologist 226:
  1622–1637 https://doi.org/10.1111/nph.16419
* Harman, I.N. & Finnigan, J.J. (2007), A simple unified theory for
  flow in the canopy and roughness sublayer. Boundary-Layer Meteorol.
  123: 339. https://doi.org/10.1007/s10546-006-9145-6
* Harman, I.N. & Finnigan, J.J. (2008), Scalar Concentration Profiles in the
  Canopy and Roughness Sublayer. Boundary-Layer Meteorol.
  129: 323. https://doi.org/10.1007/s10546-008-9328-4
* HCTN24, Hadley Centre Technical Note 24, available from `the Met Office Library
  <http://www.metoffice.gov.uk/learning/library/publications/science/climate-science-technical-notes>`_.
  For ease the direct link to this document is:
  `HCTN24 "Description of the "TRIFFID" Dynamic Global Vegetation Model" <https://digital.nmla.metoffice.gov.uk/IO_cc8f146a-d524-4243-88fc-e3a3bcd782e7>`_.
* Jogireddy, V., Cox, P. M., Huntingford, C., Harding, R. J., and
  Mercado, L. M.:  An improved description of canopy light
  interception for use in a GCM land-surface scheme: calibration and
  testing against carbon fluxes at a coniferous forest, Hadley Centre
  Technical Note 63, Hadley Centre, Met Office, Exeter,
  UK, 2006. https://digital.nmla.metoffice.gov.uk/IO_7873ea05-61ec-4615-b030-6bc33397d675
* Kattge, J. and Knorr, W., 2007,
  Temperature acclimation in a biochemical model of photosynthesis:
  a reanalysis of data from 36 species,
  Plant, Cell and Environment, 30: 1176--1190,
  https://doi.org/10.1111/j.1365-3040.2007.01690.x.
* Kattge, J. , Knorr, W. , Raddatz, T. and Wirth, C. (2009),
  Quantifying photosynthetic capacity and its relationship to leaf
  nitrogen content for global-scale terrestrial biosphere
  models. Global Change Biology, 15:
  976-991. https://doi.org/doi:10.1111/j.1365-2486.2008.01744.x
* Kumarathunge, D. P. et al (2019), Acclimation and adaptation components of
  the temperature dependence of plant photosynthesis at the global scale, New
  Phytologist, 222: 768-784, https://doi.org/10.1111/nph.15668
* Massman, W. J. (1997), An Analytical One-Dimensional Model of
  Momentum Transfer by Vegetation of Arbitrary Structure,
  Boundary-Layer Meteorol. 83: 407-421.
* Medlyn, B. E., Duursma, R. A., Eamus, D. , Ellsworth, D. S.,
  Prentice, I. C., Barton, C. V., Crous, K. Y., De angelis, P.,
  Freeman, M. and Wingate, L. (2011), Reconciling the optimal and
  empirical approaches to modelling stomatal conductance. Global
  Change Biology, 17:
  2134-2144. https://doi.org/10.1111/j.1365-2486.2010.02375.x
* Medlyn, B. E., Duursma, R. A., Eamus, D. , Ellsworth, D. S.,
  Prentice, I. C., Barton, C. V., Crous, K. Y., De angelis, P.,
  Freeman, M. and Wingate, L. (2012), Reconciling the optimal and
  empirical approaches to modelling stomatal conductance. Global
  Change Biology, 18:
  3476-3476. https://doi.org/10.1111/j.1365-2486.2012.02790.x.
* Mercado, L. M., Huntingford, C., Gash, J. H. C., Cox, P. M., and
  Jogireddy, V.: Improving the representation of radiative
  interception and photosynthesis for climate model applications,
  Tellus B, 59,
  553–565, 2007. https://doi.org/10.1111/j.1600-0889.2007.00256.x
* Mercado et al., 2018, Large sensitivity in land carbon storage due to
  geographical and temporal variation in the thermal response of
  photosynthetic capacity, New Phytologist, 218: 1462--1477,
  https://doi.org/10.1111/nph.15100.
* Sellers et al., 1992, Canopy reflectance, photosynthesis, and
  transpiration. III. A reanalysis using improved leaf models and a
  new canopy integration scheme. Remote Sens. Environ., 42, 187-216,
  https://doi.org/10.1016/0034-4257(92)90102-P
* Wang, W. (2012), An Analytical Model for Mean Wind Profiles in
  Sparse Canopies. Boundary-Layer Meteorol
  142: 383. https://doi.org/10.1007/s10546-011-9687-0
* Mathison, C , Challinor, A. J., Deva, C., Falloon, P., Garrigues, S.,
  Moulin, S., Williams, K., and Wiltshire, A. (2019),
  Developing a sequential cropping capability in the JULESvn5.2
  land–surface model, Geosci. Model Dev. Discuss.,
  https://doi.org/10.5194/gmd-2019-85, in review, 2019.
* Jones et al., 2020, The impact of a simple representation of 
  non-structural carbohydrates on the simulated response of tropical 
  forests to drought, Biogeosciences, 17: 3589--3612. 
  https://doi.org/10.5194/bg-17-3589-2020
