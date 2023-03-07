from zeri import *

x, y = zeros(f, 0, pi/2, 1e-15, 100, "rel")
z, u = zeros(f, 0, pi/2, 1e-15, 100, "mix") 
print(x, y)
print(z, u)
# print(zeros_er(f, 0, pi/2)
print(f(x), f(z))
