from numpy import array, linalg


class Vector:
    def __init__(self, vector):
        self.vector = array([int(x) for x in str(vector)])

    def __mul__(self, other):
        return self.vector * other

    def __sub__(self, other):
        return linalg.norm(self.vector, ord=1) - linalg.norm(other.vector, ord=1)

    def norm(self):
        return linalg.norm(self.vector, ord=1, axis=0)

    def __copy__(self):
        print("Копія")
        return Vector(self.vector)

