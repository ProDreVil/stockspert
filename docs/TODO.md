# Stockspert TODO

## 1. Core Expert System

* [x] Set up `main.py`
* [x] Connect GUI to CLIPS
* [x] Connect GUI market inputs to CLIPS facts
* [x] Make existing CLIPS rules work with the GUI
* [x] Fix rule overlap / recommendation priority
* [ ] Add portfolio facts to CLIPS

  * [ ] Available Cash
  * [ ] Shares Owned
* [ ] Add portfolio-aware rules

  * [ ] Insufficient cash → HOLD
  * [ ] No shares to sell → HOLD
* [x] Add fallback / no-clear-recommendation handling

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
* [x] Recommendation display
* [x] Confidence display
* [x] Rule Fired display
* [x] Reason / explanation display
* [x] BUY / HOLD / SELL visual indication
* [x] Color-code reasons by meaning

### GUI Polish

* [x] Use config colors in portfolio
* [x] Use config colors in simulation
* [x] Use config colors in remaining GUI files
* [x] Stabilize analysis layout for varying text lengths

---

## 3. Portfolio Simulation

* [ ] Starting cash: $10,000
* [ ] Track shares owned
* [ ] Track invested amount
* [ ] Calculate portfolio value
* [ ] Calculate profit / loss
* [ ] Calculate return percentage
* [ ] Buy stocks
* [ ] Sell stocks
* [ ] Prevent buying without sufficient cash
* [ ] Prevent selling without sufficient shares

---

## 4. Stock Simulation

* [x] Generate simulated stock prices
* [ ] Advance simulation by selected time
* [ ] Randomize market conditions
* [ ] Update price history
* [ ] Update market indicators
* [ ] Update simulated date

---

## 5. Testing

### Expert System

* [ ] Test BUY recommendation
* [ ] Test HOLD recommendation
* [ ] Test SELL recommendation
* [ ] Test no matching rule
* [ ] Test rule priority / overlapping rules

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
* [ ] Test graph updates
* [ ] Test portfolio value updates
* [ ] Test Random Market

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

> Get the simulator working before adding more polish.

* [x] **Priority 1:** Connect GUI → CLIPS
* [x] **Priority 2:** Make recommendations work correctly
* [x] **Priority 3:** Finish graph + confidence
* [ ] **Priority 4:** Integrate portfolio rules
* [ ] **Priority 5:** Finish day-based market simulation
* [ ] **Priority 6:** Add longer time units + Random Market
* [ ] **Priority 7:** Test everything
* [ ] **Priority 8:** Polish and document