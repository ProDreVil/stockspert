# Stockspert Confidence Calculation — Draft

## 1. Base Confidence

The CLIPS rule determines the initial confidence.

Example:

```text
BUY-UPTREND-LOW-PE → 90%
```

This is the starting point before external factors are considered.

---

## 2. External Factors

External factors do **not** change the recommendation.

They only modify the confidence.

For now:

* **Price History** → strong influence
* **Trading Volume** → moderate influence

Future factors can be added later.

---

## 3. Price History

Price history is used to determine whether the recent movement supports or contradicts the recommendation.

Example:

```text
100 → 102 → 104 → 106 → 108 → 110
```

This is strongly upward and supports a BUY recommendation.

Another example:

```text
110 → 108 → 106 → 107 → 104 → 102
```

This is mostly downward and contradicts a BUY recommendation.

### History Strength

First calculate the overall direction:

```text
direction = (newest price - oldest price) / oldest price
```

Then calculate consistency:

```text
consistency =
number of movements in the dominant direction
/
total number of movements
```

Then combine them:

```text
history_strength =
min(abs(direction) / 0.10, 1) × consistency
```

This produces a value from `0` to `1`.

A value closer to `1` means the history provides stronger evidence.

---

## 4. History vs Recommendation

The history is interpreted according to the recommendation.

### BUY

```text
Upward history → supports BUY
Downward history → contradicts BUY
```

### SELL

```text
Downward history → supports SELL
Upward history → contradicts SELL
```

### HOLD

```text
Sideways history → supports HOLD
Strong movement → weakens HOLD
```

---

## 5. Diminishing Returns

External factors use an **Achilles-and-the-Tortoise** style approach.

Instead of adding a fixed percentage:

```text
90 + 10 = 100
```

we move toward the boundary based on the **remaining distance**.

For supporting evidence:

```text
new confidence =
current confidence
+
remaining distance to 100 × adjustment strength
```

For contradictory evidence:

```text
new confidence =
current confidence
-
current confidence × adjustment strength
```

This means the closer confidence gets to `100%` or `0%`, the smaller each additional adjustment becomes.

Example:

```text
90% → 95% → 97.5% → 98.75%
```

rather than:

```text
90% → 100% → 110%
```

---

## 6. Factor Strength

Different external factors have different influence.

For now:

```text
Price History = Strong
Trading Volume = Moderate
```

Therefore, price history should generally have a larger effect on confidence than volume.

The exact adjustment strengths will be tuned during testing rather than permanently assumed.

---

## 7. Important Rule

External factors **never override the CLIPS recommendation**.

Example:

```text
CLIPS:
BUY
Base confidence: 90%

Price history:
Strongly contradicts BUY

Result:
BUY — 34% confidence
```

The system does **not** become:

```text
SELL
```

because of the history.

Instead, the confidence communicates that the rule-based BUY recommendation has weak external support.

---

## 8. Calculation Flow

```text
CLIPS
   ↓
Recommendation + Fired Rule
   ↓
Base Confidence
   ↓
Price History
   ↓
Adjusted Confidence
   ↓
Trading Volume
   ↓
Final Confidence
```

The final output is therefore:

```text
Recommendation: BUY
Rule Fired: BUY-UPTREND-LOW-PE
Confidence: 34%
```

This keeps the expert system's reasoning separate from the supporting evidence.

---

## 9. Future Expansion

Additional external factors can later be added without changing the CLIPS recommendation system.

Possible future factors:

* Additional price-history measurements
* Volume changes
* Volatility
* Other market indicators
* Portfolio conditions

Each factor would contribute evidence toward or against the existing recommendation.