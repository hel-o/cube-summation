import unittest

from app.matrix3d import Cube


class TestCubeSummation(unittest.TestCase):

    def setUp(self):
        self.n = 4
        self.matrix3d = Cube(self.n)

    def test_size_matrix(self):
        cube = self.matrix3d.get()
        assert (len(cube) * len(cube[0]) * self.n) == self.n**3

    def test_1_update_and_query_matrix(self):
        self.matrix3d.update(x=2, y=2, z=2, value=4)
        assert 4 == self.matrix3d.query(x1=1, y1=1, z1=1, x2=3, y2=3, z2=3)

    def test_2_update_and_sum_matrix(self):
        self.matrix3d.update(x=1, y=1, z=1, value=23)

        assert 4 == self.matrix3d.query(x1=2, y1=2, z1=2, x2=4, y2=4, z2=4)
        assert 27 == self.matrix3d.query(x1=1, y1=1, z1=1, x2=3, y2=3, z2=3)


if __name__ == '__main__':
    unittest.TestCase()