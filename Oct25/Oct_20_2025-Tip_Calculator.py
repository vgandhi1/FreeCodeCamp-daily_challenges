"""
Tip Calculator
Given the price of your meal and a custom tip percent, return an array with three tip values; 15%, 20%, and the custom amount.

Prices will be given in the format: "$N.NN".
Custom tip percents will be given in this format: "25%".
Return amounts in the same "$N.NN" format, rounded to two decimal places.
For example, given a "$10.00" meal price, and a "25%" custom tip value, return ["$1.50", "$2.00", "$2.50"].
"""

def calculate_tips(meal_price, custom_tip):
    meal_price = float(meal_price[1:])
    custom_tip = float(custom_tip[:-1])
    tip_15 = meal_price*.15
    tip_20 = meal_price*.2
    tip_custom = meal_price*custom_tip/100
    final_tip_amount = []
    tips = [0.15, 0.20, custom_tip/100]

    for tip in tips:
        tip_amount = meal_price*tip
        final_tip_amount.append(f"${tip_amount:.2f}",)

    return final_tip_amount

    # return [
    #     f"${tip_15:0.2f}", 
    #     f"${tip_20:0.2f}", 
    #     f"${tip_custom:0.2f}"
    # ]
print(calculate_tips("$10.00", "25%"))


"""
Tests
Passed:1. calculate_tips("$10.00", "25%") should return ["$1.50", "$2.00", "$2.50"].
Passed:2. calculate_tips("$89.67", "26%") should return ["$13.45", "$17.93", "$23.31"].
Passed:3. calculate_tips("$19.85", "9%") should return ["$2.98", "$3.97", "$1.79"].
"""

#alternative code

from decimal import Decimal, ROUND_HALF_UP

def calculate_tips(meal_price_str: str, custom_tip_str: str) -> list[str]:
    """
    Given the price of your meal and a custom tip percent, return an array with
    three tip values: 15%, 20%, and the custom amount. Uses the Decimal type
    for precise financial calculations.
    """
    # 1. Parse and Convert to Decimal
    # Remove '$' and '%' and convert to Decimal.
    meal_price = Decimal(meal_price_str.lstrip('$'))
    custom_tip_percent = Decimal(custom_tip_str.rstrip('%'))

    # 2. Define standard tip rates
    STANDARD_RATES = [
        Decimal("0.15"),  # 15%
        Decimal("0.20")   # 20%
    ]

    # 3. Calculate the custom tip rate
    # The custom tip is P/100 (e.g., 25% is 0.25)
    custom_rate = custom_tip_percent / Decimal("100")
    
    tip_rates = STANDARD_RATES + [custom_rate]
    
    tip_amounts = []
    for rate in tip_rates:
        # Calculate tip: amount * rate
        raw_tip = meal_price * rate
        
        # Round to two decimal places using standard rounding rules (ROUND_HALF_UP)
        rounded_tip = raw_tip.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        
        # Format back to the required string "$N.NN"
        tip_amounts.append(f"${rounded_tip}")

    return tip_amounts
