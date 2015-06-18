``output.nml``
==============


This file contains a variable number of namelists that are used to specify the output required by the user. The namelist :nml:lst:`JULES_OUTPUT` should occur only once at the top of the file. The value of :nml:mem:`JULES_OUTPUT::nprofiles` in :nml:lst:`JULES_OUTPUT` then determines how many times the namelist :nml:lst:`JULES_OUTPUT_PROFILE` should appear.


``JULES_OUTPUT`` namelist members
---------------------------------

.. nml:namelist:: JULES_OUTPUT

.. nml:member:: output_dir

   :type: character
   :default: None

   The directory used for output files. This can be an absolute or relative path.


.. nml:member:: run_id

   :type: character
   :default: None

   A name or identifier for the run. This is used to name output files and model dumps.


.. nml:member:: nprofiles

   :type: integer
   :permitted: >= 0
   :default: 0

   The number of output profiles that will be specified using instances of the :nml:lst:`JULES_OUTPUT_PROFILE` namelist.



``JULES_OUTPUT_PROFILE`` namelist members
-----------------------------------------

.. nml:namelist:: JULES_OUTPUT_PROFILE

This namelist should occur :nml:mem:`JULES_OUTPUT::nprofiles` times. Each occurrence of this namelist contains information about a single output profile, as described in :doc:`/output`.


.. nml:member:: profile_name

   :type: character
   :default: None

   The name of the output profile.

   This is used in file names and should be specified even if there is only one profile. The name for each profile should be unique to avoid overwriting data unintentionally.

   Although any name can be used for a profile, the user may which to choose a name that reflects the variables in the file (e.g. 'carbon', 'water') or the data frequency (e.g. 'daily', 'monthly').


.. nml:member:: file_period

   :type: integer
   :permitted: -2, -1 or 0
   :default: 0

   The period for output files, i.e. the time interval during which all output goes to the same file.

   .. note:: In all cases, output during spin-up goes into a separate file for each spin-up cycle and output during the main run goes into its own file(s).

   This can be one of three values:

   0
       All output goes into the same file.
   
   \-1
       Monthly files are produced (i.e. all output for a month goes into the same file).
   
   \-2
       Annual files (calendar years) are produced.


.. nml:group:: Members used to specify the times that the profile will generate output

   .. nml:member:: output_spinup
   
      :type: logical
      :default: F
   
      Determines whether the profile will provide output during model spin-up.
   
      TRUE
          Provide output during spin-up. Output is provided for the whole of the model spin-up. Output from each spin-up cycle goes into separate files.
   
      FALSE
          Do not provide any output during spin-up.
   
   
   .. nml:member:: output_main_run
   
      :type: logical
      :default: F
   
      Determines whether the profile will provide output during the main model run (i.e. any part of the run after spin-up).
   
      TRUE
          Provide output during the main model run. Output will be provided for all times between :nml:mem:`output_start` and :nml:mem:`output_end` below.
   
      FALSE
          Do not provide any output during the main model run.
          
   .. nml:member:: output_initial
   
      :type: logical
      :default: F
   
      Determines whether the profile will output initial data for the sections for which it is outputting.
      
      See :ref:`initial_data` for caveats on the initial data file(s) produced.
   
      TRUE
          Output initial data for the profile.
          
          If :nml:mem:`output_spinup` = T, an initial data file will be output at the start of each spinup cycle.
          
          If :nml:mem:`output_main_run` = T and :nml:mem:`output_start` = :nml:mem:`JULES_TIME::main_run_start`, an initial data file will be output at the start of the main run.
   
      FALSE
          Do not output any initial data.   
   
   .. nml:member:: output_start
   .. nml:member:: output_end
   
      :type: character
      :default: :nml:mem:`JULES_TIME::main_run_start`, :nml:mem:`JULES_TIME::main_run_end`
   
      The time to start and stop collecting data for output. The times that output is actually produced are determined by :nml:mem:`output_period` below.
   
      If :nml:mem:`output_period` is monthly, then :nml:mem:`output_start` must be 00:00:00 on the 1st of some month.
   
      If :nml:mem:`output_period` is yearly, then :nml:mem:`output_start` must be 00:00:00 on the 1st of January for some year.
   
      If :nml:mem:`output_end` is given such that an output period is not complete when the run reaches :nml:mem:`output_end`, output will not be generated for that final period (e.g. if values are being output monthly but :nml:mem:`output_end` is midday on the 31st December, then output will not be generated for December, even though most of December has been run).
   
      The times must be given in the format::
   
          "yyyy-mm-dd hh:mm:ss"
   
   
   .. nml:member:: sample_period
   
      :type: integer
      :permitted: > 1
      :default: :nml:mem:`JULES_TIME::timestep_len`
   
      The sampling period, in seconds, for time-averages and accumulations.
   
      This must be a factor of the output period and a multiple of the timestep length.
   
      .. note::
         It is strongly recommended that this be left at the default value (sample every timestep), other than in exceptional cases.
      
         In some cases, sampling every timestep adds a considerable computational burden and acceptable output can be achieved by sampling less frequently. For example, with a large domain, many output diagnostics, and a timestep of 30 minutes, a monthly average would be calculated from several hundred values if every timestep was used. For variables that evolve relatively slowly, an acceptable monthly average might be obtained by sampling only every 12 hours.
      
         If fields are not sampled every timestep, the output averages/accumulations will only be approximations.
   
   
   .. nml:member:: output_period
   
      :type: integer
      :permitted: -2, -1 or > 1
      :default: :nml:mem:`JULES_TIME::timestep_len`
   
      The period for output, in seconds.
   
      This must be a multiple of the timestep length, except for the special cases:
   
      -1. Monthly period.
      -2. Annual period.


.. nml:group:: Members used to specify the variables that the profile will output

   .. nml:member:: nvars
   
      :type: integer
      :permitted: >= 0
      :default: 0
   
      The number of variables that the profile will provide output for.
   
      The variables available for output are given in :doc:`/output-variables`.
   
   
   .. nml:member:: var
   
      :type: character(nvars)
      :default: None
   
      List of variable names to output, as recognised by JULES (see :doc:`/output-variables`). Names are case sensitive.
   
   
   .. nml:member:: var_name
   
      :type: character(nvars)
      :default: '' (empty string)
   
      For each variable specified in :nml:mem:`var`, this is the name to give the variable in output files.
   
      If the empty string (the default) is given for any variable, then the corresponding value from :nml:mem:`var` is used instead.
   
   
   .. nml:member:: output_type
   
      :type: character(nvars)
      :default: 'S'
   
      For each variable specified in :nml:mem:`var`, this indicates the type of processing required.
   
      Recognised values are:
   
      S
          Instantaneous or snapshot value.
   
      M
          Time mean value.
   
      A
          Accumulation over time.
   
      For time averaged variables, the period over which each time average is calculated is given by :nml:mem:`output_period`. For time-accumulation variables, :nml:mem:`output_period` gives the period for output of an updated accumulation (i.e. how often the value is reported). For both time averages and accumulations, the sampling frequency is given by :nml:mem:`sample_period`.
   
      .. note:: A time-accumulation is initialised at the start of a run and thereafter accumulates until the end of the run. This may mean that accuracy is lost, particularly towards the end of long runs, if small increments are added to an already large sum.



Example of requesting output
----------------------------

In this example, the user has requested two output profiles. One provides gridbox monthly means for the whole of the main run, the other provides snapshot values of per-tile variables every timestep for a single year. We assume that :nml:mem:`JULES_TIME::timestep_len` = 1800, :nml:mem:`JULES_TIME::main_run_start` = '1995-01-01 00:00:00' and :nml:mem:`JULES_TIME::main_run_end` = '2005-01-01 00:00:00', so that exactly 10 years will be run. There is no spin-up.

::

    &JULES_OUTPUT
      run_id = "jules_run001",

      output_dir = "./output",

      nprofiles = 2
    /

    &JULES_OUTPUT_PROFILE
      profile_name = "month",

      output_main_run = T,

      output_period = -1,

      nvars = 4,
      var         =    "emis_gb"        "ftl_gb"  "snow_mass_gb"  "tstar_gb",
      var_name    = "Emissivity"  "SensibleHeat"      "SnowMass"      "Temp",
      output_type =          'M'             'M'             'M'         'M'
    /

    &JULES_OUTPUT_PROFILE
      profile_name = "tstep",

      output_main_run = T,
      output_start    = "2000-01-01 00:00:00",
      output_end      = "2001-01-01 00:00:00",

      nvars = 4,
      var         = "emis"  "ftl"  "snow_mass"  "tstar",
      output_type =    'S'    'S'          'S'      'S'
    /

Or using the alternative list syntax (see :doc:`intro`)::

    &JULES_OUTPUT
      # ... as above ...
    /

    &JULES_OUTPUT_PROFILE
      # ... as above ...

      nvars = 4,
      var(1) = "emis_gb",       var_name(1) = "Emissivity",    output_type(1) = 'M',
      var(2) = "ftl_gb",        var_name(2) = "SensibleHeat",  output_type(2) = 'M',
      var(3) = "snow_mass_gb",  var_name(3) = "SnowMass",      output_type(3) = 'M',
      var(4) = "tstar_gb",      var_name(4) = "Temp",          output_type(4) = 'M'
    /

    &JULES_OUTPUT_PROFILE
      # ... as above ...

      nvars = 4,
      var(1) = "emis",       output_type(1) = 'S',
      var(2) = "ftl",        output_type(2) = 'S',
      var(3) = "snow_mass",  output_type(3) = 'S',
      var(4) = "tstar",      output_type(4) = 'S'
    /

The :nml:lst:`JULES_OUTPUT` namelist is simple - it gives an id for the run, specifies the directory to put output in and specifies the number of profile definitions that follow.

Each profile is given a unique name. Both profiles want to output part of the main run, so must set :nml:mem:`JULES_OUTPUT_PROFILE::output_main_run` to TRUE. Since :nml:mem:`JULES_OUTPUT_PROFILE::sample_period` is not given for either profile, both will use the default (sample every timestep). The same is true for :nml:mem:`JULES_OUTPUT_PROFILE::file_period` - since it is not given for either profile, it takes its default value and all output for each profile will go into a single file.

The first output profile wants to output monthly averages, so :nml:mem:`JULES_OUTPUT_PROFILE::output_period` is set to -1 (the special value indicating that calendar months should be used for the output period) and :nml:mem:`JULES_OUTPUT_PROFILE::output_type` is set to 'M' (for mean) for each variable. The user wants this profile to output for the whole of the main run, so does not need to specify :nml:mem:`JULES_OUTPUT_PROFILE::output_start` or :nml:mem:`JULES_OUTPUT_PROFILE::output_end` (note that this is only possible because the main run starts at 00:00:00 on the 1st of a month - if this was not the case, the user would have to specify a different time for :nml:mem:`JULES_OUTPUT_PROFILE::output_start`). The user has also chosen to supply the names that each variable will use in output files using :nml:mem:`JULES_OUTPUT_PROFILE::var_name`.

The second output profile has specified a section of the main run that it will provide output for using :nml:mem:`JULES_OUTPUT_PROFILE::output_start` and :nml:mem:`JULES_OUTPUT_PROFILE::output_end` such that exactly a year of data will be output. Since :nml:mem:`JULES_OUTPUT_PROFILE::output_period` is not specified, it takes its default value, and output will be produced every timestep. The user has not specified the names to use in output files for this profile, so the values from :nml:mem:`JULES_OUTPUT_PROFILE::var` will be used.

