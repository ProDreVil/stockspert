(defrule no-clear-recommendation

   (stock)

   (not (recommendation))

   =>

   (printout t crlf
      "RECOMMENDATION: N/A" crlf
      "RULE: NO-CLEAR-RECOMMENDATION" crlf
      "END RESULT" crlf))