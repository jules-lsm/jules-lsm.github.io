``jules_snow.nml``
==================


This file sets the snow options and parameters. It contains one namelist called :nml:lst:`JULES_SNOW`.



``JULES_SNOW`` namelist members
-------------------------------

HCTN30 refers to Hadley Centre technical note 30, available from `the Met Office Library <http://www.metoffice.gov.uk/learning/library/publications/science/climate-science-technical-notes>`_.


.. nml:namelist:: JULES_SNOW

.. nml:member:: nsmax

   :type: integer
   :permitted: >= 0
   :default: 0

   Maximum possible number of snow layers.

   0
       A composite soil/snow layer is used. This value gives the behaviour found in JULES2.0 and earlier.

   > 0
       The state of up to ``nsmax`` separate snow layers is modelled. Values of ``nsmax = 3`` or more are recommended.


.. nml:member:: l_snowdep_surf

   :type: logical
   :default: F

   TRUE
       Use equivalent canopy snow depth for surface calculations on surface tiles with a snow canopy.

   FALSE
       No effect.


.. nml:member:: frac_snow_subl_melt

   :type: integer
   :permitted: 0 or 1
   :default: 0

   Switch for use of snow-cover fraction in the calculation of sublimation and melting.

   0. Off
   1. On


.. nml:member:: graupel_options

   :type: integer
   :permitted: 0, 1 or 2
   :default: 0

   Switch for treatment of graupel in the snow scheme

   0. Include graupel as snowfall
   1. Ignore graupel in the surface snowfall
   2. Treat graupel separately

   Always "Include graupel as snowfall" (option 0) in standalone JULES because
   separate snow and graupel driving data are not available.
   If graupel is included in the UM surface snowfall diagnostic
   then JULES can either include this graupel as snow in the surface scheme (option 0),
   ignore this graupel completely, thereby breaking conservation
   of water and energy in the coupled land-atmosphere model (option 1) or
   treat graupel separately (currently this only means allowing graupel to
   fall straight through the canopy)


.. nml:member:: dzsnow

   :type: real(nsmax)
   :default: None

   Prescribed thickness of each snow layer (m).

   Only used if :nml:mem:`nsmax` > 0.

   The interpretation of ``dzsnow`` is slightly complicated and an example of the evolution of the snow layers is given below.

   ``dzsnow`` gives the thickness of each layer when it is not the bottom layer.

   For the top layer, the minimum thickness is ``dzsnow(1)`` and the maximum thickness is ``2 * dzsnow(1)``. For all other layers ``iz``, the minimum thickness is ``dzsnow(iz - 1)``, i.e. the given thickness of the previous layer, and the maximum thickness is ``2 * dzsnow(iz)``, i.e. twice the layer ``dzsnow`` value, except for the last possible layer (:nml:mem:`nsmax`) which has no upper limit.

   As a snowpack deepens, the bottom layer (closest to the soil; label this as layer ``b``) thickens until it reaches its maximum allowed thickness, at which point it will split into a layer of depth ``dzsnow(b)`` and a new bottom layer ``b + 1`` is added to hold the remaining snow. If a layer becomes thinner than its value in ``dzsnow`` it is removed and the snow partitioned between the remaining layers. Whenever a layer splits or is removed, the properties of the layer (e.g. temperature) are allocated to the remaining layers.

   Note that ``dzsnow(nsmax)``, the final thickness, is not used but a value must be input.


.. nml:member:: cansnowpft

   :type: logical(npft)
   :default: F

   Flag indicating whether snow can be held under the canopy of each PFT.

   Only used if :nml:mem:`JULES_VEGETATION::can_model` = 4.

   The model of snow under the canopy is currently only suitable for trees.

   TRUE
       Snow can be held under the canopy.

   FALSE
       Snow cannot be held under the canopy.


.. nml:group:: Radiation parameters

   .. nml:member:: r0

      :type: real
      :default: 50.0

      Grain size for fresh snow (\ |mu|\ m).

      Only used if :nml:mem:`JULES_RADIATION::l_snow_albedo` = TRUE or :nml:mem:`JULES_RADIATION::l_embedded_snow` = TRUE.


   .. nml:member:: rmax

      :type: real
      :default: 2000.0

      Maximum snow grain size (\ |mu|\ m).

      Only used if :nml:mem:`JULES_RADIATION::l_snow_albedo` = TRUE or :nml:mem:`JULES_RADIATION::l_embedded_snow` = TRUE.


   .. nml:member:: snow_ggr

      :type: real(3)
      :default: 0.6, 0.06, 0.23e6

      Snow grain area growth rates (\ |mu|\ m\ :sup:`2` s\ :sup:`-1`).

      Only used if :nml:mem:`JULES_RADIATION::l_snow_albedo` = TRUE or
      :nml:mem:`JULES_RADIATION::l_embedded_snow` = TRUE, and requires
      a snow grain size to calculate the albedo.

      The three values are for melting snow, cold fresh snow and cold
      aged snow respectively, the use of which depends on the setting
      :nml:mem:`i_grain_growth_opt` as follows:

      ============================= ========================= =================================================================
      :nml:mem:`i_grain_growth_opt` Growth rates used         Notes
      ============================= ========================= =================================================================
      0                             :nml:mem:`snow_ggr` (1:3) Uses all values; melting snow, cold fresh snow and cold aged snow
      1                             :nml:mem:`snow_ggr` (1)   Uses values for melting snow only.

                                                              For cold snow a separate scheme is used following
                                                              :ref:`Taillandier et al. (2007)<References_snow>`, where the
                                                              parameters are currently hard-wired.
      ============================= ========================= =================================================================


   .. nml:member:: amax

      :type: real(2)
      :default: 0.98, 0.7

      Maximum albedo for fresh snow.

      Only used if :nml:mem:`JULES_RADIATION::l_snow_albedo` or
      :nml:mem:`JULES_SURFACE::l_elev_land_ice` is TRUE.

      Values 1 and 2 are for VIS and NIR wavebands respectively.

      When:

      :nml:mem:`JULES_RADIATION::l_snow_albedo` = TRUE
	   These parameters are used as limits at all snow-covered
	   grid points.

      :nml:mem:`JULES_RADIATION::l_embedded_snow` = TRUE
	   These parameters are not used.

      :nml:mem:`JULES_SURFACE::l_elev_land_ice` = TRUE
	   Irrespective of whether either of the two previous options
	   are selected, these parameters are used to adjust the albedo
	   of dense snow to a value more appropriate for firn. See
	   also :nml:mem:`aicemax`.


   .. nml:member:: aicemax

      :type: real(2)
      :default: 0.78, 0.36

      Maximum albedo for bare ice

      Only used if :nml:mem:`JULES_SURFACE::l_elev_land_ice` =
      TRUE. See also :nml:mem:`rho_firn_albedo`.

      Values 1 and 2 are for VIS and NIR wavebands respectively.


   .. nml:member:: maskd

      :type: real
      :default: 50.0

      Used in the calculation of the weighting factor for snow in the
      setting of the overall surface albedo, the surface resistance
      and surface melting. It represents the inverse of the e-folding
      depth for masking by snow. A higher value indicates that masking
      by snow is more effective.

      N.B. This was originally used to multiply the snow mass (with a
      standard value of 0.2), but is now used to multiply the snow
      depth.


   .. nml:member:: dtland

      :type: real
      :default: 2.0

      Degrees Celsius below zero at which snow albedo equals cold deep snow albedo.

      This is used only if the diagnostic snow albedo scheme is
      selected, i.e. if :nml:mem:`JULES_RADIATION::l_snow_albedo` =
      FALSE and :nml:mem:`JULES_RADIATION::l_embedded_snow` =
      FALSE. This is 2.0 in HCTN30 Eq4.

      Must not be zero.


   .. nml:member:: kland_numerator

      :type: real
      :default: 0.3

      Used in snow-ageing effect on albedo.

      This is used only if the diagnostic snow albedo scheme is
      selected, i.e. if :nml:mem:`JULES_RADIATION::l_snow_albedo` =
      FALSE and :nml:mem:`JULES_RADIATION::l_embedded_snow` =
      FALSE. This is 2.0 in HCTN30 Eq4.

      ``kland`` is computed by dividing this value by
      :nml:mem:`dtland` - see HCTN30 Eq4.


   .. nml:member:: can_clump

      :type: real(npft)
      :default: MDI

      Clumping parameter for snow on the canopy in calculation of albedo.

      Only used if :nml:mem:`JULES_VEGETATION::can_model` = 4,
      :nml:mem:`JULES_RADIATION::l_embedded_snow` = TRUE and
      :nml:mem:`cansnowpft` = TRUE on that surface tile.

      The model of snow under the canopy is currently only suitable
      for trees.

      The inverse of this parameter specifies the fraction of the
      canopy over which snow is distributed when calculating the
      albedo. It should not be less than 1 and higher values indicate
      that snow on a canopy is more clumped, leaving more of the bare
      canopy exposed.


   .. nml:member:: n_lai_exposed

      :type: real(npft)
      :default: MDI

      LAI distribution parameter for calculation of snow albedo.

      A power-law distribution of leaf area density is assumed within
      the canopy for calculating masking of snow by vegetation using
      the embedded scheme. Higher values indicate that snow is more
      effective in covering vegetation.

      Only used if :nml:mem:`JULES_RADIATION::l_embedded_snow` = TRUE.


   .. nml:member:: lai_alb_lim_sn

      :type: real(npft)
      :default: MDI

      Minimum LAI in calculation of albedo in the presence of snow.

      A minimum albedo is imposed when calculating the albedo of plant
      canopies (historically 0.5). This parameter allows it to be set
      for each PFT in the presence of snow. Crudely, it represents the
      stem area of vegetation remaining when the true LAI is 0. A
      separate variable, :nml:mem:`JULES_PFTPARM::lai_alb_lim_io` is
      used in the absence of snow.


.. nml:group:: Other snow parameters

   .. nml:member:: rho_snow_const

      :type: real
      :default: 250.0

      Constant density of lying snow (kg m\ :sup:`-3`).

      If :nml:mem:`nsmax` = 0, snow is modelled as a single layer of
      constant density using this value.

      If :nml:mem:`nsmax` > 0, snow density is prognostic, except for
      snow on the canopy when :nml:mem:`cansnowpft` is TRUE, and for
      thin layers of snow when :nml:mem:`nsmax` > 0.


   .. nml:member:: rho_snow_fresh

      :type: real
      :default: 100.0

      Density of fresh snow (kg m\ :sup:`-3`).

      Only used if :nml:mem:`nsmax` > 0.

   .. nml:member:: rho_firn_albedo

      :type: real
      :default: 550.0

      Only used if :nml:mem:`JULES_SURFACE::l_elev_land_ice` = TRUE.

      This is the threshold density (as measured over the ~top 10 cm,
      depending on how the :nml:mem:`dzsnow` layers are specified) at
      which the grain-size calculation of prognostic snow albedo will
      switch to one dependent on the surface density of the
      snowpack. Albedo is linearly scaled between :nml:mem:`amax` for
      :nml:mem:`rho_snow_const` and :nml:mem:`aicemax` for density the
      of ice (917 kg m\ :sup:`-3`).


   .. nml:member:: snow_hcon

      :type: real
      :default: 0.265

      Thermal conductivity of lying snow (W m\ :sup:`-1` K\
      :sup:`-1`).

      This value is used for all snow if :nml:mem:`nsmax` = 0, but only
      for thin snow if :nml:mem:`nsmax` > 0.  See HCTN30 Eq.42. for its
      application.


   .. nml:member:: snow_hcap

      :type: real
      :default: 0.63e6

      Thermal capacity of lying snow (J K\ :sup:`-1` m\ :sup:`-3`).


   .. nml:member:: snowliqcap

      :type: real
      :default: 0.05

      Liquid water holding capacity of lying snow, as a fraction of snow mass.

      Only used if :nml:mem:`nsmax` > 0.


   .. nml:member:: snowinterceptfact

      :type: real
      :default: 0.7

      Constant in relationship between mass of intercepted snow and snowfall rate.

      Only used if :nml:mem:`JULES_VEGETATION::can_model` = 4.


   .. nml:member:: snowloadlai

      :type: real
      :default: 4.4

      Ratio of maximum canopy snow load to leaf area index (kg m\ :sup:`-2`).

      Only used if :nml:mem:`JULES_VEGETATION::can_model` = 4.


   .. nml:member:: snowunloadfact

      :type: real
      :default: 0.4

      Constant in relationship between canopy snow unloading and canopy snow melt rate.

      Only used if :nml:mem:`JULES_VEGETATION::can_model` = 4.


   .. nml:member:: unload_rate_cnst

      :type: real(npft)
      :default: MDI

      Constant term in the background unloading rate for snow on the
      canopy. Snow is unloaded from the canopy as a background process
      or because it is melting.

      Only used if :nml:mem:`JULES_VEGETATION::can_model` = 4 and
      :nml:mem:`cansnowpft` = TRUE on that surface tile.


   .. nml:member:: unload_rate_u

      :type: real(npft)
      :default: MDI

      Term proportional to wind speed in the background unloading rate
      for snow on the canopy.

      Only used if :nml:mem:`JULES_VEGETATION::can_model` = 4 and
      :nml:mem:`cansnowpft` = TRUE on that surface tile.


   .. nml:member:: i_snow_cond_parm

      :type: integer
      :permitted: 0 or 1
      :default: MDI

      Scheme used to calculate the conductivity of snow

      Only used if :nml:mem:`nsmax` > 0.

      Two parametrizations of snow conductivity are available
      taken from the papers of :ref:`Yen (1981)<References_snow>` and
      :ref:`Calonne et al. (2011)<References_snow>`.

      0. :ref:`Yen (1981)<References_snow>`
      1. :ref:`Calonne et al. (2011)<References_snow>`


   .. nml:member:: l_et_metamorph

      :type: logical
      :default: F

      This parametrization follows the form used by e.g. :ref:`Dutra
      et al. (2010)<References_snow>`.

      Only used if :nml:mem:`nsmax` > 0.

      TRUE
          Include the effect of thermal metamorphism on the snow density.

      FALSE
          No effect.


   .. nml:member:: l_snow_infilt

      :type: logical
      :default: F

      Only used if :nml:mem:`nsmax` > 0.

      TRUE
          Pass rainfall and melting from the canopy to the snowpack as
	  infiltration.

      FALSE
          No effect.


   .. nml:member:: l_snow_nocan_hc

      :type: logical
      :default: F

      Only used if :nml:mem:`nsmax` > 0.

      TRUE
          Do not include the canopy heat capacity in the surface energy balance at the top of the snow pack on surface tiles without a canopy snow model.

      FALSE
          The canopy heat capacity is included in the surface energy balance at the top of the snow pack.


   .. nml:member:: a_snow_et

      :type: real
      :default: MDI

      Constant in parametrization of thermal metamorphism.

      Only used if :nml:mem:`l_et_metamorph` = TRUE.

   .. nml:member:: b_snow_et

      :type: real
      :default: MDI

      Constant in parametrization of thermal metamorphism.

      Only used if :nml:mem:`l_et_metamorph` = TRUE.

   .. nml:member:: c_snow_et

      :type: real
      :default: MDI

      Constant in parametrization of thermal metamorphism.

      Only used if :nml:mem:`l_et_metamorph` = TRUE.

   .. nml:member:: rho_snow_et_crit

      :type: real
      :default: MDI

      Critical density in parametrization of thermal metamorphism.

      Only used if :nml:mem:`l_et_metamorph` = TRUE.


   .. nml:member:: i_grain_growth_opt

      :type: integer
      :permitted: 0 or 1
      :default: 0

      Scheme used to calculate the rate of growth of snow grains.

      0. Invokes the original scheme based on :ref:`Marshall
	 (1989)<References_snow>`, with no dependence of the rate of
	 growth of small grains on the temperature.

      1. Invokes the scheme for growth of snow grains proposed by
	 :ref:`Taillandier et al. (2007)<References_snow>` for
	 equitemperature metamorphism. Growth is significantly
	 slower than the default scheme at low temperatures.


   .. nml:member:: i_relayer_opt

      :type: integer
      :permitted: 0 or 1
      :default: 0

      Scheme used to relayer the snowpack.

      Only used if :nml:mem:`nsmax` > 0.

      0. Invokes the original scheme with relayering of the grain size
	 involving the grain size itself.
      1. Relayering is done using the inverse of the grain size. This
	 is more consistent with conserving the specific surface area
	 of snow, though full conservation would require mass
	 weighting to be invoked during regridding.


   .. nml:member:: i_basal_melting_opt

      :type: integer
      :permitted: 0 or 1
      :default: 0

      Option to treat basal melting of the snow pack.

      When snow falls on warm ground, it will melt from the base of
      the snowpack, where the temperature of the snow will rise to the
      melting point. The 0-layer snow scheme, which is used for thin
      snow even when the multilayer scheme is selected, did not
      represent this process and included only melting at the surface.

      0. Default: Basal melting is omitted.
      1. Basal melting takes place instantaneously if the temperature
	 of the first soil layer is above freezing, until the snow is
	 removed or the temperature of soil layer is reduced to
	 freezing.





Example of the evolution of snow layer thickness
------------------------------------------------

The table below gives an example of how the number and thickness of snow layers varies with total snow depth for the case of :nml:mem:`nsmax` = 3 and ``dzsnow = (0.1, 0.15, 0.2)``. Note that if the values given by the user for :nml:mem:`dzsnow` are a decreasing series with ``dzsnow(i) <= 2 * dzsnow(i - 1)``, the algorithm will result in layers ``i`` and ``i + 1`` being added at the same time. Don't panic - this should not be a problem for the simulation.

.. tabularcolumns:: |p{3cm}|p{1.5cm}|p{3cm}|p{7cm}|

+--------------------+-----------+----------------------+---------------------------------------------------------------------------------+
| Snow depth (m)     | Number    | Layer thickness,     | Comments                                                                        |
|                    | of layers | uppermost layer      |                                                                                 |
|                    |           | first (m)            |                                                                                 |
+====================+===========+======================+=================================================================================+
| ``d < 0.1``        | 0         |                      | While the depth of snow is less than ``dzsnow(1)``, the layer model is not      |
|                    |           |                      | active and snow and soil are combined in a composite layer.                     |
+--------------------+-----------+----------------------+---------------------------------------------------------------------------------+
| ``0.1 <= d < 0.2`` | 1         | Total snow depth     | The single layer grows until it is twice as thick as ``dzsnow(1)``.             |
+--------------------+-----------+----------------------+---------------------------------------------------------------------------------+
| ``0.2 <= d < 0.4`` | 2         | 0.1, remainder       | Above 0.2m, the single layer splits into a top layer of 0.1m and the remaining  |
|                    |           |                      | snow in the bottom layer.                                                       |
+--------------------+-----------+----------------------+---------------------------------------------------------------------------------+
| ``>= 0.4``         | 3         | 0.1, 0.15, remainder | At 0.4m depth, layer 2 (which has grown to 0.3m thick, i.e. ``2 * dzsnow(2)``), |
|                    |           |                      | splits into a layer of 0.15m and a new bottom layer holding the the remaining   |
|                    |           |                      | 0.15m. As all layers are now in use, any subsequent deepening of the pack is    |
|                    |           |                      | dealt with by increasing the thickness in this bottom layer.                    |
+--------------------+-----------+----------------------+---------------------------------------------------------------------------------+



.. |mu| unicode:: &#x03BC; .. u

.. _References_snow:

``JULES_SNOW`` references
-------------------------------

* Calonne, N., Flin, F., Morin, S., Lesaffre, B., du
  Roscoat, S. Rolland, and Geindreau, C. (2011). Numerical and
  experimental investigations of the effective thermal conductivity of
  snow, Geophys. Res. Lett., 38, L23501,
  https://doi.org/10.1029/2011GL049234.
* Dutra, E., Balsamo, G., Viterbo, P., Miranda, P. M., Beljaars, A.,
  Schar, C., and Elder, K. (2010). An improved snow scheme for the ECMWF land
  surface model: Description and offline validation, J. Hydrometeorol.,
  11, 899–916, https://doi.org/10.1175/2010JHM1249.1.
* Marshall, S.E. (1989). A physical parameterization of snow albedo for
  use in climate models. NCAR Cooperative Thesis 123. Boulder, CO :
  National Center for Atmospheric
  Research. https://atmos.washington.edu/~sgw/PAPERS/1989_Marshall.pdf
* Taillandier, A.-S., F. Domine, W. R. Simpson, M. Sturm,
  and T. A. Douglas (2007). Rate of decrease of the specific surface
  area of dry snow: Isothermal and temperature gradient
  conditions, J. Geophys. Res., 112, F03003,
  https://doi.org/10.1029/2006JF000514.
* Yen, Y.-C. (1981). Review of thermal properties of snow, ice and sea
  ice. Cold Regions Research and Engineering Laboratory (CRREL) Report
  81-10.  https://hdl.handle.net/11681/9469
