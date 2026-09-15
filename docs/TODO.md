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
* [x] Recommendation display
* [ ] Confidence display
* [x] Rule Fired display
* [x] Reason / explanation display
* [x] BUY / HOLD / SELL visual indication
* [x] Color-code reasons by meaning

### GUI Polish

* [x] Use config colors in portfolio
* [x] Use config colors in simulation
* [ ] Use config colors in remaining GUI files
* [ ] Stabilize analysis layout for varying text lengths

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

* [ ] Generate simulated stock prices
* [ ] Advance simulation by selected time
* [ ] Randomize market conditions
* [ ] Update price history
* [ ] Update market indicators
* [ ] Update simulated date

---

## Tomorrow's Plan

### During the day — Graph + Confidence

**Priority 1: Finish the price history graph**

* Make the graph properly display simulated prices
* Connect it to the existing price history
* Make sure it fits the current larger layout
* Prepare it to update when the simulation advances

**Priority 2: Implement confidence**

* Decide how confidence is calculated from the fired rule
* Replace the current placeholder `69%`
* Display the calculated confidence in Expert System Analysis

### At night — Simulation

**Priority 3: Simulate passing days**

* Implement simulated date advancement
* Implement Days first
* Update stock price when time advances
* Update price history
* Update market conditions
* Re-run CLIPS after each simulation step
* Update the GUI analysis

**Then, if time allows:**

* Weeks
* Months
* Years
* Random Market

---

## Current Priority

> Get the simulator working before adding more polish.

* [x] **Priority 1:** Connect GUI → CLIPS
* [x] **Priority 2:** Make recommendations work correctly
* [ ] **Priority 3:** Finish graph + confidence
* [ ] **Priority 4:** Integrate portfolio rules
* [ ] **Priority 5:** Finish day-based market simulation
* [ ] **Priority 6:** Add longer time units + Random Market
* [ ] **Priority 7:** Test everything
* [ ] **Priority 8:** Polish and document