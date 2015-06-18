``model_levels.nml``
====================


This file configures the surface types, number of soil layers and maximum number of snow layers. It contains a single namelist called :nml:lst:`JULES_MODEL_LEVELS`.


``JULES_MODEL_LEVELS`` namelist members
---------------------------------------

.. nml:namelist:: JULES_MODEL_LEVELS

.. nml:member:: npft

   :type: integer
   :permitted: >= 1
   :default: 5

   The number of plant functional types to be modelled.


.. nml:member:: nnvg

   :type: integer
   :permitted: >= 1
   :default: 4

   The number of non-plant surface types to be modelled.

   The total number of surface types to be modelled is called ``ntype``, and is given by ``ntype = npft + nnvg``. In the standard setup, JULES models 5 vegetation types and 4 non-vegetation types (``npft = 5``, ``nnvg = 4``). However, the model domain need not contain all 9 types, e.g. the domain could consist of a single point with 100% grass. The amount of each type in the domain is normally set in :nml:lst:`JULES_FRAC`.


.. nml:member:: urban

   :type: integer
   :default: 6

   Index of the urban surface type.

   A negative value indicates no urban surface type.


.. nml:member:: lake

   :type: integer
   :default: 7

   Index of the lake surface type.

   A negative value indicates no lake surface type.


.. nml:member:: soil

   :type: integer
   :permitted: >= 1
   :default: 8

   Index of the soil surface type.

   .. note:: A soil surface type must be given.


.. nml:member:: ice

   :type: integer
   :default: 9

   Index of the ice surface type.

   A negative value indicates no ice surface type.


.. nml:member:: urban_canyon

   :type: integer
   :default: -1

   Index of the urban canyon surface type.

   A negative value indicates no urban canyon surface type.


.. nml:member:: urban_roof

   :type: integer
   :default: -1

   Index of the urban roof surface type.

   A negative value indicates no urban roof surface type.


.. nml:member:: sm_levels

   :type: integer
   :permitted: >= 1
   :default: 4

   Number of soil layers.

   A value of 4 is often used, and the default soil layer depths have been tuned using this.


.. nml:member:: nsmax

   :type: integer
   :permitted: >= 0
   :default: 0

   Maximum possible number of snow layers.

   0
       A composite soil/snow layer is used. This value gives the behaviour found in JULES2.0 and earlier.

   > 0
       The state of up to ``nsmax`` separate snow layers is modelled. Values of ``nsmax = 3`` or more are recommended.


.. note::

    The values of :nml:mem:`urban`, :nml:mem:`urban_canyon` and :nml:mem:`urban_roof` are used to determine what urban scheme to use.

    * At most one of :nml:mem:`urban` and :nml:mem:`urban_canyon` can be given.
    * If :nml:mem:`urban_roof` is present, then JULES will use one of the 2-tile urban schemes (and so either :nml:mem:`urban` or :nml:mem:`urban_canyon` must be present, and will represent the urban canyon surface type).
    * If :nml:mem:`urban_roof` is not present, :nml:mem:`urban_canyon` cannot be given and, if present, :nml:mem:`urban` is used as the single urban surface type.

    When giving urban fraction data (see :nml:lst:`JULES_FRAC`), total urban fraction should be given in the :nml:mem:`urban` or :nml:mem:`urban_canyon` tile, whichever is present. This is partitioned internally into roof and canyon.
