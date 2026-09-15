;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Stock Market Investment Expert System
;; Intelligent Systems - CLIPS
;; Inference: Forward Chaining
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; ==========================================
;; KNOWLEDGE BASE
;; ==========================================

(deftemplate stock
   (slot trend)
   (slot pe)
   (slot revenue)
   (slot earnings)
   (slot volume))

(deftemplate recommendation
   (slot action))


;; ==========================================
;; OUTPUT FUNCTION
;; ==========================================

(deffunction report-recommendation (?action ?rule $?reasons)

   (printout t crlf
      "RECOMMENDATION: " ?action crlf
      "RULE: " ?rule crlf)

   (foreach ?reason ?reasons
      (printout t "REASON: " ?reason crlf))

   (printout t "END RESULT" crlf))


;; ==========================================
;; BUY RULES
;; ==========================================

(defrule buy-stock

   (stock
      (trend uptrend)
      (pe low)
      (revenue positive)
      (earnings positive))

   (not (recommendation))

   =>

   (assert (recommendation (action buy)))

   (report-recommendation
      "BUY"
      "BUY-UPTREND-LOW-PE"
      "Uptrend"
      "Low P/E Ratio"
      "Positive Revenue Growth"
      "Positive Earnings Growth"))


(defrule buy-stock-fair-pe

   (stock
      (trend uptrend)
      (pe fair)
      (revenue positive)
      (earnings positive))

   (not (recommendation))

   =>

   (assert (recommendation (action buy)))

   (report-recommendation
      "BUY"
      "BUY-UPTREND-FAIR-PE"
      "Uptrend"
      "Fair P/E Ratio"
      "Positive Revenue Growth"
      "Positive Earnings Growth"))


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

   (assert (recommendation (action buy)))

   (report-recommendation
      "BUY"
      "BUY-UPTREND-HIGH-VOLUME"
      "Uptrend"
      "Low P/E Ratio"
      "Positive Revenue Growth"
      "Positive Earnings Growth"
      "High trading volume supports the upward trend"))


;; ==========================================
;; HOLD RULES
;; ==========================================

(defrule hold-stock

   (stock
      (trend sideways)
      (earnings positive))

   (not (recommendation))

   =>

   (assert (recommendation (action hold)))

   (report-recommendation
      "HOLD"
      "HOLD-SIDEWAYS-POSITIVE-EARNINGS"
      "Sideways market movement"
      "Positive Earnings Growth"
      "Wait for stronger market confirmation"))


(defrule hold-stock-neutral-revenue

   (stock
      (trend uptrend)
      (pe low)
      (revenue neutral)
      (earnings positive))

   (not (recommendation))

   =>

   (assert (recommendation (action hold)))

   (report-recommendation
      "HOLD"
      "HOLD-UPTREND-NEUTRAL-REVENUE"
      "Uptrend"
      "Low P/E Ratio"
      "Neutral Revenue Growth"
      "Positive Earnings Growth"))


(defrule hold-stock-fair-neutral

   (stock
      (trend uptrend)
      (pe fair)
      (revenue neutral)
      (earnings positive))

   (not (recommendation))

   =>

   (assert (recommendation (action hold)))

   (report-recommendation
      "HOLD"
      "HOLD-UPTREND-FAIR-PE-NEUTRAL-REVENUE"
      "Uptrend"
      "Fair P/E Ratio"
      "Neutral Revenue Growth"
      "Positive Earnings Growth"))


(defrule hold-stock-downtrend

   (stock
      (trend downtrend)
      (revenue neutral)
      (earnings positive))

   (not (recommendation))

   =>

   (assert (recommendation (action hold)))

   (report-recommendation
      "HOLD"
      "HOLD-DOWNTREND-NEUTRAL-REVENUE"
      "Downtrend"
      "Neutral Revenue Growth"
      "Positive Earnings Growth"
      "Wait for further confirmation"))


(defrule hold-stock-downtrend-positive

   (stock
      (trend downtrend)
      (revenue positive)
      (earnings positive))

   (not (recommendation))

   =>

   (assert (recommendation (action hold)))

   (report-recommendation
      "HOLD"
      "HOLD-DOWNTREND-POSITIVE-FUNDAMENTALS"
      "Downtrend"
      "Positive Revenue Growth"
      "Positive Earnings Growth"
      "Positive fundamentals provide support despite the downtrend"))


(defrule hold-stock-downtrend-mixed

   (stock
      (trend downtrend)
      (revenue positive)
      (earnings negative))

   (not (recommendation))

   =>

   (assert (recommendation (action hold)))

   (report-recommendation
      "HOLD"
      "HOLD-DOWNTREND-MIXED-FUNDAMENTALS"
      "Downtrend"
      "Positive Revenue Growth"
      "Negative Earnings Growth"
      "Mixed fundamentals require close monitoring"))


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

   (assert (recommendation (action hold)))

   (report-recommendation
      "HOLD"
      "HOLD-UPTREND-LOW-VOLUME"
      "Uptrend"
      "Low P/E Ratio"
      "Positive Revenue Growth"
      "Positive Earnings Growth"
      "Low trading volume reduces confirmation of the upward trend"))


;; ==========================================
;; SELL RULES
;; ==========================================

(defrule sell-stock

   (stock
      (trend downtrend)
      (revenue negative)
      (earnings negative))

   (not (recommendation))

   =>

   (assert (recommendation (action sell)))

   (report-recommendation
      "SELL"
      "SELL-DOWNTREND-NEGATIVE-FUNDAMENTALS"
      "Downtrend"
      "Negative Revenue Growth"
      "Negative Earnings Growth"))


(defrule sell-stock-sideways

   (stock
      (trend sideways)
      (earnings negative))

   (not (recommendation))

   =>

   (assert (recommendation (action sell)))

   (report-recommendation
      "SELL"
      "SELL-SIDEWAYS-NEGATIVE-EARNINGS"
      "Sideways market movement"
      "Negative Earnings Growth"
      "Negative earnings indicate weakening company performance"))


(defrule sell-stock-overvalued

   (stock
      (trend downtrend)
      (pe high)
      (revenue negative)
      (earnings positive))

   (not (recommendation))

   =>

   (assert (recommendation (action sell)))

   (report-recommendation
      "SELL"
      "SELL-DOWNTREND-HIGH-PE"
      "Downtrend"
      "High P/E Ratio"
      "Negative Revenue Growth"
      "Positive Earnings Growth"
      "High valuation combined with a weakening trend increases risk"))


(defrule sell-stock-downtrend-neutral

   (stock
      (trend downtrend)
      (revenue neutral)
      (earnings negative))

   (not (recommendation))

   =>

   (assert (recommendation (action sell)))

   (report-recommendation
      "SELL"
      "SELL-DOWNTREND-NEGATIVE-EARNINGS"
      "Downtrend"
      "Neutral Revenue Growth"
      "Negative Earnings Growth"
      "Negative earnings indicate weakening financial performance"))


;; ==========================================
;; NO CLEAR RECOMMENDATION
;; ==========================================

(defrule no-clear-recommendation

   (stock)

   (not (recommendation))

   =>

   (printout t crlf
      "RECOMMENDATION: N/A" crlf
      "RULE: NO-CLEAR-RECOMMENDATION" crlf
      "REASON: Current indicators do not strongly support BUY, HOLD, or SELL." crlf
      "REASON: Additional information or market confirmation is recommended." crlf
      "END RESULT" crlf))


;; ==========================================
;; USER INPUT FUNCTION
;; ==========================================

(deffunction start ()

   (printout t crlf
      "==================================" crlf
      " STOCK MARKET EXPERT SYSTEM" crlf
      "==================================" crlf crlf)

   (printout t
      "Stock Trend (uptrend/sideways/downtrend): ")

   (bind ?trend (read))

   (printout t
      "P/E Ratio (low/fair/high): ")

   (bind ?pe (read))

   (printout t
      "Revenue Growth (positive/neutral/negative): ")

   (bind ?revenue (read))

   (printout t
      "Earnings Growth (positive/negative): ")

   (bind ?earnings (read))

   (printout t
      "Trading Volume (low/average/high): ")

   (bind ?volume (read))

   (assert
      (stock
         (trend ?trend)
         (pe ?pe)
         (revenue ?revenue)
         (earnings ?earnings)
         (volume ?volume)))

   (run))