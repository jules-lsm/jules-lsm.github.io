``oasis_rivers.nml``
=======================


This file contains a single namelists called :nml:lst:`OASIS_RIVERS`, which indicates how the Rivers-only executable couples via OASIS to other models (currently LFRIC and NEMO). This namelist is only used when running the river standalone program in coupled mode, i.e., compiling with the parameters RIVERS_ONLY and RIVER_CPL

.. note::  This namelist is only actually used when running the Rivers-only executable (compilation flag `RIVERS_ONLY`) in coupled mode (compilation flag `RIVER_CPL`)

``OASIS_RIVERS`` namelist members
------------------------------------

.. nml:namelist:: OASIS_RIVERS

.. nml:member:: np_receive

   :type: integer
   :permitted: 2
   :default: imdi

   The number of fields that are received from other models via OASIS coupling.

.. nml:member:: np_send

   :type: integer
   :permitted: 0,1
   :default: imdi

   The number of fields that are sent to other models via OASIS coupling.

.. nml:member:: cpl_freq

   :type: integer
   :permitted: 1:
   :default: imdi

   The river coupling frequency in seconds.

.. note::  The river coupling frequency must be a multiple of the river executable time step, and of the time steps of the models to which it is coupled.

.. nml:member:: send_fields

   :type: character(:)
   :permitted: 'outflow_per_river'
   :default: ''

   List of fields to be sent via coupling from the river executable to other models. Names are case sensitive.

.. note::  The only field that can be sent via coupling is the total river runoff (`outflow_per_river`).

.. nml:member:: receive_fields

   :type: character(:)
   :permitted: 'sub_surf_roff_rp', 'surf_roff_rp', 'sub_surf_roff', 'surf_roff'
   :default: ''

   List of fields to be received by the river executable via coupling from other models. Names are case sensitive.

.. note::  Coupled receive fields are used to substitute driving data read from file using the namelist :nml:lst:`JULES_DRIVE` by the same fields generated by a driving model running in parallel to the river executable. The only fields that can be received via coupling are the surface runoff (`surf_roff_rp`, `surf_roff`) and the sub-surface runoff (`sub_surf_roff_rp`, `sub_surf_roff`).

.. _example_coupling_request:

Example of coupling request
----------------------------

In this example, the user has requested receiving the surface and sub-surface runoffs, and sending the total river runoff via coupling. The coupling exchanges take place every hour. Please see :nml:lst:`JULES_RIVERS_PROPS` for specifying the River routing ancillary data including the river outflow number required for the calculation of 'outflow_per_river'.

::

    &JULES_RIVERS_PROPS
      # ...
      coordinate_file='$RIV_NUMBER_ANCILLARY/qrparm.rivseq.nc',
      file='file_list.txt',
      # ...
      read_list=.true.,
      # ...
      use_file=.true.,.true.,.true.,
      var='direction','sequence','rivers_outflow_number',
      var_name='river_routing_direction','river_routing_sequence',
              ='river_number',
      # ...
    /

    # ...

    &OASIS_RIVERS
      cpl_freq = 3600,
      np_receive = 2,
      np_send = 1,
      receive_fields = 'sub_surf_roff','surf_roff',
      send_fields = 'outflow_per_river',
    /

:nml:mem:`JULES_RIVERS_PROPS::read_list` = TRUE indicates that the ancillary file names should be read from ``file_list.txt``, which contains for this example::

    '$RIV_NUMBER_ANCILLARY/qrparm.rivseq.nc'
    '$RIV_NUMBER_ANCILLARY/qrparm.rivseq.nc'
    '$RIV_NUMBER_ANCILLARY/river_number_trip.nc'
