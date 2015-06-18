Further code guidance and best practices
========================================


* Avoid the use of 'magic numbers'. A 'magic number' is a numeric constant that is hard wired into the code. These are very hard to maintain and obscure the function of the code. It is much better to assign the 'magic number' to a variable or constant with a meaningful name and use this throughout the code. In many cases the variable may be best placed in a module. This ensures that all subroutines will use the correct value of the numeric constant and that alteration of it in one place will be propagated to all its occurrences. For example:

  Common practice
      .. code-block:: fortran
      
         IF (ObsType == 3) THEN
         
  Better approach
      .. code-block:: fortran
      
         INTEGER, PARAMETER :: SurfaceWind = 3 ! No. for surface wind

         ! ...

         IF (ObsType == SurfaceWind) THEN
         
* Write well structured code making use of subroutines to separate specific subtasks. In particular all file I/O should be done through subroutines. This greatly facilitates the portability of the code. Subroutines should be kept reasonably short, but don't forget there are start up overheads involved in calling an external subroutine, so they should do a reasonable amount of work.

* If you find yourself copying and pasting the same code, consider making it a ``SUBROUTINE`` or ``FUNCTION`` that can be called from the different places in the code.

* Any code that introduces new physics to JULES should have a switch to enable it to be turned off. This makes it possible to run the model in a configuration that is identical to the model before the new physics went in, in order to check that nothing unexpected has been broken.

* Code should be accompanied by technical documentation describing the physical processes that the additional code is intended to model and how this is achieved. Any equations used should be documented (in their continuous form where appropriate) along with the methods used to discretise these equations. In the case where new subroutines/functions have been added, a calling tree should be included. Any changes to the JULES control file should also be clearly documented.

The most important thing is to always bear in mind that somebody will have to maintain your code in the future. That person could even be you several years later! Make sure you comment code thoroughly and use some common sense where procedures are not clear from this document.
