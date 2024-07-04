JULES version 7.6 Release Notes
===============================

The JULES vn7.6 release consists of approximately 19 tickets from 10 authors, including work by many other people.

Full details of the tickets committed for JULES vn7.6 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v7.6+(Jun-24)>`_.

Ticket numbers are indicated below, e.g. #1512.

General/Technical changes
-------------------------

 *  Changes to how river ancillary files are processed. (#1512) 
 *  Added water tracers to the UM_TRIP river routing. (#1466)
 *  Completion of the water tracer code development so water tracers can track water through the UM and JULES. (#1389)
 *  Allowed flexible number of soil layers in the UM atmospheric model. (#1188)
 *  Removed further tab characters. (#1511)
 *  Optimisation changes for JULES standalone. (#1501)
 *  1-D fields for surface and sub-surface runoff coupling between LFRic and TRIP replaced with 2-D coupling. (#1527)
 *  Altered usage of the model_type option for LFRic use cases. (#1521)
 *  Updated CodeOwners file. (#1538)
    
Bugs fixed
----------

 *  Add a burn depth parameter :nml:mem:`JULES_SOIL_BIOGEOCHEM::z_burn_max` for when layered soil carbon is used so that fire only consumes soil carbon from above the burn depth. (#1514)
 *  Fix to stop NaNs appearing in the agriculture fraction (frac_agr) with the TRIFFID vegetation model. (#1526)
 *  Fixed JULES upgrade macro code for Rose2 and related fix for how JULES version files are imported. (#1508, 1531)
 *  Fixes for build on Met Office XC40 system. (#1513)


Changes to testing
------------------

 *  Deployment optimisations for Met Office rose stem jobs, and tweaks to nccmp jobs. (#1519, 1518, 1536, 1537)


Documentation updates
---------------------

 *  Updates associated with many of the above changes, and release notes. (#1532)


Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.

