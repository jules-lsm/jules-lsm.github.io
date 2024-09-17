``red_params.nml``
======================


This file contains a single namelist called :nml:lst:`JULES_RED` that sets parameters relevant to the Robust Ecosystem Demography submodel (RED version 1.0) <https://gmd.copernicus.org/articles/13/4067/2020/>`_.


``JULES_RED`` namelist members
----------------------------------

.. nml:namelist:: JULES_RED

This namelist is used to read PFT parameters that are only needed by the Robust Ecosystem Demography (RED). Values are not used if RED is not selected.

.. note:: Where a quantity is said to have units of "/360days", this means that it is an amount per 360 days.

.. nml:group:: Only used when :nml:mem:`JULES_VEGETATION::l_veg3 = TRUE  

.. nml:member:: alpha_recrt

   :type: real(npft)
   :default: None

   The fraction of PFT carbon assimilate devoted to reproduction.


.. nml:member:: crown_area0

   :type: real(npft)
   :default: None

   The lowest PFT crown area, value corresponds to the mass0 class (m2).


.. nml:member:: height0

   :type: real(npft)
   :default: None

   The lowest PFT height, vlue corresponds to the mass0 class (m).


.. nml:member:: lai_bal0

   :type: real(npft)
   :default: None

   The lowest PFT balanced LAI, which corresponds to the mass0 class (m2/m2).


.. nml:member:: mass0

   :type: real(npft)
   :default: None

   The lowest PFT mass class (kg C).


.. nml:member:: massi

   :type: real(npft)
   :default: None

   The highest PFT mass class (kg C).


.. nml:member:: mclass

   :type: integer(npft)
   :default: None

   Number of mass classes for each PFT.


.. nml:member:: mort_base

   :type: real(npft)
   :default: None

   The baseline PFT mortality rate (/360 days).


.. nml:member:: phi_a

   :type: real(npft)
   :default: 0.50

   The allometric/power scaling of PFT mass to PFT crown area (West, G. B., et al 2009 <https://doi.org/10.1073/pnas.0812294106>`_).


.. nml:member:: phi_g

   :type: real(npft)
   :default: 0.75

   The allometric/power scaling of PFT mass to PFT mass growth rate (West, G. B., et al., 1997 <https://www.science.org/doi/10.1126/science.276.5309.122>`_).


.. nml:member:: phi_h

   :type: real(npft)
   :default: 0.25

   The allometric/power scaling of PFT mass to PFT height (Niklas, K. J., et al., 2001 <https://doi.org/10.1073/pnas.041590298>`_).


.. nml:member:: phi_l

   :type: real(npft)
   :default: 0.25

   The allometric/power scaling of PFT mass to PFT leaf area index.

