``science_fixes.nml``
=====================


This file contains one namelist called :nml:lst:`JULES_TEMP_FIXES`.

This namelist sets 'short-term' temporary logicals used to protect science bug
fixes that lead to alterations in science results. It is expected that these
logicals will be short lived as the preference should be for all configurations
to use the corrected code. However, to maintain short term reproducibility of
results across JULES versions the fixes are protected by logicals until the
fixes become the default in all model configurations at which point the logical
is retired. See module for when the switch is due for review.

``JULES_TEMP_FIXES`` namelist members
-------------------------------------

.. nml:namelist:: JULES_TEMP_FIXES

.. nml:member:: ctile_orog_fix

   :type: integer
   :permitted: 0-2
   :default: 2

   If nonzero, corrects the surface exchange calculations in coastally
   tiled grid-boxes, assuming that the lowest level is physically
   terrain following and adjusting the temperature of the land/sea
   portions in accordance with their relative offset from the grid-box
   mean height using a dry/moist lapse rate where appropriate. Option 2
   will only adjust values over the sea.

.. nml:member:: l_accurate_rho

   :type: logical
   :default: F

   This switch improves the calculation of surface air density in the  
   surface turbulent fluxes.  It includes appropriate use of dry air density 
   when the atmospheric water vapour is expressed as a mixing ratio 
   (l_mr_physics = .TRUE.), otherwise use the wet air density when 
   it is expressed as a specific humidity. 


.. nml:member:: l_dtcanfix

   :type: logical
   :default: F

   This switch corrects a bug in the evolution of the skin temperature in
   the implicit solver,
   whereby the change in the skin temperature is
   artificially constrained. This generally has a small effect,
   but can
   cause unphysical results if a canopy with a large heat capacity is
   coupled to an underlying substrate with a small heat capacity.

.. nml:member:: l_fix_alb_ice_thick

   :type: logical
   :default: F

   When zero-layer sea ice is used the thermodynamics is calculated in the
   UM through an effective thickness calculated from snow and ice thicknesses
   and associated thermal conductivities. With multi-layer sea ice the
   thermodynamics is calculated in the sea ice component of the model, and
   the effective thickness is no longer required.  However, it was still
   being used erroneously. This fix removes the effective thickness
   adjustment when multi-layer sea ice is used.

.. nml:member:: l_fix_albsnow_ts

   :type: logical
   :default: F

   The original version of the two-stream scheme to calculate the albedo
   of snow in JULES contains a bug in the calculation of the reflection
   coefficient that renders very thin layers of snow too reflective.
   This logical applies the appropriate correction when it is enabled.

.. nml:member:: l_fix_lake_ice_temperatures

   :type: logical
   :default: F

   If true, allows sea ice temperatures in lakes to evolve over time
   for coupled models when the lake is defined as a sea point but is
   not coupled to an ocean model.

.. nml:member:: l_fix_moruses_roof_rad_coupling

   :type: logical
   :default: F

   If true, this switch corrects a bug in the surface energy balance 
   when the MORUSES radiative roof coupling is used
   (see :nml:mem:`JULES_URBAN::l_moruses_storage`). 
   If false, the thermal conductivity of the soil (hcons) is erroneously
   set to zero, which causes the roof to be effectively uncoupled when
   :nml:mem:`JULES_VEGETATION::l_vegcan_soilfx`.

.. nml:member:: l_fix_neg_snow

   :type: logical
   :default: F

   When set to  false, the original formulations of melting, interception
   and unloading of canopy snow are used. These may result in the generation
   of negative snow amounts. Firstly, the original formulation of the
   melting of canopy snow is incorrect and excessive melting may be
   generated, reducing the mass of snow below 0. This fix corrects this.
   Secondly,the interception of snow on an overloaded canopy will, under
   the original method of calculation, be negative. With the fix, this is
   set to 0 and any snow above the canopy snow capacity is unloaded.
   Overloaded canopies may be produced by changess in the snow amounts or
   by reductions in the LAI from which the canopy capacity is calculated.

.. nml:member:: l_fix_osa_chloro

   :type: logical
   :default: F

   When set to false, the chlorophyll content used to determine the optical
   properties of water, for the ocean surface albedo, are specified in gm-3
   when the parameterisation they use is defined in mg m-3.
   It is a short term logical until the code becomes the new default.

.. nml:member:: l_fix_snow_frac

   :type: logical
   :default: F

   When set to  false, there is the potential to have small snow mass, but a
   zero snow fraction due to machine precision in the calculations. This
   prevents sublimation or snow melt from removing the remaining snow mass,
   hence small values can persist.
   In addition to this there is a conceptual bug in the calculation of
   the fraction of potential evaporation because it does not add in canopy
   evaporation when the snow fraction is less than one.
   When set to true these issues are corrected and in addition the radiation
   calculations for snow fraction are also made consistent.

.. nml:member:: l_fix_ustar_dust

   :type: logical
   :default: F

   If true, corrects how ustar is calculated in the exchange
   coefficient for dust deposition

.. nml:member:: l_fix_wind_snow

   :type: logical
   :default: F

   If true, ensures that wind speed is calculated for use in snow unloading.
   If false, the wind speed for unloading will be zero on timesteps when
   10m wind diagnostics are not calculated. This will tend to leave more
   snow on the vegetation.
   It is a short term logical until the code becomes the new default.

