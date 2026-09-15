(defrule hold-stock

   (stock
      (trend sideways)
      (earnings positive))

   (not (recommendation))

   =>

   (assert
      (recommendation
         (action hold)
         (rule "HOLD-SIDEWAYS-POSITIVE-EARNINGS"))))


(defrule hold-stock-neutral-revenue

   (stock
      (trend uptrend)
      (pe low)
      (revenue neutral)
      (earnings positive))

   (not (recommendation))

   =>

   (assert
      (recommendation
         (action hold)
         (rule "HOLD-UPTREND-LOW-PE-NEUTRAL-REVENUE"))))


(defrule hold-stock-fair-neutral

   (stock
      (trend uptrend)
      (pe fair)
      (revenue neutral)
      (earnings positive))

   (not (recommendation))

   =>

   (assert
      (recommendation
         (action hold)
         (rule "HOLD-UPTREND-FAIR-PE-NEUTRAL-REVENUE"))))


(defrule hold-stock-downtrend

   (stock
      (trend downtrend)
      (revenue neutral)
      (earnings positive))

   (not (recommendation))

   =>

   (assert
      (recommendation
         (action hold)
         (rule "HOLD-DOWNTREND-NEUTRAL-REVENUE"))))


(defrule hold-stock-downtrend-positive

   (stock
      (trend downtrend)
      (revenue positive)
      (earnings positive))

   (not (recommendation))

   =>

   (assert
      (recommendation
         (action hold)
         (rule "HOLD-DOWNTREND-POSITIVE-FUNDAMENTALS"))))


(defrule hold-stock-downtrend-mixed

   (stock
      (trend downtrend)
      (revenue positive)
      (earnings negative))

   (not (recommendation))

   =>

   (assert
      (recommendation
         (action hold)
         (rule "HOLD-DOWNTREND-MIXED-FUNDAMENTALS"))))


(defrule hold-stock-low-volume

   (declare (salience 10))

   (stock
      (trend uptrend)
      (pe low)
      (revenue positive)
      (earnings positive)
      (volume low))

   (not (recommendation))

   =>

   (assert
      (recommendation
         (action hold)
         (rule "HOLD-UPTREND-LOW-VOLUME"))))