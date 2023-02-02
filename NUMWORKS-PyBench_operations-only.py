"""
>> https://my.numworks.com/python/81lennoch/numworks_pybench_beta <<
"""

import time

print("\n--------------------------------\n\nStarting...\n")

start_time = time.monotonic()
numerator = 4.0
denominator = 1.0
operation = 1.0
pi = 0.0
for _ in range(250000):
    pi += operation * (numerator / denominator)
    denominator += 2.0
    operation *= -1.0
end_time = time.monotonic()

execution_time = end_time - start_time
score = 100 / (execution_time / 1.09)

print("Done!\n")
print("Operations   : 250000")
print("Time         :", execution_time, "s")
print("Operations/s :", 250000 / execution_time)
print("Score        :", score)
print("\n--------------------------------")
