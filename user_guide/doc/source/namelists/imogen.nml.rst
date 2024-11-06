``imogen.nml``
==============


This file contains three namelists called :nml:lst:`IMOGEN_ONOFF_SWITCH`, :nml:lst:`IMOGEN_RUN_LIST` and :nml:lst:`IMOGEN_ANLG_VALS_LIST`. Values from this section are only used if IMOGEN is enabled. This is done via the following switch: :nml:mem:`IMOGEN_ONOFF_SWITCH::l_imogen` = TRUE.

Since IMOGEN calculates the forcing for an entire year at once, an IMOGEN run must have a start time of 00:00:00 on the 1st of January for some year.

IMOGEN uses the netcdf read functions in JULES to load the driving data. The required driving data is specific humidity (kg/kg), precipitation (kg/m2/s), wind speed (m/s), incoming shortwave radiation (W/m2), incoming longwave radiation (W/m2), air temeprature (K) and diurnal range of air temperature (K). IMOGEN also needs ``grid_area`` read in via :nml:lst:`JULES_LATLON`. 

The meteorological driving data used for IMOGEN are at monthly resolution. IMOGEN requires a monthly climatology and then can use either anomalies from that climatology (:nml:mem:`IMOGEN_RUN_LIST::anlg` set to FALSE and :nml:mem:`IMOGEN_RUN_LIST::anom` set to TRUE) or spatial patterns of changes in each meteorological driving variable per degree of global temperature change (:nml:mem:`IMOGEN_RUN_LIST::anlg` set to TRUE and :nml:mem:`IMOGEN_RUN_LIST::anom` set to TRUE). Patterns can be derived at the required spatial resolution using ESMValTool <https://esmvaltool.org/>.

IMOGEN still reads the 1d data from ascii files within the code - this will change in the near future.

.. seealso::
   References:

   * Huntingford, C. and P. M. Cox (2000),
     An analogue model to derive additional climate change scenarios
     from existing GCM simulations, Climate Dynamics 16(8): 575-586.
     https://doi.org/10.1007/s003820000067
   * Huntingford, C., et al. (2010), 
     IMOGEN: an intermediate complexity model to evaluate terrestrial
     impacts of a changing climate,
     Geoscientific Model Development 3(2): 679-687.
     https://doi.org/10.5194/gmd-3-679-2010
   * Comyn-Platt, E., et al. (2018),
     Carbon budgets for 1.5 and 2 C targets lowered by natural
     wetland and permafrost feedbacks,
     Nature Geoscience 11(8): 568-573.
     https://doi.org/10.1038/s41561-018-0174-9
   * Zelazowski, P., et al. (2018),
     Climate pattern-scaling set for an ensemble of 22 
     GCMs–adding uncertainty to the IMOGEN version 2.0 impact system,
     Geoscientific Model Development 11.2: 541-560.
     https://doi.org/10.5194/gmd-11-541-2018

``IMOGEN_ONOFF_SWITCH`` namelist members
----------------------------------------

.. nml:namelist:: IMOGEN_ONOFF_SWITCH


.. nml:member:: l_imogen

   :type: logical
   :default: F

   Switch for IMOGEN.

   TRUE
       IMOGEN is used to generate meteorological forcing data and drive JULES.

   FALSE
       No effect.
    
   .. note::
      If IMOGEN is enabled, at most only :nml:mem:`JULES_DRIVE::z1_tq_vary`, :nml:mem:`JULES_DRIVE::z1_tq_in`, :nml:mem:`JULES_DRIVE::z1_uv_in`, :nml:mem:`JULES_DRIVE::z1_tq_file` and :nml:mem:`JULES_DRIVE::z1_tq_var_name` are used from the :nml:lst:`JULES_DRIVE` namelist.


``IMOGEN_RUN_LIST`` namelist members
------------------------------------

.. nml:namelist:: IMOGEN_RUN_LIST


.. nml:member:: co2_init_ppmv

   :type: real
   :default: 286.085

   Initial CO2 concentration (ppmv).


.. nml:member:: file_scen_emits

   :type: character
   :default: None

   If used, file containing CO2 emissions.

   This file is expected to be in a specific format - see the IMOGEN example.


.. nml:member:: file_non_co2_radf

   :type: character
   :default: None

   If used, file containing non-CO2 radiative forcing values.

   This file is expected to be in a specific format - see the IMOGEN example.
   

.. nml:member:: nyr_non_co2

   :type: integer
   :default: 21

   Number of years for which non-co2 forcing is prescribed.


.. nml:member:: file_scen_co2_ppmv

   :type: character
   :default: None

   If used, file containing CO2 concentration (ppmv).

   This file is expected to be in a specific format - see the IMOGEN example.


.. nml:member:: ch4_init_ppbv

   :type: real
   :default: 774.1

   Initial CH4 concentration (ppbv).

   Only if :nml:mem:`land_feed_ch4` = TRUE.


.. nml:member:: yr_fch4_ref

   :type: real
   :default: 2000

   Year for reference wetland CH4 emissions and atmospheric CH4 decay rate, i.e. :nml:mem:`fch4_ref`, :nml:mem:`tau_ch4_ref` & :nml:mem:`ch4_ppbv_ref`.

   Only if :nml:mem:`land_feed_ch4` = TRUE.


.. nml:member:: ch4_ppbv_ref

   :type: real
   :default: 1751.02

   Reference atmosphere CH4 concentration at :nml:mem:`yr_fch4_ref` (ppbv).

   Only if :nml:mem:`land_feed_ch4` = TRUE.


.. nml:member:: tau_ch4_ref

   :type: real
   :default: 8.4

   Lifetime of CH4 in atmosphere at :nml:mem:`yr_fch4_ref` (years). Value used in Gedney et al. (2004) S3 (Table 1) from TAR, Table 4.3 (subscript d).

   Only if :nml:mem:`land_feed_ch4` = TRUE.


.. nml:member:: fch4_ref

   :type: real
   :default: 180.0

   Reference wetland CH4 emissions for reference year :nml:mem:`yr_fch4_ref` (Tg CH4/yr).

   Only if :nml:mem:`land_feed_ch4` = TRUE.


.. nml:member:: file_ch4_n2o

   :type: character
   :default: None

   File containing the CH4 and N2O atmos concs. The number of years in this file is defined by :nml:mem:`nyr_ch4_n2o`. This file is expected to be an ascii file with three columns: the first column is the year, the second column is the CH4 concentration (ppbv) and the third column is the N2O concentration (ppbv). There is one row for each year and no header.

   Only if :nml:mem:`land_feed_ch4` = TRUE.


.. nml:member:: nyr_ch4_n2o

   :type: integer
   :default: 241

   Number of years of CH4 and N2O data in :nml:mem:`file_ch4_n2o`.

   Only if :nml:mem:`land_feed_ch4` = TRUE.


.. nml:member:: anlg

   :type: logical
   :default: T

   If TRUE, then use the GCM analogue model.


.. nml:member:: anom

   :type: logical
   :default: T

   If TRUE, then incorporate anomalies.


.. nml:member:: c_emissions

   :type: logical
   :default: T

   If TRUE, CO2 concentration is calculated.


.. nml:member:: include_co2

   :type: logical
   :default: T

   If TRUE, include adjustments to CO2 values.


.. nml:member:: include_non_co2_radf

   :type: logical
   :default: T

   If TRUE, include adjustments to non-CO2 radiative forcing.


.. nml:member:: l_drive_with_global_temps

   :type: logical
   :default: F

   If TRUE, use imogen to provide jules forcing based on the global mean temperature change and the climate patterns.



.. nml:member:: land_feed_co2

   :type: logical
   :default: F

   If TRUE, include land CO2 feedbacks on atmospheric CO2.


.. nml:member:: land_feed_ch4

   :type: logical
   :default: F

   If TRUE, include wetland CH4 feedbacks on atmospheric CH4. Prescribed CH4 concentrations assume a non-varying natural wetland CH4 component. However, when :nml:mem:`land_feed_ch4` = TRUE the constant wetland CH4 emissions are perturbed using the anomaly in modelled natural wetland CH4 emission. The methane emissions are calculated for the diagnosed wetland area when :nml:mem:`JULES_HYDROLOGY::l_top` = TRUE. These are accumulated and passed to IMOGEN.

   To ensure consistency with the observed atmospheric CH4 growth rate the model needs to be calibrated to produce :nml:mem:`fch4_ref` TgCh4 per year (default 180) for the year  :nml:mem:`yr_fch4_ref` (default 2000). This is done by calibrating q10_ch4 (either :nml:mem:`JULES_SOIL_BIOGEOCHEM::q10_ch4_cs`, :nml:mem:`JULES_SOIL_BIOGEOCHEM::q10_ch4_npp`, :nml:mem:`JULES_SOIL_BIOGEOCHEM::q10_ch4_resps`, depending on whether cs, npp or resps is defined as the substrate by :nml:mem:`JULES_SOIL_BIOGEOCHEM::ch4_substrate`) and const_ch4 (either :nml:mem:`JULES_SOIL_BIOGEOCHEM::const_ch4_cs`, :nml:mem:`JULES_SOIL_BIOGEOCHEM::const_ch4_npp`, :nml:mem:`JULES_SOIL_BIOGEOCHEM::const_ch4_resps`, again depending on whether cs, npp or resps is defined as the substrate  by :nml:mem:`JULES_SOIL_BIOGEOCHEM::ch4_substrate`). The calibration can be carried out as discussed in Comyn-Platt et al. (2018) and needs to be checked before proceeding because the model won't necessarily produce the correct values by default.

   For wetland CH4 feedbacks values for the following: :nml:mem:`fch4_ref`, :nml:mem:`tau_ch4_ref`, :nml:mem:`ch4_ppbv_ref`, :nml:mem:`yr_fch4_ref`, :nml:mem:`ch4_init_ppbv`, :nml:mem:`file_ch4_n2o`, and :nml:mem:`nyr_ch4_n2o` are also required.

   .. seealso::
      References:

      * Gedney, N., Cox, P. M. & Huntingford, C. Climate feedback from wetland methane emissions. Geophys. Res. Lett. 31, L20503 (2004). https://doi.org/10.1029/2004GL020919

      * Comyn-Platt, E., et al. (2018),
        Carbon budgets for 1.5 and 2 C targets lowered by natural
        wetland and permafrost feedbacks,
        Nature Geoscience 11(8): 568-573.
        https://doi.org/10.1038/s41561-018-0174-9


.. nml:member:: ocean_feed

   :type: logical
   :default: F

   If TRUE, include ocean feedbacks on atmospheric CO2.


.. nml:member:: nyr_emiss

   :type: integer
   :default: 241

   Number of years of emission data in file.


.. nml:member:: initialise_from_dump

   :type: logical
   :default: F

   Indicates how the IMOGEN prognostic variables will be initialised.

   TRUE
       Use a dump file (specified in :nml:mem:`dump_file` below) from a previous run with IMOGEN to initialise the IMOGEN prognostics.

   FALSE
       IMOGEN will handle the initialisation of its prognostics internally.


.. nml:member:: dump_file

   :type: character
   :default: None

   The name of the dump file to initialise from.

   Only used if :nml:mem:`initialise_from_dump` = TRUE.




``IMOGEN_ANLG_VALS_LIST`` namelist members
------------------------------------------

.. nml:namelist:: IMOGEN_ANLG_VALS_LIST


.. nml:member:: diff_frac_const_imogen

   :type: real
   :default: 0.4

   IMOGEN uses this instead of :nml:mem:`JULES_DRIVE::diff_frac_const`


.. nml:member:: q2co2

   :type: real
   :default: 3.74

   Radiative forcing due to doubling CO2 (W m\ :sup:`-2`).


.. nml:member:: f_ocean

   :type: real
   :default: 0.711

   Fractional coverage of the ocean.


.. nml:member:: kappa_o

   :type: real
   :default: 383.8

   Ocean eddy diffusivity (W m\ :sup:`-1` K\ :sup:`-1`).


.. nml:member:: lambda_l

   :type: real
   :default: 0.52

   Inverse of climate sensitivity over land (W m\ :sup:`-2` K\ :sup:`-1`).


.. nml:member:: lambda_o

   :type: real
   :default: 1.75

   Inverse of climate sensitivity over ocean (W m\ :sup:`-2` K\ :sup:`-1`).


.. nml:member:: mu

   :type: real
   :default: 1.87

   Ratio of land to ocean temperature anomalies.


.. nml:member:: t_ocean_init

   :type: real
   :default: 289.28

   Initial ocean temperature (K).


.. nml:member:: file_patt

   :type: character
   :default: None

   Netcdf file containing the patterns.  It should be monthly data (12 months total) with the dimension 'imogen_drive' representing time. 


.. nml:member:: file_clim

   :type: character
   :default: None

   Netcdf file containing initialising climatology. It should be monthly data (12 months total) with the dimension 'imogen_drive' representing time.


.. nml:member:: file_base_anom

   :type: character
   :default: None

   Netcdf files containing prescribed anomalies. There should be one for each year and should be in the form 'file_base_anom' followed by 'year' (4 digits) and '.nc'




