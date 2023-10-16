``jules_water_resources.nml``
=============================

This file sets options for water resource modelling. It contains a single namelist called :nml:lst:`JULES_WATER_RESOURCES`.

.. warning::
   The water resource code in JULES is still in development. It should only be used by the developers.


``JULES_WATER_RESOURCES`` namelist members
------------------------------------------

.. nml:namelist:: JULES_WATER_RESOURCES

.. nml:member:: l_water_resources

   :type: logical
   :default: F

   Switch to enable modelling of water resources.

   TRUE
       Water resources are modelled.
       This also requires that river routing is selected (:nml:mem:`JULES_RIVERS::l_rivers` = TRUE).

   FALSE
       No water resources. In this case no further values from this namelist are required.


.. nml:member:: nstep_water_res

   :type: integer
   :permitted: > 0
   :default: none

   The number of model timesteps per water resource timestep. (The main model timestep is given by :nml:mem:`JULES_TIME::timestep_len`.)
   
   For example, :nml:mem:`nstep_water_res` = 12 means that demands for water will be accumulated over 12 model timesteps before the water resource code is called on the 12th timestep.

   The water resource and river routing models must be in synchrony (i.e. be called on the same timesteps).



.. nml:group:: Switches that control which water sectors are considered.


   .. nml:member:: l_water_domestic

      :type: logical
      :default: F

      Switch for modelling of water for domestic use.

      TRUE
          Consider demand for water for domestic use. This requires that the domestic demand is prescribed as an input to the model (see :doc:`prescribed_data.nml`).

      FALSE
          Do not consider domestic demand.


   .. nml:member:: l_water_environment

      :type: logical
      :default: F

      Switch for modelling of water for environmental flow requirements.

      TRUE
          Consider demand for water for environmental flows.

      FALSE
          Do not consider environmental demand.


   .. nml:member:: l_water_industry

      :type: logical
      :default: F

      Switch for modelling of water for industrial use. This requires that the industrial demand is prescribed as an input to the model (see :doc:`prescribed_data.nml`).

      TRUE
          Consider demand for water for industrial use. 

      FALSE
          Do not consider industrial demand.


   .. nml:member:: l_water_irrigation

      :type: logical
      :default: F

      Switch for modelling of water for irrigation.

      TRUE
          Consider demand for water for irrigation. This must be used with :nml:mem:`JULES_IRRIG::l_irrig_dmd` = TRUE (to activate the inclusion of irrigation in other aspects of the model) and :nml:mem:`JULES_IRRIG::l_irrig_limit` = FALSE (to avoid triggering an alternative approach to calculating the water available for irrigation).

      FALSE
          Do not consider irrigation demand.


   .. nml:member:: l_water_livestock

      :type: logical
      :default: F

      Switch for modelling of water for livestock.

      TRUE
          Consider demand for water for livestock. This requires that the livestock demand is prescribed as an input to the model (see :doc:`prescribed_data.nml`).

      FALSE
          Do not consider livestock demand.


   .. nml:member:: l_water_transfers

      :type: logical
      :default: F

      Switch for modelling of water for transfers.

      TRUE
          Consider demand for water for transfers. This requires that the demand for transfers is prescribed as an input to the model (see :doc:`prescribed_data.nml`).

      FALSE
          Do not consider transfers.


.. nml:group:: Switches that control prioritisation of demands.


   .. nml:member:: l_prioritise

      :type: logical
      :default: F

      Switch controlling prioritisation of demands.

      TRUE
          Rank demands from sectors in priority order.

      FALSE
          No prioritisation. No further items from this group are required.


   .. nml:member:: priority

      :type: character
      :default: none

      A list of water sector names, in order of decreasing priority - see the table below for valid names. Only used if :nml:mem:`l_prioritise` = TRUE. All active sectors (as selected by switches such as :nml:mem:`l_water_domestic`) must be represented in this list. The same prioritisation is used for all points in the domain.

   .. tabularcolumns:: |p{2cm}|p{9cm}|

   +------------+----------------------+
   | Name       | Description          |
   +============+======================+
   | ``dom``    | Domestic use         |
   +------------+----------------------+
   | ``env``    | Environmental flows  |
   +------------+----------------------+
   | ``ind``    | Industrial use       |
   +------------+----------------------+
   | ``irr``    | Irrigation           |
   +------------+----------------------+
   | ``liv``    | Livestock use        |
   +------------+----------------------+
   | ``tra``    | Water transfers      |
   +------------+----------------------+


.. nml:member:: nr_gwater_model

   :type: integer
   :permitted: 0,1,2
   :default: none

   Choice for the model of non-renewable groundwater. Non-renewable groundwater is water that is not otherwise explicitly included in the model. It is an idealised, infinite source of water which is typically intended to allow consideration of pumping of grounwater from deep reserves that are difficult to quantify.

   Possible values are:

   0. | No non-renewable groundwater is considered.

   1. | Non-renewable groundwater is used as a last resort, when no other sources of water are available.

   2. | Non-renewable groundwater is used as as 'part of the mix', in conjunction with other sources of water.


.. nml:member:: rf_domestic

   :type: real
   :permitted: 0-1
   :default: none

   The fraction of water that is returned after abstraction for domestic use (via sewage systems etc.). Only used if :nml:mem:`l_water_domestic` = TRUE.


.. nml:member:: rf_industry

   :type: real
   :permitted: 0-1
   :default: none

   The fraction of water that is returned after abstraction for industrial use. Only used if :nml:mem:`l_water_industry` = TRUE.


.. nml:member:: rf_livestock

   :type: real
   :permitted: 0-1
   :default: none

   The fraction of water that is returned after abstraction for livestock. Only used if :nml:mem:`l_water_livestock` = TRUE.
