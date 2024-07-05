``jules_soil_biogeochem.nml``
=============================


This file sets options and parameters for soil biogeochemistry.

If using the single-pool or 4-pool soil models, all soil parameters are read from this file.

If using the ECOSSE soil model, most soil parameters are read from a separate file (:ref:`jules-soil-ecosse-namelist`).



``JULES_SOIL_BIOGEOCHEM`` namelist members
------------------------------------------

.. nml:namelist:: JULES_SOIL_BIOGEOCHEM


.. nml:member:: soil_bgc_model

   :type: integer
   :permitted: 1, 2 or 3
   :default: 1

   Choice for model of soil biogeochemistry.

   Possible values are:

   1. | A single-pool model of soil carbon turnover in which the pool is not prognostic (not updated).
      | This must be used when the TRIFFID vegetation model is not selected (:nml:mem:`JULES_VEGETATION::l_triffid` = FALSE).

   2. | A 4-pool model of soil organic carbon and nitrogen, originally based on the Jenkinson (1990) model, with a single pool of inorganic N.
      | Historically this was bundled with the TRIFFID vegetation model.
      | This can only be used if the TRIFFID vegetation model is selected (:nml:mem:`JULES_VEGETATION::l_triffid` = TRUE).

   3. | A 4-pool model of soil organic carbon and nitrogen, and 2 inorganic N pools (ammonium and nitrate), based on the ECOSSE model (Smith et al., 2010).
      | This can only be used if the TRIFFID vegetation model is selected (:nml:mem:`JULES_VEGETATION::l_triffid` = TRUE).
      | This can also be run without nitrogen (:nml:mem:`JULES_SOIL_ECOSSE::l_soil_n` = FALSE).

   .. warning::
      The ECOSSE model in JULES is still in development and is not fully functional in this version. The code is included to allow further development. Users should not try to use ECOSSE.

   .. seealso::
      References:

      * Jenkinson, D.S., 1990. The turnover of organic carbon and nitrogen in soil. Philosophical Transactions of the Royal Society of London. Series B: Biological Sciences, 329(1255), pp.361-368. (https://doi.org/10.1098/rstb.1990.0177)

      * Smith et al., 2010, Estimating changes in Scottish soil carbon stocks using ECOSSE. I. Model description and uncertainties, Climate Research, 45: 179-192. (https://doi.org/10.3354/cr00899).


.. nml:group:: Parameters that can be used with all soil models

   .. nml:member:: q10_soil

      :type: real
      :default: 2.0

      Q10 factor for soil respiration.

      With the single-pool or 4-pool models this is only used if :nml:mem:`l_q10` = TRUE.

      With the ECOSSE model this is only used if :nml:mem:`JULES_SOIL_ECOSSE::temp_modifier` = 1.

      See Hadley Centre Technical Note 24, Eq.17, available from `the Met Office Library <http://www.metoffice.gov.uk/learning/library/publications/science/climate-science-technical-notes>`_.


.. nml:group:: Parameters for the single-pool model (only used if :nml:mem:`soil_bgc_model` = 1)

   .. nml:member:: kaps

      :type: real
      :default: 0.5e-8

      Specific soil respiration rate at 25 degC and optimum soil moisture (s\ :sup:`-1`).

      See Hadley Centre Technical Note 24, Eq.16, available from `the Met Office Library <http://www.metoffice.gov.uk/learning/library/publications/science/climate-science-technical-notes>`_.


.. nml:group:: Parameters for the single-pool and 4-pool models (only used if :nml:mem:`soil_bgc_model` = 1 or 2)

   .. nml:member:: l_q10

      :type: logical
      :default: T

      Switch for use of Q10 approach when calculating soil respiration.

      TRUE
          Use Q10 approach (Equation 65 in Clark et al., 2011).

         .. note:: This is always enforced if the single-pool model is selected (:nml:mem:`soil_bgc_model` = 1) and was used in JULES2.0.

      FALSE
          Use the approach of Jenkinson (1990) (Equation 66 in Clark et al., 2011).

      .. seealso::
         References:

         * Jenkinson, D.S., 1990. The turnover of organic carbon and nitrogen in soil. Philosophical Transactions of the Royal Society of London. Series B: Biological Sciences, 329(1255), pp.361-368. (https://doi.org/10.1098/rstb.1990.0177)

         * Clark, D. B., Mercado, L. M., Sitch, S., Jones, C. D., Gedney, N., Best, M. J., Pryor, M., Rooney, G. G., Essery, R. L. H., Blyth, E., Boucher, O., Harding, R. J., Huntingford, C., and Cox, P. M.: The Joint UK Land Environment Simulator (JULES), model description – Part 2: Carbon fluxes and vegetation dynamics, Geosci. Model Dev., 4, 701–722, (https://doi.org/10.5194/gmd-4-701-2011), 2011.

   .. nml:member:: l_soil_resp_lev2

      :type: logical
      :default: F

      Switch affecting the temperature and moisture used for soil respiration calculation.

      TRUE
          Temperature and total (frozen+unfrozen) moisture content of the second soil layer are used.

      FALSE
          Temperature and unfrozen moisture content of the first (topmost) soil layer are used.

          .. note:: If layered soil C is used (:nml:mem:`l_layeredc` = TRUE) the temperature and moisture of each soil layer is used to calculation respiration from that layer.



.. nml:group:: Parameters for the 4-pool model (only used if :nml:mem:`soil_bgc_model` = 2)

   .. nml:member:: l_layeredc

      :type: logical
      :default: F

      Switch for using the layered soil carbon model.

      If the 4-pool model is used (:nml:mem:`soil_bgc_model` = 2) this uses the approach of Burke et al. (2017) and two extra parameters are required: :nml:mem:`tau_resp`, :nml:mem:`tau_lit`.

      Layered soil nitrogen is also available if the nitrogen cycle is switched on (:nml:mem:`JULES_VEGETATION::l_nitrogen` = TRUE), but this is a highly experimental version which needs further evaluation and so should be used with extreme caution. One additional parameter is required for layered soil nitrogen: :nml:mem:`diff_n_pft`.

      TRUE
         The number and thickness of layers in the soil carbon model are set equal to those in the soil moisture model (:nml:lst:`JULES_SOIL`).

      FALSE
         There are no specific layers in the soil carbon model (a single, bulk pool).

      .. seealso::
         References:

         * Burke, E. J., Chadburn, S. E., and Ekici, A.: A vertical representation of soil carbon in the JULES land surface scheme (vn4.3_permafrost) with a focus on permafrost regions, Geosci. Model Dev., 10, 959-975, doi:10.5194/gmd-10-959-2017, 2017.
	   
   .. nml:member:: l_label_frac_cs

      :type: logical
      :default: F

      Switch for labelling and tracing a subset of the layered soil carbon (:nml:mem:`l_layeredc` = TRUE). It uses the approach of Burke et al.(2017). This requires the 4-pool model to be used (:nml:mem:`soil_bgc_model` = 2). The fraction of labelled soil carbon needs to be specified as part of the model's initial state.

      TRUE
         A user-defined fraction of soil carbon is labelled.

      FALSE
         None of the soil carbon is labelled.

      .. seealso::
         References:

         * Burke, E. J., Chadburn, S. E., and Ekici, A.: A vertical representation of soil carbon in the JULES land surface scheme (vn4.3_permafrost) with a focus on permafrost regions, Geosci. Model Dev., 10, 959-975, doi:10.5194/gmd-10-959-2017, 2017. 

   .. nml:member:: kaps_4pool

      :type: real(4)
      :default: 3.22e-7, 9.65e-9, 2.12e-8, 6.43e-10

      Specific soil respiration rate for the 4-pool submodel for each soil carbon pool (decomposable plant material, resistant plant material, biomass, humus).


   .. nml:member:: bio_hum_cn

      :type: real
      :default: 10.0

      Parameter controlling ratio of C to N for BIO and HUM pools.


   .. nml:member:: sorp

      :type: real
      :default: 10.0

      Parameter controlling the leaching of inorganic N through the soil profile. A factor of 1 means that in a timestep all the inorganic N is available for leaching. The default value of 10 means that 10% of inorganic N is available for leaching.


   .. nml:member:: n_inorg_turnover

      :type: real
      :default: 1.0

      Parameter controlling the lifetime of the inorganic N pool. A value of 1 implies the whole pool will turnover in 360 days.


   .. nml:member:: tau_resp

      :type: real
      :default: 2.0

      Parameter controlling decay of respiration with depth (m-1). Only used with layered soil carbon (:nml:mem:`l_layeredc` = TRUE).


   .. nml:member:: diff_n_pft

      :type: real
      :default: 5.0

      Parameter controlling the rate of re-filling of the available inorganic nitrogen pool (1/360 days). This parameter determines how quickly the inorganic nitrogen reaches the roots after the roots uptake from the soil around them. This should be quicker than the turnover rate of inorganic nitrogen. In addition, it has to be small compared with the triffid timestep (360/triffid_period) otherwise the available inorganic nitrogen becomes unstable. Hence the choice of the default value 5. Only used with layered soil carbon and nitrogen scheme (:nml:mem:`l_layeredc` = TRUE and :nml:mem:`JULES_VEGETATION::l_nitrogen` = TRUE). When :nml:mem:`JULES_VEGETATION::l_trif_eq` = TRUE or :nml:mem:`JULES_SOIL_BIOGEOCHEM::diff_n_pft` is greater than (0.5 * 360 / :nml:mem:`JULES_VEGETATION::triffid_period`) then all of the inorganic nitrogen pool is deemed to be available.


   .. nml:member:: z_burn_max

      :type: real
      :default: 0.2

      Parameter controlling the depth to which fire burns soil litter carbon in metres. At depths shallower than this value, the fire can burn soil carbon in the two litter pools (dpm and rpm). If z_burn_max falls within a layer only a proportion of the soil carbon is burnt. Only used with layered soil carbon scheme (:nml:mem:`l_layeredc` = TRUE) and fire (either :nml:mem:`JULES_VEGETATION::l_trif_fire` or :nml:mem:`JULES_VEGETATION::l_inferno` or both). In reality the burn depth varies so please check whether the default value of 0.2 is suitable for your application. 


.. nml:group:: Parameters for the 4-pool- or ECOSSE-based models (only used if :nml:mem:`soil_bgc_model` = 2 or 3):

   .. nml:member:: tau_lit

      :type: real
      :default: 5.0

      Parameter controlling the decay of litter with depth (m-1).
      With 4-pool, this is only used with layered soil carbon (:nml:mem:`l_layeredc` = TRUE).
      With ECOSSE, this is only used with :nml:mem:`JULES_SOIL_ECOSSE::plant_input_profile` = 2.

.. nml:group:: Methane parameters and switches. Can only be used with the single-pool and 4-pool models (:nml:mem:`soil_bgc_model` = 1 or 2).

   .. warning::
      Some parameters may need to be re-tuned for different soil biogeochemistry models.

   .. nml:member:: l_ch4_tlayered

      :type: logical
      :default: F

      Switch to calculate methane emissions based on layered soil temperature.

      TRUE
        Methane emission is calculated from layered soil temperatures.

      FALSE
        Methane emission is calculated from top 1m average soil temperature (default).

   .. nml:member:: l_ch4_interactive

      :type: logical
      :default: F

      Switch to couple the methane emission into the carbon cycle. In order to use this the methane must be calculated from layered soil temperature (:nml:mem:`l_ch4_tlayered` = TRUE).

      TRUE
        Methane flux is subtracted from soil carbon stocks.

      FALSE
        Methane emission is only diagnostic (default).

   .. nml:member:: l_ch4_microbe

      :type: logical
      :default: F

      Switch to enable the microbial methane production scheme (represents the dynamics of methanogens and a dissolved substrate pool). See Chadburn et al. (2020).

      .. note:: This will only be applied to the methane production from your chosen :nml:mem:`ch4_substrate`. The scheme has been calibrated with :nml:mem:`ch4_substrate` = 1.

      TRUE
        Microbial dynamics simulated in methane scheme.

      FALSE
        No microbial dynamics, decomposition of substrate translates immediately to methane emissions.

   .. nml:member:: ch4_substrate

      :type: integer
      :permitted: 1, 2 or 3
      :default: 1

      Choice of substrate for wetland methane. This controls the calculation method for the methane flux that is used to update soil carbon (only if :nml:mem:`l_ch4_interactive` = TRUE) and to populate the variable fch4_wetl (seen by the atmospheric model in coupled mode).

      Possible values are:

      1. | Using soil carbon as substrate (default).
      2. | Using NPP as substrate.
      3. | Using soil respiration as substrate.

      This replaces the previous switch l_wetland_ch4_npp.

   .. nml:member:: t0_ch4

      :type: real
      :default: 273.15

      Reference temperature for the Q10 function CH4 emission calculation

   .. nml:member:: const_ch4_cs

      :type: real
      :default: 7.41e-12

      Scale factor for wetland CH4 emissions when soil carbon is taken as the substrate for ch4 emissions (:nml:mem:`ch4_substrate` = 1)

      .. note:: In the UM the recommended value depends on :nml:mem:`JULES_VEGETATION::l_triffid` as follows:

	| :nml:mem:`JULES_VEGETATION::l_triffid` = FALSE, :nml:mem:`const_ch4_cs` = 5.41e-12
	| :nml:mem:`JULES_VEGETATION::l_triffid` = TRUE, :nml:mem:`const_ch4_cs` = 5.41e-10

   .. nml:member:: q10_ch4_cs

      :type: real
      :default: 3.7

      Q10 value for wetland CH4 emissions when soil carbon is taken as the substrate for ch4 emissions (:nml:mem:`ch4_substrate` = 1)

   .. nml:member:: const_ch4_npp

      :type: real
      :default: 9.99e-3

      Scale factor for wetland CH4 emissions when NPP is taken as the substrate for ch4 emissions (:nml:mem:`ch4_substrate` = 2)

   .. nml:member:: q10_ch4_npp

      :type: real
      :default: 1.5

      Q10 value for wetland CH4 emissions when npp is taken as the substrate for ch4 emissions (:nml:mem:`ch4_substrate` = 2)

   .. nml:member:: const_ch4_resps

      :type: real
      :default: 4.36e-3

      Scale factor for wetland CH4 emissions when soil respiration is taken as the substrate for ch4 emissions  (:nml:mem:`ch4_substrate` = 3)

   .. nml:member:: q10_ch4_resps

      :type: real
      :default: 1.5

      Q10 value for wetland CH4 emissions when soil respiration is taken as the substrate for ch4 emissions (:nml:mem:`ch4_substrate` = 3)

   .. nml:member:: ch4_cpow

      :type: real
      :default: 1.0

      Power of soil carbon used to calculate methane emissions with soil carbon as substrate (:nml:mem:`ch4_substrate` = 1). Methane production is calculated as cs\ :sup:`ch4_cpow`. A value of 1.0 is default, but a value of 2/3 is consistent with an assumption that only the surfaces of the organic matter are accessible.

      .. note::  :nml:mem:`const_ch4_cs` will need retuning if this parameter is changed.

.. nml:group:: Methane parameters only used with layered soil temperatures (:nml:mem:`l_ch4_tlayered` = TRUE).

   .. nml:member:: tau_ch4

      :type: real
      :default: 6.5

      Exponent in the exponential decline of methane emissions with soil depth (m-1).
      This empirically represents methane oxidation/emission processes, which only allow a fraction of the methane produced in the soil to reach the atmosphere.

.. nml:group:: Methane parameters only used with microbial methane scheme (:nml:mem:`l_ch4_microbe` = TRUE).

   .. nml:member:: k2_ch4

      :type: real
      :default: 0.01

      Baseline methanogenic respiration rate (hr-1).

   .. nml:member:: kd_ch4

      :type: real
      :default: 0.0003

      Baseline methanogenic mortality rate (hr-1).

   .. nml:member:: rho_ch4

      :type: real
      :default: 47.0

      Factor in substrate limitation function (related to half saturation of substrate for methanogenic respiration) ( (mgC/m3)-1 ).

   .. nml:member:: q10_mic_ch4

      :type: real
      :default: 4.3

      Q10 factor for methanogens.

   .. nml:member:: cue_ch4

      :type: real
      :default: 0.03

      Carbon use efficiency of methanogenic growth.

   .. nml:member:: mu_ch4

      :type: real
      :default: 0.00042

      Threshold growth rate below which methanogens die (hr-1).

   .. nml:member:: frz_ch4

      :type: real
      :default: 0.5

      Factor to reduce CH4 substrate production when soil is sufficiently frozen (only in microbial scheme).

   .. nml:member:: alpha_ch4

      :type: real
      :default: 0.001

      Ratio between maintenance and growth respiration rates for methanogens.

   .. nml:member:: ev_ch4

      :type: real
      :default: 5.0

      Timescale over which methanogenic traits adapt to temperature change (yr)

   .. nml:member:: q10_ev_ch4

      :type: real
      :default: 2.2

      Q10 for temperature response of methanogenic traits under adaptation

.. seealso::
      Reference for microbial methane scheme:

   * Chadburn, S. E. et al (2020),
     Modeled Microbial Dynamics Explain the Apparent Temperature Sensitivity 
     of Wetland Methane Emissions. Global Biogeochemical Cycles, 34:
     e2020GB006678. `https://doi.org/10.1029/2020GB006678
     <https://doi.org/10.1029/2020GB006678>`_
