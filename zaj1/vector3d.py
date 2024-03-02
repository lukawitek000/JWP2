import math

class Vector3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def norm(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mod__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        c_x = self.y * other.z - self.z * other.y
        c_y = self.z * other.x - self.x * other.z
        c_z = self.x * other.y - self.y * other.x
        return Vector3D(c_x, c_y, c_z)

    def are_orthogonal(self, other):
        return self.dot(other) == 0


def main():
    v1 = Vector3D(1, 2, 3)
    v2 = Vector3D(4, 5, 6)
    print(f"v1 = {v1}, v2 = {v2}")
    print(f"v1: x={v1.x}, y={v1.y}, z={v1.z}")
    print(f"v2: x={v2.x}, y={v2.y}, z={v2.z}")
    print(f"v1 norm = {v2.norm()}")
    print(f"v1 norm = {v1.norm()}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 3 = {v1 % 3}")
    print(f"v1 * v2 = {v1.dot(v2)}")
    print(f"v1 cross v2 = {v1.cross(v2)}")
    print(f"v1 are orthogonal to v2 = {v1.are_orthogonal(v2)}")


if __name__ == '__main__':
    main() # Wywołaj main(), jeśli ten moduł został uruchomiony, a nie zaimportowany.