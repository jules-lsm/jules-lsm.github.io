Known limitations of the code
=============================

Limit to longest possible run
-----------------------------

The longest possible run that can be attempted with JULES is approximately 100 years. A longer run should be split into smaller sections, with each later section starting from the final dump of the previous section. This restriction on run length arises because some of the time variables can become too large for the declared type of variable meaning that calculations return incorrect results and the program will probably crash. The size of each variable is in part affected by the compiler used, but a maximum run length of ~100 years appears to be a common case for 32-bit machines. Note that JULES uses the compiler's default KIND for each type of variable. Changes to the KIND of any variable would have to be propagated through the code.


Spin-up over short periods
--------------------------

The current code has not been tested with a spin-up cycle that is short in comparison to the period of any input data (e.g. a spin-up cycle of 1 day using prescribed vegetation data with a period of 10 days). The code will likely run but the evolution of the vegetation data may not be what was intended. However, it is unlikely that a user would want to try such a run.
