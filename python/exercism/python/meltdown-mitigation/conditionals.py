def is_criticality_balanced(temperature, neutrons_emitted):
    power_output = temperature * neutrons_emitted
    return temperature < 800 and neutrons_emitted > 500 and power_output < 500_000 


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency_percentage = (generated_power / theoretical_max_power) * 100
    if efficiency_percentage >= 80:
        return "green"
    elif efficiency_percentage >= 60:
        return "orange"
    elif efficiency_percentage >= 30:
        return "red"
    return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    threshold_lower = threshold * 0.90
    print(threshold_lower)
    threshold_upper = threshold * 1.10
    print(threshold_upper)
    power_output = temperature * neutrons_produced_per_second
    
    if power_output < threshold_lower:
        return "LOW"
    elif power_output <= threshold_upper:
        return "NORMAL"
    return "DANGER"