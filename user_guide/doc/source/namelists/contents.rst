The JULES namelist files
========================


Each run of JULES is controlled by a number of files containing Fortran namelists. These files specify details including:

* Switches to allow different model configurations to be selected at run-time.
* Start and end times for the run.
* What input data to use and how to read it.
* How to construct the model grid.
* Values for various parameters.
* The required output.

These files have specific names, and JULES expects all these files to exist for every run (even when their contents are not required). JULES also expects that the namelists within each file appear in the order given below.


.. toctree::
   :maxdepth: 2

   intro
   jules_prnt_control.nml
   jules_surface_types.nml
   cable_surface_types.nml
   model_environment.nml
   jules_surface.nml
   jules_radiation.nml
   jules_hydrology.nml
   jules_soil.nml
   jules_vegetation.nml
   jules_soil_biogeochem.nml
   jules_soil_ecosse.nml
   jules_deposition.nml
   jules_snow.nml
   jules_rivers.nml
   oasis_rivers.nml
   jules_water_resources.nml
   jules_irrig.nml
   science_fixes.nml
   timesteps.nml
   model_grid.nml
   ancillaries.nml
   cable_prognostics.nml
   pft_params.nml
   cable_pftparm.nml
   nveg_params.nml
   cable_soilparm.nml
   crop_params.nml
   triffid_params.nml
   urban.nml
   fire.nml
   drive.nml
   imogen.nml
   prescribed_data.nml
   initial_conditions.nml
   output.nml
