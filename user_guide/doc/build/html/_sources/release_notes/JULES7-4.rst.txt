JULES version 7.4 Release Notes
===============================

The JULES vn7.4 release consists of approximately 23 tickets from 17 authors, including work by many other people.

Full details of the tickets committed for JULES vn7.4 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v7.4+(Oct-23)>`_.

Ticket numbers are indicated below, e.g. #1344.


Science changes
-------------------------

 *  Implementated the SUGAR carbohydrate model as an alternative method for calculating plant respiration - see :nml:mem:`JULES_VEGETATION::l_sugar`. (#1344)


General/Technical changes
-------------------------

 *  Refactored the river grid setup code, including changes to the :nml:lst:`JULES_RIVERS_PROPS` namelist (#1172, 1472)
 *  The parameterisation of overbank inundation is now selected via the variable :nml:mem:`JULES_OVERBANK::overbank_model`. (#1405)
 *  Added a diagnostic of Net Biosphere Productivity for JULES and UM, and enabled diagnostics of fire emissions for output via STASH. (#1462)
 *  Added prognostic variables for the RED vegetation model to model dump files. (#1230)
 *  Adding water tracers to the surface scheme - the first stage of adding water tracers/isotopes to JULES. (#1390)

    
Bugs fixed
----------

 *  Bug fix for when deciding if surface fractions are non-zero in the initial conditions. (#1451)
 *  Fixes for atmospheric dry deposition. (#1332)
 *  Fixed bug in calculation of stem nitrogen with RED. (#1306)
 *  Corrected the variable fluxes%fqw_surft (moisture flux on land surface tiles) coming out of JULES and being passed to LFRic. (#1360)
 *  Fixing problems when JULES is coupled to the UM and layered soil nitrogen is required (:nml:mem:`JULES_SOIL_BIOGEOCHEM::l_layeredc` and :nml:mem:`JULES_VEGETATION::l_nitrogen` are TRUE). (#1463)
 *  Fixed some OpenMP non-thread-safe issues with the ancil_info module. (#1450)
 *  Removed spurious metadata directories. (#1469)


Changes to testing
------------------

 *  Added rose stem tests for a spatial version of the land surface configuration used in UKESM. (#1430, 1478)
 *  Corrections to some rose stem tests related to deposition. (#1470)
 *  JULES apps were edited to ensure they can validate, and rose-stem now automatically validates new apps. (#1441, 1464)
 *  Check for modifications to files shared with LFRic and state requirement for LFRic testing in trac.log. (#1445)
 *  Update standalone rose stem configuration on Met Office EXZ system. (#1453)


Documentation updates
---------------------

 *  Updates associated with many of the above changes, and release notes. (#1467)


Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.

