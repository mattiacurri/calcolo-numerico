from zeri import *

x, y = zeros(f, 0, pi/2, 1e-15, 100, "abs")
print(f"Zero: {x}, Passi: {y}")
x, y = zeros(f, 0, pi/2, 1e-15, 100, "mix") 
print(f"Zero: {x}, Passi: {y}")
x, y = zeros(h, 0, 10, 1e-15, 100, "abs") 
print(f"Zero: {x}, Passi: {y}")