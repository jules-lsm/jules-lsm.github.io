JULES version 5.9 Release Notes
===============================


The JULES vn5.9 release consists of approximately 21 tickets from 11 authors, including work by many other people.

Full details of the tickets committed for JULES vn5.9 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v5.9+(Oct-20)>`_.

Ticket numbers are indicated below, e.g. #499.

Science changes
---------------

 * The FLake lake model is now available in standalone JULES (as well as in the UM), modelling sub-surface conditions on the lake tile - see :nml:mem:`JULES_SURFACE::l_flake_model`. (#499)
 * Fix to stop snow from accumulating on unfrozen lakes when running the FLake lake model. (#1057)
 * Options to disaggregate the albedo of bare soil between the VIS and NIR regions and to include the zenith-angle dependence of the bare soil albedo have been included. See :nml:mem:`JULES_RADIATION::l_hapke_soil` and :nml:mem:`JULES_RADIATION::l_partition_albsoil`. (#1020)


General/Technical changes
-------------------------

 *  Modifications to ensure the irrigation namelist for standalone JULES is consistent with the UM namelist structure. This involved moving irrigation switches to namelist :nml:lst:`JULES_IRRIG` and adding the :nml:lst:`JULES_IRRIG_PROPS` namelist for ancillary fields. (#838)
 *  Added initial control-level code for water resources. (#1018)
 *  The interface for the `river_control` subroutine now follows the model used by the `surf_couple_*` routines. This is part of activities to create a standalone river routing capability. (#1066)
 *  Added latent heat flux diagnostics separately for land and sea/sea-ice (Unified Model runs only). (#992)
 *  Surface diagnostics for 1.5m temperature, specific and relative humidity, dewpoint temperature, and fog fraction separately over ocean (sea + sea ice) and land made available in the UM (not available in standalone JULES). (#1074)
 *  Removed unused arguments, to avoid UM compiler warnings. (#1069)
 *  Optimisation of code used in GA9. (#1071)
 *  Added `ONLY`\ s to all `USE` statements that did not have them, to avoid undesirable effects. (#1072)
 *  All transparent, non-functional metadata consolidated with the UM, including `sort-key`, `description`, `url` and `help`, which has been removed where duplicated by the JULES user guide or merged in. (#1055)
 *  Keep standalone and UM JULES meta data consistent. (#1083)

    
Bugs fixed
----------

 *  Fixed bug that affected the reading of soil ancillary fields when :nml:mem:`JULES_SOIL_PROPS::const_z` = TRUE in the JULES_SOIL_PROPS namelist. The bug had the potential to result in some soil ancillary fields being zero - which would likely have resulted in an obviously wrong result and/or a model crash. (#1080)
 *  Fixed bug in the reading of dumps containing rain_seed fields. (#1059)
 *  Fixes for various issues related to argument intents. (#1058, 1062)
 *  Fix for UM configs with iseasurfalg=2 (m10 now initialised). (#975)


Changes to testing
------------------

 *  The gswp2_irrig_limit rose stem tests are included in the set run at UKCEH. (#1053)
 *  Added a further rose stem test with irrigation. (#838)


Documentation updates
---------------------

 *  Updates associated with many of the above changes, and release notes. (#1078)

Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.
