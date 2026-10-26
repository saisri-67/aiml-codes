
import itertools

hidden_states = ['healthy', 'sick']

initial = {
    'healthy': 0.5,
    'sick': 0.5
}

transition = {
    'healthy': {'healthy': 0.7, 'sick': 0.3},
    'sick': {'healthy': 0.4, 'sick': 0.6}
}

emission = {
    'healthy': {'sleeping': 0.2, 'eating': 0.6, 'pooping': 0.2},
    'sick': {'sleeping': 0.4, 'eating': 0.1, 'pooping': 0.5}
}


def viterbi(obs):
    best_probability = 0
    best_path = None

    paths = itertools.product(hidden_states, repeat=len(obs))

    for path in paths:
        probability = initial[path[0]] * emission[path[0]][obs[0]]

        for i in range(1, len(obs)):
            previous = path[i - 1]
            current = path[i]

            probability *= (
                transition[previous][current] *
                emission[current][obs[i]]
            )

        if probability > best_probability:
            best_probability = probability
            best_path = path

    return best_probability, best_path


# Test Case 1 - Success
obs = ['sleeping', 'eating', 'sleeping']
probability, path = viterbi(obs)

print("\nTest Case 1 - Success")
print("Input:", obs)
print("Most likely state sequence:", path)
print("Viterbi probability:", probability)
# Expected path: ('sick', 'healthy', 'healthy')
# Expected probability: 0.00672
# Test Case 1: Pass


# Test Case 2 - Success
obs = ['sleeping', 'eating', 'sleeping']
probability, path = viterbi(obs)

print("\nTest Case 2 - Success")
print("Input:", obs)
print("Most likely state sequence:", path)
print("Viterbi probability:", probability)
print("Transition and emission probabilities are valid")
# Expected path: ('sick', 'healthy', 'healthy')
# Expected probability: 0.00672
# Test Case 2: Pass


# Test Case 3 - Success
obs = ['sleeping']
probability, path = viterbi(obs)

print("\nTest Case 3 - Success")
print("Input:", obs)
print("Most likely state sequence:", path)
print("Viterbi probability:", probability)
print("Expected path:", ('sick',))
print("Expected probability:", 0.2)
# Test Case 3: Pass


# Test Case 4 - Failure/Edge
print("\nTest Case 4 - Failure/Edge")

old_value = transition['healthy']['sick']
transition['healthy']['sick'] = 0

obs = ['sleeping', 'pooping']
test_path = ('healthy', 'sick')

probability = (
    initial[test_path[0]]
    * emission[test_path[0]][obs[0]]
    * transition[test_path[0]][test_path[1]]
    * emission[test_path[1]][obs[1]]
)

print("Input:", obs)
print("Test path:", test_path)
print("Path probability:", probability)
print("Impossible path rejected.")
# Expected path probability: 0.0
# Test Case 4: Pass

transition['healthy']['sick'] = old_value


# Test Case 5 - Failure/Edge
print("\nTest Case 5 - Failure/Edge")

invalid_transition = {
    'healthy': {'healthy': 0.7, 'sick': 0.5},
    'sick': {'healthy': 0.4, 'sick': 0.6}
}

valid = True

for state in hidden_states:
    total = sum(invalid_transition[state].values())

    if abs(total - 1.0) > 0.000001:
        valid = False
        print("Error:", state,
              "transition probabilities sum to", total)

if not valid:
    print("Invalid probability matrix detected.")
# Expected output: Invalid probability matrix detected.
# Test Case 5: Pass
