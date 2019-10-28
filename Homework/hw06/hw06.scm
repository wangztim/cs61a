;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car  (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

(define (sign x)
  (
    if (> x 0)
    1
    (if (= x 0)
      0
      -1)))

(define (square x) (* x x))

(define (pow b n)
  (
    if (= n 0)
      1
      (if (= n 1)
        b
        (if (even? n)
          (* (square b) (
            if (= (/ n 2) 1)
            1
            (pow b (/ n 2))
            ))
          (* (* b (square b))
          (if (= (floor (/ n 2)) 1)
            1
            (pow b (floor (/ n 2)))
          ))
        )
      )
  )
)

(define (unique s)
  (if
    (not(null? s))
      (begin
        (define first (car s))
        (define filtered (filter (lambda (x) (not (eq? x (car s)))) (cdr s)))
        (set! s (cons first (unique filtered)))
        s
      )
      s
  )
)