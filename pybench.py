import time

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
score = (100 / execution_time)*700

print("Time  : ", execution_time, "s")
print("Score : ", score)
