``cable_soilparm.nml``
============================


This file contains a namelist called :nml:lst:`CABLE_SOILPARM` that sets time-invariant parameters for different soil types for the CABLE land surface model.

``CABLE_SOILPARM`` namelist members
-----------------------------------------

.. nml:namelist:: CABLE_SOILPARM


This namelist reads the values of parameters for each of the soil types if the CABLE land surface model is being used. These parameters are a function of surface type only. All parameters must be defined for any configuration.
The number of soil types is stored in the `n_soiltypes` parameter and for the current version of CABLE is set to `9`.

.. nml:member:: silt_io

   :type: real(n_soiltypes)
   :default: MDI

   Fraction of soil which is silt.


.. nml:member:: clay_io

   :type: real(n_soiltypes)
   :default: MDI

   Fraction of soil which is clay.


.. nml:member:: sand_io

   :type: real(n_soiltypes)
   :default: MDI

   Fraction of soil which is sand.


.. nml:member:: swilt_io

   :type: real(n_soiltypes)
   :default: MDI

   Volume of H\ :sub:`2`\O at wilting (m\ :sup:`3` m\ :sup:`-3`)


.. nml:member:: sfc_io

   :type: real(n_soiltypes)
   :default: MDI

   Volume of H\ :sub:`2`\O at field capacity (m\ :sup:`3` m\ :sup:`-3`)


.. nml:member:: ssat_io

   :type: real(n_soiltypes)
   :default: MDI

   Volume of H\ :sub:`2`\O at saturation (m\ :sup:`3` m\ :sup:`-3`)


.. nml:member:: bch_io

   :type: real(n_soiltypes)
   :default: MDI

   Parameter b in Campbell equation.


.. nml:member:: hyds_io

   :type: real(n_soiltypes)
   :default: MDI

   Hydraulic conductivity at saturation (m\ :sup:`-1`).


.. nml:member:: sucs_io

   :type: real(n_soiltypes)
   :default: MDI

   Suction at saturation (m).


.. nml:member:: rhosoil_io

   :type: real(n_soiltypes)
   :default: MDI

   Soil bulk density (kg m\ :sup:`-3`)


.. nml:member:: css_io

   :type: real(n_soiltypes)
   :default: MDI

   Soil specific heat capacity (J kg\ :sup:`-1` K\ :sup:`-1`).



