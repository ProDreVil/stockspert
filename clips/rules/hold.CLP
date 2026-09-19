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


(defrule hold-stock-high-pe

   (stock
      (trend uptrend)
      (pe high)
      (earnings positive))

   (not (recommendation))

   =>

   (assert
      (recommendation
         (action hold)
         (rule "HOLD-UPTREND-HIGH-PE"))))


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


(defrule hold-stock-uptrend-low-pe-negative-earnings
   (stock
      (trend uptrend)
      (pe low)
      (earnings negative))
   (not (recommendation))
   =>
   (assert
      (recommendation
         (action hold)
         (rule "HOLD-UPTREND-LOW-PE-NEGATIVE-EARNINGS"))))


(defrule hold-stock-uptrend-low-pe-negative-revenue
   (stock
      (trend uptrend)
      (pe low)
      (revenue negative))
   (not (recommendation))
   =>
   (assert
      (recommendation
         (action hold)
         (rule "HOLD-UPTREND-LOW-PE-NEGATIVE-REVENUE"))))


(defrule hold-uptrend-fair-pe-negative-revenue
   (stock
      (trend uptrend)
      (pe fair)
      (revenue negative)
      (earnings positive))
   (not (recommendation))
   =>
   (assert
      (recommendation
         (action hold)
         (rule "HOLD-UPTREND-FAIR-PE-NEGATIVE-REVENUE"))))


(defrule hold-stock-downtrend-negative-revenue
   (stock
      (trend downtrend)
      (revenue negative)
      (earnings positive))
   (not (recommendation))
   =>
   (assert
      (recommendation
         (action hold)
         (rule "HOLD-DOWNTREND-NEGATIVE-REVENUE"))))


(defrule hold-uptrend-fair-pe-negative-earnings
   (stock
      (trend uptrend)
      (pe fair)
      (earnings negative))
   (not (recommendation))
   =>
   (assert
      (recommendation
         (action hold)
         (rule "HOLD-UPTREND-FAIR-PE-NEGATIVE-EARNINGS"))))


(defrule hold-uptrend-high-pe-negative-earnings
   (stock
      (trend uptrend)
      (pe high)
      (earnings negative))
   (not (recommendation))
   =>
   (assert
      (recommendation
         (action hold)
         (rule "HOLD-UPTREND-HIGH-PE-NEGATIVE-EARNINGS"))))


(defrule hold-stock-sideways-negative-earnings
   (stock
      (trend sideways)
      (earnings negative))
   (not (recommendation))
   =>
   (assert
      (recommendation
         (action hold)
         (rule "HOLD-SIDEWAYS-NEGATIVE-EARNINGS"))))