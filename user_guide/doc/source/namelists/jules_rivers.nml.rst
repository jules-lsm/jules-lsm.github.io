``jules_rivers.nml``
====================

This file sets the river routing options. It contains two namelists called :nml:lst:`JULES_RIVERS` and :nml:lst:`JULES_OVERBANK`.

River routing introduces two more grids to a JULES run: the river routing input grid and the river routing model grid. The river routing input grid must always be specified as a 2D grid in :nml:lst:`JULES_RIVERS_PROPS`. This is not required to be identical to the input or the model grid. Internally the model compresses this to the river routing model grid, which is a 1D grid with length ``np_rivers``, which is the number of valid routing points in the river routing input grid. All river routing output will be on the river routing model grid, or will be regridded to the model grid.


``JULES_RIVERS`` namelist members
---------------------------------

.. nml:namelist:: JULES_RIVERS

.. nml:member:: l_rivers

   :type: logical
   :default: F

   Switch for enabling river routing.

   TRUE
       Use the river routing algorithm specified by :nml:mem:`i_river_vn` to route runoff along river pathways.

   FALSE
       No river routing.


.. nml:member:: i_river_vn

   :type: integer
   :default: None

   Switch to select the river routing algorithm to use for river routing.

   ``1``
       Use a UM-coupled JULES implementation of the TRIP model (see Oki et al. 1999). This value is not allowed in standalone JULES

   ``2``
       Use a standalone JULES implementation of the RFM kinematic wave model (see Dadson and Bell 2010, Bell et al. 2007, Lewis et al. 2018:Appx. B).

   ``3``
       Use a standalone JULES implementation of the TRIP model (see Oki et al. 1999).

   ``4``
       Use a standalone JULES implementation of the local inertial equation version of the CaMa-Flood model (see Yamazaki et al., 2011, 2013).


.. nml:member:: l_riv_overbank

   :type: logical
   :default: F

   Switch for enabling river overbank inundation. Only used if :nml:mem:`JULES_RIVERS::l_rivers` is TRUE.

   TRUE
       Calculate overbank inundation area (i.e. frac_fplain_lp) as a fraction of gridcell area.

   FALSE
       No overbank inundation calculations

.. note::
   If :nml:mem:`JULES_RIVERS::l_riv_overbank` = FALSE, then optional namelist :nml:lst:`JULES_OVERBANK` is not required.


.. nml:member:: nstep_rivers

   :type: integer
   :permitted: > 0
   :default: None

   The number of model timesteps between calls to river routing.

   For example, :nml:mem:`nstep_rivers` = 5 means that runoff will be accumulated for 5 model timesteps before being routed on the 5th timestep. The relationship between :nml:mem:`nstep_rivers` and the timestep length for river routing depends on the model configuration. For the RFM and TRIP models (:nml:mem:`i_river_vn` = 1, 2 or 3) the timestep length for river routing is :nml:mem:`nstep_rivers` * :nml:mem:`JULES_TIME::timestep_len` seconds (i.e. there is a single timestep per call). For the CaMa-Flood model (:nml:mem:`i_river_vn` = 4) the river routing timestep length is specified separately using :nml:mem:`dt_rivers_len` and typically there will be many river timsteps per call to the river routing.


.. warning::
   The river routing parameter values can be highly dependent on model resolution, so care is required by the user to ensure that appropriate values are selected, tested and adjusted as required.

   Suggested values for global and high-resolution runs are listed below, however these should be treated as a starting point only.


.. nml:group:: TRIP parameters - used if :nml:mem:`i_river_vn` = ``1,3``

   .. nml:member:: rivers_speed

      :type: real
      :permitted: > 0
      :default: None

      The effective river velocity (m s\ :sup:`-1`). See Oki et al. (1999). :nml:mem:`rivers_speed` should equal (river flow velocity / :nml:mem:`rivers_meander`). A value of 0.4 can be used, while Oki et al. (1999) used a value of 0.5.


   .. nml:member:: rivers_meander

      :type: real
      :permitted: > 0
      :default: None

      The ratio of the actual to calculated river lengths in a river routing gridbox. See Oki et al. (1999). Oki & Sud (1998) called this the Meandering Ratio r_M and suggested an average global value of 1.4.

.. nml:group:: TRIP parameters - used if :nml:mem:`i_river_vn` = ``1``

   .. nml:member:: lake_water_conserve_method

      :type: integer
      :default: 1

      Selects different fields for use in water conservation of lake evaporation

      ``1``
          fqw_surft: This is the moisture flux on each tile, in which case the inland water tile is used. Snow sublimation has already been removed from fqw_surft at the point in the code that this is used.

      ``2``
          elake_surft: This is the lake evaporation component of fqw_surft. This avoids the impact that snow melt has on modifying fqw_surft.

   .. nml:member:: trip_globe_shape

      :type: integer
      :default: 2

      The shape of the Earth in the UM-TRIP river routing scheme.
      ``1``
          Spherical: Consistent with other component models (e.g. UM and NEMO) and is better at conserving water when passing water between these other models.
      ``2``
          Ellipsoidal: Closer to the actual shape of the Earth.


.. nml:group:: RFM parameters - used if :nml:mem:`i_river_vn` = ``2``

   .. nml:member:: a_thresh

      :type: integer
      :default: None
      :suggested: 1 (spatial resolution coarser than 20 km gridcells), ~10 (high-resolution)

      The threshold drainage area (specified in number of cells) draining to a gridbox, above which the grid cell is considered to be a river point (see a_T in Bell et al. 2007:541).
      
      Remaining points are treated as land (drainage area = 0) or sea (drainage area < 0). See Bell et al. (2007).


   .. nml:member:: cland

      :type: real
      :permitted: > 0
      :default: None
      :suggested: 0.20 m/s (global), 0.40 m/s (1 km resolution, Bell et al. 2007)

      The land wave speed (kinematic wave speed for surface flow in a land grid box on the river routing grid, m s\ :sup:`-1`). This is the speed at which water moves through surface soil in a non-river grid cell (even without major rivers, there are always minor water courses so these cells do still contribute flow to neighbouring cells).


   .. nml:member:: criver

      :type: real
      :permitted: > 0
      :default: None
      :suggested: 0.62 m/s (global), 0.50 m/s (1 km resolution, Bell et al. 2007)

      The river wave speed (kinematic wave speed for surface flow in a river grid box on the river routing grid, m s\ :sup:`-1`). This value should be close to the :nml:mem:`rivers_speed` used by TRIP, but not identical because RFM makes different assumptions about e.g. meandering.


   .. nml:member:: cbland

      :type: real
      :permitted: > 0
      :default: None
      :suggested: <= :nml:mem:`cland`. 0.10 m/s (global), 0.05 m/s (1 km resolution, Bell et al. 2007)

      The subsurface land wave speed (kinematic wave speed for subsurface flow in a land grid box on the river routing grid, m s\ :sup:`-1`).


   .. nml:member:: cbriver

      :type: real
      :permitted: > 0
      :default: None
      :suggested: <= :nml:mem:`criver`. 0.15 m/s (global), 0.05 m/s (1 km resolution, Bell et al. 2007)

      The subsurface river wave speed (kinematic wave speed for subsurface flow in a river grid box on the river routing grid, m s\ :sup:`-1`).


   .. nml:member:: retl

      :type: real
      :permitted: -1 to 1
      :default: None
      :suggested: 0.005 (1 km resolution, Bell et al. 2007)

      The (resolution dependent) land return flow fraction. Bell et al. (2007:Table1) suggested value 0.005. On non-river grid cells in the land mask: if retl>0 then fraction retl of the subsurface flow moves to the surface per routing timestep; if retl<0 then fraction retl of the surface flow moves to the subsurface per routing timestep.


   .. nml:member:: retr

      :type: real
      :permitted: -1 to 1
      :default: None
      :suggested: 0.005 (1 km resolution, Bell et al. 2007)

      The (resolution dependent) river return flow fraction. On river grid cells in the land mask: if retr>0 then fraction retr of the subsurface flow moves to the surface per routing timestep; if retr<0 then fraction retr of the surface flow moves to the subsurface per routing timestep.


   .. nml:member:: runoff_factor

      :type: real
      :permitted: > 0
      :default: None

      Values !=1.0 are generally used to correct biases in precipitation when the model is forced with observed data **It is highly recommended that this is set to 1.0 (i.e. no runoff adjustment).**


.. nml:group:: CaMa-Flood parameters - i.e. only used if :nml:mem:`i_river_vn` = ``4``

   .. nml:member:: dt_rivers_len
   
      :type: real
      :permitted: >0 and <=( :nml:mem:`JULES_TIME::timestep_len` / :nml:mem:`nstep_rivers` ) and must be a factor of :nml:mem:`nstep_rivers` * :nml:mem:`JULES_TIME::timestep_len`
      :default: none

      Maximum timestep length for CaMa-Flood river routing (s). If an adaptve timestep length is selected (:nml:mem:`l_adapt_timestep` = TRUE) the model will decide whether a shorter timestep should be used.


   .. nml:member:: l_adapt_timestep
   
      :type: logical
      :permitted: TRUE, FALSE
      :default: FALSE

      Switch to select an adaptive timestep length.

      TRUE
          Allow time step to be reduced where flows are large. This is calculated on every call to river routing using an approximate stability condition (see Yamazaki et al., 2013).

      FALSE
          Use a fixed timestep of length :nml:mem:`dt_rivers_len`.


   .. nml:member:: l_sea_level
   
      :type: logical
      :permitted: TRUE, FALSE
      :default: FALSE

      Switch controlling how mean coastal sea levels are set.

      TRUE
          Mean coastal sea level can differ from the level of the coastal land surface, e.g. if there are artificial embankments or levees (where coastal land is lower than mean coastal sea level) or cliffs (where it is higher).
      FALSE
          Mean coastal sea level equals the level of the coastal land surface.

      Note: mean coastal sea level may differ from mean sea level (see note at the end of :nml:lst:`JULES_RIVERS_PROPS`:ref:`list-of-rivers-params`).


   .. nml:member:: l_vary_sea_level
   
      :type: logical
      :permitted: TRUE, FALSE
      :default: FALSE

      Switch activating time variation of sea level at river mouths / coasts.

      TRUE
          Coastal sea level at river mouth includes a time-varying component (e.g. waves, tides or long-term sea level rise), specified via :nml:lst:`JULES_PRESCRIBED`.
      FALSE
          Coastal sea level is constant in time (equal to mean coastal sea level).


   .. nml:member:: length_mouth
   
      :type: real
      :permitted: > 0
      :default: none

      Length of estuary within a (coastal) gridcell, following the channel (m). Used instead of river_distance_grid in calculations at coastal points.


   .. nml:member:: manning_flood
   
      :type: real
      :permitted: > 0
      :default: none
      :suggested: 0.1

      Gauckler–Manning roughness coefficient for river floodplain flow (s.(m^(-1/3))).


   .. nml:group:: Only used if :nml:mem:`l_adapt_timestep` = TRUE
      .. nml:member:: alpha_stability
   
         :type: real
         :permitted: 0 to 1
         :suggested: 0.9

         Coefficient used to improve stability by reducing timestep length below that calculated from the Courant-Friedrichs-Lewy stability condition. Yamazaki et al. (2013) suggest a value of 0.9.      


.. seealso::
   References:

      * Arora VK & Boer GJ (2012). A variable velocity flow routing algorithm for GCMs. Journal of Geophysical Research D 104:30965-30979.
      * Bell, V.A. et al. (2007) Development of a high resolution grid-based river flow model for use with regional climate model output. Hydrology and Earth System Sciences 11:532-549.
      * Dadson, S.J. and Bell, V.A. (2010) Comparison of Grid-2-Grid and TRIP runoff routing schemes. Centre for Ecology & Hydrology Internal Report.
      * Dadson S.J. et al. (2011) Evaluation of a grid-based river flow model configured for use in a regional climate model. Journal of Hydrology 411:238-250.
      * Falloon, P.D. et al (2007) New global river routing scheme in the Unified Model. Hadley Centre Technical Note 72.
      * Jones R., Dadson, S. and Bell, V.A. (2007) Report on European grid-based river-flow modelling for application to Regional Climate Models. Met Office Hadley Centre report.
      * Lewis Huw W. et al. (2018). The UKC2 regional coupled environmental prediction system. Geoscientific Model Development 11:1-42.
      * Oki, T. and Sud, Y.C. (1998). Design of Total Runoff Integrating Pathways (TRIP)—A Global River Channel Network. Earth Interactions 2:1-37.
      * Oki, T., et al (1999). Assessment of annual runoff from land surface models using Total Runoff Integrating Pathways (TRIP). Journal of the Meteorological Society of Japan 77:235-255.
      * Yamazaki, D, Kanae, S, Kim, H and Oki, T (2011). A physically based description of floodplain inundation dynamics in a global river routing model. Water Resources Research 47.
      * Yamazaki, D., et al. (2013). Improving computational efficiency in global river models by implementing the local inertial flow equation and a vector-based river network map. Water Resources Research 49:7221–7235.



``JULES_OVERBANK`` namelist members
-----------------------------------

.. nml:namelist:: JULES_OVERBANK

.. note::
   If :nml:mem:`JULES_RIVERS::l_riv_overbank` = FALSE this namelist is not required.

.. warning::
   The overbank inundation parameter values can be highly dependent on model resolution, so care is required by the user to ensure that appropriate values are selected, tested and adjusted as required.

   Suggested values for global and high-resolution runs are listed below, however these should be treated as a starting point only.

.. nml:member:: l_riv_overbank

   :type: logical
   :default: F

   Switch for enabling river overbank inundation. Only used if :nml:mem:`JULES_RIVERS::l_rivers` is TRUE.

   TRUE
       Calculate overbank inundation area as a fraction of gridcell area.

   FALSE
       No overbank inundation calculations

.. note::
   If :nml:mem:`l_riv_overbank` = FALSE, no further variables are needed from this namelist.

.. nml:member:: overbank_model

   :type: integer
   :permitted: 1, 2, 3, 4
   :default: none

   Choice of model of overbank inundation.

   1. Simple model using an allometric (scaling) relationship to estimate river width, without use of
      topographic data.

   2. Simple model using allometric relationships to estimate river width and depth, and the
      Rosgen (1994) entrenchment ratio, without use of topographic data. When river flow rates are
      higher than the estimated bankfull flow, river width is constrained so that when river
      depth = 2 x bankfull depth then width = :nml:mem:`ent_ratio` * bankfull width.

   3. The inundated area is calculated using a hypsometric integral based on a lognormal area-altitude
      distribution and an allometric relationship to estimate river depth. See Dadson et al. (2010, JGR115)
      for details of the calculation.
      The parameters of the lognormal distribution are specified via :nml:lst:`JULES_OVERBANK_PROPS`.
      (**This is the recommended approach.**)

   4. The inundated area is calculated using an area-altitude distribution specified via ancillaries
      provided in :nml:lst:`JULES_OVERBANK_PROPS`. Note that for this option, a :nml:mem:`JULES_INPUT_GRID::quantile_dim_name`
      must be specified.
      (**This is the recommended approach if appropriate ancillary data are available.**)


.. nml:group:: River width scaling (used if :nml:mem:`overbank_model` = 1 or 2)

   .. nml:group:: River width allometry

      Allometry is: (WIDTH in m) = :nml:mem:`riv_a` * ( (SURFACE RIVER INFLOW in m3 s\ :sup:`-1`) ^ :nml:mem:`riv_b`) (Leopold & Maddock 1953:eqn1)


      .. nml:member:: riv_a

         :type: real
         :default: none
         :permitted: >=0 and <=(1/:nml:mem:`riv_c`)
         :suggested: 7.20 (global, from Andreadis et al. 2013)

         Coefficient in the allometry for river width (units are (m / ((m3/s)^riv_b)), i.e. dependent on the value of riv_b)


      .. nml:member:: riv_b

         :type: real
         :default: none
         :permitted: >=0 and <=(1-:nml:mem:`riv_f`)
         :suggested: 0.50 (global, from Andreadis et al. 2013)

         Exponent in the allometry for river width (dimensionless)


   .. nml:group:: Bankfull flow allometry (used if :nml:mem:`overbank_model` = 2)

      Allometry is: (BANKFULL DISCHARGE RATE QBF in m3 s\ :sup:`-1`) = :nml:mem:`coef_b` * ( (CONTRIBUTING AREA in km2) ^ :nml:mem:`exp_c` ) (see e.g. Andreadis et al. 2013)


      .. nml:member:: coef_b

         :type: real
         :default: none
         :suggested: 0.08 (for "several drainages in western Washington State, USA", Cragun 2005)

         Coefficient in the allometry for bankfull flow (see Sen 2018:eqn3.33).


      .. nml:member:: exp_c

         :type: real
         :default: none
         :suggested: 0.95 (for "several drainages in western Washington State, USA", Cragun 2005)

         Exponent in the allometry for bankfull flow (see Sen 2018:eqn3.33).


      .. nml:member:: ent_ratio

         :type: real
         :default: none

         The Rosgen entrenchment ratio (single value for all water courses in the simulation): when river depth = 2 x bankfull depth then width = :nml:mem:`ent_ratio` * bankfull width (i.e. :nml:mem:`ent_ratio` can be used to specify how wide floodplains are allowed to be).


.. nml:group:: River depth allometry (used if :nml:mem:`overbank_model` = 2 or 3)

   Allometry is: (DEPTH in m) = :nml:mem:`riv_c` * ( (SURFACE RIVER INFLOW in m3 s\ :sup:`-1`) ^ :nml:mem:`riv_f`) (Leopold & Maddock 1953:eqn2)


   .. nml:member:: riv_c

      :type: real
      :default: none
      :permitted: >=0 and <=(1/:nml:mem:`riv_a`)
      :suggested: 0.27 (global, from Andreadis et al. 2013)

      Coefficient in the allometry for river depth (units are (m / ((m3/s)^riv_f)), i.e. dependent on the value of riv_f)


   .. nml:member:: riv_f

      :type: real
      :default: none
      :permitted: >=0 and <=(1-:nml:mem:`riv_b`)
      :suggested: 0.30 (global, from Andreadis et al. 2013)

      Exponent in the allometry for river depth (dimensionless)


.. nml:group:: Elevation quantiles (used if :nml:mem:`overbank_model` = 4)

   Elevation quantiles.


   .. nml:member:: nquantile_elev

      :type: integer
      :default: none
      :permitted: >0
      :suggested: 10

      Number of quantiles used to describe the floodplain elevations. Must equal the number of values permitted for :nml:mem:`JULES_INPUT_GRID::quantile_dim_name`.


.. seealso::
   References:

      * Andreadis KM, Schumann GJ & Pavelsky T (2013). A simple global river bankfull width and depth database. Water Resources Research 49:7164-7168
      * Cragun WS (2005). Discharge-Area relations from Selected Drainages on the Colorado Plateau: A GIS Application. Utah State University, http://hydrology.usu.edu/giswr/archive05/scragun/termproject/
      * Leopold LB & Maddock T (1953). The Hydraulic Geometry of Stream Channels and Some Physiographic Implications. United States Geological Survey Professional Papers 252:1-57
      * Rosgen DL (1994). A classification of natural rivers. Catena 22:169-199.
      * Sen Z (2018). Flood Modeling, Prediction and Mitigation. Springer.
