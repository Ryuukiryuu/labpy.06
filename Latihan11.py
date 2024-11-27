import math

# Menggunakan lambda untuk mendefinisikan fungsi
a = lambda x: x**2
b = lambda x, y: math.sqrt(x**2 + y**2)
c = lambda *args: sum(args) / len(args)
d = lambda s: "".join(set(s))

if __name__ == "__main__":

    print("a(5):", a(5))

    print("b(3, 4):", b(3, 4))

    print("c(1, 2, 3, 4, 5):", c(1, 2, 3, 4, 5))

    print("d('hello world'):", d('hello world')) 