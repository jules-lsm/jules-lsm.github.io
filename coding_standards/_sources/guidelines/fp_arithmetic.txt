Floating-point arithmetic
=========================


When writing scientific code, it is important to understand the differences between normal arithmetic and the floating-point arithmetic used by computers. Due to the limited precision available to represent real numbers, many things that are true for normal arithmetic no longer hold in floating-point arithmetic. Special care must also be given to treating variables in a way that is physically realistic, not just mathematically correct. Failure to do so can result in a model that is over-sensitive to both changes in computing platform and small perturbations in initial conditions.


Comparing real numbers
----------------------

A common place for errors of this kind to arise is when comparing real numbers to each other. Consider the following code:

.. code-block:: fortran

   IF ( snow_tile > 0.0 ) THEN
     ! ...
   ELSE
     ! ...
   END IF
   
This code is meant to be modelling two different physical situations – the case where snow is present on a tile and the case where it is not. You may expect that a tile with no snow would have ``snow_tile`` set to 0. However, due to differences in compilers, optimisation options and floating-point rounding errors, ``snow_tile`` could end up being tiny (say 10\ :sup:`-20`) rather than 0. This snow amount is physically negligible, so we would want the model to behave as if there is no snow. This is not the case, however, since 10\ :sup:`-20` is greater than 0. This kind of unphysical branching can lead to significant errors.

Other than avoiding this kind of branching ``IF`` statement entirely, there are two ways around this problem:

1. Specify a physically realistic tolerance level, e.g.

   .. code-block:: fortran

      IF ( snow_tile > tolerance ) THEN
        ! ...
      ELSE
        ! ...
      END IF
      
   where ``tolerance`` is some small value greater than 0.

   One problem with this solution is that you may end up with several different tolerances defined in various places in the code. For this reason, ``tolerance`` should be obtained using the Fortran intrinsic functions ``EPSILON`` (``EPSILON(X)`` returns a nearly negligible number relative to 1) or ``TINY`` (``TINY(X)`` returns the smallest positive (non zero) number of the same type as ``X`` that the computer can represent) where possible. If the values provided by these intrinsic functions are inappropriate, the tolerance should be declared as a ``PARAMETER`` in the variable declarations section of the programming unit.
   
   When defining a value for tolerance, bear in mind that if the value is too large it could lead to problems with conservation of variables (e.g. water, energy, carbon).
 
2. Set the variable in question to 0.0 whenever it makes sense physically, e.g.

   .. code-block:: fortran

      IF ( snow_tile should be 0 physically ) THEN
        snow_tile = 0.0
      END IF

      IF ( snow_tile > 0.0 ) THEN
        ! ...
      ELSE
        ! ...
      END IF

   This solution avoids the problem of having several different tolerances defined in the code. However, depending on how the condition ``snow_tile should be 0 physically`` is defined, it could lead to problems with conservation of variables (in this case, water, due to loss of snow).
   
Which solution to use is highly dependent on the particular problem, and requires careful thought. In general, the 2nd solution is preferable, since it avoids having several different tolerances defined in the code.

Although the above conversation focuses on comparing values to zero, the same concepts apply in the general case of comparing any real number to any other. For example:

Common practice
    .. code-block:: fortran
    
       IF ( real1 > real2 ) THEN
         ! ...
       ELSE
         ! ...
       END IF

Better approach
    .. code-block :: fortran

       IF ( real1 - real2 > tolerance ) THEN
         ! ...
       ELSE
         ! ...
       END IF

where, as above, tolerance is some suitably small number.

The same concerns about rounding errors must also be considered when comparing two real numbers for equality, e.g.

Common practice
    .. code-block:: fortran

       IF ( real1 == real2 ) THEN
         ! ...
       END IF
 
Better approach
    .. code-block:: fortran

       IF ( ABS(real1 – real2) < tolerance ) THEN
         ! ...
       END IF

where, again, tolerance is some suitably small number.

Such concerns with rounding errors do not apply to ``INTEGER`` and ``LOGICAL`` comparisons, hence the form ``value1 == value2`` can be used for these.


Non-distributive arithmetic
---------------------------

Scientific programmers should also be aware that some algebraic identities that hold for normal arithmetic no longer hold in floating-point arithmetic, mainly due to rounding errors. In particular, unlike normal arithmetic, the order in which calculations are performed will affect the answer given. For example, the following statements are true for normal arithmetic, but do not hold in floating-point arithmetic::

    x + (y + z) == (x + y) + z
    x * (y * z) == (x * y) * z
    x * (y / z) == (x * y) / z

This can lead to extremely subtle errors that are hard to spot, so developers should bear this in mind at all times. Trying to enforce the order of calculation using brackets will not necessarily solve this problem, since the compiler will make decisions for itself depending on optimisation options, etc.

A more in depth discussion of these kinds of rounding errors can be found in the accompanying document :download:`Dealing with rounding issues </MO_sensitivity_project.pdf>` from the Met Office UM perturbation sensitivity project. The document also includes some real world examples of rounding issues from the Met Office Unified Model.
