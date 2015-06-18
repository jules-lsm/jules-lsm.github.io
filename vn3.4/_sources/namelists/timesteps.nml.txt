``timesteps.nml``
=================


This file sets the start and end time of the run. It can also be used to specify an optional spin-up procedure. It contains two namelists called :nml:lst:`JULES_TIME` and :nml:lst:`JULES_SPINUP`.

.. warning::
   It is recommended that all times use Greenwich Mean Time (GMT or UTC), not local time. The use of GMT is essential if certain options are set.


``JULES_TIME`` namelist members
-------------------------------

.. nml:namelist:: JULES_TIME

.. nml:member:: timestep_len

   :type: integer
   :permitted: >= 1
   :default: None

   Model timestep length in seconds.

   Typically, 30 or 60 minutes is chosen, depending on the driving data available.

   .. warning::
       If the timestep is too long, the model becomes numerically unstable.


.. nml:member:: main_run_start
.. nml:member:: main_run_end

   :type: character
   :default: None

   The start and end times for the integration.

   Each run of JULES consists of an optional spin-up period and the 'main run' that follows the spin-up. See below for more about the specification of the spin-up. These variables specify the start and end times for the 'main run'.

   The times must be given in the format::

       "yyyy-mm-dd hh:mm:ss"


.. nml:member:: phenol_period

   :type: integer
   :permitted: >= 1
   :default: None

   Period for calls to phenology model in *days*. Only relevant if :nml:mem:`JULES_SWITCHES::l_phenol` = TRUE.


.. nml:member:: triffid_period

   :type: integer
   :permitted: >= 1
   :default: None

   Period for calls to TRIFFID model in *days*. Only relevant if one of :nml:mem:`JULES_SWITCHES::l_triffid` or :nml:mem:`JULES_SWITCHES::l_trif_eq` is TRUE.


.. nml:member:: print_step

   :type: integer
   :permitted: >= 1
   :default: 1

   Number of timesteps between printing timestep information to screen, i.e. if :nml:mem:`print_step` = 48, then the timestep start time will only be printed every 48 timesteps.



``JULES_SPINUP`` namelist members
---------------------------------

.. nml:namelist:: JULES_SPINUP


.. nml:member:: max_spinup_cycles

   :type: integer
   :permitted: >= 0
   :default: 0

   The maximum number of times the spin-up period is to be repeated:

   0
       No spin-up.

   > 0
       At least 1 and at most :nml:mem:`max_spinup_cycles` repetitions of spin-up are used.

   After each repetition, the model tests whether the selected variables have changed by more than a specified amount over the last repetition (see :nml:mem:`tolerance` below).

   If the change is less than this amount, the model is considered to have spun up and the model moves on to the main run.


.. nml:member:: spinup_start
.. nml:member:: spinup_end

   :type: character
   :default: None

   Only used if :nml:mem:`max_spinup_cycles` > 0.

   The start and end times for each cycle of spin-up.

   The times must be given in the format::

       "yyyy-mm-dd hh:mm:ss"


.. nml:member:: terminate_on_spinup_fail

   :type: logical
   :default: F

   Only used if :nml:mem:`max_spinup_cycles` > 0.

   Switch controlling behaviour if the model does not pass the spin-up test after :nml:mem:`max_spinup_cycles` of spin-up.

   TRUE
       End the run if model has not spun up.

   FALSE
       Continue the run regardless.


.. nml:group:: Variables used to specify spin-up conditions

    .. nml:member:: nvars

       :type: integer
       :permitted: >= 0
       :default: 0

       Only used if :nml:mem:`max_spinup_cycles` > 0.

       The number of variables to use to assess if the model has spun up.


    .. nml:member:: var

       :type: character(nvars)
       :default: None

       Only used if :nml:mem:`nvars` > 0.

       List of variables to be used to determine if the model has spun up. Spin-up can be assessed in terms of soil temperature and soil moisture.

       Possible values are:

       ``smcl``
           Moisture content of each soil layer (kg m\ :sup:`-2`).

       ``t_soil``
           Temperature of each soil layer (K).


    .. nml:member:: use_percent

       :type: logical(nvars)
       :default: F

       Only used if :nml:mem:`nvars` > 0.

       Indicates whether the tolerance for each variable is expressed as a percentage.

       TRUE
           Tolerance is a percentage.

       FALSE
           Tolerance is an absolute value.


    .. nml:member:: tolerance

       :type: real(nvars)
       :default: None

       Only used if :nml:mem:`nvars` > 0.

       Tolerance for spin-up test for each variable.

       For each spin-up variable, this is the maximum allowed change over a spin-up cycle if the variable is to be considered as spun-up.



Note on time conventions
------------------------

When specifying start times (e.g. :nml:mem:`JULES_TIME::main_run_start`, :nml:mem:`JULES_SPINUP::spinup_start`), the time is taken to be the *start of the first timestep*. When specifying end times (e.g. :nml:mem:`JULES_TIME::main_run_end`, :nml:mem:`JULES_SPINUP::spinup_end`), the time is taken to be the *end of the last timestep*. Take the following setup::

    &JULES_TIME
      timestep_len   = 3600,
      main_run_start = "1997-01-01 00:00:00",
      main_run_end   = "1998-01-01 00:00:00",

      # ...
    /

With this setup, exactly one whole year of timesteps will be run. The first model timestep begins at 1997-01-01 00:00:00, the second at 1997-01-01 01:00:00 etc. The final model timestep begins at 1997-12-31 23:00:00 and ends at 1998-01-01 00:00:00. No processing occurs for any times in 1998.


Note on solar zenith angle
--------------------------

If a run requires that the solar zenith angle be calculated (:nml:mem:`JULES_SWITCHES::l_cosz` = TRUE), then times must be in Greenwich Mean Time (UTC), so that the code can calculate the zenith angle at each location and time.

If :nml:mem:`JULES_SWITCHES::l_cosz` = FALSE, the user might prefer to use local time, particularly if this is used for input or validation data, as the timestamp on model output will then match that on the other data. However the use of local time is not recommended as if the user later switches to :nml:mem:`JULES_SWITCHES::l_cosz` = TRUE without adjusting the time values, the model results will be in error.


Examples
--------

For all these examples, it is assumed that :nml:mem:`JULES_SWITCHES::l_phenol` = FALSE and :nml:mem:`JULES_SWITCHES::l_triffid` = FALSE, hence we do not need to specify :nml:mem:`JULES_TIME::phenol_period` or :nml:mem:`JULES_TIME::triffid_period` as they will not be used.

A run without spin-up
~~~~~~~~~~~~~~~~~~~~~

::

    &JULES_TIME
      timestep_len   = 3600,
      main_run_start = "1997-01-01 00:00:00",
      main_run_end   = "1999-01-01 01:00:00"
    /

    &JULES_SPINUP
      max_spinup_cycles = 0
    /

This specifies a run with a timestep length of one hour. The run will begin at midnight on 1st January 1997 and end at 01:00 GMT on 1st January 1999. :nml:mem:`JULES_SPINUP::max_spinup_cycles` = 0 means there is no spin-up.

A run with spin-up over a period that immediately precedes the main run
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    &JULES_TIME
      timestep_len   = 3600,
      main_run_start = "1997-01-01 00:00:00",
      main_run_end   = "1999-01-01 01:00:00"
    /

    &JULES_SPINUP
      max_spinup_cycles = 5,
      spinup_start      = "1996-01-01 00:00:00",
      spinup_end        = "1997-01-01 00:00:00"

      # <spinup variable specification>
    /

This specifies a spin-up period from midnight on 1st January 1996 to midnight on 1st January 1997. This spin-up will be repeated up to 5 times, before the main run from midnight on 1st January 1997 until 01:00 GMT on 1st January 1999.

A run with spin-up over a period that overlaps the main run
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    &JULES_TIME
      timestep_len   = 3600,
      main_run_start = "1997-01-01 00:00:00",
      main_run_end   = "1999-01-01 01:00:00"
    /

    &JULES_SPINUP
      max_spinup_cycles = 5,
      spinup_start      = "1997-01-01 00:00:00",
      spinup_end        = "1998-01-01 00:00:00"

      # <spinup variable specification>
    /

This specifies a spin-up period from midnight on 1st January 1997 to midnight on 1st January 1998. This spin-up will be repeated up to 5 times, before the main run from midnight on 1st January 1997 until 01:00 GMT on 1st January 1999.

Example of specifying requirements for spin-up
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    &JULES_SPINUP
      # <spinup time specification>

      terminate_on_spinup_fail = T,

      nvars = 2,
      var         = "smcl"  "t_soil",
      use_percent =     F         T ,
      tolerance   =   1.0       0.1
    /

With this setup, :nml:mem:`JULES_SPINUP::terminate_on_spinup_fail` = TRUE means that if the spin-up has not 'converged' after :nml:mem:`JULES_SPINUP::max_spinup_cycles` cycles, the run will end. Convergence is measured using the moisture content and temperature of each soil layer. At every point and in every layer, soil moisture must change by less than 1 kg m\ :sup:`-2`, while soil temperature must change by less than 0.1%.


Notes on spin-up
----------------

Spin-up is assessed using the difference between instantaneous values at the end of consecutive cycles of spin-up. For example, if the spin-up period is from 2005-01-01 00:00:00 to 2006-01-01 00:00:00 then every time the model gets to the end of 2005 the spin-up variables are compared with their value at the end of the previous cycle. The model is considered spun-up when *all* the spin-up variables are spun-up at *all* points. A spin-up variable is considered spun-up if, at each point, the absolute value of the change (percentage change if :nml:mem:`JULES_SPINUP::use_percent` = TRUE) over the spin-up cycle is less than or equal to the given tolerance.

At present the analysis of whether the model has spun up or not is limited to aspects of the 'physical' state of the system, and does not explicitly consider carbon stores, making it less useful for runs with interactive vegetation (the equilibrium mode of TRIFFID is designed to spin-up TRIFFID) or prognostic soil carbon.

During the spin-up phase of a run, JULES provides the correct driving data (for example, meteorological data) as the model time 'cycles' round over the spin-up period. Consider the case of a spin-up from 2005-01-01 00:00:00 to 2006-01-01 00:00:00. At or near the end of 31st December 2005 during the spin-up, the driving data will start to adjust to the values for 1st January 2005. The calculated driving data may vary slightly between the start or end of the first cycle and similar times in later cycles, because of the need to match the data at the end of each cycle to that at the start of the next cycle. When the main run begins after a period of spin-up, the driving data is reset to the start of the main run - no effort is made to adjust the data for a smooth transition. Generally this does not cause a problem.

Depending upon the details of the input data and any temporal interpolation, the driving data may vary rapidly at the end of a cycle of spin-up, causing an extreme response from the model. In most cases the model will adjust, possibly with large heat fluxes over a few hours, but the user should be aware that unusual behaviour near the end/start of a spin-up cycle may be the result of this adjustment. Consider the case of a spin-up from 2005-01-01 00:00:00 to 2006-01-01 00:00:00. At or near the end of 31st December 2005 during the spin-up, the driving data will start to adjust to the values for 1st January 2005, which could be very different from conditions on 31st December 2005. The length of time over which the driving data adjust depends on the frequency of the data, and the choice of temporal interpolation. For example, with 3-hourly data that is interpolated onto a one hour timestep, the adjustment will take place over 3 hours. However, hourly data and an hourly timestep will force an instantaneous adjustment at the start of 1st January 2005.

Although :nml:mem:`JULES_SPINUP::max_spinup_cycles` specifies the maximum number of spin-up cycles, some of which might not be used if the model is considered to have spun up earlier, it is possible to specify the exact number of cycles that will be performed. This can be done by demanding an impossible level of convergence by setting :nml:mem:`JULES_SPINUP::tolerance` < 0 (remember that :nml:mem:`JULES_SPINUP::tolerance` is compared with the absolute change over a cycle) and setting :nml:mem:`JULES_SPINUP::terminate_on_spinup_fail` = FALSE so that the integration continues when spin-up is judged to have failed after :nml:mem:`JULES_SPINUP::max_spinup_cycles` cycles.

Although it is expected that a spin-up phase will be followed by the main run in the same integration, it is possible to do the spin-up and main run in separate integrations. This can be done by demanding an impossible level of convergence by setting :nml:mem:`JULES_SPINUP::tolerance` < 0 and setting :nml:mem:`JULES_SPINUP::terminate_on_spinup_fail` = TRUE so that the integration stops when spin-up is judged to have failed. The final state of the model, after :nml:mem:`JULES_SPINUP::max_spinup_cycles` cycles of spin-up, will be written to the final dump, and a subsequent simulation can be started from this dump.

A limitation of the current code is that it cannot cope with a spin-up cycle that is short in comparison to the period of any input data. For example, a spin-up cycle of 1 day cannot use 10-day vegetation data. The code will likely run but the evolution of the vegetation data will probably not be what the user intended! However, it is unlikely that a user would want to try such a run.

Occasionally, the model fails to diagnose a spun up state when in fact the integration has reached a quasi-steady state that is not detected by the procedure of assessing spin-up through comparison of instantaneous values at the end of consecutive cycles of spin-up. An example of this is 'period-2' behaviour, where the model state repeats itself over a period of 2 cycles. Such behaviour should be apparent in the model output during spin-up, and the user can opt to repeat the integration over a given number of spin-up cycles, and not to wait for a spun-up state to be diagnosed.
