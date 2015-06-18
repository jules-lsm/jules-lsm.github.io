``snow_params.nml``
===================


This file contains two namelists called :nml:lst:`JULES_SNOW_PARAM` and :nml:lst:`JULES_RAD_PARAM` that read parameter values that are relevant for snow processes.


``JULES_SNOW_PARAM`` namelist members
-------------------------------------

.. nml:namelist:: JULES_SNOW_PARAM

HCTN30 refers to Hadley Centre technical note 30, available from `the Met Office Library <http://www.metoffice.gov.uk/learning/library/publications/science/climate-science/hadley-centre-technical-note>`_.


.. nml:member:: dzsnow_io

   :type: real(nsmax)
   :default: None

   Prescribed thickness of each snow layer (m).

   Only used if :nml:mem:`JULES_MODEL_LEVELS::nsmax` > 0.

   The interpretation of ``dzsnow`` is slightly complicated and an example of the evolution of the snow layers is given below.

   ``dzsnow`` gives the thickness of each layer when it is not the bottom layer.

   For the top layer, the minimum thickness is ``dzsnow(1)`` and the maximum thickness is ``2 * dzsnow(1)``. For all other layers ``iz``, the minimum thickness is ``dzsnow(iz - 1)``, i.e. the given thickness of the previous layer, and the maximum thickness is ``2 * dzsnow(iz)``, i.e. twice the layer ``dzsnow`` value, except for the last possible layer (:nml:mem:`JULES_MODEL_LEVELS::nsmax`) which has no upper limit.

   As a snowpack deepens, the bottom layer (closest to the soil; label this as layer ``b``) thickens until it reaches its maximum allowed thickness, at which point it will split into a layer of depth ``dzsnow(b)`` and a new bottom layer ``b + 1`` is added to hold the remaining snow. If a layer becomes thinner than its value in ``dzsnow`` it is removed and the snow partitioned between the remaining layers. Whenever a layer splits or is removed, the properties of the layer (e.g. temperature) are allocated to the remaining layers.

   Note that ``dzsnow(nsmax)``, the final thickness, is not used but a value must be input.


.. nml:member:: cansnowpft

   :type: logical(npft)
   :default: F

   Flag indicating whether snow can be held under the canopy of each PFT.

   Only used if :nml:mem:`JULES_SWITCHES::can_model` = 4.

   The model of snow under the canopy is currently only suitable for coniferous trees.

   TRUE
       Snow can be held under the canopy.

   FALSE
       Snow cannot be held under the canopy.


.. nml:member:: rho_snow_const

   :type: real
   :default: 250.0

   Constant density of lying snow (kg m\ :sup:`-3`).

   This value is used if :nml:mem:`JULES_MODEL_LEVELS::nsmax` = 0, in which case all snow is modelled as a single layer of constant density.


.. nml:member:: rho_snow_fresh

   :type: real
   :default: 100.0

   Density of fresh snow (kg m\ :sup:`-3`).

   This value is only used if :nml:mem:`JULES_MODEL_LEVELS::nsmax` > 0.


.. nml:member:: snow_hcon

   :type: real
   :default: 0.265

   Thermal conductivity of lying snow (W m\ :sup:`-1` K\ :sup:`-1`).

   See HCTN30 Eq.42.


.. nml:member:: snow_hcap

   :type: real
   :default: 0.63e6

   Thermal capacity of lying snow (J K\ :sup:`-1` m\ :sup:`-3`).


.. nml:member:: snowliqcap

   :type: real
   :default: 0.05

   Liquid water holding capacity of lying snow, as a fraction of snow mass.

   Only used if :nml:mem:`JULES_MODEL_LEVELS::nsmax` > 0.


.. nml:member:: snowinterceptfact

   :type: real
   :default: 0.7

   Constant in relationship between mass of intercepted snow and snowfall rate.

   Only used if :nml:mem:`JULES_SWITCHES::can_model` = 4.


.. nml:member:: snowloadlai

   :type: real
   :default: 4.4

   Ratio of maximum canopy snow load to leaf area index (kg m\ :sup:`-2`).

   Only used if :nml:mem:`JULES_SWITCHES::can_model` = 4.


.. nml:member:: snowunloadfact

   :type: real
   :default: 0.4

   Constant in relationship between canopy snow unloading and canopy snow melt rate.

   Only used if :nml:mem:`JULES_SWITCHES::can_model` = 4.


Example of the evolution of snow layer thickness
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The table below gives an example of how the number and thickness of snow layers varies with total snow depth for the case of :nml:mem:`JULES_MODEL_LEVELS::nsmax` = 3 and ``dzsnow = (0.1, 0.15, 0.2)``. Note that if the values given by the user for ``dzsnow`` are a decreasing series with ``dzsnow(i) <= 2 * dzsnow(i - 1)``, the algorithm will result in layers ``i`` and ``i + 1`` being added at the same time. Don't panic - this should not be a problem for the simulation.

.. tabularcolumns:: |p{3cm}|p{1.5cm}|p{3cm}|p{7cm}|

+--------------------+-----------+----------------------+----------------------------------------------------------------------------------+
| Snow depth (m)     | Number    | Layer thickness,     | Comments                                                                         |
|                    | of layers | uppermost layer      |                                                                                  |
|                    |           | first (m)            |                                                                                  |
+====================+===========+======================+==================================================================================+
| ``d < 0.1``        | 0         |                      | While the depth of snow is less than ``dzsnow(1)``, the layer model is not       |
|                    |           |                      | active and snow and soil are combined in a composite layer.                      |
+--------------------+-----------+----------------------+----------------------------------------------------------------------------------+
| ``0.1 <= d < 0.2`` | 1         | Total snow depth     | The single layer grows until it is twice as thick as ``dzsnow(1)``.              |
+--------------------+-----------+----------------------+----------------------------------------------------------------------------------+
| ``0.2 <= d < 0.4`` | 2         | 0.1, remainder       | Above 0.2m, the single layer splits into a top layer of 0.1m and the remaining   |
|                    |           |                      | snow in the bottom layer.                                                        |
+--------------------+-----------+----------------------+----------------------------------------------------------------------------------+
| ``>= 0.4``         | 3         | 0.1, 0.15, remainder | At 0.4m depth, layer 2 (which has grown to 0.3m thick, i.e. ``2 * dzsnow(2)``),  |
|                    |           |                      | splits into a layer of 0.15m and a new bottom layer holding the the remaining    |
|                    |           |                      | 0.15m. As all layers are now in use, any subsequent deepening of the pack is     |
|                    |           |                      | dealt with by increasing the thickness in this bottom layer.                     |
+--------------------+-----------+----------------------+----------------------------------------------------------------------------------+


``JULES_RAD_PARAM`` namelist members
------------------------------------

.. nml:namelist:: JULES_RAD_PARAM

HCTN30 refers to Hadley Centre technical note 30, available from `the Met Office Library <http://www.metoffice.gov.uk/learning/library/publications/science/climate-science/hadley-centre-technical-note>`_.


.. nml:member:: r0

   :type: real
   :default: 50.0

   Grain size for fresh snow (\ |mu|\ m).

   Only used if :nml:mem:`JULES_SWITCHES::l_snow_albedo` = TRUE. See HCTN30 Eq.15.


.. nml:member:: rmax

   :type: real
   :default: 2000.0

   Maximum snow grain size (\ |mu|\ m).

   Only used if :nml:mem:`JULES_SWITCHES::l_snow_albedo` = TRUE. See HCTN30 p4.


.. nml:member:: snow_ggr

   :type: real(3)
   :default: 0.6, 0.06, 0.23e6

   Snow grain area growth rates (\ |mu|\ m\ :sup:`2` s\ :sup:`-1`).

   Only used if :nml:mem:`JULES_SWITCHES::l_snow_albedo` = TRUE. See HCTN30 Eq.16.

   The 3 values are for melting snow, cold fresh snow and cold aged snow respectively.


.. nml:member:: amax

   :type: real(2)
   :default: 0.98, 0.7

   Maximum albedo for fresh snow.

   Only used if :nml:mem:`JULES_SWITCHES::l_snow_albedo` = TRUE.

   Values 1 and 2 are for VIS and NIR wavebands respectively.


.. nml:member:: maskd

   :type: real
   :default: 50.0

   Used in exponent of equation weighting snow-covered and snow-free albedo.


.. nml:member:: dtland

   :type: real
   :default: 2.0

   Degrees Celsius below zero at which snow albedo equals cold deep snow albedo.

   Only used if :nml:mem:`JULES_SWITCHES::l_snow_albedo` = FALSE. This is 2.0 in HCTN30 Eq4.


.. nml:member:: kland_numerator

   :type: real
   :default: 0.3

   Used in snow-ageing effect on albedo.

   Only used if :nml:mem:`JULES_SWITCHES::l_snow_albedo` = FALSE.

   Must not be zero.

   ``kland`` is computed by dividing this value by :nml:mem:`dtland` - see HCTN30 Eq4.



.. |mu| unicode:: &#x03BC; .. u

