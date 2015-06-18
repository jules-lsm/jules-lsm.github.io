Fortran features
================


The following is a list of Fortran features that you should use or avoid.

* Use ``IMPLICIT NONE`` in all program units. This forces you to declare all your variables explicitly. This helps to reduce bugs in your program that will otherwise be difficult to track.

* Design any derived data types carefully and use them to group related variables. Appropriate use of derived data types will allow you to design modules and procedures with simpler and cleaner interfaces.

* Where possible, module variables and procedures should be declared ``PRIVATE``. This avoids unnecessary export of symbols, promotes data hiding and may also help the compiler to optimise the code.

* When you are passing an array argument to a ``SUBROUTINE`` / ``FUNCTION``, and the ``SUBROUTINE`` / ``FUNCTION`` does not change the ``SIZE`` / ``DIMENSION`` of the array, you should pass it as an assumed shape array. Memory management of such an array is automatically handled by the ``SUBROUTINE`` / ``FUNCTION``, and you do not have to worry about having to ``ALLOCATE`` or ``DEALLOCATE`` your array. It also helps the compiler to optimise the code.

* Use an array ``POINTER`` when you are passing an array argument to a ``SUBROUTINE``, and the ``SUBROUTINE`` has to alter the ``SIZE`` / ``DIMENSION`` of the array. You should also use an array ``POINTER`` when you need a dynamic array in a component of a derived data type.

  .. note::
     Fortran 2003 allows passing ``ALLOCATABLE`` arrays as arguments as well as using ``ALLOCATABLE`` arrays as components of a derived data type. Therefore, the need for using an array ``POINTER`` should be reduced once Fortran 2003 becomes more widely accepted.

* Where possible, an ``ALLOCATE`` statement for an ``ALLOCATABLE`` array (or a ``POINTER`` used as a dynamic array) should be coupled with a ``DEALLOCATE`` within the same scope. If an ``ALLOCATABLE`` array is a ``PUBLIC`` ``MODULE`` variable, it is highly desirable if its memory allocation and deallocation are only performed in procedures within the ``MODULE`` in which it is declared. You may consider writing specific ``SUBROUTINES`` within the ``MODULE`` to handle these memory managements.

* To avoid memory fragmentation, it is desirable to ``DEALLOCATE`` in reverse order of ``ALLOCATE``.

  Common practice
      .. code-block:: fortran
      
         ALLOCATE(a(n))
         ALLOCATE(b(n))
         ALLOCATE(c(n))

         ! ... do something ...

         DEALLOCATE(a)
         DEALLOCATE(b)
         DEALLOCATE(c)

  Better approach
      .. code-block:: fortran

         ALLOCATE(a(n))
         ALLOCATE(b(n))
         ALLOCATE(c(n))

         ! ... do something ...

         DEALLOCATE(c)
         DEALLOCATE(b)
         DEALLOCATE(a)

* Always define a ``POINTER`` before using it. You can define a ``POINTER`` in its declaration by pointing it to the intrinsic function ``NULL()``. Alternatively, you can make sure that your ``POINTER`` is defined or nullified early on in the program unit. Similarly, ``NULLIFY`` a ``POINTER`` when it is no longer in use, either by using the ``NULLIFY`` statement or by pointing your ``POINTER`` to ``NULL()``.

* Avoid the ``DIMENSION`` attribute or statement. Declare the ``DIMENSION`` with the declared variables. E.g.:

  Common practice
      .. code-block:: fortran

         INTEGER, DIMENSION(10) :: array1
         INTEGER                :: array2
         DIMENSION              :: array2(20)

  Better approach
      .. code-block:: fortran

         INTEGER :: array1(10), array2(20)

* Avoid ``COMMON`` blocks and ``BLOCK DATA`` program units. Instead, use a ``MODULE`` with ``PUBLIC`` variables.

* Avoid the ``EQUIVALENCE`` statement. Use a ``POINTER`` or a derived data type, and the ``TRANSFER`` intrinsic function to convert between types.

* Avoid the ``PAUSE`` statement, as your program will hang in a batch environment. If you need to halt your program for interactive use, consider using a ``READ*`` statement instead.

* Avoid the ``ENTRY`` statement. Use a ``MODULE`` or internal ``SUBROUTINE``.

* Avoid the ``GOTO`` statement. The only commonly acceptable usage of ``GOTO`` is for error trapping. In such case, the jump should be to a commented ``9999 CONTINUE`` statement near the end of the program unit. Typically, you will only find error handlers beyond the ``9999 CONTINUE`` statement.

* Never use a ``GOTO`` to jump upwards in the code.

* Any ``GOTO`` must be commented to explain why it is there and what it is doing.

* Avoid assigned ``GOTO``, computed ``GOTO``, arithmetic ``IF``, etc. Use the appropriate modern constructs such as ``IF``, ``WHERE``, ``SELECT CASE``, etc..

* Avoid numbered statement labels. ``DO ... label CONTINUE`` constructs should be replaced by ``DO ... END DO`` constructs. Every ``DO`` loop must be terminated with a corresponding ``END DO``.

* Never use a ``FORMAT`` statement - they require the use of labels, and obscure the meaning of the I/O statement. The formatting information can be placed explicitly within the ``READ``, ``WRITE`` or ``PRINT`` statement, or be assigned to a ``CHARACTER`` variable in a ``PARAMETER`` statement in the header of the routine for later use in I/O statements. Never place output text within the format specifier, i.e. only format information may be placed within the ``FMT=`` part of an I/O statement. All variables and literals, including any character literals, must be ‘arguments’ of the I/O routine itself. This improves readability by clearly separating what is to be read/written from how to read/write it.

* Avoid the ``FORALL`` statement/construct. Despite what it is supposed to do, ``FORALL`` is often difficult for compilers to optimise (see, for example, `Implementing the Standards including Fortran 2003 <http://www.fortran.bcs.org/2007/jubilee/f50.pdf>`_ by NAG). Stick to the equivalent ``DO`` construct, ``WHERE`` statement/construct or array assignments unless there are actual performance benefits from using ``FORALL``.

* A ``FUNCTION`` should be PURE, i.e. it should have no side effects (e.g. altering an argument or module variable, or performing I/O). If you need to perform a task with side effects, you should use a ``SUBROUTINE`` instead.

* Declare the ``INTENT`` of all arguments to a subroutine or function. This allows checks against unintended access of variables to be done at compile time. The above point requiring functions to be pure means that all arguments of a ``FUNCTION`` should be declared as ``INTENT(IN)``.

* Avoid ``RECURSIVE`` procedures if possible. ``RECURSIVE`` procedures are usually difficult to understand, and are always difficult to optimise in a supercomputer environment.

* Avoid using the specific names of intrinsic procedures. Use the generic names of intrinsic procedures where possible.

* Use the ``ONLY`` clause in a ``USE <module>`` statement to declare all imported symbols (i.e. parameters, variables, functions, subroutines, etc). This makes it easier to locate the source of each symbol, and avoids unintentional access to other ``PUBLIC`` symbols within the ``MODULE``.

* Function or subroutine arguments should be declared separately from local variables.

* The standard delimiter for namelists is ``\``. In particular, note that ``&END`` is non-standard and should be avoided.

* The use of operator overloading is discouraged, as it can lead to confusion. The only acceptable use is to allow the standard operators (``+``, ``-`` etc.) to work with derived data types, where this makes sense.

* Avoid using archaic Fortran 77 features and features deprecated in Fortran 90.
