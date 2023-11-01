``cable_surface_types.nml``
=================================


This file configures the surface types used by CABLE. It contains one namelist called :nml:lst:`CABLE_SURFACE_TYPES`.


``CABLE_SURFACE_TYPES`` namelist members
----------------------------------------


.. nml:namelist:: CABLE_SURFACE_TYPES

.. nml:member:: npft_cable

   :type: integer
   :permitted: >= 1
   :default: -32768

   The number of plant functional types to be modelled.
   
   
.. nml:member:: nnvg_cable

   :type: integer
   :permitted: >= 1
   :default: -32768

   The number of non-plant surface types to be modelled.
   
   
.. note::
   The total number of surface types to be modelled is called ``ntype_cable``, and is given by ``ntype_cable = npft_cable + nnvg_cable``.
   
   In the standard setup, CABLE models 13 vegetation types and 4 non-vegetation types (``npft_cable = 13``, ``nnvg_cable = 4``). However, the model domain need not contain all 13 types, e.g. the domain could consist of a single point with 100% grass. The amount of each type in the domain is normally set in :nml:lst:`JULES_FRAC`.
   

.. nml:member:: urban_drive

   :type: integer
   :default: -32768


.. nml:member:: lakes_cable

   :type: integer
   :default: -32768

   Index of the lakes surface type.

   A negative value indicates no lakes surface type.


.. nml:member:: barren_cable

   :type: integer
   :permitted: >= 1
   :default: -32768

   Index of the barren soil surface type.

   .. note:: A barren soil surface type must be given.


.. nml:member:: ice_cable

   :type: integer
   :default: -32768

   Index of the ice surface type.

   A negative value indicates no ice surface type.

