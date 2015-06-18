JULES science configurations
============================


As a component of the Met Office Unified Model (UM), JULES is used for a wide range of purposes, from very short-term forecasting to earth system modelling over timespans of many decades. To achieve this, the UM uses the same code configured in different ways (e.g. switching science options on and off, changing scientific parameter values). The JULES science configurations aim to replicate some of the commonly used UM configurations for standalone JULES, making it simple to run JULES with appropriate science options for different purposes.

These configurations do not include all the namelists that JULES requires to run - they only define the scientific options (e.g. which pieces of science are switched on, scientific parameter values). They must be combined with dataset-specific namelists to run JULES - examples are provided showing how to run each configuration using the Loobos weather station data that is bundled with JULES (see :doc:`/examples`).

The namelists for each configuration can be found in the ``configurations`` directory.

ESM1.0
    This is an earth-system type configuration designed to produce reasonable global vegetation distributions and carbon fluxes. The first version of the configuration is based on parameters used in the ISI-MIP project and uses :nml:mem:`JULES_SWITCHES::can_rad_mod` = 1. Future versions will replicate the setup used in HadGEM3-ES/UK-ESM1.

    It is the only configuration to use TRIFFID, competing vegetation and the multi-layer snow scheme. It is also the only configuration that is made up of two parts:
    
    1.  A spin up run using :nml:mem:`JULES_SWITCHES::l_trif_eq` = T and a long :nml:mem:`JULES_TIME::triffid_period`.
    2.  A transient run, started from the end dump of the spinup run, using :nml:mem:`JULES_SWITCHES::l_trif_eq` = F and a shorter :nml:mem:`JULES_TIME::triffid_period`.

EURO4
    This configuration replicates the science used in the Met Office European 4km forecast model.

GL4.0
    Global Land (GL) is a configuration of JULES that is developed over an annual release cycle for use across weather and climate modelling timescales and systems. Global Land is used in the Met Office Unified Model with the Global Atmosphere (GA) configuration. More information can be found on the Met Office collbaration wikis for `GL <http://collab.metoffice.gov.uk/trac/GL/>`_ and `GA <http://collab.metoffice.gov.uk/trac/GA/wiki>`_.

Operational Forecast
    This configuration replicates the science used in the Met Office global forecast model. It is designed to run as fast as possible, and this is reflected in the selected science options. This is the only configuration that uses the aggregate surface tile.

UKV
    This configuration replicates the science used in the Met Office UK Variable resolution forecast model.
