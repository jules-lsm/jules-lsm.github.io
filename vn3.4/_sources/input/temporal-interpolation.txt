Temporal interpolation
======================

When providing time-varying input data to JULES, the user must specify how the data should be interpolated onto the model timestep. The permitted interpolation flags are shown the following table. These flags are case-sensitive.

+------------+-----------------------------------------------------------------------------------------+
| Flag value | Notes                                                                                   |
+============+=========================================================================================+
| ``b``      | Backward time average, ending at given time. Will be interpolated with time.            |
|            |                                                                                         |
+------------+-----------------------------------------------------------------------------------------+
| ``c``      | Centred time average, centred on given time. Will be interpolated with time.            |
+------------+-----------------------------------------------------------------------------------------+
| ``f``      | Forward time average, starting at given time. Will be interpolated with time.           |
+------------+-----------------------------------------------------------------------------------------+
| ``i``      | Instantaneous value at the given time. Will be linearly interpolated with time.         |
+------------+-----------------------------------------------------------------------------------------+
| ``nb``     | Backward time average, ending at the given time. Value will be held constant with time. |
+------------+-----------------------------------------------------------------------------------------+
| ``nc``     | Centred time average, centred on given time. Value will be held constant with time.     |
+------------+-----------------------------------------------------------------------------------------+
| ``nf``     | Forward time average, starting at given time. Value will be held constant with time.    |
+------------+-----------------------------------------------------------------------------------------+

Depending on the time interpolation flags, driving data may need to be supplied for one or two times that fall before or after the times for the integration. The interpolation scheme implemented in JULES for flags ``b``, ``c`` and ``f`` is a simplified version of the Sheng and Zwiers (1998) [#]_ method that conserves the period means of the driving data file. In order to ensure conservation of the average, these flags should be used only if the data period is an even multiple of the model timestep (i.e., if ``data_period = 2 * n * timestep_len; n = 1, 2, 3, ...``). In these cases the curve-fitting process tends to produce occasional values near turning points that fall outside the range of the input values. Note that for centred data (flags ``c`` and ``nc``) the time of the data should be given as that at the start of the averaging period, rather than the centre, e.g. the 3-hour average over 06H to 09H, centred at 07:30H, should be treated as having timestamp 06H.

.. figure:: interpolation_schematic.png
   :alt: Schematic of JULES interpolation
   
   Schematic of JULES interpolation of driving variable from a 3 hour timestep to a 45 minute timestep. Simulation start time is 0000Z (on an arbitrary day) and end time is 1200Z. Blue circles indicate driving data required to complete a JULES simulation.


.. rubric:: Footnotes

.. [#] Sheng and Zwiers (1998) An improved scheme for time-dependent boundary conditions in atmospheric general circulation models, Climate Dynamics, 14, 609-613.
