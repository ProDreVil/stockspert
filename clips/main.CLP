;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Stock Market Investment Expert System
;; Intelligent Systems - CLIPS
;; Inference: Forward Chaining
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

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
;; RULES
;; ==========================================

;; ----- Buy -----

(defrule buy-stock
   (stock
      (trend uptrend)
      (pe low)
      (revenue positive)
      (earnings positive))
   =>
   (assert (recommendation (action buy)))
   (printout t crlf
      "==================================" crlf
      " RECOMMENDATION: BUY" crlf
      "----------------------------------" crlf
      "Reason:" crlf
      "- Stock is in an Uptrend" crlf
      "- Low P/E Ratio (Undervalued)" crlf
      "- Positive Revenue Growth" crlf
      "- Positive Earnings Growth" crlf
      "==================================" crlf))

(defrule buy-stock-fair-pe
   (stock
      (trend uptrend)
      (pe fair)
      (revenue positive)
      (earnings positive))
   =>
   (assert (recommendation (action buy)))
   (printout t crlf
      "==================================" crlf
      " RECOMMENDATION: BUY" crlf
      "----------------------------------" crlf
      "Reason:" crlf
      "- Stock is in an Uptrend" crlf
      "- Fair P/E Ratio" crlf
      "- Positive Revenue Growth" crlf
      "- Positive Earnings Growth" crlf
      "==================================" crlf))

(defrule buy-stock-high-volume
   (stock
      (trend uptrend)
      (pe low)
      (revenue positive)
      (earnings positive)
      (volume high))
   =>
   (assert (recommendation (action buy)))
   (printout t crlf
      "==================================" crlf
      " RECOMMENDATION: BUY" crlf
      "----------------------------------" crlf
      "Reason:" crlf
      "- Uptrend is supported by High Trading Volume" crlf
      "- Strong investor interest confirms the trend" crlf
      "==================================" crlf))

;; ----- Hold -----

(defrule hold-stock
   (stock
      (trend sideways)
      (earnings positive))
   =>
   (assert (recommendation (action hold)))
   (printout t crlf
      "==================================" crlf
      " RECOMMENDATION: HOLD" crlf
      "----------------------------------" crlf
      "Reason:" crlf
      "- Market is moving sideways" crlf
      "- Company still has positive earnings" crlf
      "- Wait for stronger confirmation" crlf
      "==================================" crlf))

(defrule hold-stock-neutral-revenue
   (stock
      (trend uptrend)
      (pe low)
      (revenue neutral)
      (earnings positive))
   =>
   (assert (recommendation (action hold)))
   (printout t crlf
      "==================================" crlf
      " RECOMMENDATION: HOLD" crlf
      "----------------------------------" crlf
      "Reason:" crlf
      "- Stock is in an Uptrend" crlf
      "- Low P/E Ratio" crlf
      "- Revenue Growth is Neutral" crlf
      "- Earnings Growth is Positive" crlf
      "==================================" crlf))

(defrule hold-stock-fair-neutral
   (stock
      (trend uptrend)
      (pe fair)
      (revenue neutral)
      (earnings positive))
   =>
   (assert (recommendation (action hold)))
   (printout t crlf
      "==================================" crlf
      " RECOMMENDATION: HOLD" crlf
      "----------------------------------" crlf
      "Reason:" crlf
      "- Stock is in an Uptrend" crlf
      "- Fair P/E Ratio" crlf
      "- Revenue Growth is Neutral" crlf
      "- Positive Earnings Growth" crlf
      "==================================" crlf))

(defrule hold-stock-downtrend
   (stock
      (trend downtrend)
      (revenue neutral)
      (earnings positive))
   =>
   (assert (recommendation (action hold)))
   (printout t crlf
      "==================================" crlf
      " RECOMMENDATION: HOLD" crlf
      "----------------------------------" crlf
      "Reason:" crlf
      "- Market is in a Downtrend" crlf
      "- Revenue Growth is Neutral" crlf
      "- Earnings remain Positive" crlf
      "- Wait for further confirmation" crlf
      "==================================" crlf))

(defrule hold-stock-downtrend-positive
   (stock
      (trend downtrend)
      (revenue positive)
      (earnings positive))
   =>
   (assert (recommendation (action hold)))
   (printout t crlf
      "==================================" crlf
      " RECOMMENDATION: HOLD" crlf
      "----------------------------------" crlf
      "Reason:" crlf
      "- Market is in a Downtrend" crlf
      "- Revenue and Earnings remain Positive" crlf
      "- Company fundamentals are still strong" crlf
      "==================================" crlf))

(defrule hold-stock-downtrend-mixed
   (stock
      (trend downtrend)
      (revenue positive)
      (earnings negative))
   =>
   (assert (recommendation (action hold)))
   (printout t crlf
      "==================================" crlf
      " RECOMMENDATION: HOLD" crlf
      "----------------------------------" crlf
      "Reason:" crlf
      "- Revenue remains Positive" crlf
      "- Earnings are Negative" crlf
      "- Indicators are mixed; monitor closely" crlf
      "==================================" crlf))

(defrule hold-stock-low-volume
   (stock
      (trend uptrend)
      (pe low)
      (revenue positive)
      (earnings positive)
      (volume low))
   =>
   (assert (recommendation (action hold)))
   (printout t crlf
      "==================================" crlf
      " RECOMMENDATION: HOLD" crlf
      "----------------------------------" crlf
      "Reason:" crlf
      "- Fundamentals are strong" crlf
      "- Low Trading Volume weakens confidence" crlf
      "- Wait for stronger market participation" crlf
      "==================================" crlf))

;; ----- Sell -----

(defrule sell-stock
   (stock
      (trend downtrend)
      (revenue negative)
      (earnings negative))
   =>
   (assert (recommendation (action sell)))
   (printout t crlf
      "==================================" crlf
      " RECOMMENDATION: SELL" crlf
      "----------------------------------" crlf
      "Reason:" crlf
      "- Stock is in a Downtrend" crlf
      "- Negative Revenue Growth" crlf
      "- Negative Earnings Growth" crlf
      "==================================" crlf))

(defrule sell-stock-sideways
   (stock
      (trend sideways)
      (earnings negative))
   =>
   (assert (recommendation (action sell)))
   (printout t crlf
      "==================================" crlf
      " RECOMMENDATION: SELL" crlf
      "----------------------------------" crlf
      "Reason:" crlf
      "- Stock is moving sideways" crlf
      "- Earnings Growth is Negative" crlf
      "- Company performance is weakening" crlf
      "==================================" crlf))

(defrule sell-stock-overvalued
   (stock
      (trend downtrend)
      (pe high)
      (revenue negative)
      (earnings positive))
   =>
   (assert (recommendation (action sell)))
   (printout t crlf
      "==================================" crlf
      " RECOMMENDATION: SELL" crlf
      "----------------------------------" crlf
      "Reason:" crlf
      "- Stock is in a Downtrend" crlf
      "- High P/E Ratio" crlf
      "- Negative Revenue Growth" crlf
      "- Stock appears overvalued" crlf
      "==================================" crlf))

(defrule sell-stock-downtrend-neutral
   (stock
      (trend downtrend)
      (revenue neutral)
      (earnings negative))
   =>
   (assert (recommendation (action sell)))
   (printout t crlf
      "==================================" crlf
      " RECOMMENDATION: SELL" crlf
      "----------------------------------" crlf
      "Reason:" crlf
      "- Market is in a Downtrend" crlf
      "- Earnings Growth is Negative" crlf
      "- Financial performance is weakening" crlf
      "==================================" crlf))

;; ----- N/A -----

(defrule no-clear-recommendation
   (stock)
   (not (recommendation))
   =>
   (printout t crlf
      "==================================" crlf
      " NO CLEAR RECOMMENDATION" crlf
      "----------------------------------" crlf
      "Reason:" crlf
      "- The current indicators do not" crlf
      "  strongly support BUY, HOLD, or SELL." crlf
      "- More information or confirmation" crlf
      "  is recommended." crlf
      "==================================" crlf))

;; ==========================================
;; USER INPUT FUNCTION
;; ==========================================

(deffunction start ()

   (printout t crlf
      "==================================" crlf
      " STOCK MARKET EXPERT SYSTEM" crlf
      "==================================" crlf crlf)

   (printout t "Stock Trend (uptrend/sideways/downtrend): ")
   (bind ?trend (read))

   (printout t "P/E Ratio (low/fair/high): ")
   (bind ?pe (read))

   (printout t "Revenue Growth (positive/neutral/negative): ")
   (bind ?revenue (read))

   (printout t "Earnings Growth (positive/negative): ")
   (bind ?earnings (read))

   (printout t "Trading Volume (low/average/high): ")
   (bind ?volume (read))

   (assert
      (stock
         (trend ?trend)
         (pe ?pe)
         (revenue ?revenue)
         (earnings ?earnings)
         (volume ?volume)))
   (run))