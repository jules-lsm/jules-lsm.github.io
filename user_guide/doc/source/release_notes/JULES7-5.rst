JULES version 7.5 Release Notes
===============================

The JULES vn7.5 release consists of approximately 17 tickets from 12 authors, including work by many other people.

Full details of the tickets committed for JULES vn7.5 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v7.5+(Feb-24)>`_.

Ticket numbers are indicated below, e.g. #1491.


Science changes
-------------------------

 *  The stomatal conductance formulation of Eller et al. (2020, doi: 10.1111/nph.16419) is included as an option on the stomatal model switch :nml:mem:`JULES_VEGETATION::stomata_model`. (#1491)


General/Technical changes
-------------------------

 *  Added water tracers to the hydrology and snow schemes - part of ongoing work to add water tracers/isotopes to JULES. (#1391, 1465)
 *  For runs with rivers, the new option :nml:mem:`JULES_RIVERS_PROPS::l_find_grid` can be used to avoid requiring values for variables related to the model grid. This also revises how the area searched for river points is set up. (#1380)
 *  IMOGEN now reads netcdf files for driving data. (#1265)
 *  :nml:mem:`JULES_RIVERS::trip_globe_shape` allows the TRIP river routing scheme to consider the Earth as either spherical or ellipsoidal (a more accurate approximation but inconsistent with other component models - e.g. UM and NEMO - which assume the Earth is spherical. Note that this change only affects the UM version of TRIP. (#1374)
 *  Optimisation and OpenMP efficiency improvements in various places. (#1471)
 *  Metadata: `jules_snow` and `jules_radiation` LFRic shared items have been migrated to jules-shared, which is also now imported by the UM, and `jules_snow` metadata differences have been consolidated. This is an important step towards having only one source of JULES metadata. Users should experience no difference. JULES developers should refer to the Working Practices. (#1482)

 *  ModuleLeaders file renamed for consistency with other projects. (#1452)

    
Bugs fixed
----------

 *  The switch :nml:mem:`JULES_TEMP_FIXES::l_fix_neg_snow` corrects the formulation of snow melting and introduces an extra limit in the calculation of canopy unloading, both of which changes are required to prevent the occurrence of negative snow. Additionally and generically, the snow melt will now be passed through the control code as an increment, not as a rate. This prevents the occurrence of lingering tiny amounts of snow and is required with the fix. (#1396)
 *  Improved code for water table calculations, accounting for for vertically-varying soil properties. (#1488)
 *  Bug fix for when `f_wetl is zero` in the layered methane flux code. (#1496)


Changes to testing
------------------

 *  Changed initial conditions file for gswp2_es tests. (#1475)
 *  Added a test (Met Office only) based on how SURF (the Met Office land surface data assimilation system)  uses JULES; these namelists follow the global operational GL9 configuration. (#1477)
 *  Updated the rose-stem suite to be compatible with Cylc8. (#1474)
 *  Minor changes to NIWA to correct previous errors. (#1487)
 *  Added a site_validator script, for easier identification of certain errors. (#1483)
 *  Fixed the parsing of the lfric extract list in suite_report. (#1497)
 *  Changes for running on the Met Office EXA system. (#1502)
 *  Introduced SimSys_Scripts checkout. (#1503)


Documentation updates
---------------------

 *  Updates associated with many of the above changes, and release notes. (#1498)


Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.

