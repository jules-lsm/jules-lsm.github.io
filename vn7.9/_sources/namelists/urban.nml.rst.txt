``urban.nml``
=============


This file contains one namelist called :nml:lst:`JULES_URBAN`.

This section predominantly sets the options available for the two-tile urban scheme MORUSES. These namelists are only read if :nml:mem:`JULES_SURFACE::l_urban2t`, which requires both the :nml:mem:`JULES_SURFACE_TYPES::urban_canyon` and :nml:mem:`JULES_SURFACE_TYPES::urban_roof` surface types to be used. MORUSES provides parameters for: snow free canyon albedo (:nml:mem:`JULES_URBAN::l_moruses_albedo`), canyon emissivity (:nml:mem:`JULES_URBAN::l_moruses_emissivity`), roughness length for heat (:nml:mem:`JULES_URBAN::l_moruses_rough`), roughness length for momentum (:nml:mem:`JULES_URBAN::l_moruses_macdonald`) and thermal inertia (:nml:mem:`JULES_URBAN::l_moruses_storage`). Ancillary data, predominantly required for MORUSES, is read in via :nml:lst:`URBAN_PROPERTIES`.

For all other parameters that MORUSES does not provide, and for any MORUSES parametrisations that are turned off, values from :doc:`nveg_params.nml` will be used instead. See the switches below for more information.


   .. seealso::
      References:

      *   Porson, A., et al. (2010), Implementation of a new urban energy budget scheme in the MetUM. Part I: Description and idealized simulations, Quarterly Journal of the Royal Meteorological Society, 136: 1514-1529. doi: 10.1002/qj.668
      *   Porson, A., et al. (2010), Implementation of a new urban energy budget scheme into MetUM. Part II: Validation against observations and model Intercomparison, Quarterly Journal of the Royal Meteorological Society, 136: 1530-1542. doi: 10.1002/qj.572


``JULES_URBAN`` namelist members
-----------------------------------------

.. nml:namelist:: JULES_URBAN

.. nml:member:: anthrop_heat_scale

   :type: real
   :default: 1.0

   Distribution scaling factor, which allows the anthropogenic heat flux to be spread between the :nml:mem:`JULES_SURFACE_TYPES::urban_canyon` and :nml:mem:`JULES_SURFACE_TYPES::urban_roof` surface tiles such that:

   *   ``H_roof = anthrop_heat_scale x H_canyon``
   *   ``H_canyon x (W/R) + H_roof x ( 1.0 - W/R ) = anthrop_heat``

   Has a value between 0.0 and 1.0 where the extremes correspond to:

   *   0.0 = all released within the canyon.
   *   1.0 = evenly spread between canyon and roof.

   Only used if :nml:mem:`JULES_SURFACE::l_anthrop_heat_src` = TRUE.


.. nml:member:: l_moruses_albedo

   :type: logical
   :default: F

   MORUSES switch for effective canyon albedo parameterisation (snow free).

   Shortwave radiative exchange in the form of an effective canyon albedo, including shading and multiple reflections, which depends on building materials, geometry and zenith angle.

   TRUE
       Use MORUSES parameterisation. Requires that :nml:mem:`JULES_RADIATION::l_cosz` = TRUE. Also, check whether the data are provided in UTC or local solar time. To assume local solar time set :nml:mem:`JULES_TIME::l_local_solar_time` = TRUE.

   FALSE
       The snow free canyon albedo is taken from :nml:mem:`JULES_NVEGPARM::albsnf_nvg_io`.

   In all cases the snow covered albedo is :nml:mem:`JULES_NVEGPARM::albsnc_nvg_io`. MORUSES does not parameterise the roof albedo, so this is also taken from :nml:mem:`JULES_NVEGPARM::albsnf_nvg_io`.


.. nml:member:: l_moruses_emissivity

   :type: logical
   :default: F

   MORUSES switch for effective canyon emissivity parameterisation.

   Long-wave radiative exchange in the form of an effective canyon emissivity, including multiple reflections, which depends on building materials and geometry.

   TRUE
       Use MORUSES parameterisation.

   FALSE
       The canyon emissivity is taken from :nml:mem:`JULES_NVEGPARM::emis_nvg_io`.

   In either case, the roof emissivity is taken from :nml:mem:`JULES_NVEGPARM::emis_nvg_io`.


.. nml:member:: l_moruses_rough

   :type: logical
   :default: F

   MORUSES switch for effective roughness length for heat parameterisation.

   The effective roughness length for heat has a physical basis and is not calculated as a fraction of momentum. It depends on the geometry of the canyon, which affects the recirculation of the jet within the canyon. Flow within the canyon can be broken down into two regions; the recirculation and ventilation regions, where the recirculation region forms in the wake of each building. Three different flow regimes are represented:

   1. Isolated roughness - Canyon has separate recirculation and ventilation regions
   2. Wake interference - Recirculation region begins to impinge on the downstream building
   3. Skimming flow - Recirculation region fills the entire canyon

   | The effective roughness length for heat is calculated using a resistance network within these regions.

   TRUE
       Use MORUSES parameterisation for canyon and roof.

   FALSE
       Values for canyon and roof are taken from :nml:mem:`JULES_NVEGPARM::z0_nvg_io` and :nml:mem:`JULES_NVEGPARM::z0hm_nvg_io`.


.. nml:member:: l_moruses_storage

   :type: logical
   :default: F

   MORUSES switch for thermal inertia and coupling with the underlying soil for canyon and roof.

   MORUSES consists of two surfaces; a canyon (:nml:mem:`JULES_SURFACE_TYPES::urban_canyon`) and a roof (:nml:mem:`JULES_SURFACE_TYPES::urban_roof`). This MORUSES parametrisation calculates the heat capacity of each of these surface types and also modifies how they are coupled with the underlying soil. The heat capacities of the canyon and roof are calculated using the properties of the urban fabric and the geometry of the canyon. The roof has a lower thermal inertia and can respond more rapidly to changes in forcing. The nature of the coupling (radiative, conductive or none) is controlled via :nml:mem:`JULES_NVEGPARM::vf_nvg_io` as descibed below.

   **The canyon**:
   Consists of two walls and a road where the road only is coupled to the underlying soil. The walls are uncoupled and have a zero-flux boundary condition. The coupling of the road is therefore parametrised using a canyon scaling factor. The nature of the canyon (or road surface) coupling is specified as follows:

   :nml:mem:`JULES_NVEGPARM::vf_nvg_io` (:nml:mem:`JULES_SURFACE_TYPES::urban_canyon`):
       = =====================
       0 conductively coupled
       1 radiatively coupled
       = =====================

   **The roof**:
   As the roof is not in direct contact with the soil, it physically cannot be conductively coupled. It can either be radiatively coupled or uncoupled. To allow for no coupling, MORUSES modifies the code to change the meaning of conductively coupled to **NOT** coupled. The nature of the coupling is therefore specified as follows:

   :nml:mem:`JULES_NVEGPARM::vf_nvg_io` (:nml:mem:`JULES_SURFACE_TYPES::urban_roof`):
       = =====================
       0 **NOT** coupled
       1 radiatively coupled
       = =====================

   TRUE
       Use MORUSES parameterisation as described above.

   FALSE
       Values for canyon and roof are taken from :nml:mem:`JULES_NVEGPARM::ch_nvg_io` and :nml:mem:`JULES_NVEGPARM::vf_nvg_io` (with no modifications to coupling).


.. nml:member:: l_moruses_storage_thin

   :type: logical
   :default: F

   MORUSES switch to use a thin roof to simulate the effects of insulation.

   Only used if :nml:mem:`l_moruses_storage` = TRUE.

   TRUE
       Use thin, insulated roof.

   FALSE
       Use damping depth diffusivity of roofing materials.


.. nml:member:: l_moruses_macdonald

   :type: logical
   :default: F

   MORUSES switch for using MacDonald et al. (1998) to calculate effective roughness length of urban areas and displacement height from urban geometry.

   TRUE
       Use MacDonald et al. (1998) formulations.

   FALSE
       Appropriate data needs to be supplied instead.

   .. note:: If :nml:mem:`l_urban_empirical` = TRUE then :nml:mem:`l_moruses_macdonald` should also be TRUE, to keep the roughness length and displacement height consistent with the morphology.

   .. seealso::
      References:

      *   Macdonald RW, Griffiths RF, Hall D. 1998. An improved method for the estimation of surface roughness of obstacle arrays. Atmos. Env. 32: 1857-1864


.. nml:member:: l_urban_empirical

   :type: logical
   :default: F

   Switch to use empirical relationships for urban geometry, based on total urban fraction. Dimensions calculated are W/R, H/W and H.

   If no MORUSES parametrisations are used, i.e. the basic URBAN-2T, then only W/R is required.

   If the roof fraction is not supplied i.e. canyon fraction = total urban fraction, then W/R will be used to calculate the canyon and roof fractions. W/R is also used to distribute anthropogenic heat between the roof and the canyon if :nml:mem:`JULES_SURFACE::l_anthrop_heat_src` = TRUE.

   TRUE
       Use empirical relationships for urban geometry.

   FALSE
       Appropriate data needs to be supplied instead.

   .. warning:: These are only valid for high resolutions (~1 km).

   .. seealso::
      References:

      *   Bohnenstengel SI, Evans S, Clark P, Belcher SE (2010). Simulations of the London urban heat island, Quarterly Journal of the Royal Meteorological Society (submitted)
