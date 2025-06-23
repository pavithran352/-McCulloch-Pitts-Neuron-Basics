# McCulloch-Pitts neuron model logic gate implementation

def mp_and(x1, x2):
    w1, w2 = 1, 1
    theta = 2
    return 1 if (w1 * x1 + w2 * x2) >= theta else 0

def mp_or(x1, x2):
    w1, w2 = 1, 1
    theta = 1
    return 1 if (w1 * x1 + w2 * x2) >= theta else 0

def mp_not(x):
    w = -1
    theta = -0.5
    return 1 if (w * x) >= theta else 0

# Truth table for AND gate
print("AND Gate")
print("x1 x2 | Output")
for x1 in [0, 1]:
    for x2 in [0, 1]:
        print(f"{x1}  {x2}  |   {mp_and(x1, x2)}")

print("\nOR Gate")
print("x1 x2 | Output")
for x1 in [0, 1]:
    for x2 in [0, 1]:
        print(f"{x1}  {x2}  |   {mp_or(x1, x2)}")

print("\nNOT Gate")
print("x | Output")
for x in [0, 1]:
    print(f"{x} |   {mp_not(x)}")
