JULES version 8.1 Release Notes
===============================

The JULES vn8.1 release consists of approximately 12 contributions, including work by many people.

Full details of the changes committed for JULES vn8.1 can be found on the `JULES GitHub repository <https://github.com/MetOffice/jules/milestone/2>`_.

Issue numbers are indicated below, e.g. #39.


General/Technical changes
-------------------------

 *  Migrated metadata for :nml:lst:`JULES_MODEL_ENVIRONMENT` and the remainder of :nml:lst:`JULES_SURFACE` to the shared metadata in jules-shared. (#39)
 *  Updated URLs in metadata. (#55)
 *  Various improvements to GitHub workflow. (#27, 48, 52, 56, 57, 58)

    
Changes to testing
------------------

 *  Updates for testing at UKCEH: added a Rocky9 platform and enabled testing of the rivers-only build. (#35)
 *  Changed Met Office Cray EX queue used by remote init jobs to shared to reduce resource usage and improve turnaround. (#51)
 *  Added a configuration for the Bureau of Meteorology's Cray EX Sentinel system. (#53)


Documentation updates
---------------------

 *  Updates associated with many of the above changes, and release notes.


Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.
