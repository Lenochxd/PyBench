import time
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

print(
      "\n--------------------------------"
      "\n\nStarting..."
      "\n\nStarting Image Generation..."
     )

def generate_random_image(width, height):
    image = Image.new("RGB", (width, height))
    pixels = image.load()
    for i in range(width):
        for j in range(height):
            pixels[i, j] = (np.random.randint(0, 255), np.random.randint(
                0, 255), np.random.randint(0, 255))
    return image

start_time = time.perf_counter()
image = generate_random_image(900, 900)
end_time = time.perf_counter()

image_gen_time = end_time - start_time
score1 = 100 / image_gen_time * 55


print("Starting Graph Generation...")

def generate_plot(x, y):
    plt.plot(x, y)
    return plt.figure()

start_time = time.perf_counter()
x = np.linspace(0, 20 * np.pi, 1000)
y = np.sin(x) * np.exp(-0.1 * x)
generate_plot(x, y)
end_time = time.perf_counter()

plot_gen_time = end_time - start_time
score2 = 100 / plot_gen_time * 2.1


print("Starting Calculating Pi...")

def calculate_pi(n_terms):
    numerator = 4.0
    denominator = 1.0
    operation = 1.0
    pi = 0.0
    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return pi

start_time = time.perf_counter()
calculate_pi(100000000)
end_time = time.perf_counter()

pi_calc_time = end_time - start_time
score3 = 4000 / pi_calc_time * 2

total_time = image_gen_time + plot_gen_time + pi_calc_time
total_score = score1 + score2 + score3


print(
      "Done!\n"
      "\n"
      "\n== Image Generation =="
      "\nSize         : 300x300"
      f"\nTime         : {round(image_gen_time, 3)}s"
      f"\nScore        : {round(score1, 3)}"
      "\n"
      "\n== Graph Generation =="
      f"\nTime         : {round(plot_gen_time, 3)}s"
      f"\nScore        : {round(score2, 3)}"
      "\n"
      "\n== Operations =="
      "\nOperations   : 100000000"
      f"\nTime         : {round(pi_calc_time, 3)}s"
      f"\nOperations/s : {round(100000000/pi_calc_time, 3)}"
      f"\nScore        : {round(score3, 3)}"
      "\n\n"
      f"\nTotal Time   : {round(total_time, 3)}"
      f"\nTotal Score  : {round(total_score, 3)}"
      "\n\n--------------------------------"
     )
