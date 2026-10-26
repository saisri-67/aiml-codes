
# Experiment 5: Bayesian Network

# Prior probabilities
p_burglary = 0.001
p_earthquake = 0.002

# Alarm conditional probabilities
p_alarm_given_burglary_and_earthquake = 0.95
p_alarm_given_burglary_and_no_earthquake = 0.94
p_alarm_given_no_burglary_and_earthquake = 0.29
p_alarm_given_no_burglary_and_no_earthquake = 0.001

# David's call probabilities
p_david_call_given_alarm = 0.91
p_david_no_call_given_alarm = 0.09
p_david_call_given_no_alarm = 0.05
p_david_no_call_given_no_alarm = 0.95

# Sophia's call probabilities
p_sophia_call_given_alarm = 0.75
p_sophia_no_call_given_alarm = 0.25
p_sophia_call_given_no_alarm = 0.02
p_sophia_no_call_given_no_alarm = 0.98


def validate_probability(p):
    if not (0 <= p <= 1):
        raise ValueError("Probability must be between 0 and 1")


def joint_probability(alarm, burglary, earthquake,
                      david_call, sophia_call):

    # Probability of burglary
    pb = p_burglary if burglary else 1 - p_burglary

    # Probability of earthquake
    pe = p_earthquake if earthquake else 1 - p_earthquake

    # Probability of alarm
    if burglary and earthquake:
        pa = p_alarm_given_burglary_and_earthquake
    elif burglary:
        pa = p_alarm_given_burglary_and_no_earthquake
    elif earthquake:
        pa = p_alarm_given_no_burglary_and_earthquake
    else:
        pa = p_alarm_given_no_burglary_and_no_earthquake

    pa = pa if alarm else 1 - pa

    # Probability of David's call
    if alarm:
        pd = (p_david_call_given_alarm if david_call
              else p_david_no_call_given_alarm)
    else:
        pd = (p_david_call_given_no_alarm if david_call
              else p_david_no_call_given_no_alarm)

    # Probability of Sophia's call
    if alarm:
        ps = (p_sophia_call_given_alarm if sophia_call
              else p_sophia_no_call_given_alarm)
    else:
        ps = (p_sophia_call_given_no_alarm if sophia_call
              else p_sophia_no_call_given_no_alarm)

    # Validate probabilities
    for p in [pb, pe, pa, pd, ps]:
        validate_probability(p)

    return pb * pe * pa * pd * ps


# Test Case 1: Alarm true, no burglary, no earthquake,
# both David and Sophia call
print("Test Case 1:")
print("Joint probability:",
      round(joint_probability(True, False, False, True, True), 9))
# Output:
# Joint probability: 0.000680454


# Test Case 2: Burglary and alarm, both call
print("\nTest Case 2:")
print("Joint probability:",
      round(joint_probability(True, True, False, True, True), 9))
# Output:
# Joint probability: 0.000640267


# Test Case 3: Earthquake and alarm, David calls,
# Sophia does not call
print("\nTest Case 3:")
print("Joint probability:",
      round(joint_probability(True, False, True, True, False), 9))
# Output:
# Joint probability: 0.000131818


# Test Case 4: No alarm, no burglary, no earthquake,
# neither person calls
print("\nTest Case 4:")
print("Joint probability:",
      round(joint_probability(False, False, False, False, False), 9))
# Output:
# Joint probability: 0.927280653


# Test Case 5: Invalid probability
print("\nTest Case 5:")
try:
    validate_probability(1.5)
except ValueError as e:
    print("Error:", e)
# Output:
# Error: Probability must be between 0 and 1
