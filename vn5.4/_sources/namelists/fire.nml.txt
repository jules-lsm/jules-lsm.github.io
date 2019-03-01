``fire.nml``
===================

This file contains a single namelist called :nml:lst:`FIRE_SWITCHES` that sets time-invariant parameters for performing wildfire-related calculations.

``FIRE_SWITCHES`` namelist members
-----------------------------------

.. nml:namelist:: FIRE_SWITCHES

.. nml:member:: l_fire

   :type: logical
   :default: F

   Switch to enable the fire module.

   TRUE
       The fire module will be executed according to the settings of subsequent namelist members.

   FALSE
       The fire module will not be executed and subsequent members of the namelist will have no effect.



.. nml:member:: mcarthur_flag

   :type: boolean
   :default: F

   Switch for calculating the McArthur Forest Fire Danger Index (FFDI).


.. nml:member:: mcarthur_opt

   :type: real
   :default: MDI

   Switch for choosing which method of calculating the soil moisture deficit required for the McArthur Forest Fire Danger Index (FFDI). 1 uses the model soil moisture, 2 uses a fixed value of 120 mm.

.. nml:member:: canadian_flag

   :type: boolean
   :default: F

   Switch for calculating the Canadian Fire Weather Index (FWI).

.. nml:member:: canadian_hemi_opt

   :type: boolean
   :default: F

   If TRUE, then the month-dependent parameters used in the calculation will be offset by 6 months for the southern hemisphere. This will cause a discontinuity in results when crossing the equator.

.. nml:member:: nesterov_flag

   :type: boolean
   :default: F

   Switch for calculating the Nesterov Index.
