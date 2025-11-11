

This file contains a single namelist called :nml:lst:`JULES_RED` that sets parameters relevant to the Robust Ecosystem Demography submodel (RED version 1.0) <https://gmd.copernicus.org/articles/13/4067/2020/>`_.
Activate RED in the :nml:mem:`JULES_VEGETATION::l_red`.

``JULES_RED`` namelist members
----------------------------------

.. nml:namelist:: JULES_RED

This namelist is used to read PFT parameters that are only needed by the Robust Ecosystem Demography (RED). Values are not used if RED is not selected.

.. note:: Where a quantity is said to have units of "/360days", this means that it is an amount per 360 days.

.. nml:group:: Only used when :nml:mem:`JULES_VEGETATION::l_red` = TRUE.

   .. nml:member:: alpha_recrt

      :type: real(npft)
      :default: None

      The fraction of PFT carbon assimilate devoted to reproduction.


   .. nml:member:: crwn_area0

      :type: real(npft)
      :default: None

      The lowest PFT crown area, value corresponds to the mass0 class (m\ :sup:`2`).


   .. nml:member:: dom_order

      :type: integer(npft)
      :default: None

      The value that describes the competitive hierarchy of PFTs competition in
      JULES-RED, the higher the value the more dominant: 3 (trees), 2 (shrubs), 1 (grass).


   .. nml:member:: height0

      :type: real(npft)
      :default: None

      The lowest PFT height, value corresponds to the mass0 class (m).


   .. nml:member:: lai_bal0

      :type: real(npft)
      :default: None

      The lowest PFT balanced LAI, which corresponds to the mass0 class (m\ :sup:`2`/m\ :sup:`2`).


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

