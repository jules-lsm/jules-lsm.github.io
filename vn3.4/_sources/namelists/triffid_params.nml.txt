``triffid_params.nml``
======================


This file contains a single namelist called :nml:lst:`JULES_TRIFFID` that sets parameters relevant to the TRIFFID submodel.


``JULES_TRIFFID`` namelist members
----------------------------------

.. nml:namelist:: JULES_TRIFFID

This namelist is used to read PFT parameters that are only needed by the dynamic vegetation model (TRIFFID). Values are not used if TRIFFID is not selected.

.. note:: Where a quantity is said to have units of "/360days", this means that it is an amount per 360 days.

.. nml:member:: crop_io

   :type: integer(npft)
   :permitted: 0 or 1
   :default: None

   Flag indicating whether the PFT is a crop.

   Only crop PFTs are allowed to grow in the agricultural area.

   0. Not a crop.
   1. A crop.


.. nml:member:: g_area_io

   :type: real(npft)
   :default: None

   Disturbance rate (/360days).


.. nml:member:: g_grow_io

   :type: real(npft)
   :default: None

   Rate of leaf growth (/360days).


.. nml:member:: g_root_io

   :type: real(npft)
   :default: None

   Turnover rate for root biomass (/360days).


.. nml:member:: g_wood_io

   :type: real(npft)
   :default: None

   Turnover rate for woody biomass (/360days).


.. nml:member:: lai_max_io

   :type: real(npft)
   :default: None

   Maximum LAI.


.. nml:member:: lai_min_io

   :type: real(npft)
   :default: None

   Minimum LAI.

