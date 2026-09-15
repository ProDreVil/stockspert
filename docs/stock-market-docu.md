# Stock Market Investment Expert System

## Goal

Help beginner investors decide whether a stock should be **Buy**, **Hold**, or **Sell** using knowledge gathered from a stock market expert.

The system will also include a simple **portfolio simulation** so that recommendations can consider the investor's available cash and shares owned.

---

## 1. Questions to the Expert

These questions are designed to capture the expert's knowledge and decision-making process.

### General Knowledge

* How does the stock market work?
* How are currencies handled in stock trading?
* What are the most common problems investors face in the stock market?

### Decision-Making Questions

* What indicators do you check before buying a stock?
* What P/E ratio is considered undervalued or overvalued?
* How important are revenue growth and earnings growth?
* When should an investor hold a stock instead of selling it?
* How much price decline signals a sell recommendation?
* How does trading volume affect your decision?
* Which factors are most important: market trend, valuation, or company performance?

**Purpose:** The answers become the expert knowledge that will be converted into IF--THEN rules for the system.

---

## 2. Shape of the Data

The expert system stores information as structured facts (attributes) with predefined categorical values.

| Attribute       | Description                      | Possible Values              |
| --------------- | -------------------------------- | ---------------------------- |
| Stock Trend     | Overall market direction         | Uptrend, Sideways, Downtrend |
| P/E Ratio       | Price-to-Earnings valuation      | Low, Fair, High              |
| Revenue Growth  | Company sales performance        | Positive, Neutral, Negative  |
| Earnings Growth | Company profit performance       | Positive, Negative           |
| Trading Volume  | Amount of shares traded          | Low, Average, High           |
| Stock Price     | Current price of the stock       | Numeric value                |
| Available Cash  | Money available in the portfolio | Numeric value                |
| Shares Owned    | Number of shares currently owned | Numeric value                |
| Recommendation  | Final system output              | Buy, Hold, Sell              |

### Example Record

| Attribute       | Value    |
| --------------- | -------- |
| Stock Trend     | Uptrend  |
| P/E Ratio       | Low      |
| Revenue Growth  | Positive |
| Earnings Growth | Positive |
| Trading Volume  | High     |
| Stock Price     | $100.00  |
| Available Cash  | $10,000  |
| Shares Owned    | 0        |
| Recommendation  | Buy      |

**Why categorical data?**

Instead of using exact numerical values for market indicators, the system converts them into categories. This makes the knowledge easier to represent as expert rules and simplifies decision-making.

Stock price, available cash, and shares owned remain numerical because they are used for the portfolio and trading simulation.

---

## 3. Planned Inference

### Inference Approach

The system will use **Rule-Based Forward Chaining**.

Forward chaining begins with the facts provided by the user, compares them against the knowledge base, and produces a recommendation once a rule is satisfied.

### Knowledge Base Rules

#### BUY Rules

**Rule 1**

**IF**

* Stock Trend = Uptrend
* P/E Ratio = Low
* Revenue Growth = Positive
* Earnings Growth = Positive

**THEN** Recommendation = **BUY**

**Rule 2**

**IF**

* Stock Trend = Uptrend
* P/E Ratio = Fair
* Revenue Growth = Positive
* Earnings Growth = Positive

**THEN** Recommendation = **BUY**

**Rule 3**

**IF**

* Stock Trend = Uptrend
* P/E Ratio = Low
* Revenue Growth = Positive
* Earnings Growth = Positive
* Trading Volume = High

**THEN** Recommendation = **BUY**

---

#### HOLD Rules

**Rule 4**

**IF**

* Stock Trend = Sideways
* Earnings Growth = Positive

**THEN** Recommendation = **HOLD**

**Rule 5**

**IF**

* Stock Trend = Uptrend
* P/E Ratio = Low
* Revenue Growth = Neutral
* Earnings Growth = Positive

**THEN** Recommendation = **HOLD**

**Rule 6**

**IF**

* Stock Trend = Uptrend
* P/E Ratio = Fair
* Revenue Growth = Neutral
* Earnings Growth = Positive

**THEN** Recommendation = **HOLD**

**Rule 7**

**IF**

* Stock Trend = Downtrend
* Revenue Growth = Neutral
* Earnings Growth = Positive

**THEN** Recommendation = **HOLD**

**Rule 8**

**IF**

* Stock Trend = Downtrend
* Revenue Growth = Positive
* Earnings Growth = Positive

**THEN** Recommendation = **HOLD**

**Rule 9**

**IF**

* Stock Trend = Downtrend
* Revenue Growth = Positive
* Earnings Growth = Negative

**THEN** Recommendation = **HOLD**

**Rule 10**

**IF**

* Stock Trend = Uptrend
* P/E Ratio = Low
* Revenue Growth = Positive
* Earnings Growth = Positive
* Trading Volume = Low

**THEN** Recommendation = **HOLD**

---

#### SELL Rules

**Rule 11**

**IF**

* Stock Trend = Downtrend
* Revenue Growth = Negative
* Earnings Growth = Negative

**THEN** Recommendation = **SELL**

**Rule 12**

**IF**

* Stock Trend = Sideways
* Earnings Growth = Negative

**THEN** Recommendation = **SELL**

**Rule 13**

**IF**

* Stock Trend = Downtrend
* P/E Ratio = High
* Revenue Growth = Negative
* Earnings Growth = Positive

**THEN** Recommendation = **SELL**

**Rule 14**

**IF**

* Stock Trend = Downtrend
* Revenue Growth = Neutral
* Earnings Growth = Negative

**THEN** Recommendation = **SELL**

---

### Portfolio-Aware Rules

The portfolio is used to make the recommendation more practical for the current investor.

**Rule 15 — Insufficient Funds**

**IF**

* Market conditions indicate **BUY**
* Available Cash is less than the required purchase amount

**THEN** Recommendation = **HOLD**

**Reason:** Insufficient funds to purchase the stock.

**Rule 16 — No Shares to Sell**

**IF**

* Market conditions indicate **SELL**
* Shares Owned = 0

**THEN** Recommendation = **HOLD**

**Reason:** No shares available to sell.

These rules allow the expert system to consider both the **stock's market conditions** and the **investor's current portfolio**.

---

### Fallback Rule

**Rule 17**

**IF**

* No recommendation has been produced

**THEN**

* Output **NO CLEAR RECOMMENDATION**

This prevents the system from forcing a Buy, Hold, or Sell decision when none of the rules match.

---

## 4. Portfolio Simulation

The system will include a simple portfolio simulation.

### Starting Portfolio

* Starting Cash: **$10,000**
* Starting Shares: **0**

### Buying

The user can enter the number of shares they want to buy.

**Buy calculation:**

`Total Cost = Stock Price × Quantity`

The purchase is allowed only if the investor has enough available cash.

### Selling

The user can enter the number of shares they want to sell.

The sale is allowed only if the investor owns enough shares.

### Portfolio Value

`Portfolio Value = Available Cash + (Shares Owned × Stock Price)`

The portfolio information will update after each successful transaction and when the simulated stock price changes.

---

## 5. Simulation

The system will simulate changes in the stock market over time.

The user can select a time amount and unit, such as:

* 3 Days
* 2 Months
* 6 Years

The **NEXT** button advances the simulation.

The system will:

1. Advance the simulated date.
2. Update the stock price.
3. Update the price history graph.
4. Run the expert system using the current market indicators.
5. Update the portfolio value.
6. Display the new recommendation and explanation.

A **Random Market** option can also generate different market conditions for testing.

---

## 6. Decision Flow

1. User enters the stock's market indicators.
2. User provides the current stock price.
3. The system stores the investor's available cash and shares owned.
4. The system converts market indicators into categorical facts.
5. The inference engine compares the facts with the IF--THEN rules.
6. A matching market rule is fired.
7. Portfolio conditions are checked when necessary.
8. The system outputs **Buy**, **Hold**, or **Sell**.
9. The system displays the rule and reason behind the recommendation.
10. The user can simulate the market or buy/sell a chosen number of shares.

---

## 7. Why This Design?

* **Expert questions** capture real investment knowledge.
* **Structured categorical data** makes facts easy to store and process.
* **Forward chaining** provides transparent, explainable recommendations.
* **Portfolio information** makes recommendations more relevant to the investor's current situation.
* **Quantity-based trading** allows the user to actually simulate buying and selling shares.
* **Simulation** allows the expert system to be tested under different market conditions.
* The system remains simple enough for beginner investors to understand.