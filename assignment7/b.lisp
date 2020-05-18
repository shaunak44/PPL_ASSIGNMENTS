(defun factorial_with_recursion( n )
  (if (= n 0)
    	1
	(* n (factorial_with_recursion(- n 1)))))
(defun factorial_without_recursion(n) 
  (loop for i from 1 to n
	with a = 1
	do(setf a (* a i))
	finally (return a)))

(defvar fac (read) )

(format t "Factorial of ~D (using recursion) = ~D~%" fac (factorial_with_recursion fac))
(format t "Factorial of ~D (without using recursion) = ~D~%" fac (factorial_without_recursion fac))

