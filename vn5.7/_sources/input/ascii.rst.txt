ASCII files
===========

JULES only supports the use of ASCII files for data at a single location. In this case, the input grid can be specified either as a 1D grid with length 1 or as a 2D grid of size 1 x 1. The data should be laid out in columns with one timestep of data per row (with time increasing with the number of rows). For variables with additional 'levels' dimensions (e.g. soil layers), the values for each level should be in consecutive columns. 

.. note:: Variables should be given to JULES in the order they appear in the file, and there should be no unused variables in between. This may mean that some datasets may require pre-processing for use with JULES, even if they are already columnar.

If the first character of a line is either ``#`` or ``!``, the line is taken to be a comment. JULES reads no information from comments - they are purely for annotating the dataset for users.

Example ASCII input
-------------------

ASCII meteorological forcing data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    # Meteorological data for Loobos, 1997.
    # One year of 30 minute data.
    #   Down  Down      Rainfall      Snowfall     Air       Wind                 Specific
    #   SWR   LWR        rate           rate      temp.      speed     Pressure   humidity
    #(W m-2) (W m-2)  (kg m-2 s-1) (kg m-2 s-1)   (K)       (m s-1) )   (Pa)      (kg kg-1)
        0.0  187.8     0.000E+00     0.000E+00   259.800     2.017     102400.0   1.384E-03
        0.0  186.9     0.000E+00     0.000E+00   259.700     3.770     102400.0   1.384E-03
        0.0  186.7     0.000E+00     0.000E+00   259.600     4.290     102400.0   1.373E-03
    # ...

Each row represents a timestep of data. Each column represents a variable. Driving variables have no additional dimension.

Initial conditions
~~~~~~~~~~~~~~~~~~

::

    # sthuf(1:sm_levels)            t_soil(1:sm_levels)
      0.749  0.743  0.754  0.759    276.78  277.46  278.99  282.48

Although only one 'timestep' of data is supplied, the data must still be laid out in columns. These variables have a value for each soil layer, which are given in consecutive columns. This quickly becomes cumbersome for large numbers of variables, which is why NetCDF is recommended even
for data at a single point.

Time varying data with an additional dimension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    # lai(1:npft)                canht(1:npft)
      0.0  0.0  0.2  0.0  0.0    0.0  0.0  0.6  0.0  0.0
      0.0  0.0  0.2  0.0  0.0    0.0  0.0  0.6  0.0  0.0
      0.0  0.0  0.2  0.0  0.0    0.0  0.0  0.7  0.0  0.0
    # ... 

These variables have one value for each plant functional type (see :doc:`/overview/intro`). For each variable, the values for each pft are in consecutive columns. Each row is one timestep of data.
