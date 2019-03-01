JULES version 5.0 Release Notes
===============================


The JULES vn5.0 release consists of approximately 34 tickets from 12 authors, including work by many other people.

Full details of the tickets committed for JULES vn5.0 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v5.0+release>`_.

This release was unusual in that it was closed to science tickets so as to allow work of a more technical nature, principally ensuring compliance with the coding standards and improved optimisation.

The extensive styling changes that were introduced at vn5.0 have made minor changes to a large number of lines of code, meaning that updating your work from an older branch may not be as straightforward as with most release cycles. For advice on how best to upgrade your branch to vn5.0 see `Notes on moving to vn5.0 <https://code.metoffice.gov.uk/trac/jules/wiki/MoveBranchesToVn5.0>`_.

Ticket numbers are indicated below, e.g. #230.


General/Technical changes
-------------------------

 * Applied a code style-checking script, also included as part of rose stem tests. (#230, 387, 593)
 * Modularise the root_frac() subroutine to improve interface checking. (#571)
 * More use of OpenMP threading to surface and soil code to improve performance. (#575, 600, 607)
 * Various code changes to prevent or warn if an inconsistent combination of vegetation flags and parameters is used. When TRIFFID is on and the phenology model is off (not recommended), LAI is now set to the balanced LAI rather than taken from the (:nml:lst:`JULES_PFTPARM`) namelist. (#592)
 * Remove references to outdated or deprecated functions (#577, 585), and other technical improvements. (#596, 616)
 * More variables given initial values. (#579)
 * Reduced size of outputs from rose stem tests. (#580)
 * Superfluous messages from vegetation code removed. (#581)
 * General code improvements to meet coding standards and use a consistent style. (#574, 576, 578, 584, 594, 620, 621)
 * Namelists are printed before checking for errors, for easier debugging. (UM only, #582)
 * Snowdepth diagnostic made available in the UM. (#569)
 * Module leadership clarified across the code base. (#611)
 * Unnecessary subversion properties removed. (#597)


Bugs fixed
----------

 * Fixed minor bug in variable names when soil moisture prescribed. (#573)
 * Prevent duplicate names for output streams. (#590)
 * Fixed bug in vegetation competition routine lotka_eq. (#603)
 * Fixed bug in output variable smc_avail_top. (#604)
 * Fixed minor bugs in use of l_trait_phys. (#613)
 * Corrected wood product pool diagnostics in the UM. (#587)
 * Bugs fixed in soil respiration, and in carbon conservation diagnostics, for runs with N limitation. (#595)
 * Enables ability to perform bit comparable NRUN in the UM. (#612)
 * Fix JULES rose stem so that it works on the MO XCS-C system (aka MONSooN). (#615)
 * Fixed broken hyperlinks in the user guide. (#636)
   
Documentation updates
---------------------
Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.
