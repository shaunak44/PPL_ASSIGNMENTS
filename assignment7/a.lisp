(defparameter *n* '(2 4 6 5 7))

(defun lis(l f) 
    (format t "2nd Item in the List = ~a ~%" (nth (- f 1) l)) 
)

(lis *n* 2)