BASE_CONFIDENCE = {
    "BUY-UPTREND-LOW-PE": 90,
    "BUY-UPTREND-FAIR-PE": 82,
    "BUY-UPTREND-HIGH-VOLUME": 95,

    "HOLD-SIDEWAYS-POSITIVE-EARNINGS": 75,
    "HOLD-UPTREND-LOW-PE-NEUTRAL-REVENUE": 72,
    "HOLD-UPTREND-FAIR-PE-NEUTRAL-REVENUE": 68,
    "HOLD-UPTREND-HIGH-PE": 60,
    "HOLD-DOWNTREND-NEUTRAL-REVENUE": 65,
    "HOLD-DOWNTREND-POSITIVE-FUNDAMENTALS": 70,
    "HOLD-DOWNTREND-MIXED-FUNDAMENTALS": 60,
    "HOLD-UPTREND-LOW-VOLUME": 78,

    "SELL-DOWNTREND-NEGATIVE-FUNDAMENTALS": 90,
    "SELL-SIDEWAYS-NEGATIVE-EARNINGS": 80,
    "SELL-DOWNTREND-HIGH-PE": 82,
    "SELL-DOWNTREND-NEGATIVE-EARNINGS": 78,

    "NO-CLEAR-RECOMMENDATION": 0,
}


def get_base_confidence(rule):
    return BASE_CONFIDENCE.get(rule, 0)


def get_history_strength(price_history):
    if len(price_history) < 2:
        return 0

    direction = (
        price_history[-1] - price_history[0]
    ) / price_history[0]

    movements = [
        price_history[i + 1] - price_history[i]
        for i in range(len(price_history) - 1)
    ]

    positive = sum(
        1 for movement in movements
        if movement > 0
    )

    negative = sum(
        1 for movement in movements
        if movement < 0
    )

    consistency = (
        max(positive, negative)
        / len(movements)
    )

    strength = (
        min(abs(direction) / 0.10, 1)
        * consistency
    )

    return strength


def get_history_direction(price_history):
    if len(price_history) < 2:
        return 0

    return (
        price_history[-1] - price_history[0]
    ) / price_history[0]


def apply_external_factor(
    confidence,
    strength,
    supports_recommendation,
    adjustment_strength
):
    adjustment = strength * adjustment_strength

    if supports_recommendation:
        confidence += (
            (100 - confidence)
            * adjustment
        )
    else:
        confidence -= (
            confidence
            * adjustment
        )

    return max(0, min(100, confidence))


def get_volume_strength(volume):
    if volume == "high":
        return 1.0

    if volume == "average":
        return 0.0

    if volume == "low":
        return 1.0

    return 0.0


def volume_supports_recommendation(
    recommendation,
    volume
):
    if recommendation == "BUY":
        return volume == "high"

    if recommendation == "SELL":
        return volume == "high"

    if recommendation == "HOLD":
        return volume == "low"

    return False


def calculate_confidence(
    rule,
    recommendation,
    price_history,
    volume
):
    confidence = get_base_confidence(rule)

    history_direction = get_history_direction(
        price_history
    )

    history_strength = get_history_strength(
        price_history
    )

    if recommendation == "BUY":
        history_supports = history_direction > 0

    elif recommendation == "SELL":
        history_supports = history_direction < 0

    else:
        history_supports = abs(history_direction) < 0.02

    confidence = apply_external_factor(
        confidence,
        history_strength,
        history_supports,
        0.5
    )

    volume_strength = get_volume_strength(volume)

    volume_supports = volume_supports_recommendation(
        recommendation,
        volume
    )

    confidence = apply_external_factor(
        confidence,
        volume_strength,
        volume_supports,
        0.25
    )

    return round(confidence)