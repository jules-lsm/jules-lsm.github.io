``jules_irrig.nml``
========================


This file sets the irrigation options. It contains one namelist called :nml:lst:`JULES_IRRIG`.


``JULES_IRRIG`` namelist members
--------------------------------

.. nml:namelist:: JULES_IRRIG

This namelist specifies the different options available for setting up the irrigation.

.. note::

  Irrigation can be applied at a constant rate in three ways:
   * 1. To apply a constant irrigation to all surface tiles the irrigation settings are as follows: frac_irrig_all_tiles=T, set_irrfrac_on_irrtiles=F and set a value for :nml:mem:`JULES_IRRIG_PROPS::const_frac_irr`.
   * 2. To apply a constant irrigation to only specific surface tiles the irrigation settings are as follows: frac_irrig_all_tiles=F and set_irrfrac_on_irrtiles=T and set a value for :nml:mem:`JULES_IRRIG_PROPS::const_irrfrac_irrtiles`.
   * 3. To apply a constant irrigation to specific surface tiles as an average across the gridbox, which is the way irrigation on specific tiles was done prior to vn5.7, the irrigation settings are as follows: frac_irrig_all_tiles=F, set_irrfrac_on_irrtiles=F and set a value for :nml:mem:`JULES_IRRIG_PROPS::const_frac_irr`.

  In both option 2 and 3, :nml:mem:`irrigtiles` is the index of surface tiles you wish to irrigate, the length of which is :nml:mem:`nirrtile` e.g. if you include wheat and maize in your run at index 5 and 6 then irrigtiles=5,6 and nirrtile=2.

.. nml:member:: l_irrig_dmd

   :type: logical
   :default: F

   Switch controlling the implementation of irrigation demand code.

   TRUE
      Tiles are irrigated.

   FALSE
      No effect.

   This must be set to TRUE if :nml:mem:`JULES_WATER_RESOURCES::l_water_irrigation` = TRUE.


.. nml:member:: l_irrig_limit

   :type: logical
   :default: F

   Switch controlling whether the amount of water used to irrigate tiles is limited.

   TRUE
      Water for irrigation is taken first from the deep soil
      (groundwater) store, and then from the river storage when the
      deep soil store is exhausted. Tiles are irrigated up to the
      critical point if the necessary water is available. This option
      requires :nml:mem:`JULES_IRRIG::l_irrig_dmd` = TRUE,
      :nml:mem:`JULES_HYDROLOGY::l_top` = TRUE,
      :nml:mem:`JULES_RIVERS::l_rivers` = TRUE and
      :nml:mem:`JULES_RIVERS::i_river_vn` = ``1,3``.

      .. warning::
         The irrigation supply code in JULES is still in development,
  	 and is available in this release to support beta testing
  	 activities.

         Users should ensure that results are as expected, and provide
  	 feedback where deficiencies are identified.

   FALSE
      Tiles will be irrigated to critical point from an unconstrained water supply.


   This must be set to FALSE if :nml:mem:`JULES_WATER_RESOURCES::l_water_irrigation` = TRUE.

.. nml:member:: irr_crop

   :type: integer
   :permitted: 0, 1 or 2
   :default: 0

   0. Irrigation season (i.e. season in which crops might be growing
      on the gridbox) lasts the entire year.

   1. Irrigation season is determined from driving data according to
      :ref:`Döll & Siebert (2002)<References_irrig>` method. No irrigation
      is applied outside the irrigation season.

   2. Irrigation season is determined by maximum dvi across all
      surface tiles. Requires :nml:mem:`JULES_SURFACE_TYPES::ncpft` > 0. No
      irrigation is applied outside the irrigation season.


.. nml:member:: frac_irrig_all_tiles

   :type: logical
   :default: T

   If T, then irrigation fraction is applied to all surface tiles, and F, it is applied only to the surface tiles specified in :nml:mem:`irrigtiles`.


.. nml:member:: set_irrfrac_on_irrtiles

   :type: logical
   :default: F

   If F then irrigation is applied as an average across the gridbox and not to specific surface tiles. If T, then the irrigation fraction is only applied to the surface tile specified in :nml:mem:`irrigtiles`. Both :nml:mem:`frac_irrig_all_tiles` and :nml:mem:`set_irrfrac_on_irrtiles` cannot be set to T.


.. nml:member:: nirrtile

   :type: integer
   :default: None

   The number of surface tiles to be irrigated. Only used if :nml:mem:`frac_irrig_all_tiles` = F.


.. nml:member:: irrigtiles

   :type: integer(nirrtile)
   :default: None

   Indices of the surface tiles to be irrigated. Only used if :nml:mem:`frac_irrig_all_tiles` = F.


.. nml:member:: nstep_irrig

   :type: integer
   :permitted: > 0
   :default: 86400/:nml:mem:`JULES_TIME::timestep_len`

   The number of model timesteps per irrigation update step

   Irrigation will be updated every :nml:mem:`nstep_irrig` timesteps. For example, with a model timestep of 1 hour, :nml:mem:`nstep_irrig` = 24 means that irrigation will be updated on the 24th timestep, i.e. daily updates.

   :nml:mem:`nstep_irrig` = NINT(frequency of irrigation update (in sec)) / :nml:mem:`JULES_TIME::timestep_len`)


.. _References_irrig:

``JULES_IRRIG`` references
-------------------------------

* Döll, P., and Siebert, S., Global modeling of irrigation water
  requirements, Water Resour. Res., 38(4),
  https://doi.org/10.1029/2001WR000355, 2002.
