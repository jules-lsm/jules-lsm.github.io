``jules_deposition.nml``
=============================


This file contains options and parameters for modelling of dry deposition of atmospheric trace constituents. It contains a variable number of namelists depending on the required model configuration. The namelist :nml:lst:`JULES_DEPOSITION` is always required, the namelist :nml:lst:`JULES_DEPOSITION_SPECIES_SPECIFIC` and one or more instances of the namelist :nml:lst:`JULES_DEPOSITION_SPECIES` is required if dry deposition has been selected.

.. warning::
   Atmospheric deposition in JULES is still in development. In this version, two options are provided: (1) :nml:mem:`JULES_DEPOSITION::dry_dep_model` = 1, which implements the existing UKCA interactive gas-phase dry deposition routines in JULES. The parameters are hard-wired in the code and only 4 surface tile configurations are permitted; and (2) :nml:mem:`JULES_DEPOSITION::dry_dep_model` = 2, which removes the surface tile restrictions and uses namelists to define the various deposition parameters. Deposition parameters specific to a single deposited species are input on :nml:lst:`JULES_DEPOSITION_SPECIES_SPECIFIC` namelist. There is a separate :nml:lst:`JULES_DEPOSITION_SPECIES` namelist for each deposited species for deposition parameters common to more than one deposited species. To activate the deposition code: set :nml:mem:`JULES_DEPOSITION::l_deposition` to TRUE.



``JULES_DEPOSITION`` namelist members
-------------------------------------

.. nml:namelist:: JULES_DEPOSITION


.. nml:member:: l_deposition

   :type: logical
   :default: FALSE

   Switch to activate deposition code in JULES.
   
   TRUE
      Model deposition in JULES.

   FALSE
      Do not model deposition in JULES.

   .. note:: There is now a requirement to specify all surface types in :nml:lst:`JULES_SURFACE_TYPES` (the plant functional types need to be defined, e.g. :nml:mem:`JULES_SURFACE_TYPES::brd_leaf` =1, :nml:mem:`JULES_SURFACE_TYPES::ndl_leaf` =2, :nml:mem:`JULES_SURFACE_TYPES::c3_grass` =3, :nml:mem:`JULES_SURFACE_TYPES::c4_grass` =4, :nml:mem:`JULES_SURFACE_TYPES::shrub` =5 for the 5-pft configuration).


.. nml:group:: Only used if :nml:mem:`l_deposition` = TRUE.


   .. nml:member:: dry_dep_model

      :type: integer
      :permitted: 1, 2
      :default: none

      Choice for model of dry deposition.

      Possible values are:

      1. | Parameterisation based on the interactive dry deposition scheme in the UKCA.
      2. | Parameterisation based on the interactive dry deposition scheme in the UKCA, with the restriction on the allowable surface tile configuration removed.


   .. nml:member:: dep_h2_soil_scheme

      :type: integer
      :permitted: 1, 2
      :default: none

      Choice for scheme for soil uptake of H2 from the atmosphere.

      Possible values are:

      1. | Parameterisation based on Conrad & Seiler uptake scheme in the UKCA.
      2. | Parameterisation based on Paulot et al. scheme.

      Note: The Paulot et al. scheme is currently not available in UM-coupled JULES applications. 


   .. nml:member:: l_deposition_flux

      :type: logical
      :default: FALSE

      Switch for calculation of deposition fluxes as opposed to deposition velocities.

      TRUE
         Calculate deposition fluxes. This requires that the concentrations of atmopsheric tracer species are provided as prescribed data (see :ref:`supported-prescribed-variables`).

      FALSE
         Calculate deposition velocities.


   .. nml:member:: ndry_dep_species

      :type: integer
      :permitted: >= 1 and <= 200 (ndep_species_max)
      :default: none

      Number of species for which dry deposition is calculated.


   .. nml:member:: tundra_s_limit

      :type: real
      :default: none

      Latitude of southern limit of tundra (radians). This is used to alter the calculation of deposition of certain species in the tundra region (actually for all points north of this limit). Only used if the list of species (see :nml:mem:`JULES_DEPOSITION_SPECIES::dep_species_name_io`) includes one or more of 'CO', 'NO2', 'O3', 'PAN', 'PPAN', 'MPAN' or 'ONITU'. 


   .. nml:member:: dzl_const

      :type: real
      :default: none

      Constant value for separation of boundary layer levels (m). All layer thicknesses are set to this value. This is used as a simple way to prescribe the layer thicknesses in standalone mode. This value can be overriden by prescribed data - see :nml:lst:`JULES_PRESCRIBED`. This can be considered as the representative depth for tracer concentration and the depth over which the deposition flux is removed.


   .. nml:member:: l_deposition_from_ukca

      :type: logical
      :default: FALSE

      Switch to determine calling routine for the JULES-based interactive deposition routines.

      TRUE
         Calls the JULES-based deposition routines from the same UKCA routine ukca_chemistry_ctl (or the equivalents: ukca_chemistry_ctl_BE or ukca_chemistry_ctl_col), which is used to call the UKCA-based interactive deposition routines.

      FALSE
         Calls the JULES-based deposition routines from the JULES routine surf_couple_extra.

   .. note:: For JULES standalone applications, the JULES-based deposition routines can only be called from surf_couple_extra() and :nml:mem:`JULES_DEPOSITION::l_deposition_from_ukca` is false and not enabled. For UM-coupled JULES applications, the JULES-based deposition routines can currently only be called from the UKCA and :nml:mem:`JULES_DEPOSITION::l_deposition_from_ukca` should be set to true.


.. nml:group:: (1) Switches that are only available for use in standalone JULES applications.

   .. nml:member:: l_deposition_gc_corr

      :type: logical
      :default: FALSE

      Switch to use stomatal conductances with or without bare soil evaporation.

      TRUE
         Use calculation of stomatal conductance without bare soil evaporation.

      FALSE
         Use calculation of stomatal conductance with bare soil evaporation.


.. nml:group:: (2) For UM-coupled JULES applications, the following switches are set during the run to be equivalent to the corresponding switches in the UKCA (which are set in the UM run_ukca namelist).

   .. nml:member:: l_ukca_ddep_lev1

      :type: logical
      :default: FALSE

      Switch from the UKCA controlling which atmospheric levels in the boundary layer are used for dry deposition. For UM-coupled JULES applications, the UKCA interactive dry deposition switch (l_ukca_intdd in the run_ukca namelist) needs to be true. 

      TRUE
         Deposition occurs only from the lowest level in the atmospheric boundary layer.

      FALSE
         Deposition occurs from all levels within the atmospheric boundary layer.


   .. nml:member:: l_ukca_emsdrvn_ch4

      :type: logical
      :default: FALSE

      Switch from the UKCA in which the UKCA chemistry scheme uses methane (CH\ :sub:`4`) emissions instead of prescribed CH\ :sub:`4` surface mole fractions.

      TRUE
         UKCA chemistry scheme uses methane (CH\ :sub:`4`) emissions.

      FALSE
         UKCA chemistry scheme uses prescribed CH\ :sub:`4` surface mole fractions.


.. nml:group:: (3) Switches that are only available for UM-coupled JULES applications. The following switches are set during the run to be equivalent to the corresponding switches in the UKCA (which are set in the UM run_ukca namelist).

   .. nml:member:: l_ukca_ddepo3_ocean

      :type: logical
      :default: FALSE

      Switch from the UKCA to use a mechanistic calculation for deposition of ozone to the ocean from Luhar et al. (2018).

      TRUE
         Use the mechanistic calculation of Luhar et al. (2018).

      FALSE
         Use the surface resistance term for water provided in rsurf_std_io.


   .. nml:member:: l_ukca_dry_dep_so2wet

      :type: logical
      :default: FALSE

      Switch from the UKCA to account for surface wetness in the dry deposition for SO\ :sub:`2`. The calculation uses the parameterisation in Erisman, Pul and Wyers (1994).

      TRUE
         Account for surface wetness in the dry deposition for SO\ :sub:`2`.

      FALSE
         Do not account for surface wetness in the dry deposition for SO\ :sub:`2`.


Notes on the ``JULES_DEPOSITION`` namelist
------------------------------------------

The height of the atmospheric boundary layer is required and is set to a default constant value of 1000 m. This value can be overridden via the namelist variable :nml:mem:`JULES_DRIVE::bl_height`, or can be prescribed (i.e. allowed to vary in time and/or space) by providing ``bl_height`` as prescribed data (see :ref:`supported-prescribed-variables`).

The number of model levels in the boundary layer is required and is set to a default balues of 1. This can be overridden via the namelist variable :nml:mem:`JULES_NLSIZES::bl_levels`. The number of levels is only used to communicate with the atmospheric model (e.g. UKCA).

The separation of the model levels in the boundary layer is required and is set to a constant value via :nml:mem:`dzl_const`. The separation can be prescribed (i.e. allowed to vary in time and/or space) by providing ``level_separation`` as prescribed data (see :ref:`supported-prescribed-variables`). This can be considered as the representative depth for tracer concentration and the depth over which the deposition flux is removed.

If deposition fluxes (rather than deposition velocities) are to be calculated (see :nml:mem:`l_deposition_flux`), the concentrations of atmospheric tracer species need to be prescribed (see ``tracer_field`` in :ref:`supported-prescribed-variables`).


``JULES_DEPOSITION_SPECIES`` namelist members
---------------------------------------------

.. nml:namelist:: JULES_DEPOSITION_SPECIES

This namelist should occur :nml:mem:`JULES_DEPOSITION::ndry_dep_species` times, with each occurence containing parameters for an atmospheric tracer species that is to be considered in dry deposition.

.. nml:member:: dep_species_name_io

   :type: character
   :default: none

   Name of an atmospheric tracer species to be included in deposition modelling.


.. nml:member:: dep_species_rmm_io

   :type: real
   :default: none

   Relative molecular mass (g mol\ :sup:`-1`), as used in the UKCA. It is used in the calculation of the quasi-laminar resistance term (R\ :sub:`b`), if no diffusion coefficient is provided.


.. nml:member:: diffusion_coeff_io

   :type: real
   :default: none

   Diffusion coefficient (m\ :sup:`-2` s\ :sup:`-1`).

   .. note:: If there is no measured value of the diffusion coefficient for any chemical species in the chemical mechanism, the diffusion coefficient for those species should be set to -1.0. This will be used to indicate that the diffusion coefficient will be calculated from the diffusion coefficient of water and the relative molecular masses of water and the chemical species.


.. nml:member:: rsurf_std_io

   :type: real(ntype)
   :default: none

   Standard value of surface resistance for each surface type (s m\ :sup:`-1`).


.. nml:group:: Only used if :nml:mem:`dep_species_name_io` = ``NO2``, ``O3``, ``PAN``, ``PPAN``, ``MPAN`` or ``ONITU``. Values provided for other species will be ignored.

   .. nml:member:: diffusion_corr_io

      :type: real
      :default: none

      Diffusion correction factor for stomatal resistance, accounting for the different diffusivities of water and other species (dimensionless).


.. nml:group:: Only used if :nml:mem:`dep_species_name_io` = ``CO``, ``NO2``, ``O3``, ``PAN``, ``PPAN``, ``MPAN`` or ``ONITU``. Values provided for other species will be ignored.

   .. nml:member:: r_tundra_io

      :type: real
      :default: none

      Surface resistance used in tundra region (s m\ :sup:`-1`).


.. nml:group:: Only used if :nml:mem:`dep_species_name_io` = ``HNO3``, ``HONO2``, ``ISON`` and if :nml:mem:`JULES_TEMP_FIXES::l_fix_improve_drydep` = true, also for ``HCl``, ``HOCl``, ``HBr`` or ``HOBr``.

   .. nml:member:: dd_ice_coeff_io

      :type: real(3)
      :default: none

      Coefficients in quadratic function relating dry deposition over ice to temperature.


``JULES_DEPOSITION_SPECIES_SPECIFIC`` namelist members
------------------------------------------------------

.. nml:namelist:: JULES_DEPOSITION_SPECIES_SPECIFIC

This namelist is used for deposition parameters specific to a single deposited species. This namelist is used to avoid redundant entries on the :nml:lst:`JULES_DEPOSITION_SPECIES` namelists.

.. nml:group:: Deposition parameters specific to :nml:mem:`JULES_DEPOSITION_SPECIES::dep_species_name_io` = ``CH4``.

   .. nml:member:: ch4_scaling_io

      :type: real
      :default: none

      Scaling applied to methane soil uptake (dimensionless). (Originally this was used to match the value from the IPCC Third Assessment Report.)


   .. nml:member:: ch4_mml_io

      :type: real
      :default: none

      Factor used in UKCA to convert the methane soil uptake flux in (\ |mu|\ g m\ :sup:`-2` h\ :sup:`-1`) to a dry dep velocity (in m s\ :sup:`-1`). The current value of ch4_mml_io = 3600.0 * 0.016 * 1.0 x 10\ :sup:`9` * 1.75 x 10\ :sup:`-6` = 1.008 x 10\ :sup:`5`, where 0.016 is the relative molecular mass of methane (kg), 1.0 x 10\ :sup:`9` converts \ |mu|\ g to kg, and 1.75 x 10\ :sup:`-6` ppmv is the assumed mean global atmospheric volume mixing ratio of methane.


   .. nml:member:: ch4dd_tundra_io

      :type: real(4)
      :default: none

      Coefficients of cubic polynomial relating methane loss for tundra to temperature. Flux is in units of \ |mu|\ g (CH\ :sub:`4`) m\ :sup:`-2` s\ :sup:`-1`.


   .. nml:member:: ch4_up_flux_io

      :type: real(ntype)
      :default: none

      Value of uptake flux for methane for each surface type (\ |mu|\ g (CH\ :sub:`4`) m\ :sup:`-2` s\ :sup:`-1`).


.. nml:group:: Deposition parameters specific to :nml:mem:`JULES_DEPOSITION_SPECIES::dep_species_name_io` = ``H2``.


   .. nml:member:: h2dd_c_io

      :type: real(ntype)
      :default: none

      Constant in quadratic function relating hydrogen deposition to soil moisture (s m\ :sup:`-1`).


   .. nml:member:: h2dd_m_io

      :type: real(ntype)
      :default: none

      Coefficient of first order term in quadratic function relating hydrogen deposition to soil moisture (s m\ :sup:`-1`).


   .. nml:member:: h2dd_q_io

      :type: real(ntype)
      :default: none

      Coefficient of second order term in quadratic function relating hydrogen deposition to soil moisture (s m\ :sup:`-1`).


.. nml:group:: Deposition parameters specific to :nml:mem:`JULES_DEPOSITION_SPECIES::dep_species_name_io` = ``O3``.


   .. nml:member:: cuticle_o3_io

      :type: real
      :default: none

      Constant for calculation of cuticular resistance for ozone (s m\ :sup:`-1`).


   .. nml:member:: r_wet_soil_o3_io

      :type: real
      :default: none

      Wet soil surface resistance for ozone (s m\ :sup:`-1`).


Example
~~~~~~~

The following gives an example of how you would set up the :nml:lst:`JULES_DEPOSITION` namelist for atmospheric deposition for a JULES standalone run. ::

 [namelist:jules_deposition]
 dry_dep_model=2
 dzl_const=50.0
 l_deposition=.true.
 l_deposition_flux=.false.
 l_deposition_from_ukca=.false.
 l_deposition_gc_corr=.false.
 l_ukca_ddep_lev1=.false.
 !!l_ukca_ddepo3_ocean=.false.
 !!l_ukca_dry_dep_so2wet=.false.
 l_ukca_emsdrvn_ch4=.false.
 ndry_dep_species=7
 tundra_s_limit=0.866

Note: :nml:mem:`JULES_DEPOSITION::l_deposition_from_ukca` should be false for JULES standalone and true for UM-coupled JULES. :nml:mem:`JULES_DEPOSITION::l_ukca_ddepo3_ocean` and :nml:mem:`JULES_DEPOSITION::l_ukca_dry_dep_so2wet` are not available for JULES standalone applications.

The following gives an example of how to set-up the :nml:lst:`JULES_DEPOSITION_SPECIES` and :nml:lst:`JULES_DEPOSITION_SPECIES_SPECIFIC` for the standard 5 pft/9 tile configuration for a single chemical species 'O3'. In general, there will be ndry_dep_species :nml:lst:`JULES_DEPOSITION_SPECIES` namelists, one for each atmospheric species that is deposited. Some deposition parameters are required for all chemical species, others are species specific and not available (e.g. dd_ice_coeff for ``O3``). ::

 [namelist:jules_deposition_species(1)]
 !!dd_ice_coeff_io=-13.57,6841.9,-857410.6
 dep_species_name_io='O3'
 dep_species_rmm_io=48.0
 diffusion_coeff_io=1.400000e-05
 diffusion_corr_io=1.6
 r_tundra_io=800.0
 rsurf_std_io=200.0,200.0,200.0,200.0,400.0,800.0,2200.0,800.0,2500.0

 [namelist:jules_deposition_species_specific]
 ch4_mml_io=1.008e5
 ch4_scaling_io=15.0
 ch4_up_flux_io=39.5,50.0,30.0,37.0,27.5,0.0,0.0,27.5,0.0
 ch4dd_tundra_io=-4.757e-6,4.0288e-3,-1.13592,106.636
 cuticle_o3_io=5000.0
 h2dd_c_io=0.00197,0.00197,0.00177,1.2346,0.0001,0.0,0.0,0.0,0.0
 h2dd_m_io=-0.00419,-0.00419,-0.00414,-0.472,5*0.0
 h2dd_q_io=0.0,0.0,0.0,0.27,5*0.0
 r_wet_soil_o3_io=500.0

.. |mu| unicode:: &#x03BC; .. u
