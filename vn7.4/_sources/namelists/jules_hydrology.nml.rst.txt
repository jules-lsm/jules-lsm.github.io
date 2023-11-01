``jules_hydrology.nml``
=======================


This file sets the hydrology options. It contains one namelist called :nml:lst:`JULES_HYDROLOGY`.



``JULES_HYDROLOGY`` namelist members
-------------------------------------

.. nml:namelist:: JULES_HYDROLOGY

.. nml:member:: l_top

   :type: logical
   :default: F

   Switch for a TOPMODEL-type model of runoff production.

   TRUE
       Use a TOPMODEL-type scheme. This is based on Gedney and Cox (2003); see also Clark and Gedney (2008).

   FALSE
       No TOPMODEL scheme.

   .. seealso::
      References:

      * Gedney, N. and P.M.Cox, 2003 , The sensitivity of global climate model simulations to the representation of soil moisture heterogeneity, J. Hydrometeorology, 4, 1265-1275.
      * Clark and Gedney, 2008, Representing the effects of subgrid variability of soil moisture on runoff generation in a land surface model, Journal of Geophysical Research - Atmospheres, 113, D10111, doi:10.1029/2007JD008940.


.. nml:member:: l_pdm

   :type: logical
   :default: F

   Switch for a PDM-type model of runoff production.

   PDM is the Probability Distributed Model (Moore, 1985), implemented in JULES following Clark and Gedney (2008).

   TRUE
       Use a PDM scheme.

   FALSE
       No PDM scheme.

   .. seealso::
      References:

      * Moore, R. J. (1985), The probability-distributed principle and runoff production at point and basin scales, Hydrol. Sci. J., 30, 273-297.
      * Clark and Gedney, 2008, Representing the effects of subgrid variability of soil moisture on runoff generation in a land surface model, Journal of Geophysical Research - Atmospheres, 113, D10111, doi:10.1029/2007JD008940.


   .. note::
       Setting :nml:mem:`JULES_HYDROLOGY::l_top` = FALSE and :nml:mem:`JULES_HYDROLOGY::l_pdm` = FALSE selects a more basic runoff production scheme. In this scheme, surface runoff comes only from infiltration excess runoff (no saturation excess runoff), and subsurface runoff comes only from free drainage from the deepest soil layer (no lateral flow from mid-layers), as described in Essery et al. (2001, HCTN 30).

.. nml:member:: l_limit_gsoil

   :type: logical
   :default: F

   TRUE
       Limit the soil conductance to the value when the top layer soil moisture is at the critical soil moisture. Below this threshold, the soil conductance follows Best et al. (2011) equation 7. 

   FALSE
       Allow the soil conductance to increase as the top layer soil moisture goes above the critical soil moisture, as in Best et al. (2011) equation 7.


.. nml:group:: Only used if :nml:mem:`JULES_HYDROLOGY::l_top` = TRUE

   .. nml:member:: zw_max

      :type: real
      :default: None

      The maximum allowed depth to the water table (m).

      This is the depth from the soil surface to the bottom of an additional layer that is used to track water tables below the standard soil model (which has layer thicknesses given by :nml:mem:`JULES_SOIL::dzsoil_io`). A value of ~10m can often be used (though the previous default value was 6m) - the suitability of any value depends on values of the ancillary variable ``fexp`` (see :ref:`list-of-topmodel-params`) and the sum of the soil layer thicknesses (denoted `sum_dzsoil` here). The saturated hydraulic conductivity declines exponentially with depth in the additional deep TOPMODEL layer, with decay parameter ``fexp``, and should be sufficiently small at depth ``zw_max`` that the flow at this depth can be neglected, that is  `EXP(-fexp(zw_max-sum_dzsoil))` should be sufficiently small at all locations.  (As a minimum guide, the code tests that the value of this expression is <= 0.05 and a warning is printed where this condition is not met; users should check model output logs for these messages.)


   .. nml:member:: ti_max

      :type: real
      :default: None

      The maximum possible value of the topographic index. A value of 10.0 can be used.

   .. nml:member:: ti_wetl

      :type: real
      :default: None

      A calibration parameter used in the calculation of the wetland fraction.

      It is used to increment the "critical" value of the topographic index that is used to calculate the saturated fraction of the gridbox. It excludes locations with large values of the topographic index from the wetland fraction. A value of 1.5 can be used.


   .. note::
      When TOPMODEL is on (i.e. :nml:mem:`JULES_HYDROLOGY::l_top` = TRUE), JULES follows Gedney & Cox (2003, J Hydromet, eqn 14) in assuming that wetlands occur where gridcell elevation is low enough (assumed to be where topographic index is large enough) that the water table is above the land surface (topidx > :nml:mem:`ti_wetl`) but not above the land surface by enough that streamflow may be assumed to occur (topidx < :nml:mem:`ti_max`). Both :nml:mem:`ti_wetl` and :nml:mem:`ti_max` are levels calibrated from observed wetland fractions. So, if the water table is above the surface then JULES can calculate an areal fraction of total inundation (fsat) and also the areal fraction that is inundated but shallow enough to be stagnant/non-flowing (fwetl, with fwetl<=fsat), which is the 'wetland fraction'.


   .. nml:member:: nfita

      :type: integer
      :default: None

      The number of values tried when fitting wetland and saturation fractions to water table depth in the initialisation. A value of 20 can be used.

      This controls the range of ``cfit`` values tried in
      ``calc_fit_fsat.F90`` where ``cfitmax = 0.15 * nfita``


   .. nml:member:: l_wetland_unfrozen

      :type: logical
      :default: F

   TRUE
      Treat the calculations of wetland and surface saturation fractions more like those of an unfrozen soil.

   FALSE
       Use standard wetland and surface saturation fraction calculations.


.. nml:group:: Only used if :nml:mem:`JULES_HYDROLOGY::l_pdm` = TRUE

   .. nml:member:: dz_pdm

      :type: real
      :default: None

      The depth of soil considered by PDM (m).

      A value of ~1m can be used.


   .. nml:member:: b_pdm

      :type: real
      :default: None

      PDM shape parameter (exponent) of the Pareto distribution controlling spatial variability of storage capacity. A value ~1 can be used. b=0 implies a constant storage capacity at all points.

   .. nml:member:: l_spdmvar

      :type: logical
      :default: F

      TRUE
         Use a linear function of topographic slope to calculate S0/Smax (the minimum soil water storage below which there is no saturation excess runoff from PDM, expressed as a fraction of the maximum storage Smax): S0/Smax=MAX(0.0,1-(slope/:nml:mem:`JULES_HYDROLOGY::slope_pdm_max`)). The slope is read as an ancillary field (see :nml:lst:`JULES_PDM`).

         This function will result in high S0/Smax values for flatter regions and low values for steeper regions, and has been tested for catchments in Great Britain.

      FALSE
          Use a fixed value for S0/Smax, specified in :nml:mem:`JULES_HYDROLOGY::s_pdm`.


   .. nml:group:: Only used if :nml:mem:`l_spdmvar` = TRUE

      .. nml:member:: slope_pdm_max

         :type: real
         :default: None

         The maximum topographic slope (deg) in the linear function of slope to calculate S0/Smax. Slopes above this value will result in a S0/Smax value of zero.

         A value of 6.0 has been tested for slope fields calculated from a high resolution DEM dataset (50m IHDTM for Great Britain).

	 For slopes calculated from coarser DEM datasets, a lower value might be more appropriate as fine-resolution features of the terrain are not included.


   .. nml:group:: Only used if :nml:mem:`l_spdmvar` = FALSE

      .. nml:member:: s_pdm

      :type: real
      :permitted: 0-1
      :default: None

      Minimum soil water storage below which there is no saturation excess runoff from PDM, expressed as a fraction of the maximum storage Smax)

      e.g. A value of 0 indicates that surface saturation can occur for any
      value of water storage. A value of 0.5 would indicate that
      no surface runoff is produced until the soil is 50% saturated.
