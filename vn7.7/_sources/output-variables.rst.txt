.. _output_variables_section:

JULES Output variables
======================


Variables that are available for output from JULES are listed in this section, separated according to the broad area of science. If a variable cannot be found, users should also check in related sections.

.. note::
   Most variables are output on the full model grid (even for variables defined on land points only).

   Most river variables are output on the river routing model grid, which is a 1D grid defined on the valid river routing points only. These are indicated by names ending in ``_rp`` and have a single spatial dimension of size ``np_rivers``. A regridded version of some river variables can also be output on the full model grid."

   Any points on the grid for which a variable is not defined with be filled with a missing data value.

   Any variables also available on soil tiles are indicated next to their non-soil-tiled analogues, e.g. ``var[_soilt]``, in which case they have an additional dimension of size ``nsoilt``.

   All variables include a land point dimension, unless specified otherwise.

   The sizes of dimensions are indicated in the tables below using links to other sections of this documentation, wherever possible. Other sizes are discussed in the table below.

.. tabularcolumns:: |p{2.5cm}|p{12.0cm}|

+-----------------+--------------------------------------------------------------------------------------------------------+
| Name            | Description                                                                                            |
+=================+========================================================================================================+
| ``ch4layer``    | Number of soil methane layers.                                                                         |
|                 |                                                                                                        |
|                 | Equals :nml:mem:`JULES_SOIL::sm_levels` if :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_ch4_tlayered` = TRUE,    |
|                 | otherwise = 1.                                                                                         |
+-----------------+--------------------------------------------------------------------------------------------------------+
| ``cslayer``     | Number of layers for soil carbon and nitrogen.                                                         |
|                 |                                                                                                        |
|                 | With the single-pool soil model (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 1),                |
|                 | ``cslayer`` = 1.                                                                                       |
|                 |                                                                                                        |
|                 | With 4-pool model (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2),                              |
|                 | if :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_layeredc` = TRUE ``cslayer`` = :nml:mem:`JULES_SOIL::sm_levels`, |
|                 | otherwise ``cslayer`` = 1.                                                                             |
|                 |                                                                                                        |
|                 | With the ECOSSE model (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 3),                          |
|                 | ``cslayer`` = :nml:mem:`JULES_SOIL_ECOSSE::dim_cslayer`.                                               |
+-----------------+--------------------------------------------------------------------------------------------------------+
| ``cspool``      | Number of soil carbon pools.                                                                           |
|                 |                                                                                                        |
|                 | =1 with the single-pool soil model (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 1).             |
|                 |                                                                                                        |
|                 | =4 with the 4-pool or ECOSSE models (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2 or 3).       |
+-----------------+--------------------------------------------------------------------------------------------------------+
| ``land+sea``    | Variable is available on all points (land and sea).                                                    |
+-----------------+--------------------------------------------------------------------------------------------------------+
| ``ncpft``       | Number of crop plant functional types - see :nml:mem:`JULES_SURFACE_TYPES::ncpft`.                     |
+-----------------+--------------------------------------------------------------------------------------------------------+
| ``npft``        | Number of plant functional types - see :nml:mem:`JULES_SURFACE_TYPES::npft`.                           |
+-----------------+--------------------------------------------------------------------------------------------------------+
| ``ns_deep``     | The number of levels in the thermal-only bedrock - see :nml:mem:`JULES_SOIL::ns_deep`.                 |
+-----------------+--------------------------------------------------------------------------------------------------------+
| ``nsmax``       | Maximum-allowed number of snow layers - see :nml:mem:`JULES_SNOW::nsmax`.                              |
+-----------------+--------------------------------------------------------------------------------------------------------+
| ``nsoilt``      | Number of soil tiles.                                                                                  |
|                 | ``nsurft`` if :nml:mem:`JULES_SOIL::l_tile_soil` = TRUE, otherwise 1.                                  |
+-----------------+--------------------------------------------------------------------------------------------------------+
| ``nsurft``      | Number of surface tiles.                                                                               |
|                 | 1 if :nml:mem:`JULES_SURFACE::l_aggregate` = TRUE, otherwise ``ntype``.                                |
+-----------------+--------------------------------------------------------------------------------------------------------+
| ``ntype``       | Number of surface types,                                                                               |
|                 | = :nml:mem:`JULES_SURFACE_TYPES::npft` + :nml:mem:`JULES_SURFACE_TYPES::nnvg`                          |
+-----------------+--------------------------------------------------------------------------------------------------------+
| ``sm_levels``   | Number of soil layers (for soil moisture) - see :nml:mem:`JULES_SOIL::sm_levels`.                      |
+-----------------+--------------------------------------------------------------------------------------------------------+



Meteorology
-------------------------------------------------------------------

Unlesss stated otherwise these variables have values at both land and sea points.

.. tabularcolumns:: |p{2.5cm}|p{10.8cm}|p{2.2cm}|

+---------------------+----------------------------------------------------------------------+-------------+
| Name                | Description                                                          | Dimensions  |
+=====================+======================================================================+=============+
| ``precip``          | Gridbox precipitation rate (kg m\ :sup:`-2` s\ :sup:`-1`).           |             |
+---------------------+----------------------------------------------------------------------+-------------+
| ``rainfall``        | Gridbox rainfall rate (kg m\ :sup:`-2` s\ :sup:`-1`).                |             |
+---------------------+----------------------------------------------------------------------+-------------+
| ``snowfall``        | Gridbox snowfall rate (kg m\ :sup:`-2` s\ :sup:`-1`).                |             |
+---------------------+----------------------------------------------------------------------+-------------+
| ``con_rain``        | Gridbox convective rainfall (kg m\ :sup:`-2` s\ :sup:`-1`).          |             |
+---------------------+----------------------------------------------------------------------+-------------+
| ``con_snow``        | Gridbox convective snowfall (kg m\ :sup:`-2` s\ :sup:`-1`).          |             |
+---------------------+----------------------------------------------------------------------+-------------+
| ``ls_rain``         | Gridbox large-scale rainfall (kg m\ :sup:`-2` s\ :sup:`-1`).         |             |
+---------------------+----------------------------------------------------------------------+-------------+
| ``ls_snow``         | Gridbox large-scale snowfall (kg m\ :sup:`-2` s\ :sup:`-1`).         |             |
+---------------------+----------------------------------------------------------------------+-------------+
| ``pstar``           | Gridbox surface pressure (Pa).                                       |             |
+---------------------+----------------------------------------------------------------------+-------------+
| ``q1p5m_gb``        | Gridbox specific humidity at 1.5m height (kg kg\ :sup:`-1`).         |             |
+---------------------+----------------------------------------------------------------------+-------------+
| ``qw1``             | Gridbox specific humidity (total water content) (kg kg\ :sup:`-1`).  |             |
+---------------------+----------------------------------------------------------------------+-------------+
| ``q1p5m``           | Tile specific humidity at 1.5m over land tiles (kg kg\ :sup:`-1`).   | land,nsurft |
+---------------------+----------------------------------------------------------------------+-------------+
| ``lw_down``         | Gridbox surface downward LW radiation (W m\ :sup:`-2`).              |             |
+---------------------+----------------------------------------------------------------------+-------------+
| ``sw_down``         | Gridbox surface downward SW radiation (W m\ :sup:`-2`).              |             |
+---------------------+----------------------------------------------------------------------+-------------+
| ``t1p5m_gb``        | Gridbox temperature at 1.5m height (K).                              |             |
+---------------------+----------------------------------------------------------------------+-------------+
| ``t1p5m``           | Tile temperature at 1.5m over land tiles (K).                        | land,nsurft |
+---------------------+----------------------------------------------------------------------+-------------+
| ``tl1``             | Gridbox ice/liquid water temperature (K).                            |             |
+---------------------+----------------------------------------------------------------------+-------------+
| ``u1``              | Gridbox westerly wind component (m s\ :sup:`-1`).                    |             |
+---------------------+----------------------------------------------------------------------+-------------+
| ``u10m``            | Gridbox westerly wind component at 10 m height (m s\ :sup:`-1`).     |             |
+---------------------+----------------------------------------------------------------------+-------------+
| ``v1``              | Gridbox southerly wind component (m s\ :sup:`-1`).                   |             |
+---------------------+----------------------------------------------------------------------+-------------+
| ``v10m``            | Gridbox southerly wind component at 10m height (m s\ :sup:`-1`).     |             |
+---------------------+----------------------------------------------------------------------+-------------+
| ``wind``            | Gridbox wind speed (m s\ :sup:`-1`).                                 |             |
+---------------------+----------------------------------------------------------------------+-------------+



Radiation
-------------------------------------------------------------------

.. tabularcolumns:: |p{3.0cm}|p{10.3cm}|p{2.2cm}|

+---------------------+-------------------------------------------------------------------------+------------+
| Name                | Description                                                             | Dimensions |
+=====================+=========================================================================+============+
| Albedos and emissivities                                                                                   |
+---------------------+-------------------------------------------------------------------------+------------+
| ``albedo_land``     | Gridbox albedo (as used to calculate net shortwave radiation) (-).      |            |
+---------------------+-------------------------------------------------------------------------+------------+
| ``alb_tile_1``      | Tile land albedo, waveband 1 (direct beam visible).                     | nsurft     |
+---------------------+-------------------------------------------------------------------------+------------+
| ``alb_tile_2``      | Tile land albedo, waveband 2 (diffuse visible).                         | nsurft     |
+---------------------+-------------------------------------------------------------------------+------------+
| ``alb_tile_3``      | Tile land albedo, waveband 3 (direct beam NIR).                         | nsurft     |
+---------------------+-------------------------------------------------------------------------+------------+
| ``alb_tile_4``      | Tile land albedo, waveband 4 (diffuse NIR).                             | nsurft     |
+---------------------+-------------------------------------------------------------------------+------------+
| ``land_albedo_1``   | Gridbox band 1 albedo (direct beam visible).                            | land+sea   |
+---------------------+-------------------------------------------------------------------------+------------+
| ``land_albedo_2``   | Gridbox band 2 albedo (diffuse visible).                                | land+sea   |
+---------------------+-------------------------------------------------------------------------+------------+
| ``land_albedo_3``   | Gridbox band 3 albedo (direct beam NIR).                                | land+sea   |
+---------------------+-------------------------------------------------------------------------+------------+
| ``land_albedo_4``   | Gridbox band 4 albedo (diffuse NIR).                                    | land+sea   |
+---------------------+-------------------------------------------------------------------------+------------+
| ``emis_gb``         | Gridbox emissivity.                                                     |            |
+---------------------+-------------------------------------------------------------------------+------------+
| ``emis``            | Tile emissivity.                                                        | nsurft     |
+---------------------+-------------------------------------------------------------------------+------------+
| Radiation fluxes                                                                                           |
+---------------------+-------------------------------------------------------------------------+------------+
| ``apar``            | PFT absorbed photosynthetically active radiation (W m\ :sup:`-2`).      | npft       |
+---------------------+-------------------------------------------------------------------------+------------+
| ``apar_gb``         | Gridbox absorbed photosynthetically active radiation (W m\ :sup:`-2`).  |            |
+---------------------+-------------------------------------------------------------------------+------------+
| ``lw_down_surft``   | Tile downwelling longwave radiation  (W m\ :sup:`-2`).                  | nsurft     |
+---------------------+-------------------------------------------------------------------------+------------+
| ``lw_up_surft``     | Tile upwelling longwave radiation  (W m\ :sup:`-2`).                    | nsurft     |
+---------------------+-------------------------------------------------------------------------+------------+
| ``lw_net``          | Gridbox surface net LW radiation (W m\ :sup:`-2`).                      |            |
+---------------------+-------------------------------------------------------------------------+------------+
| ``lw_up``           | Gridbox surface upward LW radiation (W m\ :sup:`-2`).                   |            |
+---------------------+-------------------------------------------------------------------------+------------+
| ``rad_net``         | Surface net radiation (W m\ :sup:`-2`).                                 |            |
+---------------------+-------------------------------------------------------------------------+------------+
| ``rad_net_tile``    | Tile surface net radiation (W m\ :sup:`-2`).                            | nsurft     |
+---------------------+-------------------------------------------------------------------------+------------+
| ``sw_net``          | Gribox net shortwave radiation at the surface (W m\ :sup:`-2`).         |            |
+---------------------+-------------------------------------------------------------------------+------------+
| ``sw_net_surft``    | Tile net shortwave radiation  (W m\ :sup:`-2`).                         | nsurft     |
+---------------------+-------------------------------------------------------------------------+------------+
| Other radiation variables                                                                                  |
+---------------------+-------------------------------------------------------------------------+------------+
| ``cosz``            | Cosine of the zenith angle (-).                                         | land+sea   |
+---------------------+-------------------------------------------------------------------------+------------+
| ``diff_frac``       | Gridbox fraction of radiation that is diffuse (-).                      | land+sea   |
+---------------------+-------------------------------------------------------------------------+------------+
| ``fapar``           | PFT fraction of absorbed photosynthetically active radiation (-).       | npft       |
+---------------------+-------------------------------------------------------------------------+------------+
| ``NDVI_land``       | Gridbox NDVI (using sum of direct and diffuse for (NIR-VIS)/(NIR+VIS)). |            |
+---------------------+-------------------------------------------------------------------------+------------+
| ``trad``            | Gridbox effective radiative temperature (K).                            |            |
+---------------------+-------------------------------------------------------------------------+------------+



Energy and momentum fluxes, and surface temperatures
-------------------------------------------------------------------

.. tabularcolumns:: |p{3.5cm}|p{9.8cm}|p{2.2cm}|

+-------------------------+-------------------------------------------------------------------------------------+------------+
| Name                    | Description                                                                         | Dimensions |
+=========================+=====================================================================================+============+
| ``ftl``                 | Tile surface sensible heat flux for land tiles (W m\ :sup:`-2`).                    | nsurft     |
+-------------------------+-------------------------------------------------------------------------------------+------------+
| ``ftl_gb``              | Gridbox surface sensible heat flux (W m\ :sup:`-2`).                                | land+sea   |
+-------------------------+-------------------------------------------------------------------------------------+------------+
| ``le``                  | Tile surface latent heat flux for land tiles (W m\ :sup:`-2`).                      | nsurft     |
+-------------------------+-------------------------------------------------------------------------------------+------------+
| ``latent_heat``         | Gridbox surface latent heat flux (W m\ :sup:`-2`).                                  | land+sea   |
+-------------------------+-------------------------------------------------------------------------------------+------------+
| ``surf_ht_flux``        | Downward heat flux for each tile (W m\ :sup:`-2`).                                  | nsurft     |
+-------------------------+-------------------------------------------------------------------------------------+------------+
| ``surf_ht_store``       | C*(dT/dt) for each tile (W m\ :sup:`-2`).                                           | nsurft     |
+-------------------------+-------------------------------------------------------------------------------------+------------+
| ``surf_ht_flux_gb``     | Gridbox net downward heat flux at surface over land and sea-ice fraction of gridbox | land+sea   |
|                         | (W m\ :sup:`-2`).                                                                   |            |
+-------------------------+-------------------------------------------------------------------------------------+------------+
| ``anthrop_heat``        | Anthropogenic heat flux for each tile (W m\ :sup:`-2`).                             | nsurft     |
+-------------------------+-------------------------------------------------------------------------------------+------------+
| ``hf_snow_melt``        | Gridbox snowmelt heat flux (W m\ :sup:`-2`).                                        |            |
+-------------------------+-------------------------------------------------------------------------------------+------------+
| ``snomlt_surf_htf``     | Gridbox heat flux used for surface melting of snow (W m\ :sup:`-2`).                | land+sea   |
+-------------------------+-------------------------------------------------------------------------------------+------------+
| ``snomlt_sub_htf``      | Gridbox sub-canopy snowmelt heat flux (W m\ :sup:`-2`).                             |            |
+-------------------------+-------------------------------------------------------------------------------------+------------+
| ``tstar_gb``            | Gridbox surface temperature (K).                                                    | land+sea   |
+-------------------------+-------------------------------------------------------------------------------------+------------+
| ``tstar``               | Tile surface temperature (K).                                                       | nsurft     |
+-------------------------+-------------------------------------------------------------------------------------+------------+
| ``tsurf_elev_surft``    | Tile temperature of elevated subsurface tiles (K).                                  | nsurft     |
+-------------------------+-------------------------------------------------------------------------------------+------------+
| ``tau``                 | Tile surface wind stress for land tiles (N m\ :sup:`-2`).                           | nsurft     |
+-------------------------+-------------------------------------------------------------------------------------+------------+
| ``taux1``               | Gridbox westerly component of surface wind stress (N m\ :sup:`-2`).                 | land+sea   |
+-------------------------+-------------------------------------------------------------------------------------+------------+
| ``tauy1``               | Gridbox southerly component of surface wind stress (N m\ :sup:`-2`).                | land+sea   |
+-------------------------+-------------------------------------------------------------------------------------+------------+
| ``tauy_gb``             | Gridbox scalar magnitude of surface wind stress (N m\ :sup:`-2`).                   | land+sea   |
+-------------------------+-------------------------------------------------------------------------------------+------------+
| ``z0``                  | Tile surface roughness (m).                                                         | nsurft     |
+-------------------------+-------------------------------------------------------------------------------------+------------+



Soil moisture and temperature, and soil characteristics
-------------------------------------------------------------------

.. tabularcolumns:: |p{4.0cm}|p{9.3cm}|p{2.2cm}|

+-------------------------+-------------------------------------------------------------------------------+------------+
| Name                    | Description                                                                   | Dimensions |
+=========================+===============================================================================+============+
| Soil moisture                                                                                                        |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``smcl[_soilt]``        | Moisture content of each soil layer (kg m\ :sup:`-2`).                        | sm_levels  |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``soil_wet``            | Total moisture content of each soil layer, as fraction of saturation (-).     | sm_levels  |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``sthu[_soilt]``        | Unfrozen moisture content of each soil layer as a fraction of saturation (-). | sm_levels  |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``sthu_irr[_soilt]``    | Unfrozen moisture content of each soil layer as a fraction of saturation in   | sm_levels  |
|                         | irrigated fraction (-) (only available if l_irrig_dmd = T).                   |            |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``sthf[_soilt]``        | Frozen moisture content of each soil layer as a fraction of saturation (-).   | sm_levels  |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``smc_tot``             | Gridbox total soil moisture in column (kg m\ :sup:`-2`).                      |            |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``swet_liq_tot``        | Gridbox unfrozen soil moisture as fraction of saturation (-).                 |            |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``swet_tot``            | Gridbox soil moisture as fraction of saturation (-).                          |            |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``sthzw[_soilt]``       | Soil wetness in the deep LSH/TOPMODEL layer (-).                              |            |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``zw[_soilt]``          | Gridbox mean depth to water table (m).                                        |            |
+-------------------------+-------------------------------------------------------------------------------+------------+
| Soil temperature                                                                                                     |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``t_soil[_soilt]``      | Sub-surface temperature of each layer (K).                                    | sm_levels  |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``tsoil_deep``          | Temperature of each bedrock layer (K).                                        | ns_deep    |
|                         | Only available when :nml:mem:`JULES_SOIL::l_bedrock` = TRUE.                  |            |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``depth_frozen``        | Gridbox depth of frozen ground at surface defined from soil temperature (m).  |            |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``depth_frozen_sthf``   | Gridbox depth of frozen ground at surface defined from soil moisture (m).     |            |
|                         | Recommended over ``depth_frozen`` except where the soil is very dry.          |            |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``depth_unfrozen``      | Gridbox depth of unfrozen ground at surface defined from soil temperature (m).|            |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``depth_unfrozen_sthf`` | Gridbox depth of unfrozen ground at surface defined from soil moisture (m).   |            |
|                         | Recommended over ``depth_unfrozen`` except where the soil is very dry.        |            |
+-------------------------+-------------------------------------------------------------------------------+------------+
| Soil characteristics                                                                                                 |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``b[_soilt]``           | Brooks-Corey exponent for each soil layer (-).                                | sm_levels  |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``hcap[_soilt]``        | Dry soil heat capacity (J K\ :sup:`-1` m\ :sup:`-3`) for each soil layer.     | sm_levels  |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``hcon[_soilt]``        | Dry soil thermal conductivity (W m\ :sup:`-1` K\ :sup:`-1`) for each soil     | sm_levels  |
|                         | layer.                                                                        |            |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``satcon[_soilt]``      | Saturated hydraulic conductivity (kg m\ :sup:`-2` s\ :sup:`-1`) for each soil | sm_levels  |
|                         | layer.                                                                        |            |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``sathh[_soilt]``       | Saturated soil water pressure (m) for each soil layer.                        | sm_levels  |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``sm_crit[_soilt]``     | Volumetric moisture content at critical point for each soil layer (-),        | sm_levels  |
|                         | as given in :nml:lst:`JULES_SOIL_PROPS`.                                      |            |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``sm_sat[_soilt]``      | Volumetric moisture content at saturation for each soil layer (-).            | sm_levels  |
+-------------------------+-------------------------------------------------------------------------------+------------+
| ``sm_wilt[_soilt]``     | Volumetric moisture content at wilting point for each soil layer (-),         | sm_levels  |
|                         | as given in :nml:lst:`JULES_SOIL_PROPS`.                                      |            |
+-------------------------+-------------------------------------------------------------------------------+------------+



Hydrology
-------------------------------------------------------------------

.. tabularcolumns:: |p{4.6cm}|p{8.7cm}|p{2.2cm}|

+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| Name                          | Description                                                                                   | Dimensions |
+===============================+===============================================================================================+============+
| Canopy hydrology                                                                                                                           |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``canopy_gb``                 | Gridbox canopy water content (kg m\ :sup:`-2`).                                               |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``canopy``                    | Tile surface/canopy water for snow-free land tiles (kg m\ :sup:`-2`).                         | nsurft     |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``catch``                     | Tile surface/canopy water capacity of snow-free land tiles (kg m\ :sup:`-2`).                 | nsurft     |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``tfall``                     | Gridbox throughfall (kg m\ :sup:`-2` s\ :sup:`-1`).                                           |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| Evaporation and sublimation                                                                                                                |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``fqw``                       | Tile surface moisture flux for land tiles (kg m\ :sup:`-2` s\ :sup:`-1`).                     | nsurft     |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``fqw_gb``                    | Gridbox moisture flux from surface (kg m\ :sup:`-2` s\ :sup:`-1`).                            | land+sea   |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``ecan``                      | Tile evaporation from canopy/surface store for snow-free                                      |            |
|                               | land tiles (kg m\ :sup:`-2` s\ :sup:`-1`).                                                    | nsurft     |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``ecan_gb``                   | Gridbox mean evaporation from canopy/surface store (kg m\ :sup:`-2` s\ :sup:`-1`).            | land+sea   |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``ei``                        | Tile sublimation from lying snow for land tiles (kg m\ :sup:`-2` s\ :sup:`-1`).               | nsurft     |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``ei_gb``                     | Gridbox sublimation from lying snow or sea-ice (kg m\ :sup:`-2` s\ :sup:`-1`).                | land+sea   |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``elake``                     | Gridbox mean evaporation from lakes (kg m\ :sup:`-2` s\ :sup:`-1`).                           |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``esoil``                     | Tile surface evapotranspiration from soil moisture store for                                  | nsurft     |
|                               | snow-free land tile (kg m\ :sup:`-2` s\ :sup:`-1`).                                           |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``esoil_gb``                  | Gridbox surface evapotranspiration from soil moisture store (kg m\ :sup:`-2` s\ :sup:`-1`).   | land+sea   |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``et_stom``                   | Tile transpiration (kg m\ :sup:`-2` s\ :sup:`-1`).                                            | nsurft     |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``et_stom_gb``                | Gridbox transpiration (kg m\ :sup:`-2` s\ :sup:`-1`).                                         | land+sea   |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``fao_et0``                   | FAO Penman-Monteith evapotranspiration for reference crop (kg m\ :sup:`-2` s\ :sup:`-1`)      |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``gc``                        | Tile surface conductance to evaporation for land tiles (m s\ :sup:`-1`).                      | nsurft     |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``gs``                        | Gridbox surface conductance to evaporation (m s\ :sup:`-1`).                                  |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``ext[_soilt]``               | Extraction of water from each soil layer (kg m\ :sup:`-2` s\ :sup:`-1`).                      | sm_levels  |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``fsmc_gb``                   | Gridbox soil moisture availability factor (beta) (-).                                         |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``fsmc``                      | PFT soil moisture availability factor (-).                                                    | npft       |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``smc_avail_top``             | Gridbox available moisture in surface layer of depth given by :nml:mem:`JULES_SOIL::zsmc`     |            |
|                               | (kg m\ :sup:`-2`). Calculated using ``sm_wilt`` from :nml:lst:`JULES_SOIL_PROPS`.             |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``smc_avail_tot``             | Gridbox available moisture in soil column (kg m\ :sup:`-2`).                                  |            |
|                               | Calculated using ``sm_wilt`` from :nml:lst:`JULES_SOIL_PROPS`.                                |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| Runoff                                                                                                                                     |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``runoff``                    | Gridbox runoff rate (kg m\ :sup:`-2` s\ :sup:`-1`).                                           |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``sub_surf_roff``             | Gridbox sub-surface runoff (kg m\ :sup:`-2` s\ :sup:`-1`).                                    |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``surf_roff``                 | Gridbox surface runoff (kg m\ :sup:`-2` s\ :sup:`-1`).                                        |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``sat_excess_roff[_soilt]``   | Gridbox saturation excess runoff rate (kg m\ :sup:`-2` s\ :sup:`-1`).                         |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``drain[_soilt]``             | Gridbox drainage at bottom of soil column (kg m\ :sup:`-2` s\ :sup:`-1`).                     |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``qbase[_soilt]``             | Gridbox baseflow (lateral subsurface runoff) (kg m\ :sup:`-2` s\ :sup:`-1`), i.e. the sum of  |            |
|                               | surface and subsurface lateral flows from all soil layers (inc. deep LSH/TOPMODEL layer).     |            |
|                               | Only available if :nml:mem:`JULES_HYDROLOGY::l_top` = TRUE.                                   |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``qbase_zw[_soilt]``          | Gridbox baseflow (lateral subsurface runoff) from deep LSH/TOPMODEL layer                     |            |
|                               | (kg m\ :sup:`-2` s\ :sup:`-1`).                                                               |            |
|                               | Only available if :nml:mem:`JULES_HYDROLOGY::l_top` = TRUE.                                   |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| Other hydrological variables                                                                                                               |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``fsat[_soilt]``              | Gridbox surface saturated fraction (-). The fraction of grid cell where the water table is    |            |
|                               | above the land surface. Only available if :nml:mem:`JULES_HYDROLOGY::l_top` = TRUE.           |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``fwetl[_soilt]``             | Gridbox wetland fraction at end of model timestep (-). The fraction of grid cell where the    |            |
|                               | water table is above the land surface, but water is not flowing (stagnant) (fwetl<=fsat).     |            |
|                               | Only available if :nml:mem:`JULES_HYDROLOGY::l_top` = TRUE.                                   |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+



Rivers
-------------------------------------------------------------------

.. tabularcolumns:: |p{4.6cm}|p{8.7cm}|p{2.2cm}|

+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| Name                          | Description                                                                                   | Dimensions |
+===============================+===============================================================================================+============+
| Output on the river routing model grid                                                                                                     |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``rflow_rp``                  | River routing gridbox river flow rate (kg m\ :sup:`-2` s\ :sup:`-1`).                         | np_rivers  |
|                               | Only available if :nml:mem:`JULES_RIVERS::l_rivers` = TRUE.                                   |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``rivers_outflow_rp``         | River outflow on river routing grid (kg s\ :sup:`-1`).                                        | np_rivers  |
|                               | Only available if :nml:mem:`JULES_RIVERS::l_rivers` = TRUE.                                   |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``outflow_per_river``         | River outflow into the ocean for each river (kg s\ :sup:`-1`).                                | np_rivers  |
|                               | Only available if :nml:mem:`JULES_RIVERS::l_rivers` = TRUE.                                   |            |
|                               |                                                                                               |            |
|                               | This technically has dimensions of "np_rivers", although only ``[1:n_rivers]``, defined by    |            |
|                               | the :nml:mem:`JULES_RIVERS_PROPS::riv_number_file`, is populated.                             |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``rrun_rp``                   | River routing gridbox runoff rate received by river routing routine                           | np_rivers  |
|                               | (kg m\ :sup:`-2` s\ :sup:`-1`).                                                               |            |
|                               | Only available if :nml:mem:`JULES_RIVERS::l_rivers` = TRUE.                                   |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``rrun_surf_rp``              | River routing gridbox surface runoff rate received by river routing routine                   | np_rivers  |
|                               | (kg m\ :sup:`-2` s\ :sup:`-1`).                                                               |            |
|                               | Only available if :nml:mem:`JULES_RIVERS::l_rivers` = TRUE.                                   |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``rrun_sub_surf_rp``          | River routing gridbox sub-surface runoff rate received by river routing routine               | np_rivers  |
|                               | (kg m\ :sup:`-2` s\ :sup:`-1`).                                                               |            |
|                               | Only available if :nml:mem:`JULES_RIVERS::l_rivers` = TRUE.                                   |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``rfm_surfstore_rp``          | Surface storage on river points (m\ :sup:`3`).                                                | np_rivers  |
|                               | Only available if :nml:mem:`JULES_RIVERS::l_rivers` = TRUE and                                |            |
|                               | :nml:mem:`JULES_RIVERS::i_river_vn` = 2.                                                      |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``rfm_substore_rp``           | Sub-surface storage on river points (m\ :sup:`3`).                                            | np_rivers  |
|                               | Only available if :nml:mem:`JULES_RIVERS::l_rivers` = TRUE and                                |            |
|                               | :nml:mem:`JULES_RIVERS::i_river_vn` = 2.                                                      |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``rfm_flowin_rp``             | Surface inflow on river points (m\ :sup:`3` s\ :sup:`-1`).                                    | np_rivers  |
|                               | Only available if :nml:mem:`JULES_RIVERS::l_rivers` = TRUE and                                |            |
|                               | :nml:mem:`JULES_RIVERS::i_river_vn` = 2.                                                      |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``rfm_bflowin_rp``            | Sub-surface inflow on river points (m\ :sup:`3` s\ :sup:`-1`).                                | np_rivers  |
|                               | Only available if :nml:mem:`JULES_RIVERS::l_rivers` = TRUE and                                |            |
|                               | :nml:mem:`JULES_RIVERS::i_river_vn` = 2.                                                      |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``rivers_sto_rp``             | River routing gridbox river storage (kg)                                                      | np_rivers  |
|                               | Only available if :nml:mem:`JULES_RIVERS::l_rivers` = TRUE and                                |            |
|                               | :nml:mem:`JULES_RIVERS::i_river_vn` = 3.                                                      |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``frac_fplain_rp``            | Overbank inundation area as a fraction of river routing gridcell area.                        | np_rivers  |
|                               | Only available if :nml:mem:`JULES_RIVERS::l_riv_overbank` = TRUE.                             |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| Output regridded to the JULES model grid                                                                                                   |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``rflow``                     | Gridbox river flow rate (kg m\ :sup:`-2` s\ :sup:`-1`).                                       |            |
|                               | Only available if :nml:mem:`JULES_RIVERS::l_rivers` = TRUE.                                   |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``rrun``                      | Gridbox runoff rate received by river routing routine (kg m\ :sup:`-2` s\ :sup:`-1`).         |            |
|                               | Only available if :nml:mem:`JULES_RIVERS::l_rivers` = TRUE                                    |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+
| ``frac_fplain_lp``            | Overbank inundation area as a fraction of gridcell area.                                      |            |
|                               | Only available if :nml:mem:`JULES_RIVERS::l_riv_overbank` = TRUE.                             |            |
+-------------------------------+-----------------------------------------------------------------------------------------------+------------+



Snow
-------------------------------------------------------------------

.. tabularcolumns:: |p{4.5cm}|p{8.8cm}|p{2.2cm}|

+--------------------------+-----------------------------------------------------------------------------------+--------------+
| Name                     | Description                                                                       | Dimensions   |
+==========================+===================================================================================+==============+
| Snow state                                                                                                                  |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snow_mass``            | Tile lying snow (total) (kg m\ :sup:`-2`).                                        | nsurft       |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snow_mass_gb``         | Gridbox snowmass (kg m\ :sup:`-2`).                                               | land+sea     |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snow_depth``           | Tile snow depth (m).                                                              | nsurft       |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snow_depth_gb``        | Gridbox depth of snow (m).                                                        |              |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snow_can``             | Tile snow on canopy (kg m\ :sup:`-2`).                                            | nsurft       |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snow_can_gb``          | Gridbox snow on canopy (kg m\ :sup:`-2`).                                         |              |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snow_ground``          | Tile snow on ground (``snow_tile`` or ``snow_grnd`` depending                     | nsurft       |
|                          | on configuration) (kg m\ :sup:`-2`).                                              |              |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snow_grnd_gb``         | Gridbox average snow beneath canopy (snow_grnd) (kg m\ :sup:`-2`).                |              |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snow_grnd``            | Tile snow on ground below canopy (kg m\ :sup:`-2`).                               | nsurft       |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snow_grnd_rho``        | Tile bulk density of snow on ground (kg m\ :sup:`-3`).                            | nsurft       |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snow_frac``            | Gridbox snow-covered fraction of land points (-).                                 |              |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snow_ice_tile``        | Tile total frozen mass in snow on ground (kg m\ :sup:`-2`).                       | nsurft       |
|                          | Only available if :nml:mem:`JULES_SNOW::nsmax` > 0.                               |              |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snow_ice_gb``          | Gridbox frozen water in snowpack (kg m\ :sup:`-2`).                               |              |
|                          | Only available if :nml:mem:`JULES_SNOW::nsmax` > 0.                               |              |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snow_liq_tile``        | Tile total liquid mass in snow on ground (kg m\ :sup:`-2`).                       | nsurft       |
|                          | Only available if :nml:mem:`JULES_SNOW::nsmax` > 0.                               |              |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snow_liq_gb``          | Gridbox liquid water in snowpack (kg m\ :sup:`-2`).                               |              |
|                          | Only available if :nml:mem:`JULES_SNOW::nsmax` > 0.                               |              |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``nsnow``                | Tile number of snow layers (-).                                                   | nsurft       |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``rgrain``               | Tile snow surface grain size (\ |mu|\ m).                                         | nsurft       |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| Snow layer variables                                                                                                        |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snow_ds``              | Depth of each snow layer for each tile (m).                                       | nsurft,nsmax |
|                          | Only available if :nml:mem:`JULES_SNOW::nsmax` > 0.                               |              |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snow_ice``             | Mass of ice in each snow layer for each tile (kg m\ :sup:`-2`).                   | nsurft,nsmax |
|                          | Only available if :nml:mem:`JULES_SNOW::nsmax` > 0.                               |              |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snow_liq``             | Mass of liquid water in each snow layer for each tile (kg m\ :sup:`-2`).          | nsurft,nsmax |
|                          | Only available if :nml:mem:`JULES_SNOW::nsmax` > 0.                               |              |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``tsnow``                | Temperature of each snow layer (K).                                               | nsurft,nsmax |
|                          | Only available if :nml:mem:`JULES_SNOW::nsmax` > 0.                               |              |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``rgrainl``              | Grain size in snow layers for each tile (\ |mu|\ m).                              | nsurft,nsmax |
|                          | Only available if :nml:mem:`JULES_SNOW::nsmax` > 0.                               |              |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| Snow fluxes and rates of change                                                                                             |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snow_melt``            | Tile snow melt rate (melt_tile) (kg m\ :sup:`-2` s\ :sup:`-1`).                   | nsurft       |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snow_melt_gb``         | Gridbox rate of snowmelt (kg m\ :sup:`-2` s\ :sup:`-1`).                          |              |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snow_can_melt``        | Tile melt of snow on canopy (kg m\ :sup:`-2` s\ :sup:`-1`).                       | nsurft       |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snice_freez_surft``    | Tile internal refreezing rate in snowpack (kg m\ :sup:`-2` s\ :sup:`-1`).         | nsurft       |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snice_m_surft``        | Tile total internal melt rate of snowpack (kg m\ :sup:`-2` s\ :sup:`-1`).         | nsurft       |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snice_runoff_surft``   | Tile net rate of liquid leaving snowpack on tiles (kg m\ :sup:`-2` s\ :sup:`-1`). | nsurft       |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snice_sicerate_surft`` | Tile rate of change of solid mass in snowpack (kg m\ :sup:`-2` s\ :sup:`-1`).     | nsurft       |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snice_sliqrate_surft`` | Tile rate of change of liquid in snowpack (kg m\ :sup:`-2` s\ :sup:`-1`).         | nsurft       |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snice_smb_surft``      | Tile rate of change of snowpack mass (kg m\ :sup:`-2` s\ :sup:`-1`).              | nsurft       |
+--------------------------+-----------------------------------------------------------------------------------+--------------+
| ``snow_soil_htf``        | Tile downward heat flux after snowpack to subsurface" (W m\ :sup:`-2`).           | nsurft       |
+--------------------------+-----------------------------------------------------------------------------------+--------------+



Vegetation carbon and related fluxes
-------------------------------------------------------------------

.. tabularcolumns:: |p{3.5cm}|p{9.8cm}|p{2.2cm}|

+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| Name                     | Description                                                                                       | Dimensions |
+==========================+===================================================================================================+============+
| ``c_veg``                | PFT total carbon content of the vegetation at end of model timestep (kg C m\ :sup:`-2`).          | npft       |
|                          |     (including leaf, wood and root carbon, both above and below ground)                           |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``cv``                   | Gridbox mean vegetation carbon at end of model timestep (kg m\ :sup:`-2`).                        |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``leafC``                | PFT carbon in leaf biomass (kg m\ :sup:`-2` ).                                                    | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``rootC``                | PFT carbon in root biomass (kg m\ :sup:`-2` ).                                                    | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``woodC``                | PFT carbon in woody biomass (kg m\ :sup:`-2` ).                                                   | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``frac_agr``             | Fractional area of agricultural land in each gridbox. If :nml:mem:`JULES_VEGETATION::l_trif_crop` |            |
|                          | is TRUE, frac_agr is the fractional area of crop land in each gridbox.                            |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``frac_agr_prev``        | Fractional area of agricultural land at the previous timestep.                                    |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``frac_past``            | Fractional area of pasture land in each gridbox.                                                  |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``plantNumDensity``      | Number density of plants  ( m\ :sup:`-2` ).                                                       | npft,nmasst|
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| Fractional cover, leaf area and turnover, and canopy height                                                                               |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``frac``                 | Fractional cover of each surface type.                                                            | ntype      |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``lai``                  | PFT leaf area index (-).                                                                          | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``lai_gb``               | Gridbox leaf area index (-).                                                                      |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``lai_bal``              | PFT balanced leaf area index in sf_stom (-).                                                      | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``lai_phen``             | PFT leaf area index after phenology (-).                                                          | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``canht``                | PFT canopy height (m).                                                                            | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``g_leaf``               | PFT leaf turnover rate ([360days]\ :sup:`-1`).                                                    | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``g_leaf_day``           | PFT mean leaf turnover rate for input to PHENOL ([360days]\ :sup:`-1`).                           | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``g_leaf_dr_out``        | PFT mean leaf turnover rate for driving TRIFFID ([360days]\ :sup:`-1`).                           | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``g_leaf_phen``          | PFT mean leaf turnover rate over phenology period([360days]\ :sup:`-1`).                          | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| GPP, NPP, respiration                                                                                                                     |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``gpp``                  | PFT gross primary productivity of biomass expressed as carbon                                     | npft       |
|                          | (kg C m\ :sup:`-2` s\ :sup:`-1`).                                                                 |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``gpp_gb``               | Gridbox gross primary productivity of biomass expressed as carbon                                 |            |
|                          | (kg C m\ :sup:`-2` s\ :sup:`-1`).                                                                 |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``npp``                  | PFT net primary productivity of biomass expressed as carbon prior to nitrogen limitation          | npft       |
|                          | (kg C m\ :sup:`-2` s\ :sup:`-1`).                                                                 |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``npp_n_gb``             | Gridbox net primary productivity of biomass expressed as carbon after nitrogen limitation         |            |
|                          | (kg C m\ :sup:`-2` (360days)\ :sup:`-1`).                                                         |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``npp_n``                | PFT net primary productivity of biomass expressed as carbon after nitrogen limitation             | npft       |
|                          | (kg C m\ :sup:`-2` (360days)\ :sup:`-1`).                                                         |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``npp_dr_out``           | PFT mean NPP of biomass expressed as carbon for driving TRIFFID                                   | npft       |
|                          | (kg C m\ :sup:`-2` (360days)\ :sup:`-1`).                                                         |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``nbp_gb``               | Gridbox mean net biosphere productivity. This is NPP minus the sum of all carbon fluxes out of    |            |
|                          | land: soil respiration, exudates, harvest flux, wood product pool decay fluxes, and loss of       |            |
|                          | carbon from vegetation and soil due to fire (kg C m\ :sup:`-2` (360days)\ :sup:`-1`)              |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``resp_p``               | PFT plant respiration carbon flux (kg m\ :sup:`-2` s\ :sup:`-1`).                                 | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``resp_p_gb``            | Gridbox plant respiration carbon flux (kg m\ :sup:`-2` s\ :sup:`-1`).                             |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``resp_w_dr_out``        | PFT mean wood respiration carbon flux for driving TRIFFID                                         | npft       |
|                          | (kg m\ :sup:`-2` (360days)\ :sup:`-1`).                                                           |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``resp_l``               | PFT leaf respiration carbon flux (kg m\ :sup:`-2` s\ :sup:`-1`).                                  | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``resp_r``               | PFT root respiration carbon flux (kg m\ :sup:`-2` s\ :sup:`-1`).                                  | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``resp_w``               | PFT wood respiration carbon flux (kg m\ :sup:`-2` s\ :sup:`-1`).                                  | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| Litter carbon fluxes                                                                                                                      |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``lit_c``                | PFT carbon litter (kg m\ :sup:`-2` (360days)\ :sup:`-1`).                                         | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``lit_c_mean``           | Gridbox mean carbon litter (kg m\ :sup:`-2` (360days)\ :sup:`-1`).                                |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``lit_c_ag``             | PFT carbon litter from LU/agriculture (kg C m\ :sup:`-2` (360days)\ :sup:`-1`).                   | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``lit_c_orig``           | PFT carbon litter including LU (kg C m\ :sup:`-2` (360days)\ :sup:`-1`).                          | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``leaf_litC``            | PFT litter carbon due to leaf turnover (kg m\ :sup:`-2` )(360days)\ :sup:`-1`).                   | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``root_litC``            | PFT litter carbon due to root turnover (kg m\ :sup:`-2` )(360days)\ :sup:`-1`).                   | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``wood_litC``            | PFT litter carbon due to wood turnover (kg m\ :sup:`-2` )(360days)\ :sup:`-1`).                   | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``plant_input_c_gb``     | Gridbox input of C to the soil by plant litterfall (kg m\ :sup:`-2` s\ :sup:`-1`).                |            |
|                          | Only available with the ECOSSE soil model (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 3). |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| Other carbon fluxes                                                                                                                       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``exudates``             | PFT exudates - excess carbon not assimilable into plant due lack of nitrogen                      | npft       |
|                          | availability (kg C m\ :sup:`-2` (360days)\ :sup:`-1`).                                            |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``exudates_gb``          | Gridbox exudates: excess carbon not assimilable into plant due lack of nitrogen                   |            |
|                          | (kg m\ :sup:`-2` (360days)\ :sup:`-1`).                                                           |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``pc_s``                 | PFT net carbon available for spreading in TRIFFID                                                 | npft       |
|                          | (kg m\ :sup:`-2` (360 days)\ :sup:`-1`).                                                          |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| Harvest, wood products and land use                                                                                                       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``root_abandon``         | PFT carbon flux from roots abandoned during landuse change to soil                                | npft       |
|                          | (kg C m\ :sup:`-2` (360days)\ :sup:`-1`).                                                         |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``root_abandon_gb``      | Carbon from roots abandoned during landuse change to soil kg C m\ :sup:`-2` (360days)\ :sup:`-1`).|            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``harvest``              | Flux of carbon to product pools due to harvest (kg C m\ :sup:`-2` (360days)\ :sup:`-1`).          | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``harvest_gb``           | Gridbox flux of carbon to product pools due to harvest (kg C m\ :sup:`-2` (360days)\ :sup:`-1`).  |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``harvest_biocrop``      | Flux of carbon to product pools due to biocrop harvest (kg C m\ :sup:`-2` (360days)\ :sup:`-1`).  | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``harvest_biocrop_gb``   | Gridbox flux of carbon to product pools due to biocrop harvest (kg C m\ :sup:`-2`                 |            |
|                          | (360days)\ :sup:`-1`).                                                                            |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``wood_prod_fast``       | Carbon content of the fast decay-rate wood product pool (kg m\ :sup:`-2`).                        |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``wood_prod_med``        | Carbon content of the medium decay-rate wood product pool (kg m\ :sup:`-2`).                      |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``wood_prod_slow``       | Carbon content of the slow decay-rate wood product pool (kg m\ :sup:`-2`).                        |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``WP_fast_in``           | Carbon flux from vegetation to the fast decay-rate wood product pool                              |            |
|                          | (kg m\ :sup:`-2` [360days]\ :sup:`-1`).                                                           |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``WP_med_in``            | Carbon flux from vegetation to the medium decay-rate wood product pool                            |            |
|                          | (kg m\ :sup:`-2` [360days]\ :sup:`-1`).                                                           |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``WP_slow_in``           | Carbon flux from vegetation to the slow decay-rate wood product pool                              |            |
|                          | (kg m\ :sup:`-2` [360days]\ :sup:`-1`).                                                           |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``WP_fast_out``          | Carbon flux from the fast decay-rate wood product pool to atmosphere                              |            |
|                          | (kg m\ :sup:`-2` [360days]\ :sup:`-1`).                                                           |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``WP_med_out``           | Carbon flux from the medium decay-rate wood product pool to atmosphere                            |            |
|                          | (kg m\ :sup:`-2` [360days]\ :sup:`-1`).                                                           |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``WP_slow_out``          | Carbon flux from the slow decay-rate wood product pool to atmosphere                              |            |
|                          | (kg m\ :sup:`-2` [360days]\ :sup:`-1`).                                                           |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| Carbon conservation                                                                                                                       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``cnsrv_carbon_veg2``    | Error in land carbon conservation in veg2 routine (kg m-2)                                        |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``cnsrv_carbon_triffid`` | Error in land carbon conservation in triffid routine (kg m-2)                                     |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``cnsrv_veg_triffid``    | Error in vegetation carbon conservation in triffid routine (kg m-2)                               |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``cnsrv_soil_triffid``   | Error in soil carbon conservation in triffid routine (kg m-2)                                     |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``cnsrv_prod_triffid``   | Error in wood product carbon conservation in triffid routine (kg m-2)                             |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| Thermal acclimation of photosynthesis                                                                                                     |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``t_home_gb``            | Long-term home temperature for C3 photosynthesis (K).                                             |            |
|                          | Only available if :nml:mem:`JULES_VEGETATION::photo_acclim_model` = 1 or 3.                       |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``t_growth_gb``          | Short-term growth temperature for C3 photosynthesis (K).                                          |            |
|                          | Only available if :nml:mem:`JULES_VEGETATION::photo_acclim_model` = 2 or 3.                       |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+



Vegetation nitrogen and related fluxes
-------------------------------------------------------------------

.. tabularcolumns:: |p{4.5cm}|p{8.8cm}|p{2.2cm}|

+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| Name                     | Description                                                                                       | Dimensions |
+==========================+===================================================================================================+============+
| ``n_veg``                | PFT plant nitrogen content N_LEAF+N_ROOT+N_WOOD from carbon equivalents                           | npft       |
|                          | (kg m\ :sup:`-2`).                                                                                |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``n_veg_gb``             | Gridbox mean plant nitrogen content: n_leaf+n_root+n_wood from carbon equivalents                 |            |
|                          | (kg m\ :sup:`-2` ).                                                                               |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``n_leaf``               | PFT leaf nitrogen scaled by LAI in sf_stom (kg m\ :sup:`-2`).                                     | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``n_root``               | PFT root nitrogen scaled by LAI_BAL in sf_stom (kg m\ :sup:`-2`).                                 | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``n_stem``               | PFT stem nitrogen scaled by LAI in sf_stom; scaled by LAI_BAL if l_stem_resp_fix=T                | npft       |
|                          | (kg m\ :sup:`-2`).                                                                                |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| Nitrogen fluxes                                                                                                                           |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``deposition_n``         | Nitrogen deposition (kg m\ :sup:`-2` s\ :sup:`-1`).                                               |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``n_demand``             | PFT total nitrogen demand                                                                         | npft       |
|                          | (kg m\ :sup:`-2` (360 days)\ :sup:`-1`).                                                          |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``n_demand_gb``          | Gridbox mean demand for nitrogen (kg m\ :sup:`-2` (360days)\ :sup:`-1`).                          |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``n_fix``                | PFT fixed nitrogen (kg N m\ :sup:`-2` (360days)\ :sup:`-1`).                                      | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``n_fix_gb``             | Gridbox mean nitrogen fixed by plants (kg m\ :sup:`-2` (360days)\ :sup:`-1`).                     |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``n_uptake``             | PFT nitrogen taken up by plants (kg m\ :sup:`-2` (360 days)\ :sup:`-1`).                          | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``n_uptake_gb``          | Gridbox total nitrogen uptake by plants (kg N m\ :sup:`-2` (360days)\ :sup:`-1`).                 |            |
|                          | Only available if :nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2 or 3.                      |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``n_demand_growth``      | PFT nitrogen demand for growth of existing plant biomass                                          | npft       |
|                          | (kg m\ :sup:`-2` (360 days)\ :sup:`-1`).                                                          |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``n_uptake_growth``      | PFT nitrogen taken up for growth of existing plant biomass                                        | npft       |
|                          | (kg m\ :sup:`-2` (360 days)\ :sup:`-1`).                                                          |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``n_demand_lit``         | PFT nitrogen demand of litter: nitrogen lost in leaf, wood and root biomass                       | npft       |
|                          | (kg m\ :sup:`-2` (360 days)\ :sup:`-1`).                                                          |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``n_demand_spread``      | PFT nitrogen demand for spreading plants across gridbox                                           | npft       |
|                          | (kg m\ :sup:`-2` (360 days)\ :sup:`-1`).                                                          |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``n_fertiliser``         | Nitrogen addition from fertiliser (kg N m\ :sup:`-2` (360days)\ :sup:`-1`).                       | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| Nitrogen fluxes in litter, harvest and land use                                                                                           |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``lit_n_t``              | Gridbox mean total nitrogen litter (kg m\ :sup:`-2` (360days)\ :sup:`-1`).                        |            |
|                          | (kg m\ :sup:`-2` s\ :sup:`-1`).                                                                   |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``lit_n``                | PFT nitrogen litter (kg N m\ :sup:`-2` (360days)\ :sup:`-1`).                                     | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``leaf_litN``            | PFT litter nitrogen due to leaf turnover (kg m\ :sup:`-2` )(360days)\ :sup:`-1`).                 | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``lit_n_ag``             | PFT nitrogen loss due to LU/agriculture (kg N m\ :sup:`-2` (360days)\ :sup:`-1`).                 | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``litterN``              | PFT local nitrogen litter production (kg N m\ :sup:`-2` (360days)\ :sup:`-1`).                    | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``lit_n_orig``           | PFT nitrogen litter including LU (kg N m\ :sup:`-2` (360days)\ :sup:`-1`).                        | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``root_litN``            | PFT nitrogen lost as litter due to root turnover (kg m\ :sup:`-2` )(360days)\ :sup:`-1`).         | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``wood_litN``            | PFT litter nitrogen due to wood turnover (kg m\ :sup:`-2` )(360days)\ :sup:`-1`).                 | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``plant_input_n_gb``     | Gridbox input of N to the soil by plant litterfall (kg m\ :sup:`-2` s\ :sup:`-1`).                |            |
|                          | Only available with the ECOSSE soil model (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 3). |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``harvest_n``            | flux of nitrogen to atmosphere due to harvest (kg N m\ :sup:`-2` (360days)\ :sup:`-1`).           | npft       |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``harvest_n_gb``         | Gridbox flux of nitrogen to atmosphere due to harvest (kg N m\ :sup:`-2` (360days)\ :sup:`-1`).   |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``harvest_biocrop_n``    | flux of nitrogen to product pools due to biocrop harvest (kg N m\ :sup:`-2`                       | npft       |
|                          | (360days)\ :sup:`-1`).                                                                            |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``harvest_biocrop_n_gb`` | Gridbox flux of nitrogen to product pools due to biocrop harvest (kg N m\ :sup:`-2`               |            |
|                          | (360days)\ :sup:`-1`).                                                                            |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``root_abandon_n``       | PFT nitrogen flux from roots abandoned during landuse change to soil                              | npft       |
|                          | (kg N m\ :sup:`-2` (360days)\ :sup:`-1`).                                                         |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``root_abandon_n_gb``    | Nitrogen from roots abandoned during landuse change to soil                                       |            |
|                          | kg N m\ :sup:`-2` (360days)\ :sup:`-1`).                                                          |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| Nitrogen conservation                                                                                                                     |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``cnsrv_nitrogen_triffd``| Error in land nitrogen conservation in triffid routine (kg m-2)                                   |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``cnsrv_vegN_triffid``   | Error in vegetation nitrogen conservation in triffid routine (kg m-2)                             |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``cnsrv_soilN_triffid``  | Error in soil nitrogen conservation in triffid routine (kg m-2)                                   |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+
| ``cnsrv_n_inorg_triffid``| Error in inorganic nitrogen conservation in triffid routine (kg m-2)                              |            |
+--------------------------+---------------------------------------------------------------------------------------------------+------------+



Soil carbon and related fluxes
-------------------------------------------------------------------

.. tabularcolumns:: |p{4.6cm}|p{8.7cm}|p{2.2cm}|

+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| Name                        | Description                                                                                   | Dimensions     |
+=============================+===============================================================================================+================+
| ``cs[_soilt]``              | Carbon in each soil pool and each soil biogeochemistry layer                                  | cspool,cslayer |
|                             | (kg m\ :sup:`-2`).                                                                            |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``cs_label``                | Labelled carbon in each soil pool and each soil biogeochemistry layer (kg m\ :sup:`-2`).      | cspool,cslayer |
|                             | Only available if :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_label_frac_cs` = TRUE.                   |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``cs_gb``                   | Gridbox total soil carbon (kg m\ :sup:`-2`).                                                  |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``cs_label_gb``             | Gridbox total labelled soil carbon (kg m\ :sup:`-2`).                                         |                |
|                             | Only available if :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_label_frac_cs` = TRUE.                   |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``c_bio_gb``                | Gridbox soil carbon in biomass pool (kg m\ :sup:`-2`).                                        |                |
|                             | Only available if :nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2 or 3.                  |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``c_dpm_gb``                | Gridbox soil carbon in decomposable plant material pool (kg m\ :sup:`-2`).                    |                |
|                             | Only available if :nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2 or 3.                  |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``c_hum_gb``                | Gridbox soil carbon in humus pool (kg m\ :sup:`-2`).                                          |                |
|                             | Only available if :nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2 or 3.                  |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``c_rpm_gb``                | Gridbox soil carbon in resistant plant material pool (kg m\ :sup:`-2`).                       |                |
|                             | Only available if :nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2 or 3.                  |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| Soil carbon fluxes                                                                                                                           |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``co2_soil_gb``             | Gridbox C in CO\ :sub:`2` flux from soil to atmosphere (kg m\ :sup:`-2` s\ :sup:`-1`).        |                |
|                             | Only available with the ECOSSE soil model (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model`   |                |
|                             | = 3).                                                                                         |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``resp_s``                  | Respiration rate from each soil carbon pool each soil biogeochemistry layer                   | cspool,cslayer |
|                             | (kg m\ :sup:`-2` s\ :sup:`-1`).                                                               |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``resp_label_cs``           | Respiration rate from each labelled soil carbon pool each soil biogeochemistry layer          | cspool,cslayer |
|                             | (kg m\ :sup:`-2` s\ :sup:`-1`).                                                               |                |
|                             | Only available if :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_label_frac_cs` = TRUE.                   |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``resp_s_gb``               | Gridbox total soil respiration carbon flux (kg m\ :sup:`-2` s\ :sup:`-1`).                    |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``resp_label_cs_gb``        | Gridbox total labelled soil respiration carbon flux (kg m\ :sup:`-2` s\ :sup:`-1`).           |                |
|                             | Only available if :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_label_frac_cs` = TRUE.                   |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``resp_s_to_atmos_gb``      | Respired carbon from soil carbon emitted to atmosphere (kg m\ :sup:`-2` s\ :sup:`-1`).        |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``resp_s_dr_out``           | Gridbox mean soil respiration carbon flux for driving TRIFFID                                 |                |
|                             | (kg m\ :sup:`-2` (360days)\ :sup:`-1`)                                                        |                |
|                             | This is the gross soil respiration; some of this carbon flux is from one soil carbon pool to  |                |
|                             | another.                                                                                      |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| Other soil carbon variables                                                                                                                  |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``dpm_ratio``               | Gridbox DPM:RPM ratio of overall litter input (:).                                            |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``fsth``                    | Soil moisture modifier of soil respiration rate (-).                                          | sm_levels      |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``ftemp``                   | Temperature modifier of soil respiration rate (-).                                            | sm_levels      |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``fprf``                    | Modifier of soil respiration rate due to vegetation cover (-).                                |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``soil_CN``                 | Soil C:N in each soil pool and each soil biogeochemistry layer                                | cspool,cslayer |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``soil_cn_gb``              | Gridbox total soil carbon : nitrogen ratio.                                                   |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| Soil methane variables                                                                                                                       |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``fch4_wetl``               | Gridbox scaled methane flux from wetland fraction using soil carbon as substrate if           |                |
|                             | ch4_substrate=1, NPP as substrate if ch4_substrate=2, or soil respiration as substrate if     |                |
|                             | ch4_substrate=3 (10\ :sup:`-9` kg m\ :sup:`-2` s\ :sup:`-1`).                                 |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``fch4_wetl_cs[_soilt]``    | Gridbox methane flux from wetland fraction using soil carbon as substrate                     |                |
|                             | (kg m\ :sup:`-2` s\ :sup:`-1`).                                                               |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``fch4_wetl_npp[_soilt]``   | Gridbox methane flux from wetland fraction using NPP as substrate                             |                |
|                             | (kg m\ :sup:`-2` s\ :sup:`-1`).                                                               |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``fch4_wetl_resps[_soilt]`` | Gridbox methane flux from wetland fraction using soil respiration as substrate                |                |
|                             | (kg m\ :sup:`-2` s\ :sup:`-1`).                                                               |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``substr_ch4``              | Carbon in substrate pool used by methanogens for each soil methane layer                      | ch4layer       |
|                             | (kg m\ :sup:`-2`).                                                                            |                |
|                             | Only available if :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_ch4_microbe` = TRUE.                     |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``mic_ch4``                 | Carbon in methanogenic biomass for each soil methane layer (kg m\ :sup:`-2`).                 | ch4layer       |
|                             | Only available if :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_ch4_microbe` = TRUE.                     |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``mic_act_ch4``             | Activity level of methanogenic biomass for each soil methane layer (-).                       | ch4layer       |
|                             | Only available if :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_ch4_microbe` = TRUE.                     |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``acclim_ch4``              | Acclimation factor for methanogenic processes in each soil methane layer (-).                 | ch4layer       |
|                             | Only available if :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_ch4_microbe` = TRUE.                     |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+



Soil nitrogen and related fluxes
-------------------------------------------------------------------

.. tabularcolumns:: |p{4.0cm}|p{9.3cm}|p{2.2cm}|

+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| Name                        | Description                                                                                   | Dimensions     |
+=============================+===============================================================================================+================+
| ``n_soil_gb``               | Gridbox total soil nitrogen (organic and inorganic) (kg m\ :sup:`-2`).                        |                |
|                             | Only available if :nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2 or 3.                  |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``ns``                      | Gridbox organic nitrogen in each soil pool and each soil biogeochemistry                      | cspool,cslayer |
|                             | layer (kg m\ :sup:`-2`).                                                                      |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``ns_gb``                   | Gridbox soil organic nitrogen (kg m\ :sup:`-2`).                                              |                |
|                             | Only available if :nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2 or 3.                  |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``n_bio_gb``                | Gridbox soil nitrogen in biomass pool (kg m\ :sup:`-2`).                                      |                |
|                             | Only available if :nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2 or 3.                  |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``n_dpm_gb``                | Gridbox soil nitrogen in decomposable plant material pool (kg m\ :sup:`-2`).                  |                |
|                             | Only available if :nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2 or 3.                  |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``n_rpm_gb``                | Gridbox soil nitrogen in resistant plant material pool (kg m\ :sup:`-2`).                     |                |
|                             | Only available if :nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2 or 3.                  |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``n_hum_gb``                | Gridbox soil nitrogen in humus pool (kg m\ :sup:`-2`).                                        |                |
|                             | Only available if :nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2 or 3.                  |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``n_amm_gb``                | Gridbox soil nitrogen in ammonium pool (kg m\ :sup:`-2`).                                     |                |
|                             | Only available if :nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 3.                       |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``n_nit_gb``                | Gridbox soil ammonium in ammonium pool (kg m\ :sup:`-2`).                                     |                |
|                             | Only available if :nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 3.                       |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``n_inorg_gb``              | Gridbox soil inorganic nitrogen (kg m\ :sup:`-2`).                                            |                |
|                             | Only available if :nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2 or 3.                  |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``n_inorg_avail_pft``       | PFT inorganic nitrogen pool that is available for plant uptake                                | npft           |
|                             | for each soil biogeochemistry layer (kg m\ :sup:`-2`).                                        |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| Soil nitrogen fluxes                                                                                                                         |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``immob_n``                 | Soil nitrogen immobilisation in each soil pool                                                | cspool,cslayer |
|                             | and each soil biogeochemistry layer (kg m\ :sup:`-2` (360days)\ :sup:`-1`).                   |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``immob_n_gb``              | Gridbox mean soil nitrogen immobilisation (kg m\ :sup:`-2` (360days)\ :sup:`-1`).             |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``immob_n_pot``             | Soil potential nitrogen immobilisation in each soil pool                                      | cspool,cslayer |
|                             | and each soil biogeochemistry layer (kg m\ :sup:`-2` (360days)\ :sup:`-1`).                   |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``immob_n_pot_gb``          | Gridbox mean potential soil nitrogen immobilisation (kg m\ :sup:`-2` (360days)\ :sup:`-1`).   |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``minl_n_pot``              | Soil potential nitrogen mineralisation in each pool soil pool                                 | cspool,cslayer |
|                             | and each soil biogeochemistry layer (kg m\ :sup:`-2` (360days)\ :sup:`-1`).                   |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``minl_n_pot_gb``           | Gridbox mean potential soil nitrogen mineralisation (kg m\ :sup:`-2` (360days)\ :sup:`-1`).   |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``minl_n``                  | Soil nitrogen mineralisation in each pool soil pool                                           | cspool,cslayer |
|                             | and each soil biogeochemistry layer (kg m\ :sup:`-2` (360days)\ :sup:`-1`).                   |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``minl_gb``                 | Gridbox mean soil nitrogen mineralisation (kg m\ :sup:`-2` (360days)\ :sup:`-1`).             |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``n_miner_gb``              | Gribox rate of net mineralisation of soil N (kg m\ :sup:`-2` s\ :sup:`-1`).                   |                |
|                             | Only available with the ECOSSE soil model (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model`   |                |
|                             | = 3).                                                                                         |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``n_nitrif_gb``             | Gridbox mean rate of nitrification, expressed as N (kg m\ :sup:`-2` s\ :sup:`-1`).            |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``n_denitrif_gb``           | Gridbox mean rate of denitrification, expressed as N (kg m\ :sup:`-2` s\ :sup:`-1`).          |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``n2o_nitrif_gb``           | Gridbox mean N in N\ :sub:`2`\ O lost during nitrification, including partial nitrification   |                |
|                             | (kg m\ :sup:`-2` s\ :sup:`-1`).                                                               |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``n2o_part_nitrif_gb``      | Gridbox mean N in N\ :sub:`2`\ O lost by partial nitrification (kg m\ :sup:`-2` s\ :sup:`-1`).|                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``n2_denitrif_gb``          | Gridbox mean N in N\ :sub:`2` lost from soil during denitrification                           |                |
|                             | (kg m\ :sup:`-2` s\ :sup:`-1`).                                                               |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``n2o_denitrif_gb``         | Gridbox mean N in N\ :sub:`2`\ O lost during denitrification (kg m\ :sup:`-2` s\ :sup:`-1`).  |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``n2o_soil_gb``             | Gridbox mean N in N\ :sub:`2`\ O flux from soil to atmosphere (kg m\ :sup:`-2` s\ :sup:`-1`). |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``no_soil_gb``              | Gridbox mean N in NO flux from soil to atmosphere (kg m\ :sup:`-2` s\ :sup:`-1`).             |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``n_fertiliser_gb``         | Gridbox nitrogen addition from fertiliser (kg N m\ :sup:`-2` (360days)\ :sup:`-1`).           |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``n_gas_gb``                | Gridbox mean mineralised nitrogen gas emissions (kg m\ :sup:`-2` (360days)\ :sup:`-1`).       |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``n_leach``                 | Gridbox leached nitrogen loss term (kg N m\ :sup:`-2` s\ :sup:`-1`).                          |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+
| ``n_loss``                  | Gridbox nitrogen loss term (fixed fraction of n_inorg) (kg N m\ :sup:`-2`                     |                |
|                             | (360days)\ :sup:`-1`).                                                                        |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+----------------+



Fire
-------------------------------------------------------------------

.. tabularcolumns:: |p{4.0cm}|p{9.3cm}|p{2.2cm}|

+------------------------+------------------------------------------------------------------------------------+------------+
| Name                   | Description                                                                        | Dimensions |
+========================+====================================================================================+============+
| Fire indices                                                                                                             |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_mcarthur``      | McArthur Forest Fire Danger Index (No units)                                       |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_canadian``      | Canadian Fire Weather Index (No units).                                            |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_canadian_ffmc`` | Canadian Fire Weather Index- Fine Fuel Moisture Code (No units).                   |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_canadian_dmc``  | Canadian Fire Weather Index- Duff Moisture Code (No units).                        |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_canadian_dc``   | Canadian Fire Weather Index- Drought Code (No units).                              |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_canadian_isi``  | Canadian Fire Weather Index- Initial Spread Index (No units).                      |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_canadian_bui``  | Canadian Fire Weather Index- Build-up Index (No units).                            |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_nesterov``      | Nesterov Fire Index (No units).                                                    |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| Burnt area                                                                                                               |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``burnt_area``         | PFT burnt area fraction (s\ :sup:`-1`).                                            | npft       |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``burnt_area_gb``      | Gridbox mean burnt area fraction (s\ :sup:`-1`).                                   |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| Fire emissions                                                                                                           |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``emitted_carbon``     | PFT emitted carbon flux (kg m\ :sup:`-2` s\ :sup:`-1`).                            | npft       |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``emitted_carbon_gb``  | Gridbox mean emitted carbon flux (kg m\ :sup:`-2` s\ :sup:`-1`).                   |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``emitted_carbon_DPM`` | Decomposable Plant Material emitted carbon flux (kg m\ :sup:`-2` s\ :sup:`-1`).    |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``emitted_carbon_RPM`` | Resistant Plant Material emitted carbon flux (kg m\ :sup:`-2` s\ :sup:`-1`).       |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_CO2_gb``     | Gridbox mean fire CO2 emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).                |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_CO2_DPM``    | Decomposable Plant Material fire CO2 emission flux (kg m\ :sup:`-2` s\ :sup:`-1`). |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_CO2_RPM``    | Resistant Plant Material fire CO2 emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).    |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_CO_gb``      | Gridbox mean fire CO emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).                 |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_CO_DPM``     | Decomposable Plant Material fire CO emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).  |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_CO_RPM``     | Resistant Plant Material fire CO emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).     |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_CH4_gb``     | Gridbox mean fire CH4 emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).                |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_CH4_DPM``    | Decomposable Plant Material fire CH4 emission flux (kg m\ :sup:`-2` s\ :sup:`-1`). |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_CH4_RPM``    | Resistant Plant Material fire CH4 emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).    |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_NOx_gb``     | Gridbox mean fire NOx emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).                |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_NOx_DPM``    | Decomposable Plant Material fire NOx emission flux (kg m\ :sup:`-2` s\ :sup:`-1`). |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_NOx_RPM``    | Resistant Plant Material fire NOx emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).    |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_SO2_gb``     | Gridbox mean fire SO2 emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).                |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_SO2_DPM``    | Decomposable Plant Material fire SO2 emission flux (kg m\ :sup:`-2` s\ :sup:`-1`). |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_SO2_RPM``    | Resistant Plant Material fire SO2 emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).    |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_OC_gb``      | Gridbox mean fire OC emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).                 |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_OC_DPM``     | Decomposable Plant Material fire OC emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).  |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_OC_RPM``     | Resistant Plant Material fire OC emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).     |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_BC_gb``      | Gridbox mean fire BC emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).                 |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_BC_DPM``     | Decomposable Plant Material fire BC emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).  |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_BC_RPM``     | Resistant Plant Material fire BC emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).     |            |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_CO2``        | PFT fire CO2 emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).                         | npft       |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_CO``         | PFT fire CO emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).                          | npft       |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_CH4``        | PFT fire CH4 emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).                         | npft       |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_NOx``        | PFT fire NOx emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).                         | npft       |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_SO2``        | PFT fire SO2 emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).                         | npft       |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_OC``         | PFT fire OC emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).                          | npft       |
+------------------------+------------------------------------------------------------------------------------+------------+
| ``fire_em_BC``         | PFT fire BC emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).                          | npft       |
+------------------------+------------------------------------------------------------------------------------+------------+



Crops
-------------------------------------------------------------------

These variables are only available when :nml:mem:`JULES_SURFACE_TYPES::ncpft` > 0.

.. tabularcolumns:: |p{3.5cm}|p{9.8cm}|p{2.2cm}|

+---------------------+--------------------------------------------------------------------------------+------------+
| Name                | Description                                                                    | Dimensions |
+=====================+================================================================================+============+
| ``croplai``         | Crop PFT leaf area index (LAI).                                                | ncpft      |
+---------------------+--------------------------------------------------------------------------------+------------+
| ``cropcanht``       | Crop PFT canopy height (m).                                                    | ncpft      |
+---------------------+--------------------------------------------------------------------------------+------------+
| ``cropleafc``       | Crop PFT carbon in leaf parts (kg m\ :sup:`-2`).                               | ncpft      |
+---------------------+--------------------------------------------------------------------------------+------------+
| ``cropstemc``       | Crop PFT carbon in stem parts (kg m\ :sup:`-2`).                               | ncpft      |
+---------------------+--------------------------------------------------------------------------------+------------+
| ``croprootc``       | Crop PFT root carbon pool (kg m\ :sup:`-2`).                                   | ncpft      |
+---------------------+--------------------------------------------------------------------------------+------------+
| ``cropreservec``    | Crop PFT carbon in stem reserve pool (kg m\ :sup:`-2`).                        | ncpft      |
+---------------------+--------------------------------------------------------------------------------+------------+
| ``cropharvc``       | Crop PFT carbon in harvested parts (kg m\ :sup:`-2`).                          | ncpft      |
+---------------------+--------------------------------------------------------------------------------+------------+
| ``cropyield``       | Crop PFT yield carbon (kg m\ :sup:`-2`).                                       | ncpft      |
|                     |                                                                                |            |
|                     | ``cropyield`` is zero in every timestep where there is no harvest, so this     |            |
|                     | variable will mostly be used with :nml:mem:`JULES_OUTPUT_PROFILE::output_type` |            |
|                     | set to 'A' or 'X'.                                                             |            |
+---------------------+--------------------------------------------------------------------------------+------------+
| ``cropdvi``         | Crop PFT developmental index (DVI).                                            | ncpft      |
+---------------------+--------------------------------------------------------------------------------+------------+
| ``cropsowdate``     | PFT sowing date (1.0 to 365.0).                                                | ncpft      |
|                     |                                                                                |            |
|                     | If :nml:mem:`JULES_VEGETATION::l_prescsow` = FALSE then this will always be 0. |            |
+---------------------+--------------------------------------------------------------------------------+------------+
| ``harvest_counter`` | 1 in a timestep where crop is harvested, 0 otherwise.                          | ncpft      |
|                     |                                                                                |            |
|                     | When used with :nml:mem:`JULES_OUTPUT_PROFILE::output_type` = 'A', will count  |            |
|                     | the number of harvests since the beginning of the run.                         |            |
+---------------------+--------------------------------------------------------------------------------+------------+
| ``harvest_trigger`` | Indicates which condition triggered the harvest:                               | ncpft      |
|                     |                                                                                |            |
|                     | 0. No harvest in timestep.                                                     |            |
|                     | 1. Crop reached maturity (DVI=2).                                              |            |
|                     | 2. Crop leaf area index became too high (LAI>15).                              |            |
|                     | 3. Crop has flowered (DVI>1) and temperature in the second soil layer dropped  |            |
|                     |    below :nml:mem:`JULES_CROPPARM::t_mort_io`.                                 |            |
|                     | 4. Crop has flowered (DVI>1), ``cropharvc`` > 0 and                            |            |
|                     |    (``croprootc`` + ``cropleafc`` + ``cropstemc`` + ``cropreservec``) <        |            |
|                     |    :nml:mem:`JULES_CROPPARM::initial_carbon_io`.                               |            |
|                     | 5. :nml:mem:`JULES_VEGETATION::l_prescsow` = T, crop has emerged (DVI>=0), and |            |
|                     |    the day of year is the day before the sowing date.                          |            |
+---------------------+--------------------------------------------------------------------------------+------------+



Trace gas concentrations and fluxes
-------------------------------------------------------------------

.. tabularcolumns:: |p{3.0cm}|p{10.3cm}|p{2.2cm}|

+--------------------+-------------------------------------------------------------------------+------------+
| Name               | Description                                                             | Dimensions |
+====================+=========================================================================+============+
| ``co2_mmr``        | Concentration of atmospheric CO2, expressed as a mass mixing ratio.     |            |
+--------------------+-------------------------------------------------------------------------+------------+
| ``flux_o3_stom``   | PFT flux of O3 to stomata (nmol m\ :sup:`-2` s\ :sup:`-1`).             | npft       |
+--------------------+-------------------------------------------------------------------------+------------+
| ``o3_exp_fac``     | PFT ozone exposure factor.                                              | npft       |
+--------------------+-------------------------------------------------------------------------+------------+
| ``acetone``        | PFT monoterpene emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).           | npft       |
+--------------------+-------------------------------------------------------------------------+------------+
| ``acetone_gb``     | Gridbox mean monoterpene emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).  |            |
+--------------------+-------------------------------------------------------------------------+------------+
| ``isoprene``       | PFT isoprene emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).              | npft       |
+--------------------+-------------------------------------------------------------------------+------------+
| ``isoprene_gb``    | Gridbox mean isoprene emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).     |            |
+--------------------+-------------------------------------------------------------------------+------------+
| ``methanol``       | PFT methanol emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).              | npft       |
+--------------------+-------------------------------------------------------------------------+------------+
| ``methanol_gb``    | Gridbox mean methanol emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).     |            |
+--------------------+-------------------------------------------------------------------------+------------+
| ``terpene``        | PFT monoterpene emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).           | npft       |
+--------------------+-------------------------------------------------------------------------+------------+
| ``terpene_gb``     | Gridbox mean monoterpene emission flux (kg m\ :sup:`-2` s\ :sup:`-1`).  |            |
+--------------------+-------------------------------------------------------------------------+------------+



Water resources
-------------------------------------------------------------------

.. tabularcolumns:: |p{4.5cm}|p{8.8cm}|p{2.2cm}|

+---------------------------+--------------------------------------------------------------------------------+------------+
| Name                      | Description                                                                    | Dimensions |
+===========================+================================================================================+============+
| ``water_demand``          | Demand for water across all water resource sectors (kg).                       |            |
|                           | Only available if :nml:mem:`JULES_WATER_RESOURCES::l_water_resources` = TRUE.  |            |
+---------------------------+--------------------------------------------------------------------------------+------------+
| ``demand_domestic``       | Demand for water for domestic use (kg).                                        |            |
|                           | Only available if :nml:mem:`JULES_WATER_RESOURCES::l_water_domestic` = TRUE.   |            |
+---------------------------+--------------------------------------------------------------------------------+------------+
| ``demand_environment``    | Demand for water for environmental use (kg).                                   |            |
|                           | Only available if :nml:mem:`JULES_WATER_RESOURCES::l_water_environment` = TRUE.|            |
+---------------------------+--------------------------------------------------------------------------------+------------+
| ``demand_industry``       | Demand for water for industrial use (kg).                                      |            |
|                           | Only available if :nml:mem:`JULES_WATER_RESOURCES::l_water_industry` = TRUE.   |            |
+---------------------------+--------------------------------------------------------------------------------+------------+
| ``demand_irrigation``     | Demand for water for irrigation (kg).                                          |            |
|                           | Only available if :nml:mem:`JULES_WATER_RESOURCES::l_water_irrigation` = TRUE. |            |
+---------------------------+--------------------------------------------------------------------------------+------------+
| ``demand_livestock``      | Demand for water for livestock use (kg).                                       |            |
|                           | Only available if :nml:mem:`JULES_WATER_RESOURCES::l_water_livestock` = TRUE.  |            |
+---------------------------+--------------------------------------------------------------------------------+------------+
| ``demand_transfers``      | Demand for water for transfers (kg).                                           |            |
|                           | Only available if :nml:mem:`JULES_WATER_RESOURCES::l_water_transfers` = TRUE.  |            |
+---------------------------+--------------------------------------------------------------------------------+------------+
| ``demand_rate_domestic``  | Demand rate for water for domestic use (kg s\ :sup:`-1`).                      |            |
|                           | Only available if :nml:mem:`JULES_WATER_RESOURCES::l_water_irrigation` = TRUE. |            |
+---------------------------+--------------------------------------------------------------------------------+------------+
| ``demand_rate_industry``  | Demand rate for water for industrial use (kg s\ :sup:`-1`).                    |            |
|                           | Only available if :nml:mem:`JULES_WATER_RESOURCES::l_water_industry` = TRUE.   |            |
+---------------------------+--------------------------------------------------------------------------------+------------+
| ``demand_rate_livestock`` | Demand rate for water for livestock use (kg s\ :sup:`-1`).                     |            |
|                           | Only available if :nml:mem:`JULES_WATER_RESOURCES::l_water_livestock` = TRUE.  |            |
+---------------------------+--------------------------------------------------------------------------------+------------+
| ``demand_rate_transfers`` | Demand rate for water for transfers (kg s\ :sup:`-1`).                         |            |
|                           | Only available if :nml:mem:`JULES_WATER_RESOURCES::l_water_transfers` = TRUE.  |            |
+---------------------------+--------------------------------------------------------------------------------+------------+
| ``irrig_water``           | Water applied as irrigation (kg m\ :sup:`-2` s\ :sup:`-1`).                    |            |
|                           | Only available if :nml:mem:`JULES_IRRIG::l_irrig_dmd` = TRUE.                  |            |
+---------------------------+--------------------------------------------------------------------------------+------------+



Urban
-----

.. tabularcolumns:: |p{3.5cm}|p{9.8cm}|p{2.2cm}|

+---------------+-----------------------------------------------------------------------------------------+------------+
| Name          | Description                                                                             | Dimensions |
+===============+=========================================================================================+============+
| ``wrr``       | Urban morphology: Repeating width ratio (or canyon fraction, W/R).                      |            |
|               | Calculated if :nml:mem:`JULES_URBAN::l_urban_empirical` = TRUE,                         |            |
|               | otherwise it will be the same as the input value (see :ref:`list-of-urban-properties`). |            |
+---------------+-----------------------------------------------------------------------------------------+------------+
| ``hwr``       | Urban morphology: Height-to-width ratio (H/W). See for ``wrr`` above.                   |            |
|               | Only used by MORUSES.                                                                   |            |
+---------------+-----------------------------------------------------------------------------------------+------------+
| ``hgt``       | Urban morphology: Building height (H). See for ``wrr`` above. Only used by MORUSES.     |            |
+---------------+-----------------------------------------------------------------------------------------+------------+



IMOGEN
-------------------------------------------------------------------

.. tabularcolumns:: |p{3.5cm}|p{9.8cm}|p{2.2cm}|

+----------------------+---------------------------------------------------------------------+------------+
| Name                 | Description                                                         | Dimensions |
+======================+=====================================================================+============+
| ``c_emiss_out``      | Prescribed carbon emissions in IMOGEN (Gt / year).                  |            |
|                      | This is a global value repeated over all land points and is only    |            |
|                      | available when IMOGEN is switched on.                               |            |
+----------------------+---------------------------------------------------------------------+------------+
| ``d_land_atmos_co2`` | Change in atmospheric CO2 concentration from land-atmosphere.       |            |
|                      | CO2 feedbacks in IMOGEN (ppm / year). This is a global value        |            |
|                      | repeated over all land points and is only available when IMOGEN     |            |
|                      | is switched on.                                                     |            |
+----------------------+---------------------------------------------------------------------+------------+
| ``d_ocean_atmos``    | Change in atmospheric CO2 concentration from ocean-atmosphere       |            |
|                      | CO2 feedbacks in IMOGEN (ppm / year). This is a global value        |            |
|                      | repeated over all land points and is only available when IMOGEN is  |            |
|                      | switched on.                                                        |            |
+----------------------+---------------------------------------------------------------------+------------+




Grid and indexing variables
-------------------------------------------------------------------

.. tabularcolumns:: |p{2.5cm}|p{10.8cm}|p{2.2cm}|

+--------------------+----------------------------------------------------------------------------------------+------------+
| Name               | Description                                                                            | Dimensions |
+====================+========================================================================================+============+
| ``grid_area``      | Gridbox surface area (m\ :sup:`2`).                                                    | land+sea   |
|                    | Only available if :nml:mem:`JULES_WATER_RESOURCES::l_water_irrigation` = TRUE.  or     |            |
|                    | Only available if :nml:mem:`IMOGEN_ONOFF_SWITCH::l_imogen` = TRUE.                     |            |
+--------------------+----------------------------------------------------------------------------------------+------------+
| ``grid_area_rp``   | River routing gridbox surface area (m\ :sup:`2`).                                      | np_rivers  |
|                    | Only available if :nml:mem:`JULES_RIVERS::l_rivers` = TRUE.                            |            |
|                    | Note that this is defined on the river routing model grid, not on the land point grid. |            |
+--------------------+----------------------------------------------------------------------------------------+------------+
| ``land_index``     | Index (gridbox number) of land points.                                                 |            |
+--------------------+----------------------------------------------------------------------------------------+------------+
| ``lice_index``     | Index (gridbox number) of land ice points.                                             |            |
+--------------------+----------------------------------------------------------------------------------------+------------+
| ``soil_index``     | Index (gridbox number) of soil points.                                                 |            |
+--------------------+----------------------------------------------------------------------------------------+------------+
| ``tile_index``     | Index (gridbox number) of land points with each surface type.                          | ntype      |
+--------------------+----------------------------------------------------------------------------------------+------------+



.. |mu| unicode:: &#x03BC; .. u
