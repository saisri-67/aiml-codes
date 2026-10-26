
from sympy import symbols, Not, Implies
from sympy.logic.inference import satisfiable

# Define symbols
Rain, Harry_visited_Hagrid, Harry_visited_Dumbledore = symbols(
    'Rain Harry_visited_Hagrid Harry_visited_Dumbledore'
)

# Define knowledge base rules
kb = [
    Implies(Not(Rain), Harry_visited_Hagrid),
    Implies(Harry_visited_Hagrid, Harry_visited_Dumbledore)
]

def run_test(test_name, facts):
    print("\n" + "=" * 40)
    print(test_name)
    print("=" * 40)

    # Combine facts and rules
    knowledge_base = kb + facts

    # Check whether the knowledge base is satisfiable
    result = satisfiable(knowledge_base)

    print("Knowledge Base Satisfiable:", bool(result))

    # Infer conclusions
    if satisfiable(knowledge_base + [Harry_visited_Hagrid]):
        print("Harry visited Hagrid: True")
    else:
        print("Harry visited Hagrid: False")

    if satisfiable(knowledge_base + [Harry_visited_Dumbledore]):
        print("Harry visited Dumbledore: True")
    else:
        print("Harry visited Dumbledore: False")

# Test Case 1: Harry visits Dumbledore
run_test(
    "TEST CASE 1",
    [Harry_visited_Dumbledore]
)

# Test Case 2: Harry visited Hagrid
run_test(
    "TEST CASE 2",
    [Harry_visited_Hagrid]
)

# Test Case 3: Rain is true
run_test(
    "TEST CASE 3",
    [Rain]
)

# Test Case 4: No rain
run_test(
    "TEST CASE 4",
    [Not(Rain)]
)

# Test Case 5: Contradictory facts
run_test(
    "TEST CASE 5",
    [Rain, Not(Rain)]
)
