``triffid_params.nml``
======================


This file contains a single namelist called :nml:lst:`JULES_TRIFFID` that sets parameters relevant to the TRIFFID submodel.


``JULES_TRIFFID`` namelist members
----------------------------------

.. nml:namelist:: JULES_TRIFFID

This namelist is used to read PFT parameters that are only needed by the dynamic vegetation model (TRIFFID). Values are not used if TRIFFID is not selected.

.. note:: Where a quantity is said to have units of "/360days", this means that it is an amount per 360 days.

.. note:: If the crop model is on (i.e. :nml:mem:`JULES_SURFACE_TYPES::ncpft` > 0), only ``nnpft = npft - ncpft`` values will be used for each variable.


.. nml:member:: crop_io

   :type: integer(npft)
   :permitted: 0,1,2,3
   :default: None

   Flag indicating whether the PFT is natural, crop, or pasture. Only
   crop / pasture PFTs are allowed to grow in the agricultural
   area. See :nml:mem:`JULES_VEGETATION::l_trif_crop` for more
   details.

   | If :nml:mem:`JULES_VEGETATION::l_trif_crop` is FALSE permitted values of ``crop_io`` are 0 and 1.

   0. Natural vegetation (not a crop).
   1. A crop.

   | If :nml:mem:`JULES_VEGETATION::l_trif_crop` is TRUE permitted values of ``crop_io`` are 0, 1 and 2.

   0. Natural vegetation (neither crop nor pasture).
   1. Crop.
   2. Pasture.

   | If :nml:mem:`JULES_VEGETATION::l_trif_biocrop` is TRUE permitted values are 0, 1, 2 and 3. Flag indicating whether the PFT is natural, crop, pasture, or bioenergy. See :nml:mem:`JULES_VEGETATION::l_trif_biocrop` for more details.

   0. Natural vegetation.
   1. Crop.
   2. Pasture.
   3. Bioenergy crops or trees. 

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


.. nml:member:: alloc_fast_io

   :type: real(npft)
   :default: None

   Fraction of the carbon flux from vegetation to wood products to add to the rapidly decaying wood products pool (wood_prod_fast).


.. nml:member:: alloc_med_io

   :type: real(npft)
   :default: None

   Fraction of the carbon flux from vegetation to wood products to add to the wood products pool with a moderate decay rate (wood_prod_med).


.. nml:member:: alloc_slow_io

   :type: real(npft)
   :default: None

   Fraction of the carbon flux from vegetation to wood products to add to the slowly decaying wood products pool (wood_prod_slow).

.. nml:member:: retran_l_io

   :type: real(npft)
   :default: 0.5

   Fraction of retranslocated leaf N.

.. nml:member:: retran_r_io

   :type: real(npft)
   :default: 0.2

   Fraction of retranslocated root N.

.. nml:member:: ag_expand_io

   :type: integer(npft)
   :permitted: 0,1
   :default: 0

   Only used if :nml:mem:`JULES_VEGETATION::l_ag_expand` = TRUE.

   0. No automatic expansion of PFT area when the agricultural area increases.
   1. Automatically plant out new crop areas with the selected PFT.

.. nml:group:: Only used when :nml:mem:`JULES_VEGETATION::l_trif_biocrop` = TRUE  

   .. nml:member:: harvest_type_io

      :type: integer(npft)
      :permitted: 0,1,2
      :default: 0

      0. No harvest (default).
      1. Continuous harvest from litter, as per :nml:mem:`JULES_VEGETATION::l_trif_crop`.
      2. Periodic harvesting.

      .. note:: For "natural" PFTs (:nml:mem:`JULES_TRIFFID::crop_io` = 0), this must be set to 0. For agricultural PFTs, this can be set to 0, 1 or 2.

   .. nml:group:: Only used when :nml:mem:`JULES_TRIFFID::harvest_type_io` = 2 

      A placeholder value must be used for all other PFTs.

      .. nml:member:: harvest_freq_io

         :type: integer(npft)
         :permitted: >= 0
         :default: none

         Harvest freqency in years. 

      .. nml:member:: harvest_ht_io

         :type: real(npft)
         :permitted: > 0
         :default: none

         Height [m] to which the PFT is reduced at each harvest cycle. 

      .. note:: :nml:mem:`lai_min_io` must be set such that PFT height at :nml:mem:`lai_min_io` <= :nml:mem:`harvest_ht_io`, otherwise JULES will not start (the required value will be shown in error output). 

