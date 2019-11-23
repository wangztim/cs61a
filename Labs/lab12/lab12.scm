(define (partial-sums stream)

  (define (helper cum_sum s)
    (if (null? s)
      nil
      (begin
        (define a (+ (car s) cum_sum))
        (cons-stream a (helper a (cdr-stream s)))
      )
    )
  )

  (helper 0 stream)
)