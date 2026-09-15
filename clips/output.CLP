(deffunction print-recommendation (?action ?rule)

   (printout t crlf
      "RECOMMENDATION: " ?action crlf
      "RULE: " ?rule crlf))


(defrule output-recommendation

   ?r <- (recommendation
      (action ?action)
      (rule ?rule))

   =>

   (print-recommendation ?action ?rule))