JULES version 7.1 Release Notes
===============================

The JULES vn7.1 release consists of approximately 20 tickets from 18 authors, including work by many other people.

Full details of the tickets committed for JULES vn7.1 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+Oct-2022>`_.

Ticket numbers are indicated below, e.g. #931.


Science changes
---------------

 *  Interactive gas-phase deposition routines from UKCA have been added to JULES, together with a variant version that removes the restriction on the surface tile configuration. See :nml:mem:`JULES_DEPOSITION::dry_dep_model`. (#931)


General/Technical changes
-------------------------

 *  Added a switch to allow interpretation of times in the model and the driving data as local solar time - see :nml:mem:`JULES_TIME::l_local_solar_time`. (#1327)
 *  Added a switch :nml:mem:`IMOGEN_RUN_LIST::l_drive_with_global_temps` so that JULES can be driven with global temperatures and climate patterns. (#1322)
 *  Made Medlyn stomatal conductance, Farquhar C\ :sub:`3` photosynthesis, and thermal acclimation available in the UM. (#1246)
 *  Further work towards allowing layered soil carbon (:nml:mem:`JULES_SOIL_BIOGEOCHEM::l_layeredc` = TRUE ) in the UM. (#1237)
 *  A varying grey tile emissivity has been passed in to JULES - currently only available if selected in LFRic. (#1247)
 *  OMP improvements in various routines. (#1310)
 *  Enabled a call to CABLE albedo (part of ongoing work to provide access to CABLE). (#1314)
 *  MORUSES and anthropogenic heat related metadata migrated to jules-shared to facilitate their implementation in LFRic. The simple two-tile urban scheme now no longer requires W/R as an input unless the total urban fraction only is specified in the ancillary data. (#1255)
 *  Included the fab_jules app which builds JULES using Fab software. (#1331, 1364)
 *  Updated compiler in JASMIN gfortran platform file. (#1347)
 *  Upgraded rose stem testing on Met Office EXZ to use latest availiable CPE, and fixes for EXZ. (#1362, 1358)

    
Bugs fixed
----------

 *  Corrected a bug in the `surf_ht_flux` diagnostic when using the Flake lake model. (#1340)
 *  Fixing problems in the WARNING output messages. (#1303)
 *  Fixed a metadata/rose config error introduced by a bug in Rose. (#1363)


Changes to testing
------------------

 *  Updated NCI rose stem tests. (#1266)


Documentation updates
---------------------

 *  Updates associated with many of the above changes and to module leaders file, and release notes. (#1275, 1343)

Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.

