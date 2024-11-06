JULES version 7.7 Release Notes
===============================

The JULES vn7.7 release consists of approximately XX tickets from XX authors, including work by many other people.

Full details of the tickets committed for JULES vn7.7 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v7.7+(Oct-24)>`_.

Ticket numbers are indicated below, e.g. #XXX.

General/Technical changes
-------------------------

 *  Initialisation related to the CaMa-Flood model of river routing and inundation. Note that this model is still in development and cannot yet be used. (#1000)
 *  Developments to allow the blending height to be increased and passed between timesteps - for use with the UM atmospheric model. (#1500)
    
Bugs fixed
----------

 *  Fixed a bug that prevented the calculation of time-mean river-point variables in MPI runs. (#1544)
 *  Enables the lake_evap field to be populated in LFRic-based models, even when river routing is not selected. (#1546)


Changes to testing
------------------

 *  Correct PBS directives used for runs on Met Office EX platforms. (#1547)


Documentation updates
---------------------

 *  Updates associated with many of the above changes, and release notes. (#1567)


Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.

