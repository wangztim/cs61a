
; Tail recursion

(define (replicate x n)
  (if (= n 0)
    (if (list? x)
      x
      nil
    )
    (if (list? x)
      (replicate  (append `(,(car x)) x) (- n 1))
      (replicate (list x) (- n 1))
    )
  )
)

(define (accumulate combiner start n term)
  (if (= n 0)
    start
    (begin
      (define termed (term n))
      (accumulate combiner (combiner start termed) (- n 1) term)
    ) 
  )
)

(define (accumulate-tail combiner start n term)
  (if (= n 0)
    start
    (begin
      (define termed (term n))
      (accumulate combiner (combiner start termed) (- n 1) term)
    ) 
  )
)

; Streams

(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
  (begin
    (define (naturals n)
      (cons-stream n (naturals (+ 3 n)))
    )
    (naturals 3)
  )
)

(define (make-list s)
      (begin
        (cond
        ((null? (cdr-stream s)) (list (car s)))
        ((>= (car (cdr-stream s)) (car s)) (cons (car s) (make-list (cdr-stream s))))
        (else (list (car s)))
      )
      )
)

(define (search-for-decrease s)
    (cond
        ((null? (cdr-stream s)) nil)
        ((< (car (cdr-stream s)) (car s)) (cdr-stream s))
        (else (search-for-decrease (cdr-stream s)))
    )
)

(define (nondecreastream s)
  (begin
    (define curr (car s))
    (define next (cdr-stream s))
    (if (null? (search-for-decrease s))
      (cons-stream (make-list s) nil)
      (cons-stream (make-list s) (nondecreastream (search-for-decrease s)))
    )
  )
)



(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))