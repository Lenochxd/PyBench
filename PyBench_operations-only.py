import time

print("\n--------------------------------\n\nStarting...\n")

start_time = time.perf_counter()
numerator = 4.0
denominator = 1.0
operation = 1.0
pi = 0.0
for _ in range(100000000):
    pi += operation * (numerator / denominator)
    denominator += 2.0
    operation *= -1.0
end_time = time.perf_counter()

execution_time = end_time - start_time
score = 100 / execution_time * 400

print("Done!\n")
print("Operations   : 100000000")
print(f"Time         : {round(execution_time, 3)}s")
print(f"Operations/s : {round(100000000/execution_time, 3)}")
print(f"Score        : {round(score, 3)}")
print("\n--------------------------------")
