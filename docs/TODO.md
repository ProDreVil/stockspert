# Stockspert TODO

## 1. Core Expert System

* [x] Set up `main.py`
* [ ] Connect GUI to CLIPS
* [ ] Connect GUI market inputs to CLIPS facts
* [ ] Make existing CLIPS rules work with the GUI
* [ ] Fix rule overlap / recommendation priority
* [ ] Add portfolio facts to CLIPS

  * [ ] Available Cash
  * [ ] Shares Owned
* [ ] Add portfolio-aware rules

  * [ ] Insufficient cash → HOLD
  * [ ] No shares to sell → HOLD
* [ ] Add fallback / no-clear-recommendation handling

---

## 2. GUI

### Market Information

* [x] Stock Price input
* [x] Trend dropdown
* [x] P/E Ratio dropdown
* [x] Revenue Growth dropdown
* [x] Earnings Growth dropdown
* [x] Trading Volume dropdown
* [ ] Price Change display
* [ ] Last Updated display
* [x] Apply Market Changes button

### Simulation Status

* [x] Current simulated date
* [x] Time amount input
* [x] Time unit dropdown
* [x] NEXT button
* [x] RANDOM button
* [x] Stack NEXT and RANDOM vertically
* [x] Center NEXT and RANDOM buttons

### Portfolio

* [x] Portfolio section/layout
* [ ] Available Cash display
* [ ] Shares Owned display
* [ ] Portfolio Value display
* [ ] Buy quantity input
* [ ] BUY button
* [ ] Sell quantity input
* [ ] SELL button

### Price History

* [x] Price history graph
* [x] Make graph fit the larger layout
* [ ] Update graph when simulation advances

### Expert System Analysis

* [x] Expert System Analysis section
* [ ] Recommendation display
* [ ] Confidence display
* [ ] Rule Fired display
* [ ] Reason / explanation display
* [ ] BUY / HOLD / SELL visual indication

---

## 3. Portfolio Simulation

* [ ] Set starting cash to `$10,000`
* [ ] Set starting shares to `0`
* [ ] Implement buying

  * [ ] Calculate `Stock Price × Quantity`
  * [ ] Check available cash
  * [ ] Deduct cash after successful purchase
  * [ ] Add purchased shares
* [ ] Implement selling

  * [ ] Check shares owned
  * [ ] Add sale proceeds to cash
  * [ ] Remove sold shares
* [ ] Calculate portfolio value

```text
Portfolio Value =
Available Cash + (Shares Owned × Stock Price)
```

* [ ] Calculate price change in Python
* [ ] Update portfolio value when stock price changes
* [ ] Make transactions affect the expert system's portfolio facts

---

## 4. Market Simulation

* [x] Start simulation at January 1, 2026
* [ ] Implement Days
* [ ] Implement Weeks
* [ ] Implement Months
* [ ] Implement Years
* [ ] Advance simulated date with NEXT
* [ ] Update stock price
* [ ] Update price history
* [ ] Run CLIPS after simulation advances
* [ ] Update portfolio value
* [ ] Implement RANDOM
* [ ] Make random market scenarios reasonably coherent

---

## 5. Testing

### Expert System

* [ ] Test BUY recommendation
* [ ] Test HOLD recommendation
* [ ] Test SELL recommendation
* [ ] Test no matching rule
* [ ] Test rule priority / overlapping rules
* [ ] Test confidence calculation

### Portfolio

* [ ] Test buying 1 share
* [ ] Test buying multiple shares
* [ ] Test insufficient cash
* [ ] Test selling 1 share
* [ ] Test selling multiple shares
* [ ] Test selling with 0 shares
* [ ] Test selling more shares than owned

### Simulation

* [ ] Test day advancement
* [ ] Test week advancement
* [ ] Test month advancement
* [ ] Test year advancement
* [ ] Test stock price changes
* [ ] Test price change calculation
* [ ] Test graph updates
* [ ] Test portfolio value updates
* [ ] Test RANDOM

---

## 6. Final Polish

* [ ] Check GUI layout
* [ ] Check dark theme
* [ ] Check button states
* [ ] Check input validation
* [ ] Check error messages
* [ ] Check recommendation explanations
* [ ] Remove unnecessary code/files
* [ ] Test complete user flow
* [ ] Update README
* [ ] Final demo test

---

## Current Priority

> Work from top to bottom. Don't polish until the core system works.

* [ ] **Priority 1:** Connect GUI → CLIPS
* [ ] **Priority 2:** Make recommendations work correctly
* [ ] **Priority 3:** Integrate portfolio rules
* [ ] **Priority 4:** Finish buy/sell simulation
* [ ] **Priority 5:** Finish market simulation
* [ ] **Priority 6:** Test everything
* [ ] **Priority 7:** Polish and document