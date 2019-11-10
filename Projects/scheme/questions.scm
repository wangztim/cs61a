(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests)
  (define (add-to-front rest)
    (cons first rest)
  )
  (map add-to-front rests)
)

(define (zip pairs)
  (if (null? pairs)
      `(() ())
      (begin
        (define pair (car pairs))
        (define front (list (car pair)))
        (define back (list (car (cdr pair))))
        (define recurse (zip (cdr pairs)))
        (define rfront (car recurse))
        (define rback (car (cdr recurse)))
        (list (append front rfront) (append back rback))
      )
  )
)
;; Problem 16
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 16
  (define (helper idx s)
    (if (null? s)
      `()
      (cons (list idx (car s)) (helper (+ 1 idx) (cdr s)))
    )
  )

  (helper 0 s)
)
  ; END PROBLEM 16

;; Problem 17
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN PROBLEM 17
  (cond
    ((<= total 0) `(()))
    ((= (length denoms) 0) `())
    (else
      (begin
        (define denom (car denoms))
        (if (< total denom)
          (list-change total (cdr denoms))
          (begin
            (define change `())
            (cond ((= total denom) (
              define change (append change (list (list total)))
            )))
            (append
              (cons-all
                (car denoms)
                (list-change (- total (car denoms)) denoms)
              )
              (list-change total (cdr denoms))
            )
          )
        )
      )
    )
  )
)
  ; END PROBLEM 17

;; Problem 18
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))
;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 18
         expr
         ; END PROBLEM 18
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 18
         (define quote `quote)
         (cons quote (let-to-lambda (cdr expr)))
         ; END PROBLEM 18
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
          ; BEGIN PROBLM 18
              (define mapped-body (map (lambda (x) (let-to-lambda x)) body))
              (define func `(,form ,params))
              (append func mapped-body)
           ; END PROBLEM 18
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
            (define zipped (zip values))
            (define args (car zipped))
            (define params (cadr zipped))
            (define mapped-params (map (lambda (x) (let-to-lambda x)) params))
            (define mapped-body (map (lambda (x) (let-to-lambda x)) body))
            (define func `(lambda ,args ,(car mapped-body)))
            (cons func mapped-params)
           ; END PROBLEM 18
           ))
        (else
         ; BEGIN PROBLEM 18
         (define operator (car expr))
         (define body (cdr expr))
         (define mapped-body (map (lambda (x) (let-to-lambda x)) body))
         (cons operator mapped-body)
         ; END PROBLEM 18
         )))

(let-to-lambda '(let ((a (let ((a 2)) a))
             (b 2))
             (+ a b)))