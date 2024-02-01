``pft_params.nml``
==================

This file sets the time and space-invariant parameters for plant functional types for the JULES land surface model. It contains one namelist called :nml:lst:`JULES_PFTPARM`.

.. note::
   If the crop model is on (i.e. :nml:mem:`JULES_SURFACE_TYPES::ncpft` > 0), the order of PFTs must be natural PFTs followed by crop PFTs.


``JULES_PFTPARM`` namelist members
----------------------------------

.. nml:namelist:: JULES_PFTPARM

This namelist reads the values of parameters for each of the plant functional types (PFTs) if the JULES land surface model is being used. These parameters are a function of PFT only. Parameters that also vary with time and location can be prescribed in :doc:`prescribed_data.nml`. Parameters that are only required if the dynamic vegetation (TRIFFID) or phenology sections are requested are read separately in :doc:`triffid_params.nml`. Every member must be given a value for every run.

HCTN24 and 30 refer to Hadley Centre technical notes 24 and 30,
available from `the Met Office Library
<http://www.metoffice.gov.uk/learning/library/publications/science/climate-science-technical-notes>`_. For
ease the direct links to these documents are:

* `HCTN24 "Description of the "TRIFFID" Dynamic Global Vegetation Model" <https://digital.nmla.metoffice.gov.uk/IO_cc8f146a-d524-4243-88fc-e3a3bcd782e7>`_
* `HCTN30 "MOSES 2.2 technical documentation" <https://digital.nmla.metoffice.gov.uk/IO_7f434aa4-338e-497c-8e66-23488d2e1bd3>`_

.. nml:member:: canht_ft_io

   :type: real(npft)
   :default: None

   The height of each PFT (m), also known as the canopy height.

   The value read here is only used if TRIFFID is not active (:nml:mem:`JULES_VEGETATION::l_triffid` = FALSE).

   .. note:: If TRIFFID is active, canopy height is a prognostic variable and its initial value is read in :doc:`initial_conditions.nml`.


.. nml:member:: lai_io

   :type: real(npft)
   :default: None

   The leaf area index (LAI) of each PFT.

   The value read here is only used if neither phenology nor TRIFFID is active (:nml:mem:`JULES_VEGETATION::l_phenol` = FALSE and :nml:mem:`JULES_VEGETATION::l_triffid` = FALSE).

   .. note:: If phenology is active, LAI is a prognostic variable and its initial value is read in :doc:`initial_conditions.nml`. When TRIFFID is active but phenology is not active (not recommended), LAI is calculated from the canopy height (meaning that the seasonal cycle of LAI will not be correctly represented).


.. nml:member:: c3_io

   :type: integer(npft)
   :default: None

   Flag indicating whether PFT is C3 type.

   0. Not C3 (i.e. C4).

   1. C3.


.. nml:member:: orient_io

   :type: integer(npft)
   :default: None

   Flag indicating leaf angle distribution.

   0. Spherical.

   1. Horizontal.


.. nml:member:: can_struct_a_io

   :type: real(npft)
   :default: None

   Canopy structure factor (dimensionless). can_struct_a_io=1.0 indicates a structurally homogeneous canopy. Corresponds to the structure factor Zeta in Pinty et al 2006 except assumed not to vary with zenith angle i.e. b=0. The canopy structure factor has no effect if :nml:mem:`JULES_VEGETATION::can_rad_mod` = 1.

.. nml:member:: a_wl_io

   :type: real(npft)
   :default: None

   Allometric coefficient relating the target woody biomass to the
   leaf area index (kg carbon m\ :sup:`-2`)  (Clark et al., 2011; Table 7)


.. nml:member:: a_ws_io

   :type: real(npft)
   :default: None

   Woody biomass as a multiple of live stem biomass (Clark et al., 2011; Table 7).


.. nml:member:: albsnc_max_io

   :type: real(npft)
   :default: None

   Snow-covered albedo for large leaf area index.

   Only used if :nml:mem:`JULES_RADIATION::l_snow_albedo` = FALSE. See HCTN30 Eq.2.


.. nml:member:: albsnc_min_io

   :type: real(npft)
   :default: None

   Snow-covered albedo for zero leaf area index.

   Only used if :nml:mem:`JULES_RADIATION::l_snow_albedo` = FALSE. See HCTN30 Eq.2.


.. nml:member:: albsnf_max_io

   :type: real(npft)
   :default: None

   Snow-free albedo for large LAI.

   Only used if :nml:mem:`JULES_RADIATION::l_spec_albedo` = FALSE. See HCTN30 Eq.1.


.. nml:member:: albsnf_maxu_io

   :type: real(npft)
   :default: None

   Upper bound for the snow-free albedo for large LAI, when scaled to match input obs.

   Only used if :nml:mem:`JULES_RADIATION::l_spec_albedo` = FALSE and :nml:mem:`JULES_RADIATION::l_albedo_obs` = TRUE.


.. nml:member:: albsnf_maxl_io

   :type: real(npft)
   :default: None

   Lower bound for the snow-free albedo for large LAI, when scaled to match input obs.

   Only used if :nml:mem:`JULES_RADIATION::l_spec_albedo` = FALSE and :nml:mem:`JULES_RADIATION::l_albedo_obs` = TRUE.


.. nml:member:: alpha_io

   :type: real(npft)
   :default: None

   Quantum efficiency of photosynthesis (mol CO\ :sub:`2` per mol PAR photons).


.. nml:member:: alnir_io

   :type: real(npft)
   :default: None

   Leaf reflection coefficient for NIR. See HCTN30 Table 3.

   Always used unless :nml:mem:`JULES_VEGETATION::can_rad_mod` = 1 and
   :nml:mem:`JULES_RADIATION::l_spec_albedo` = FALSE.


.. nml:member:: alniru_io

   :type: real(npft)
   :default: None

   Upper limit for the leaf reflection coefficient for NIR, when
   :nml:mem:`JULES_RADIATION::l_albedo_obs` = TRUE and when
   :nml:mem:`alnir_io` is used.


.. nml:member:: alnirl_io

   :type: real(npft)
   :default: None

   Lower limit for the leaf reflection coefficient for NIR, when
   :nml:mem:`JULES_RADIATION::l_albedo_obs` = TRUE and when
   :nml:mem:`alnir_io` is used.


.. nml:member:: alpar_io

   :type: real(npft)
   :default: None

   Leaf reflection coefficient for VIS (photosyntehtically active radiation). See HCTN30 Table 3.

   Always used unless :nml:mem:`JULES_VEGETATION::can_rad_mod` = 1 and
   :nml:mem:`JULES_RADIATION::l_spec_albedo` = FALSE.


.. nml:member:: alparu_io

   :type: real(npft)
   :default: None

   Upper limit for the leaf reflection coefficient for VIS, when
   :nml:mem:`JULES_RADIATION::l_albedo_obs` = TRUE and when
   :nml:mem:`alpar_io` is used.


.. nml:member:: alparl_io

   :type: real(npft)
   :default: None

   Lower limit for the leaf reflection coefficient for VIS, when
   :nml:mem:`JULES_RADIATION::l_albedo_obs` = TRUE and when
   :nml:mem:`alpar_io` is used.


.. nml:member:: b_wl_io

   :type: real(npft)
   :default: None

   Allometric exponent relating the target woody biomass to the leaf
   area index. This is 5/3 in HCTN24 Eq.8. See also Clark et
   al. (2011, Table 7).


.. nml:member:: catch0_io

   :type: real(npft)
   :default: None

   Minimum canopy capacity (kg m\ :sup:`-2`).

   This is the minimum amount of water that can be held on the canopy. See HCTN30 p7.


.. nml:member:: dcatch_dlai_io

   :type: real(npft)
   :default: None

   Rate of change of canopy capacity with LAI (kg m\ :sup:`-2`).

   Canopy capacity is calculated as ``catch0 + dcatch_dlai*lai``. See HCTN30 p7.


.. nml:member:: dgl_dm_io

   :type: real(npft)
   :default: None

   Rate of change of leaf turnover rate with moisture availability.


.. nml:member:: dgl_dt_io

   :type: real(npft)
   :default: None

   Rate of change of leaf turnover rate with temperature (K\ :sup:`-1`).

   This is 9 in HCTN24 Eq.10.


.. nml:member:: dqcrit_io

   :type: real(npft)
   :default: None

   Critical humidity deficit (kg H\ :sub:`2`\ O per kg air).

   Only used with the Jacobs model of stomatal conductance (:nml:mem:`JULES_VEGETATION::stomata_model` = 1).


.. nml:member:: dz0v_dh_io

   :type: real(npft)
   :default: None

   Rate of change of vegetation roughness length for momentum with height.

   Roughness length is calculated as ``dz0v_dh * canht_ft``. See HCTN30 p5.

   Used if logical :nml:mem:`JULES_VEGETATION::l_spec_veg_z0` is set to .false.

.. nml:member:: z0v_io

   :type: real(npft)
   :default: None

   Specified values for the vegetation roughness length for momentum.

   Used if logical :nml:mem:`JULES_VEGETATION::l_spec_veg_z0` is set to .true.


.. nml:member:: eta_sl_io

   :type: real(npft)
   :default: None

   Live stemwood coefficient (kg C/m/(m2 leaf)) (Clark et al., 2011; Table 7).


.. nml:member:: fd_io

   :type: real(npft)
   :default: None

   Scale factor for dark respiration. See HCTN 24 Eq. 56.


.. nml:member:: fsmc_of_io

   :type: real(npft)
   :default: None

   Moisture availability below which leaves are dropped.


.. nml:member:: f0_io

   :type: real(npft)
   :default: None

   ``CI / CA`` for ``DQ = 0``. See HCTN 24 Eq. 32.

   Only used with the Jacobs model of stomatal conductance (:nml:mem:`JULES_VEGETATION::stomata_model` = 1).


.. nml:member:: g1_stomata_io

   :type: real(npft)
   :default: None

   Parameter g1 for the Medlyn et al. (2011) model of stomatal conductance (kPa\ :sup:`0.5`) - this is the sensitivity of the stomatal conductance to the assimilation rate. See Eqn.11 in Medlyn et al. (2012), https://doi.org/10.1111/j.1365-2486.2012.02790.x.

   Only used with the Medlyn model of stomatal conductance (:nml:mem:`JULES_VEGETATION::stomata_model` = 2).


.. nml:group:: Only used with the SOX (Eller et al. 2020) model of stomatal conductance (:nml:mem:`JULES_VEGETATION::stomata_model` = 3). A value is required for each PFT.


   .. nml:member:: sox_a_io

      :type: real(npft)
      :default: None

      The shape parameter in the xylem vulnerability curve.

   .. nml:member:: sox_p50_io

      :type: real(npft)
      :default: None

      Xlem water potential at which xylem hydraulic conductance is half its maximum value (MPa).

   .. nml:member:: sox_rp_min_io

      :type: real(npft)
      :default: None

      Plant minimum hydraulic resistance (m2 s MPa/mol).


.. nml:member:: g_leaf_0_io

   :type: real(npft)
   :default: None

   Minimum turnover rate for leaves (/360days).


.. nml:member:: glmin_io

   :type: real(npft)
   :default: None

   Minimum leaf conductance for H\ :sub:`2`\ O (m s\ :sup:`-1`).


.. nml:member:: infil_f_io

   :type: real(npft)
   :default: None

   Infiltration enhancement factor.

   The maximum infiltration rate defined by the soil parameters for the whole gridbox may be modified for each PFT to account for PFT-dependent factors, such as macro-pores related to vegetation roots.

   See HCTN30 p14 for full details.

.. nml:member:: gsoil_f_io

   :type: real(npft)
   :default: None

   Soil conductance enhancement factor.

   The soil conductance for soil under a PFT canopy may be modified for each PFT (as compared to the bare soil conductance) to account for PFT-dependent factors.

.. nml:member:: hw_sw_io

   :type: real(npft)
   :default: None

   Ratio of N stem to N heartwood (kgN/kgN) from the TRY database.

   Only used if :nml:mem:`JULES_VEGETATION::l_trait_phys` = T.


.. nml:member:: kext_io

   :type: real(npft)
   :default: None

   Light extinction coefficient - used with Beer's Law for light absorption through plant canopies. See HCTN30 Eq.3.


.. nml:member:: kpar_io

   :type: real(npft)
   :default: None

   PAR Extinction coefficient (m\ :sup:`2` leaf / m\ :sup:`2` ground).


.. nml:member:: lai_alb_lim_io

   :type: real(npft)
   :default: None

   Minimum LAI permitted in calculation of the albedo in snow-free conditions.


.. nml:member:: neff_io

   :type: real(npft)
   :default: None

   Scale factor relating V\ :sub:`cmax` with leaf nitrogen concentration. See HCTN 24 Eq. 51.

   Only used if :nml:mem:`JULES_VEGETATION::l_trait_phys` = F.


.. nml:member:: nl0_io

   :type: real(npft)
   :default: None

   Top leaf nitrogen concentration (kg N/kg C).

   Only used if :nml:mem:`JULES_VEGETATION::l_trait_phys` = F.


.. nml:member:: nr_nl_io

   :type: real(npft)
   :default: None

   Ratio of root nitrogen concentration to leaf nitrogen concentration.

.. nml:member:: nr_io

   :type: real(npft)
   :default: None

   Root nitrogen concentration  (kgN/kgC).
   Only used if :nml:mem:`JULES_VEGETATION::l_trait_phys` = T.

.. nml:member:: ns_nl_io

   :type: real(npft)
   :default: None

   Ratio of stem nitrogen concentration to leaf nitrogen concentration.

.. nml:member:: nsw_io

   :type: real(npft)
   :default: None

   Stemwood nitrogen concentration (kgN/kgC).
   Only used if :nml:mem:`JULES_VEGETATION::l_trait_phys` = T.

.. nml:member:: hw_sw_io

   :type: real(npft)
   :default: None

   Ratio of Heartwood to Stemwood Nitrogen Concentration (typically 0.5)
   Only used if :nml:mem:`JULES_VEGETATION::l_trait_phys` = T.

.. nml:member:: omega_io

   :type: real(npft)
   :default: None

   Leaf scattering coefficient for PAR.

   Always used unless :nml:mem:`JULES_VEGETATION::can_rad_mod` = 1 and
   :nml:mem:`JULES_RADIATION::l_spec_albedo` = FALSE.


.. nml:member:: omegau_io

   :type: real(npft)
   :default: None

   Upper limit for the leaf scattering coefficient for PAR, when
   :nml:mem:`JULES_RADIATION::l_albedo_obs` = TRUE and when
   :nml:mem:`omega_io` is used.


.. nml:member:: omegal_io

   :type: real(npft)
   :default: None

   Lower limit for the leaf scattering coefficient for PAR, when
   :nml:mem:`JULES_RADIATION::l_albedo_obs` = TRUE and when
   :nml:mem:`omega_io` is used.


.. nml:member:: omnir_io

   :type: real(npft)
   :default: None

   Leaf scattering coefficient for NIR.

   Always used unless :nml:mem:`JULES_VEGETATION::can_rad_mod` = 1 and
   :nml:mem:`JULES_RADIATION::l_spec_albedo` = FALSE.


.. nml:member:: omniru_io

   :type: real(npft)
   :default: None

   Upper limit for the leaf scattering coefficient for NIR, when
   :nml:mem:`JULES_RADIATION::l_albedo_obs` = TRUE and when
   :nml:mem:`omnir_io` is used.


.. nml:member:: omnirl_io

   :type: real(npft)
   :default: None

   Lower limit for the leaf scattering coefficient for NIR, when
   :nml:mem:`JULES_RADIATION::l_albedo_obs` = TRUE and when
   :nml:mem:`omnir_io` is used.


.. nml:member:: r_grow_io

   :type: real(npft)
   :default: None

   Growth respiration fraction.


.. nml:member:: fsmc_mod_io

   :type: integer(npft)
   :default: None

   Switch for method of weighting the contribution that different soil layers make to the soil moisture availability factor fsmc.

   0. (recommended) Calculate fsmc in each soil layer and take a weighted average, using the fraction of roots in each layer as weights. Root distribution e-folding depth is given by :nml:mem:`rootd_ft_io`.

   1. Calculate fsmc using average properties for the root zone. Depth of root zone is given by :nml:mem:`rootd_ft_io`. This is not currently allowed if layered soil C (:nml:mem:`JULES_SOIL_BIOGEOCHEM::l_layeredc` = TRUE) and the 4-pool model are selected (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2)  because of unplanned effects on litter inputs.


.. nml:member:: psi_open_io

   :type: real(npft)
   :default: None

   Soil potential above which the soil moisture stress factor on vegetation (fsmc) is one. Unit: Pa. Allowed range: must be negative. Only used if :nml:mem:`JULES_VEGETATION::l_use_pft_psi` = T.


.. nml:member:: psi_close_io

   :type: real(npft)
   :default: None

   Soil potential below which the soil moisture stress factor on vegetation (fsmc) is zero. Unit: Pa. Allowed range: must be negative. Only used if :nml:mem:`JULES_VEGETATION::l_use_pft_psi` = T.


.. nml:member:: rootd_ft_io

   :type: real(npft)
   :default: None

   Parameter determining the root depth (m).

   If :nml:mem:`fsmc_mod_io` = 0, an exponential root distribution with depth is assumed, with e-folding depth ``rootd_ft`` (see HCTN30 Eq.32). Note that this means that generally some of the roots exist at depths greater than ``rootd_ft``. If :nml:mem:`fsmc_mod_io` = 1, ``rootd_ft`` is the total depth of the root zone.


.. nml:member:: fsmc_p0_io

   :type: real(npft)
   :default: None

   Pft-dependent parameter governing the threshold at which the plant starts to experience water stress due to lack of water in the soil. Only used if :nml:mem:`JULES_VEGETATION::l_use_pft_psi` = F. The volumetric soil moisture content (m\ :sup:`3` water per m\ :sup:`3` soil) at which the plant starts to become water stressed is ``sm_wilt+(sm_crit-sm_wilt)*(1-fsmc_p0)`` (see :nml:lst:`JULES_SOIL_PROPS` for a description of ``sm_wilt`` and ``sm_crit``).


.. nml:member:: sigl_io

   :type: real(npft)
   :default: None

   Specific density of leaf carbon (kg C/m\ :sup:`2` leaf) (Clark et al., 2011; Table 7).

   Only used if :nml:mem:`JULES_VEGETATION::l_trait_phys` = F.


.. nml:member:: tleaf_of_io

   :type: real(npft)
   :default: None

   Temperature below which leaves are dropped (K).


.. nml:member:: tlow_io

   :type: real(npft)
   :default: None

   Lower temperature parameter for photosynthesis (deg C), for the Collatz model of leaf photosynthesis.

   Always used for C\ :sub:`4` plants. Only used for C\ :sub:`3` plants with the Collatz model of leaf photosynthesis (:nml:mem:`JULES_VEGETATION::photo_model` = 1).


.. nml:member:: tupp_io

   :type: real(npft)
   :default: None

   Upper temperature  parameter for photosynthesis (deg C), for the Collatz model of leaf photosynthesis.

   Always used for C\ :sub:`4` plants. Only used for C\ :sub:`3` plants with the Collatz model of leaf photosynthesis (:nml:mem:`JULES_VEGETATION::photo_model` = 1).


.. nml:member:: emis_pft_io

   :type: real(npft)
   :default: None

   Surface emissivity of vegetated surfaces.


.. nml:member:: z0hm_pft_io

   :type: real(npft)
   :default: None

   Ratio of the roughness length for heat to the roughness length for momentum.

   This is generally assumed to be 0.1. See HCTN30 p6. Note that this is the ratio of the roughness length for heat to that for momentum. It does not alter the roughness length for momentum, which is calculated using :nml:mem:`canht_ft_io` and :nml:mem:`dz0v_dh_io`.


.. nml:member:: z0hm_classic_pft_io

   :type: real(npft)
   :default: None

   Ratio of the roughness length for heat to the roughness length for momentum *for the CLASSIC aerosol scheme only*.

   .. note:: This makes no difference to the model when running standalone, and is only required to keep the standalone and UM interfaces consistent.


.. nml:member:: fl_o3_ct_io

   :type: real(npft)
   :default: None

   Critical flux of O3 to vegetation (nmol m\ :sup:`-2` s\ :sup:`-1`).


.. nml:member:: dfp_dcuo_io

   :type: real(npft)
   :default: None

   Plant type specific O3 sensitivity parameter (nmol\ :sup:`-1` m\ :sup:`2` s).


.. nml:member:: ief_io

   :type: real(npft)
   :default: None

   Isoprene Emission Factor (\ |mu|\ g g\ :sup:`-1` h\ :sup:`-1`).


.. nml:member:: tef_io

   :type: real(npft)
   :default: None

   Monoterpene Emission Factor (\ |mu|\ g g\ :sup:`-1` h\ :sup:`-1`).


.. nml:member:: mef_io

   :type: real(npft)
   :default: None

   Methanol Emission Factor (\ |mu|\ g g\ :sup:`-1` h\ :sup:`-1`).


.. nml:member:: aef_io

   :type: real(npft)
   :default: None

   Acetone Emission Factor (\ |mu|\ g g\ :sup:`-1` h\ :sup:`-1`).


.. nml:member:: ci_st_io

   :tybe: real(npft)
   :default: None

   Leaf-internal CO\ :sub:`2`\ concentration at standard conditions (Pa),

   .. note:: Standard conditions are: T = 303.15K, p = 1013.25 hPa, atmospheric CO\ :sub:`2` = 370 ppmv,  PAR = 1000 \ |mu|\ mol m\ :sup:`-2` s\ :sup:`-1`.


.. nml:member:: gpp_st_io

   :tybe: real(npft)
   :default: None

   Gross primary production (GPP) at standard conditions (kgC m\ :sup:`-2` s\ :sup:`-1`),

   .. note:: Standard conditions are: T = 303.15K, p = 1013.25 hPa, atmospheric CO\ :sub:`2` = 370 ppmv, PAR = 1000 \ |mu|\ mol m\ :sup:`-2` s\ :sup:`-1`.


.. nml:member:: nmass_io

   :type: real(npft)
   :default: None

   Top leaf nitrogen content per unit mass (kgN kgLeaf\ :sup:`-1`).

   Only used if :nml:mem:`JULES_VEGETATION::l_trait_phys` = T.


.. nml:member:: lma_io

   :type: real(npft)
   :default: None

   Leaf mass per unit area (kgLeaf m\ :sup:`-2`).

   Only used if :nml:mem:`JULES_VEGETATION::l_trait_phys` = T.


.. nml:member:: vint_io

   :type: real(npft)
   :default: None

   There is a linear relationship between Vcmax and Narea. Previously Vcmax was calculated as the product of nl0 and neff.

   This is now replaced by a linear regression based on data reported in Kattge et al. 2009. Vint is the y-intercept, vsl is the slope.

   Units: \ |mu|\ mol CO\ :sub:`2` m\ :sup:`-2` s\ :sup:`-1`.

   Only used if :nml:mem:`JULES_VEGETATION::l_trait_phys` = T.


.. nml:member:: vsl_io

   :type: real(npft)
   :default: None

   Slope in the linear regression between Vcmax and Narea.

   Units: \ |mu|\ mol CO\ :sub:`2` gN\ :sup:`-1` s\ :sup:`-1`.

   Only used if :nml:mem:`JULES_VEGETATION::l_trait_phys` = T.


.. nml:member:: kn_io

   :type: real(npft)
   :default: None.

   Parameter for decay of  nitrogen through the canopy, as a function of layers. Only used if :nml:mem:`JULES_VEGETATION::can_rad_mod` = 4 or 5.


.. nml:member:: knl_io

   :type: real(npft)
   :default: None.

   Parameter for decay of  nitrogen through the canopy, as a function of LAI. Only used if :nml:mem:`JULES_VEGETATION::can_rad_mod` = 6.


.. nml:member:: q10_leaf_io

   :type: real(npft)
   :default: None.

   Q10 factor for plant respiration.

   See Cox et al. (1999) Eq. 66.

   .. note:: Was previously a single parameter but now can have PFT-dependent values.


.. nml:member:: fef_co2_io

   :type: real(npft)
   :default: None

   Fire CO\ :sub:`2` Emission Factor (g kg\ :sup:`-1`).

.. nml:member:: fef_co_io

   :type: real(npft)
   :default: None

   Fire CO Emission Factor (g kg\ :sup:`-1`).

.. nml:member:: fef_ch4_io

   :type: real(npft)
   :default: None

   Fire CH\ :sub:`4` Emission Factor (g kg\ :sup:`-1`).

.. nml:member:: fef_nox_io

   :type: real(npft)
   :default: None

   Fire NOx Emission Factor (g kg\ :sup:`-1`).

.. nml:member:: fef_so2_io

   :type: real(npft)
   :default: None

   Fire SO\ :sub:`2` Emission Factor (g kg\ :sup:`-1`).

.. nml:member:: fef_oc_io

   :type: real(npft)
   :default: None

   Fire OC Emission Factor (g kg\ :sup:`-1`).

.. nml:member:: fef_bc_io

   :type: real(npft)
   :default: None

   Fire BC Emission Factor (g kg\ :sup:`-1`).

.. nml:member:: ccleaf_min_io

   :type: real(npft)
   :default: None

   Leaf minimum combustion completeness.

.. nml:member:: ccleaf_max_io

   :type: real(npft)
   :default: None

   Leaf maximum combustion completeness.

.. nml:member:: ccwood_min_io

   :type: real(npft)
   :default: None

   Wood minimum combustion completeness.

.. nml:member:: ccwood_max_io

   :type: real(npft)
   :default: None

   Wood maximum combustion completeness.

.. nml:member:: avg_ba_io

   :type: real(npft)
   :default: None

   Average PFT Burnt Area per fire (m\ :sup:`2`).

.. nml:member:: fire_mort_io

   :type: real(npft)
   :default: None

   Scaling factor for vegetation mortality caused by fire (from INFERNO burned area). Can be varied between 0.0 (no morality) and 1.0 (100% mortality) for each PFT.

   .. seealso::
      References:

      * Clark et al., 2011, The Joint UK Land Environment Simulator
	(JULES), model description – Part 2: Carbon fluxes and
	vegetation dynamics, Geosci. Model Dev., 4, 701-722,
	https://doi.org/10.5194/gmd-4-701-2011
      * Pinty, B., T. Lavergne, R. E. Dickinson,
	J.-L. Widlowski, N. Gobron, and M. M. Verstraete (2006),
	Simplifying the interaction of land surfaces with radiation
	for relating remote sensing products to climate
	models, J. Geophys. Res., 111, D02116,
	https://doi.org/10.1029/2005JD005952.


   


.. nml:group:: Only used with the Farquhar model of leaf photosynthesis (:nml:mem:`JULES_VEGETATION::photo_model` = 2). A value is required for each PFT, but only those for C\ :sub:`3` plants are used (since only C\ :sub:`3` plants use the Farquhar model). Below, J\ :sub:`max` is the potential rate of electron transport, and V\ :sub:`cmax` is the maximum rate of carboxylation of Rubisco.


   .. nml:member:: act_jmax_io

      :type: real(npft)
      :default: None

      Activation energy for temperature response of J\ :sub:`max` (J mol\ :sup:`-1`).


   .. nml:member:: act_vcmax_io

      :type: real(npft)
      :default: None

      Activation energy for temperature response of V\ :sub:`cmax` (J mol\ :sup:`-1`).

      .. note::
         :nml:mem:`act_jmax_io` and :nml:mem:`act_vcmax_io` are NOT required if thermal adaptation or acclimation of photosynthesis is selected (:nml:mem:`JULES_VEGETATION::photo_acclim_model` = 1, 2 or 3) together with :nml:mem:`JULES_VEGETATION::photo_act_model` = 2.


   .. nml:member:: alpha_elec_io

      :type: real(npft)
      :default: None

      Quantum yield of electron transport (mol electrons [mol\ :sup:`-1` PAR photons]).


   .. nml:member:: deact_jmax_io

      :type: real(npft)
      :default: None

      Deactivation energy for temperature response of J\ :sub:`max` (J mol\ :sup:`-1`). This describes the rate of decrease above the optimum temperature.


   .. nml:member:: deact_vcmax_io

      :type: real(npft)
      :default: None

      Deactivation energy for temperature response of V\ :sub:`cmax` (J mol\ :sup:`-1`). This describes the rate of decrease above the optimum temperature.


   .. nml:member:: jv25_ratio_io

      :type: real(npft)
      :default: None

      Ratio of J\ :sub:`max` to V\ :sub:`cmax` at 25 deg C (mol electrons [mol\ :sup:`-1` CO\ :sub:`2`]).

      .. note::
         If thermal adaptation or acclimation of photosynthesis is selected (:nml:mem:`JULES_VEGETATION::photo_acclim_model` = 1 or 2) together with :nml:mem:`JULES_VEGETATION::photo_jv_model` =2 (J\ :sub:`max`/V\ :sub:`cmax` calculated assuming constant total nitrogen allocation)), this value is used along with parameters :nml:mem:`JULES_VEGETATION::n_alloc_jmax` and :nml:mem:`JULES_VEGETATION::n_alloc_vcmax` to calculate the final value of J\ :sub:`max`/V\ :sub:`cmax`.


.. nml:group:: Only used if thermal adaptation or acclimation of photosynthetic capacity is NOT modelled (:nml:mem:`JULES_VEGETATION::photo_acclim_model` = 0). A value is required for each PFT, but only those for C\ :sub:`3` plants are used (since only C\ :sub:`3` plants use the Farquhar model).


   .. nml:member:: ds_jmax_io

      :type: real(npft)
      :default: None

      Entropy factor for temperature reponse of  J\ :sub:`max` (J mol\ :sup:`-1` K\ :sup:`-1`).


   .. nml:member:: ds_vcmax_io

      :type: real(npft)
      :default: None

      Entropy factor for temperature reponse of  V\ :sub:`cmax` (J mol\ :sup:`-1` K\ :sup:`-1`).

.. nml:group:: Only used if the respiration is modelled using the SUGAR carbohydrate model (:nml:mem:`JULES_VEGETATION::l_sugar` = T). A value is required for each PFT.


   .. nml:member:: sug_grec_io

      :type: real(npft)
      :default: None

      Specific structural carbon recycling rate (kg carbon m\ :sup:`-2` s\ :sup:`-1`).


   .. nml:member:: sug_g0_io

      :type: real(npft)
      :default: None

      Specific structural carbon production rate (kg carbon m\ :sup:`-2` s\ :sup:`-1`).

   .. nml:member:: sug_yg_io

      :type: real(npft)
      :default: None

      Growth yield for SUGAR model

.. |mu| unicode:: &#x03BC; .. u
