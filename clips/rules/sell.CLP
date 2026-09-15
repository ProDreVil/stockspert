(defrule sell-stock

   (stock
      (trend downtrend)
      (revenue negative)
      (earnings negative))

   (not (recommendation))

   =>

   (assert
      (recommendation
         (action sell)
         (rule "SELL-DOWNTREND-NEGATIVE-FUNDAMENTALS"))))


(defrule sell-stock-sideways

   (stock
      (trend sideways)
      (earnings negative))

   (not (recommendation))

   =>

   (assert
      (recommendation
         (action sell)
         (rule "SELL-SIDEWAYS-NEGATIVE-EARNINGS"))))


(defrule sell-stock-overvalued

   (stock
      (trend downtrend)
      (pe high)
      (revenue negative)
      (earnings positive))

   (not (recommendation))

   =>

   (assert
      (recommendation
         (action sell)
         (rule "SELL-DOWNTREND-HIGH-PE"))))


(defrule sell-stock-downtrend-neutral

   (stock
      (trend downtrend)
      (revenue neutral)
      (earnings negative))

   (not (recommendation))

   =>

   (assert
      (recommendation
         (action sell)
         (rule "SELL-DOWNTREND-NEGATIVE-EARNINGS"))))