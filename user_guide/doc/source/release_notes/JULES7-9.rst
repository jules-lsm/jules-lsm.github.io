JULES version 7.9 Release Notes
===============================

The JULES vn7.9 release consists of approximately 18 tickets from 12 authors, including work by many other people.

Full details of the tickets committed for JULES vn7.9 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v7.9+(Jun-25)>`_.

Ticket numbers are indicated below, e.g. #1590.


Science changes
---------------

 *  Additional scheme for soil uptake of H\ :sub:`2` from the atmosphere - see :nml:mem:`JULES_DEPOSITION::dep_h2_soil_scheme`. (#1590)


General/Technical changes
-------------------------

 *  Add variables to a namelist and a logical switch for the Robust Ecosystem Demography code. (#1425)
 *  Add further parameters for the Random Parameter scheme used in regional ensemble forecasting. (#1439)
 *  Allow the MORUSES canyon emissivity to be set externally via the switch `l_emis_surft_set`, as for other tiles. (#1597)
 *  Avoid creation of temporary arrays. (#1595, 1606)
 *  The INFERNO coupling framework was extended to pass additional INFERNO-derived emissions to the UKCA chemistry and aerosol model of C\ :sub:`2`\ H\ :sub:`4`, C\ :sub:`2`\ H\ :sub:`6`, C\ :sub:`3`\ H\ :sub:`8`, HCHO, MeCHO, NH\ :sub:`3` and DMS. (#1579)
 *  All metadata items ported to LFRic now reside in jules-shared and have been deleted from um-atmos. (#1588)
 *  Allow JULES to build using Fab on azspice at the Met Office. (#1596)
 *  Provide a set up for rivers-only jobs on the Met Office EX machines. (1598)

    
Bugs fixed
----------

 *  Bug fix to prevent possible array-bounds error when reading a list of ancillary file names from file. (#1607)
 *  Fix for rose stem on azspice at Met Office. (#1600)
 *  Tidy the use of USE with LFRic. (#1604)
 *  Enable rivers coupled to LFRic to run on the EX machines at Met Office. (#1608)


Changes to testing
------------------

 *  Add a remote initialisation task as part of moving to cylc8. (#1605)
 *  Allow rose stem to use both EX Host Zones at Met Office. (#1599)
 *  Remove spice and xc40 rose-stem set ups. (#1602)


Documentation updates
---------------------

 *  Updates associated with many of the above changes, and release notes. (#1613)


Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.

