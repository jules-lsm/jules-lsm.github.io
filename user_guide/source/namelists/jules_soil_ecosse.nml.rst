
.. _jules-soil-ecosse-namelist:

``jules_soil_ecosse.nml``
=============================


This file sets options and parameters for the ECOSSE model of soil biogeochemistry. It is used only if the ECOSSE model is chosen (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 3).

.. warning::
   The ECOSSE model in JULES is still in development and is not fully functional in this version. The code is included to allow further development. Users should not try to use ECOSSE.

.. seealso::
   References:

   * Smith et al., 2010, Estimating changes in Scottish soil carbon stocks using ECOSSE. I. Model description and uncertainties, Climate Research, 45: 179-192. (https://doi.org/10.3354/cr00899).

   * Clark, D. B., Mercado, L. M., Sitch, S., Jones, C. D., Gedney, N., Best, M. J., Pryor, M., Rooney, G. G., Essery, R. L. H., Blyth, E., Boucher, O., Harding, R. J., Huntingford, C., and Cox, P. M.: The Joint UK Land Environment Simulator (JULES), model description – Part 2: Carbon fluxes and vegetation dynamics, Geosci. Model Dev., 4, 701–722, (https://doi.org/10.5194/gmd-4-701-2011), 2011.


``JULES_SOIL_ECOSSE`` namelist members
------------------------------------------

.. nml:namelist:: JULES_SOIL_ECOSSE


.. nml:member:: l_soil_n

   :type: logical
   :default: T

   Switch to include soil nitrogen in ECOSSE.
   
   TRUE
      Model soil carbon and nitrogen.

   FALSE
      Model only soil carbon.


.. nml:member:: l_match_layers

   :type: logical
   :default: T

   Switch to match ECOSSE soil C and N layers to those for soil moisture.
   
   TRUE
      Use the same layering as for soil moisture. The number of soil carbon layers will equal :nml:mem:`JULES_SOIL::sm_levels`, with layer thicknesses given by :nml:mem:`JULES_SOIL::dzsoil_io`.

   FALSE
      The number of layers will be specified by :nml:mem:`dim_cslayer` and the thicknesses by :nml:mem:`dz_soilc_io`.


.. nml:member:: dim_cslayer

   :type: integer
   :permitted: >= 1
   :default: None

   The number of ECOSSE soil carbon layers. Not used if :nml:mem:`l_match_layers` = TRUE. Despite the similar name, this parameter is unrelated to :nml:mem:`JULES_INPUT_GRID::sclayer_dim_name`.


.. nml:member:: dz_soilc_io

   :type: real(dim_cslayer)
   :permitted: > 0
   :default: None

   Thicknesses of the ECOSSE soil carbon layers (m). Not used if :nml:mem:`l_match_layers` = TRUE. In most cases the total depth must equal that of the soil moisture layers (see :nml:mem:`JULES_SOIL::dzsoil_io`). The exception is the case of a single layer, bulk model (:nml:mem:`dim_cslayer` = 1), for which dz_soilc(1) is interpreted as the representative or averaging depth for the bulk layer (e.g. the temperature of the bulk model is taken as the average over this depth).


.. nml:member:: dt_soilc

   :type: REAL
   :permitted: >= :nml:mem:`JULES_TIME::timestep_len`
   :default: :nml:mem:`JULES_TIME::timestep_len`

   The timestep length for ECOSSE (seconds). The main JULES timestep length :nml:mem:`JULES_TIME::timestep_len` must be a multiple of this timestep length, so that ECOSSE is called on JULES timesteps. The TRIFFID timestep length :nml:mem:`JULES_VEGETATION::triffid_period` (converted to seconds) must also be a multiple of the ECOSSE timestep length.


.. nml:member:: l_driver_ave

   :type: logical
   :default: T

   Switch controlling the averaging of the physical driving variables that are input to ECOSSE (e.g. soil temperature).
   
   TRUE
      Average the driving variables over the ECOSSE timestep length.

   FALSE
      Use instantaneous values of the driving variables at the time when ECOSSE is called.

 
.. nml:member:: plant_input_profile

   :type: INTEGER
   :permitted: 1 or 2
   :default: 1

   Switch for the vertical distribution of litterfall inputs of C and N to the soil.
      
   Possible values are:

   1. | Fraction :nml:mem:`pi_sfc_frac` of inputs are distributed uniformly in a surface layer of depth :nml:mem:`pi_sfc_depth`, the remainder are distributed according to the distribution of roots.

   2. | Inputs decrease exponentially with depth with decay constant :nml:mem:`JULES_SOIL_BIOGEOCHEM::tau_lit`.


.. nml:member:: pi_sfc_frac

   :type: REAL
   :default: 0.3

   Fraction of plant litterfall that is added to the surface soil layer of depth :nml:mem:`pi_sfc_depth`. Only used if :nml:mem:`plant_input_profile` = 1.


.. nml:member:: pi_sfc_depth

   :type: REAL
   :default: 0.1

   Depth of soil over which fraction :nml:mem:`pi_sfc_frac` of plant litterfall is added (m). Only used if :nml:mem:`plant_input_profile` = 1.


.. nml:member:: temp_modifier

   :type: INTEGER
   :permitted: 1 or 2
   :default: 2

   Switch for the form of the temperature rate modifier for decomposition.

   1. | Use a Q10 approach (Eqn. 65 of Clark et al. (2011))

   2. | Use the Smith et al. (2010) form of the modifier (Eqn.1 of Smith et al. (2010))


.. nml:member:: water_modifier

   :type: INTEGER
   :permitted: 1 or 2
   :default: 2

   Switch for the form of the water rate modifier for decomposition and nitrification.

  1. | Use the Clark et al. (2011) form of the modifier (Eqn. 67 of Clark et al. (2011)). Note however that only the unfrozen water is considered here.

  2. | Use the Smith et al. (2010) form of the modifier.


.. nml:member:: decomp_rate

   :type: REAL(4)
   :default: 3.22e-7, 9.65e-9, 2.12e-8, 6.43e-10

   Rate constant for decomposition of each soil carbon pool (s\ :sup:`-1`).

   Note that these default values are also those for use with the 4-pool model (:nml:mem:`JULES_SOIL_BIOGEOCHEM::kaps_4pool`).


.. nml:member:: decomp_ph_rate_min

   :type: REAL
   :default: 0.2

   Minimum allowed value of pH rate modifier for decomposition.


.. nml:member:: decomp_ph_min

   :type: REAL
   :permitted: decomp_ph_min <= decomp_ph_max
   :default: 1.0

   Soil pH below which rate of decomposition is minimum.


.. nml:member:: decomp_ph_max

   :type: REAL
   :permitted: decomp_ph_max >= decomp_ph_min
   :default: 4.5

   Soil pH above which rate of decomposition is maximum.


.. nml:member:: decomp_temp_coeff_smith

   :type: REAL(3)
   :default: 47.9, 106.0, 18.3

   Constants in the 4-pool from of the decomposition temperature modifier (:nml:mem:`temp_modifier` = 2).

   Note that these default values are also those harwired in the code for use with the 4-pool model (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2, :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_q10` = F ).



.. nml:member:: decomp_wrate_min_smith

   :type: REAL
   :default: 0.2

   Minimum allowed value of the water rate modifier for decomposition when the 4-pool form is used (:nml:mem:`water_modifier` = 2).


.. nml:member:: decomp_wrate_min_clark

   :type: REAL
   :default: 0.2

   Minimum allowed value of the water rate modifier for decomposition when the Clark et al. (2011) form is used (:nml:mem:`water_modifier` = 1).

   Note that this default value is also that harwired in the code for use with the 4-pool model (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2).


.. nml:group:: Parameters for ECOSSE that are only used if soil N is included (:nml:mem:`l_soil_n` = TRUE).


   .. nml:member:: l_decomp_slow

      :type: logical
      :default: T

      Switch controlling how lack of nitrogen affects soil decomposition.
   
      TRUE
         Reduce the decomposition rate.

      FALSE
         Reduce the efficiency of decomposition, so that decomposition results in increased production of CO\ :sub:`2` and decreased production of further soil C. This is the approach used in the standalone version of ECOSSE.


   .. nml:member:: depo_nit_frac

      :type: REAL
      :permitted: 0 <= depo_nit_frac <= 1
      :default: 1.0

      The fraction of nitrogen deposition that is aded to the soil nitrate pool. The complement is aded to the ammonium pool.

	 
   .. nml:member:: bacteria_min_frac

      :type: REAL
      :permitted: 0 <= bacteria_min_frac <= 1
      :default: 0.2

      The minimum fraction of the decomposer community that are bacteria.


   .. nml:member:: bacteria_max_frac

      :type: REAL
      :permitted: bacteria_min_frac <= bacteria_max_frac <= 1
      :default: 0.5

      The maximum fraction of the decomposer community that are bacteria.


   .. nml:member:: bacteria_min_frac_pH

      :type: REAL
      :default: 4.0

      The soil pH at or below which the fraction of bacteria is at a minimum.


   .. nml:member:: bacteria_max_frac_pH

      :type: REAL
      :permitted: bacteria_min_frac_pH <= bacteria_max_frac_pH
      :default: 5.5

      The soil pH at or above which the fraction of bacteria is at a maximum.


   .. nml:member:: cn_bacteria

      :type: REAL
      :default: 5.5

      The C:N ratio of soil bacteria.


   .. nml:member:: cn_fungi

      :type: REAL
      :default: 5.5

      The C:N ratio of soil fungi.

   
   .. nml:member:: depth_nitrif

      :type: REAL
      :default: 0.25

      Greatest depth at which nitrification and denitrification are allowed (m).


   .. nml:member:: nitrif_rate

      :type: REAL
      :default: 9.921e-7

      Rate constant for nitrification (s\ :sup:`-1`).


   .. nml:member:: nitrif_wrate_min

      :type: REAL
      :default: 0.6

      Minimum allowed value of the water rate modifier for nitrification when 4-pool form is used. Only used if :nml:mem:`water_modifier` = 2.).


   .. nml:member:: nitrif_max_factor

      :type: REAL
      :default: 0.1

      Shape factor in rate modifier for nitrification (kg m\ :sup:`-3`).


   .. nml:member:: nitrif_frac_n2o_fc

      :type: REAL
      :permitted: 0 <= nitrif_frac_n2o_fc <= 1
      :default: 0.02

      Fraction of nitrification lost as N\ :sub:`2`\ O by partial nitrification at field capacity.


   .. nml:member:: nitrif_frac_gas

      :type: REAL
      :permitted: 0 <= nitrif_frac_gas <= 1
      :default: 0.02

      Fraction of nitrification lost as gas through full nitrification.


		  
   .. nml:member:: nitrif_frac_no

      :type: REAL
      :permitted: 0 <= nitrif_frac_no <= 1
      :default: 0.4

      Fraction of nitrification gas loss through full nitrification that is NO.


   .. nml:member:: denit50

      :type: REAL
      :default: 0.033

      Amount of nitrate at which denitrification rate is 50% of the potential rate (kg m\ :sup:`-3`).


   .. nml:member:: denit_bio_factor

      :type: REAL
      :default: 0.005

      Factor in denitrification calculation to convert flux of CO\ :sub:`2` into a representation of biological activity (m\ :sup:`2` kg\ :sup:`-1`).
	 

   .. nml:member:: denit_frac_n2_fc

      :type: REAL
      :permitted: 0 <= denit_frac_n2_fc <= 1
      :default: 0.55

      Proportion of denitrified N that becomes N\ :sub:`2` when soil moisture is at field capacity.
	 

   .. nml:member:: denit_nitrate_equal

      :type: REAL
      :default: 0.4

      Amount of N in soil nitrate at which denitrified N is released as equal amounts of N\ :sub:`2` and N\ :sub:`2`O (kg m\ :sup:`-3`).
	 

   .. nml:member:: denit_water_coeff

      :type: REAL(3)
      :default: 0.62, 0.38, 1.74 

      Constants describing water modifier for denitrification.
	 

   .. nml:member:: amm_leach_min

      :type: REAL
      :default: 0.02

      Minimum allowed amount of N in soil ammonium after leaching (kg m\ :sup:`-3`).
	 

   .. nml:member:: n_inorg_max_conc

      :type: REAL
      :default: -1.0

      Maximum-allowed concentration of inorganic N in a layer (kg m\ :sup:`-3`). A value less than zero means no maximum concentration is imposed.
