(defrule buy-stock

   (stock
      (trend uptrend)
      (pe low)
      (revenue positive)
      (earnings positive))

   (not (recommendation))

   =>

   (assert
      (recommendation
         (action buy)
         (rule "BUY-UPTREND-LOW-PE"))))


(defrule buy-stock-fair-pe

   (stock
      (trend uptrend)
      (pe fair)
      (revenue positive)
      (earnings positive))

   (not (recommendation))

   =>

   (assert
      (recommendation
         (action buy)
         (rule "BUY-UPTREND-FAIR-PE"))))


(defrule buy-stock-high-volume

   (declare (salience 10))

   (stock
      (trend uptrend)
      (pe low)
      (revenue positive)
      (earnings positive)
      (volume high))

   (not (recommendation))

   =>

   (assert
      (recommendation
         (action buy)
         (rule "BUY-UPTREND-HIGH-VOLUME"))))


(defrule buy-low-price-positive-earnings
   (declare (salience 20))
   (stock
      (price low)
      (earnings positive)
      (trend sideways|uptrend))
   (not (recommendation))
   =>
   (assert
      (recommendation
         (action buy)
         (rule "BUY-LOW-PRICE-POSITIVE-EARNINGS"))))