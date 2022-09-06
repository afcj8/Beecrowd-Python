import math

a,b,c = map(float,input().split())
delta = (b ** 2) - (4 * a * c)

if (a == 0 or delta < 0):
    print("Impossivel calcular")
else:
    x1 = (- b + math.sqrt(delta)) / (2 * a)
    x2 = (- b - math.sqrt(delta)) / (2 * a)
    print("R1 = {:.5f}".format(x1))
    print("R2 = {:.5f}".format(x2))