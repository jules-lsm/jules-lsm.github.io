JULES version 5.5 Release Notes
===============================


The JULES vn5.5 release consists of approximately 18 tickets from 14 authors, including work by many other people.

Full details of the tickets committed for JULES vn5.5 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v5.5+release>`_.

Ticket numbers are indicated below, e.g. #434.

Science changes
---------------

 *  Methane feedbacks from natural wetlands added to IMOGEN - see :nml:mem:`IMOGEN_RUN_LIST::land_feed_ch4`. This is done by adding an anomaly relative to the default emissions. Users should confirm that the wetland emissions are correct - see the notes under :nml:mem:`IMOGEN_RUN_LIST::land_feed_ch4`.
 *  Code changes for the GL9 configuration, including options to specify specific values for the roughness length of each Plant Functional Type (:nml:mem:`JULES_VEGETATION::l_spec_veg_z0`) and to impose a maximum-allowed value of the canopy heat capacity for vegetation (:nml:mem:`JULES_VEGETATION::l_limit_canhc`). (#903)
 *  Additional options for distributed form drag (`fd_stab_dep`) - not available in off-line JULES.  (#870)


General/Technical changes
-------------------------

 *  Separate the calculation of plant-soil N fluxes from the updating of the soil stores - to allow the fluxes to be used with alternative soil models. (#651)
 *  Initial steps towards representing dry deposition in JULES: new namelists :nml:lst:`JULES_DEPOSITION` and :nml:lst:`JULES_DEPOSITION_SPECIES`. Note that deposition cannot yet be modelled in JULES. (#662)
 *  River routing code tidied. (#877)
 *  The interface (API) between the JULES program and the CONTROL subroutine now includes the atmospheric forcing variables as input and the gridbox mean surface flxues as output. This creates a clean "managed API" that can be used by parent models to call the JULES code at the CONTROL subroutine level. (#914)
 *  Added diagnostics for absorbed photosynthetically active radiation (`apar` and `apar_gb`) and gridbox mean leaf area index (`lai_gb`) - see :ref:`output_variables_section`. (#614, 890)
 *  Corrected the units given for the ozone flux diagnostic (`flux_o3_stom`). (#905)
 *  Improved computational performance of ice-related and other routines. (#866, 894)
 *  Removed code only used for UM (atmospheric model) diagnostics; now using the sf_diag structure. (#899)
 *  Changes for UM diagnostics - to accommodate the fact that copydiag is now in a module. (#908)
 *  Moved the CABLE soil parameters to a separate namelist :nml:lst:`CABLE_SOILPARM`. (#900)
 *  Improvements to code involved in creating the JULES release, including the documentation. (#893)


Bugs fixed
----------

 *  Removed use of uninitialised memory in RFM river routing scheme. (#896)


Documentation updates
---------------------

 *  Updates associated with many of the above changes, and release notes. (#924)

Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.
