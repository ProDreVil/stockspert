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

* [x] Stock Price display
* [x] Trend dropdown
* [x] P/E Ratio dropdown
* [x] Revenue Growth dropdown
* [x] Earnings Growth dropdown
* [x] Trading Volume dropdown
* [ ] Price Change display
* [ ] Last Updated display
* [x] Automatic market input updates

### Simulation Status

* [x] Current simulated date
* [x] Day / Week / Month inputs
* [x] NEXT button
* [x] ADVANCE button
* [x] RANDOMIZE button
* [x] Direction controls
* [x] Add Cash controls

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
* [x] Update graph when simulation advances
* [x] Candle hover information

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
* [x] Read-only simulated stock price
* [x] Automatically update displayed stock price

---

## 3. Portfolio Simulation

* [ ] Starting cash: decide between `$100` and `$1,000`
* [ ] Track shares owned
* [ ] Track invested amount
* [ ] Calculate portfolio value
* [ ] Calculate profit / loss
* [ ] Calculate return percentage
* [ ] Buy stocks
* [ ] Sell stocks
* [ ] Prevent buying without sufficient cash
* [ ] Prevent selling without sufficient shares
* [ ] Connect portfolio state to GUI
* [ ] Connect portfolio state to CLIPS

---

## 4. Stock Simulation

* [x] Generate simulated stock prices
* [x] Advance simulation by selected time
* [ ] Make longer advances feel meaningfully different
* [ ] Randomize market conditions
* [x] Update price history
* [ ] Update market indicators
* [x] Update simulated date
* [ ] Make market indicators change coherently with price movement
* [ ] Add longer time units / year advancement

---

## 5. Testing

### Expert System

* [ ] Test BUY recommendation
* [ ] Test HOLD recommendation
* [ ] Test SELL recommendation
* [ ] Test no matching rule
* [ ] Test rule priority / overlapping rules
* [ ] Test Uptrend + High P/E rule
* [ ] Test automatic recommendation updates

### Portfolio

* [ ] Test buying 1 share
* [ ] Test buying multiple shares
* [ ] Test insufficient cash
* [ ] Test selling 1 share
* [ ] Test selling multiple shares
* [ ] Test selling with 0 shares
* [ ] Test selling more shares than owned
* [ ] Test portfolio value calculation

### Simulation

* [ ] Test day advancement
* [ ] Test week advancement
* [ ] Test month advancement
* [ ] Test year advancement
* [ ] Test stock price changes
* [x] Test graph updates
* [ ] Test market indicator updates
* [ ] Test portfolio value updates
* [ ] Test Random Market
* [ ] Test longer time advances

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
* [ ] **Priority 4:** Fix market simulation
* [ ] **Priority 5:** Integrate portfolio rules
* [ ] **Priority 6:** Finish buy/sell simulation
* [ ] **Priority 7:** Test everything
* [ ] **Priority 8:** Polish and document

### Next Session

1. **Decide starting money:** `$100` vs `$1,000`
2. **Fix market indicators not updating**
3. **Make ADVANCE feel like an actual week/month instead of one day**
4. Continue with portfolio