import pandas as pd

def calculate_contract_value(
    injection_events: list[tuple[str, float]],
    withdrawal_events: list[tuple[str, float]],
    injection_rate_limit_per_day: float,
    withdrawal_rate_limit_per_day: float,
    max_storage_volume: float,
    storage_cost_per_unit_per_day: float
) -> float:
    """
    Calculates the net value (profit/loss) of a natural gas storage contract.

    Args:
        injection_events: A list of tuples, where each tuple is
                          (date_str, requested_volume_to_inject_on_that_day).
                          date_str should be in 'YYYY-MM-DD' format.
        withdrawal_events: A list of tuples, where each tuple is
                           (date_str, requested_volume_to_withdraw_on_that_day).
                           date_str should be in 'YYYY-MM-DD' format.
        injection_rate_limit_per_day: The maximum volume of gas that can be
                                      injected on any single day.
        withdrawal_rate_limit_per_day: The maximum volume of gas that can be
                                       withdrawn on any single day.
        max_storage_volume: The maximum capacity of the storage facility.
        storage_cost_per_unit_per_day: The cost of storing one unit of gas for one day.

    Returns:
        The net value (profit/loss) of the contract.
    """

    all_events = []
    for date_str, volume in injection_events:
        all_events.append((pd.to_datetime(date_str), 'inject', volume))
    for date_str, volume in withdrawal_events:
        all_events.append((pd.to_datetime(date_str), 'withdraw', volume))

    # Sort all events chronologically
    all_events.sort(key=lambda x: x[0])

    current_volume = 0.0
    total_profit_loss = 0.0
    last_processed_date = None

    for event_date, event_type, requested_volume in all_events:
        # Calculate storage costs for the period since the last event
        if last_processed_date is not None and event_date > last_processed_date:
            days_since_last_event = (event_date - last_processed_date).days
            storage_cost_for_period = current_volume * days_since_last_event * storage_cost_per_unit_per_day
            total_profit_loss -= storage_cost_for_period

        # Update the last processed date for the next iteration's storage cost calculation
        last_processed_date = event_date

        # Get the estimated price for the current event date using the previously defined function
        current_price = get_price_estimate(event_date)

        if event_type == 'inject':
            # Volume is limited by requested amount, remaining storage capacity, and daily injection rate
            injectable_volume = min(requested_volume,
                                    max_storage_volume - current_volume,
                                    injection_rate_limit_per_day)
            
            cost = injectable_volume * current_price
            total_profit_loss -= cost
            current_volume += injectable_volume

        elif event_type == 'withdraw':
            # Volume is limited by requested amount, currently stored gas, and daily withdrawal rate
            withdrawable_volume = min(requested_volume,
                                      current_volume,
                                      withdrawal_rate_limit_per_day)
            
            revenue = withdrawable_volume * current_price
            total_profit_loss += revenue
            current_volume -= withdrawable_volume
            
    return round(total_profit_loss, 2)

# --- Test Cases ---
print("\n--- Test Case 1: Simple Injection and Withdrawal ---")
injection_events_1 = [('2024-10-31', 100), ('2024-11-30', 150)]
withdrawal_events_1 = [('2025-01-31', 120), ('2025-02-28', 80)]
max_volume_1 = 200
injection_rate_1 = 100
withdrawal_rate_1 = 100
storage_cost_1 = 0.01

value_1 = calculate_contract_value(
    injection_events_1,
    withdrawal_events_1,
    injection_rate_1,
    withdrawal_rate_1,
    max_volume_1,
    storage_cost_1
)
print(f"Contract Value (Test 1): ${value_1}")

print("\n--- Test Case 2: Max Volume Limit ---")
injection_events_2 = [('2024-10-31', 150), ('2024-11-15', 100)] # Tries to inject 250, but max is 200
withdrawal_events_2 = [('2025-01-15', 200)]
max_volume_2 = 200
injection_rate_2 = 150
withdrawal_rate_2 = 150
storage_cost_2 = 0.005

value_2 = calculate_contract_value(
    injection_events_2,
    withdrawal_events_2,
    injection_rate_2,
    withdrawal_rate_2,
    max_volume_2,
    storage_cost_2
)
print(f"Contract Value (Test 2): ${value_2}")

print("\n--- Test Case 3: Rate Limit ---")
injection_events_3 = [('2024-10-01', 200)] # Tries to inject 200, but rate is 50
withdrawal_events_3 = [('2024-11-01', 200)]
max_volume_3 = 200
injection_rate_3 = 50 # Strict rate limit
withdrawal_rate_3 = 50
storage_cost_3 = 0.02

value_3 = calculate_contract_value(
    injection_events_3,
    withdrawal_events_3,
    injection_rate_3,
    withdrawal_rate_3,
    max_volume_3,
    storage_cost_3
)
print(f"Contract Value (Test 3): ${value_3}")

print("\n--- Test Case 4: No events, just storage cost (should be 0) ---")
value_4 = calculate_contract_value([], [], 100, 100, 100, 0.01)
print(f"Contract Value (Test 4): ${value_4}")