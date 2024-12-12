query-table:: false
#+BEGIN_QUERY 
{:title "Broken References"
:query [:find (pull ?b [*])
		:where
		[?b :block/refs ?t]
		[(missing? $ ?t :block/name)]
		[(missing? $ ?t :block/content)]]
}
#+END_QUERY
