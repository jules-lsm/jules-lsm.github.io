JULES version 7.8 Release Notes
===============================

The JULES vn7.8 release consists of approximately 12 tickets from 7 authors, including work by many other people.

Full details of the tickets committed for JULES vn7.8 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v7.8+(Feb-25)>`_.

Ticket numbers are indicated below, e.g. #1565.

General/Technical changes
-------------------------

 *  Introduced a daily climatology (alongside existing monthly) option for IMOGEN using a 360 day calendar - see :nml:mem:`IMOGEN_ONOFF_SWITCH::l_daily_metdata_climatol`. Also changes to the IMOGEN options to clarify the different ways they drive JULES - see :nml:mem:`IMOGEN_RUN_LIST::l_change_metdata` and :nml:mem:`IMOGEN_RUN_LIST::change_metdata_method`. (#1565)
 *  Functionality added to allow specification of the ancillary file that each of the required ancillary variables should be read from. (#1525)
 *  Diagnostics for RFM river routing now available in the UM atmosphere model. (#1555)
 *  Allowing JULES to be used on the Met Office's Azspice system. Change to the default EX machine for rose stem and allowing use of EXCD. (#1576, 1580, 1585)
 *  Updates for the upgraded JASMIN system. (#1586)

    
Bugs fixed
----------

 *  Fix for dry deposition on elevated tiles. (#1568)
 *  Bug fix for fire-permafrost interactions in the UM (altered the upper limit when checking value of z_burn_max). (#1581)
 *  Bug fix to avoid zero lengths being calculated for a high resolution river grid. (#1583)


Changes to testing
------------------

 *  Additional rose stem tests for IMOGEN. (#1566)


Documentation updates
---------------------

 *  Updates associated with many of the above changes, and release notes. (#1584)


Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.

