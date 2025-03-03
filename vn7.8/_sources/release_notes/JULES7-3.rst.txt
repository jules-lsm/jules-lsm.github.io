JULES version 7.3 Release Notes
===============================

The JULES vn7.3 release consists of approximately 19 tickets from 9 authors, including work by many other people.

Full details of the tickets committed for JULES vn7.3 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v7.3+(Jun-23)>`_.

Ticket numbers are indicated below, e.g. #1180.


General/Technical changes
-------------------------

 *  Removed default numerical values from variables in the :nml:lst:`JULES_HYDROLOGY` and :nml:lst:`JULES_RIVERS` namelists. (#1180)
 *  Allow a model domain that straddles the edge of the input grid (for grids that are cyclic in longitude). (#1301)
 *  Simplification of the namelists required for OASIS-Rivers to aid maintenance of the LFRic coupled miniapp. (#1385)
 *  Water resource variables bundled in a new TYPE. (#1401)
 *  Clarification of timestep-related variables. (#1403)
 *  Change kind type names to avoid clash with Fortran intrinsics. (#1408)
 *  Removed some include files by moving code to module files. (#1411, 1412. 1418)

    
Bugs fixed
----------

 *  Fixed standalone diagnostics `sat_excess_roff` and `drain`. (#1039)
 *  Fix for possible floating point exceptions in veg2 code. (#1155)
 *  Bug fixes for irrigation code. (#1386)
 *  Bug fixes for OASIS-Rivers coupling field, `rflow_outflow`. (#1435)


Changes to testing
------------------

 *  Updated `suite_report.py`. (#1442)


Documentation updates
---------------------

 *  Simplified the description of platform files. (#1353)
 *  Minor syntax changes in the JULES Coding Standards. (#1402)
 *  Minor corrections to code and documentation. (#1421, 1443)
 *  Updates associated with many of the above changes, and release notes. (#1384)


Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.

