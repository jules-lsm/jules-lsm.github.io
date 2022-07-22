JULES output
============


JULES separates output into one or more output 'profiles'. Within each profile, all variables selected for output are written to the same file with the same frequency (also referred to as the 'output period'). The output period can be any multiple of the model timestep, including calendar months or years.

Most output is provided on the model grid only. Some variables are provided on the river routing model grid instead. Each output profile can contain **either** model grid **or** river routing model grid variables, but not both.

Each output file contains the latitude and longitude of each point to allow the points to be located in a grid if desired (e.g. for visualisation). Output files also contain two time related variables to locate the values in time (this is described in more detail `below <#associating-output-values-with-the-correct-time>`_).

JULES is capable of performing five different types of time-processing - snapshot (instantaneous) values, time averages, time minima, time maxima and time accumulations. Snapshots are instantaneous values produced during the first model timestep of each output period. Time averages, minima, maxima and accumulations are calculated over the output period. Each output variable is annotated with a |cell methods attribute|_ to indicate whether it is a snapshot value (``time : point``), time average (``time : mean``), time minimum (``time : minimum``), time maximum (``time : maximum``) or time accumulation (``time : sum``).

.. |cell methods attribute| replace:: CF convention ``cell_methods`` attribute
.. _cell methods attribute: http://cfconventions.org/Data/cf-conventions/cf-conventions-1.6/build/cf-conventions.html#cell-methods


Each profile can be considered as a separate data stream. By using more than one profile the user can, for example:

* Output one set of variables to one file, and other variables to another file.
* Write instantaneous values to one file, and time-averaged values to another.
* Write low-frequency output throughout the run to one file, and high-frequency output from a smaller part of the run (e.g. a 'special observation period') to another file.

All output files will be NetCDF if JULES is compiled with 'proper' NetCDF libraries (see :doc:`/building-and-running/intro`). Otherwise all output will be in columnar ASCII files.


Associating output values with the correct time
-----------------------------------------------

JULES output files contain two time related variables to allow model output to be associated with the correct model time:

``time``
    For each output period, this variable contains the time of the end of the output period. This is the time that any snapshot values apply at.

``time_bounds``
    For each output period, this variable contains two values - the start and end of the output period. The output period is then the half-open interval given by:
    
    .. code-block:: fortran

        time_bounds(1) < time <= time_bounds(2)
        
    This is the interval that means, minima, maxima and accumulations are calculated over.
    
During each model timestep, JULES captures values for output at the end of the timestep (i.e. after all the science code). This means that in output files, snapshot data at a particular timestep is:

* The state of the model at the end of the model timestep.
* The fluxes that produced that state over the model timestep.

Due to the way the model equations work, this ensures that all output at a given timestep in the output files is consistent.


.. _initial_data:

Initial data
------------

With the formulation given above, the initial state of the model (i.e. the state at the beginning of the first timestep of a section) is never output (except to dump files). For the majority of users, this will not be an issue. If the initial state is required, it is possible for an output profile to output the initial state for each section of a run (i.e. initial state of each spinup cycle and the main run) to a separate file - see :nml:mem:`JULES_OUTPUT_PROFILE::output_initial`.

.. warning::
   In initial data files, **only snapshot values for state variables will be valid**. All other variables specified in the output profile will exist in the file, but their values will be garbage - *not necessarily NAN* - so use these files with caution.


Dump files
----------

JULES writes dump files (a snapshot of the current model state) at several points during a run. These can be used to restart the model from that point if desired. The times that dump files are written are:

* After initialisation is complete, immediately before the start of the run (initial state).
* Before starting each cycle of spin-up.
* Before starting the main run.
* At the end of the run (final state).
* At the start of each calendar year.

Each dump is marked with the model date and time that it was produced.

Prior to vn4.3, the dump file contained sufficient prognostic variables such that the pre-dump model state could be recreated. From vn 4.3 onwards, the dump file now includes ancillary data. The model can optionally restart from these data rather than the values given in the ancillaries namelists. Latitude and longitude information are also now written to (but not read from) the dump file to aid users wishing to interrogate dump files for debugging or other purposes.
