JULES version 3.2 Release Notes
===============================


JULES version 3.2 sees several enhancements and bug fixes in both the science and control code.


Standard Configurations
-----------------------

A set of standard science configurations have been defined. These are based on well tested operational Met Office models, and are intended to cover a wide range of use cases.


Improvements to output
----------------------

In JULES version 3.1, under some circumstances, it was not entirely clear how the timestamps in output files applied to the values. This has been thoroughly addressed in version 3.2.

Changes have also been made to the attributes of output variables:

* The units attribute for output variables has been updated to be compliant with `UDUNITS2 <http://www.unidata.ucar.edu/software/udunits/>`_.
* A `CF conventions <http://cfconventions.org>`_ coordinates attribute has been added to all output variables that explicitly links the latitude and longitude to the data.


Biogenic Volatile Organic Compound (BVOC) emissions
---------------------------------------------------

Code written by Federica Pacifico for isoprene emissions has been implemented and extended to include monoterpene, acetone and methanol emissions. This addition is purely diagnostic in the standalone model (i.e. provides new output variables, but has no feedbacks), but will allow the UM to implement interactive BVOC emissions (i.e. with feedbacks) in the future.

A paper has been written describing and evaluating the isoprene emission scheme - Pacifico et. al., 2011. Atmos. Chem. and Phys., 11, 4371-4389 (`PDF <http://www.atmos-chem-phys.net/11/4371/2011/acp-11-4371-2011.pdf>`_).


Alternative build system
------------------------

It is now possible to build JULES using FCM make. FCM is a set of tools developed by the Met Office for managing and building source code, with a particular focus on making it easy to build large Fortran programs (such as JULES). FCM is open source software, and can be downloaded for free from `Github <https://github.com/metomi/fcm>`_.


Bugs fixed
----------

*   Array bounds error with ``SICE_INDEX_NCAT``.
*   Incorrect usage of ``COR_MO_ITER``.
*   Monthly/yearly output files not rolling over properly on certain configurations of GFortran.
*   A collection of small memory leaks.
*   Not able to read or write ASCII dumps with the new snow scheme on.
*   Use fixed dimension names for output files (rather than using those given for input files).
*   Using ``can_rad_mod = 5`` causes night-time dark respiration to be 0 under certain circumstances.

