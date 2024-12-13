query-table:: false
#+BEGIN_QUERY 
{:title "Broken References"
:query [:find (pull ?b [*])
       :in $ ?matcher
       :where
       [(re-pattern ?matcher) ?regex]
       [?b :block/content ?c]
       [(re-find ?regex ?c)]
       [?b :block/refs ?br]
       [(missing? $ ?br :block/content)]
       [(missing? $ ?br :block/name)]
]
:inputs [ "\\([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\\)"]
:table-view? false
}
#+END_QUERY
