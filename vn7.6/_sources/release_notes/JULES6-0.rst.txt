JULES version 6.0 Release Notes
===============================


The JULES vn6.0 release consists of approximately 18 tickets from 10 authors, including work by many other people.

Full details of the tickets committed for JULES vn6.0 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v6.0+(Feb-21)>`_.

Ticket numbers are indicated below, e.g. #847.

Science changes
---------------

 *  Added a microbial scheme for methane production (see :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_ch4_microbe`). (#847)
 *  Changes to soil evaporation: added a PFT-specific factor to multiply soil conductance under the canopy (:nml:mem:`JULES_PFTPARM::gsoil_f_io`) and a switch to limit soil conductance above the critical point (:nml:mem:`JULES_HYDROLOGY::l_limit_gsoil`). (#1093)
 *  Added option (l_icerough_prognostic) to use the prognostic sea ice roughness length calculated in CICE, rather than a constant value (available only when coupled). (#583)
 *  Calculate sea ice penetrating solar radiation to be sent to sea ice model. (#1100)


General/Technical changes
-------------------------

 *  Irrigation code adapted for use with :nml:mem:`JULES_WATER_RESOURCES::l_water_resources` = TRUE. (#1086)
 *  Surface type IDs have been made available to JULES on a switch ``l_surface_type_ids``, however they currently have no functionality and are not passed to the JULES I/O. As part of the metadata consolidation project the namelists :nml:lst:`JULES_SURFACE_TYPES` and `JULES_LSM_SWITCH` are now consolidated, the latter by amalgamating it with :nml:lst:`JULES_MODEL_ENVIRONMENT`. The GUI panels are also now consistently named in UM and standalone. In parallel runs, informative output can now also be limited to Task 0 (see :nml:lst:`JULES_PRNT_CONTROL`). (#1095)
 *  Prevented duplicate (lat,lon) pairs being prescribed. (#1107)
 *  Extended the TYPE design to sweep up several small modules. (#1102)
 *  Optimisation in snow control routine. (#1110)
 *  Removed some default values for values read via the :nml:lst:`JULES_DRIVE` namelist, and improved triggering. (#1033)
 *  Initialised further namelist variables before use. (#598)
 *  Fixed bad characters in metadata. (#1103)
 *  Further work to keep JULES and UM metadata consistent. (#1118)

    
Bugs fixed
----------

 *  Added option (:nml:mem:`JULES_TEMP_FIXES::l_accurate_rho`) to use accurate calculation of surface air density in surface exchange calculations. (#194)
 *  Fix to remove erroneously large river flows at river mouths with RFM (:nml:mem:`JULES_RIVERS::i_river_vn` = 2). (#1081)
 *  Fixed unallocated TRIFFID variable in the new progs structure. (#1109)


Documentation updates
---------------------

 *  Updates associated with many of the above changes, and release notes. (#1097, 1112)

Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.

