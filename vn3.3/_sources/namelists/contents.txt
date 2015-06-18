The JULES namelist files
========================


Each run of JULES is controlled by a number of files containing Fortran namelists. These files specify details including:

* Switches to allow different model configurations to be selected at run-time.
* Start and end times for the run.
* What input data to use and how to read it.
* How to construct the model grid.
* Values for various parameters.
* The required output.

These files have specific names, and JULES expects all these files to exist for every run (even when their contents are not required).


.. toctree::
   :maxdepth: 2

   intro
   logging.nml
   switches.nml
   model_levels.nml
   timesteps.nml
   model_grid.nml
   ancillaries.nml
   pft_params.nml
   nveg_params.nml
   triffid_params.nml
   snow_params.nml
   misc_params.nml
   urban.nml
   imogen.nml
   drive.nml
   prescribed_data.nml
   initial_conditions.nml
   output.nml
