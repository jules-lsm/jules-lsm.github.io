JULES version 7.2 Release Notes
===============================

The JULES vn7.2 release consists of approximately 19 tickets from 17 authors, including work by many other people.

Full details of the tickets committed for JULES vn7.2 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v7.2+(Feb-23)>`_.

Ticket numbers are indicated below, e.g. #1317.


General/Technical changes
-------------------------

 *  Switch :nml:mem:`JULES_LATLON::l_coord_latlon` specifies if the coordinate system is latitude-longitude or something else (e.g. a rotated grid). This makes it easier to model and postprocess grids that are not defined by latitude and longitude. (#1317)
 *  Addition of OASIS coupling capabilities to the river routing executable. (#1191)
 *  The RothC soil C model is now referred to as the 4-pool model. (#1348)
 *  Removed the remaining 2D field being passed into JULES via a module, replacing it with an argument list variable. (#1376)
 *  Removed a redundant print statement from the urban code. (#1367)
 *  Updated CABLE (as part of consolidating CABLE across its main applications, ACCESS-CM2, ESM1.5 and CABLE standalone), also corrected an inconsistency in the order of arguments for a few subroutines. (#1373)
 *  Increase compile-time checking with Cray's CCE. (#1061)
 *  Updated configuration for NIWA. (#1387)

    
Bugs fixed
----------

 *  Improved numerical implementation of an EXP calculation in the spectral albedo scheme. (#1189)
 *  Full initialisation of soil carbon arrays used with the INFERNO fire model. (#1356)
 *  Fixed the upgrde macro chain. (#1368)
 *  Fixes to umdp3_checker. (#1397)


Changes to testing
------------------

 *  Rose stem testing extended to include overbank inundation. (#999)
 *  loobos_gl4_cable now generates output files and is included in rose stem testing at several sites. (#1375)
 *  Updated suite_report.py and changed rosestem_branch_checker.py to use generic variable names to match the UKCA version. (#1369, 1379)
 *  Refactored rose stem tests for building JULES with FAB. (#1354)


Documentation updates
---------------------

 *  Updates associated with many of the above changes, and release notes. (#1381)
 *  Updated JULES docs to ensure that they build with a more recent version of Sphinx - they can now be built using Sphinx 2.4.0 and Python 3.6.10. (#1382)

Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.

