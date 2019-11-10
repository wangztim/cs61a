; Macros

(define-macro (list-of map-expr for var in lst if filter-expr)
  (begin
    (define func `(lambda (,var) (if ,filter-expr
    ,map-expr 
    `null
    )))
    (define john-denero `(map ,func ,lst))
    `(filter (lambda (x) (not (eq? x `null))) ,john-denero)
   )
)