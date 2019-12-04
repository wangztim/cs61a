; Lab 14: Final Review

(define (compose-all funcs)
  (begin
    (define (composer x)
      (begin
        (define (applier y func-list)
          (if (null? func-list)
            y
            (applier ((car func-list) y) (cdr func-list))
          )
        )
        (applier x funcs)
      )
    )
    composer
  )
)

(define (has-cycle? s)
  (define (pair-tracker seen-so-far curr)
    (cond
          (null? curr) #f
          (eq? s curr) #t
          (else (pair-tracker `() (cdr-stream curr)))
    )
  )
  (pair-tracker `() s)
)

(define (contains? lst s)
  (cond
    (null? lst) #f
    (eq? (car lst) s) #t
    (else (contains (cdr lst) s))
  )
)

