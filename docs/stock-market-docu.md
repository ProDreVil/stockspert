# Stock Market Investment Expert System

## Goal

Help beginner investors decide whether a stock should be **Buy**,
**Hold**, or **Sell** using knowledge gathered from a stock market
expert.

------------------------------------------------------------------------

## 1. Questions to the Expert

These questions are designed to capture the expert's knowledge and
decision-making process.

### General Knowledge

-   How does the stock market work?
-   How are currencies handled in stock trading?
-   What are the most common problems investors face in the stock
    market?

### Decision-Making Questions

-   What indicators do you check before buying a stock?
-   What P/E ratio is considered undervalued or overvalued?
-   How important are revenue growth and earnings growth?
-   When should an investor hold a stock instead of selling it?
-   How much price decline signals a sell recommendation?
-   How does trading volume affect your decision?
-   Which factors are most important: market trend, valuation, or
    company performance?

**Purpose:** The answers become the expert knowledge that will be
converted into IF--THEN rules for the system.

------------------------------------------------------------------------

## 2. Shape of the Data

The expert system stores information as structured facts (attributes)
with predefined categorical values.

| **Attribute** | **Description** | **Possible Values** |
|---|---|---|
| Stock Trend | Overall market direction | Uptrend, Sideways, Downtrend |
| P/E Ratio | Price-to-Earnings valuation | Low, Fair, High |
| Revenue Growth | Company sales performance | Positive, Neutral, Negative |
| Earnings Growth | Company profit performance | Positive, Negative |
| Trading Volume | Amount of shares traded | Low, Average, High |
| Recommendation | Final system output | Buy, Hold, Sell |

### Example Record

  Attribute         Value
  ----------------- ----------
  Stock Trend       Uptrend
  P/E Ratio         Low
  Revenue Growth    Positive
  Earnings Growth   Positive
  Trading Volume    High
  Recommendation    Buy

**Why categorical data?**

Instead of using exact numerical values, the system converts market
information into categories. This makes the knowledge easier to
represent as expert rules and simplifies decision-making.

------------------------------------------------------------------------

## 3. Planned Inference

### Inference Approach

The system will use **Rule-Based Forward Chaining**.

Forward chaining begins with the facts provided by the user, compares
them against the knowledge base, and produces a recommendation once a
rule is satisfied.

### Knowledge Base Rules

#### Rule 1 --- BUY

**IF** - Stock Trend = Uptrend - P/E Ratio = Low - Revenue Growth =
Positive - Earnings Growth = Positive

**THEN** Recommendation = **BUY**

#### Rule 2 --- HOLD

**IF** - Stock Trend = Sideways - Earnings Growth = Positive

**THEN** Recommendation = **HOLD**

#### Rule 3 --- SELL

**IF** - Stock Trend = Downtrend - Revenue Growth = Negative - Earnings
Growth = Negative

**THEN** Recommendation = **SELL**

### Decision Flow

1.  User enters the stock's indicators.
2.  The system converts them into categorical facts.
3.  The inference engine compares the facts with every IF--THEN rule.
4.  The matching rule is fired.
5.  The system outputs **Buy**, **Hold**, or **Sell**, along with the
    rule that explains the recommendation.

------------------------------------------------------------------------

## Why This Design?

-   **Expert questions** capture real investment knowledge.
-   **Structured categorical data** makes facts easy to store and
    process.
-   **Forward chaining** provides transparent, explainable
    recommendations suitable for beginner investors.
