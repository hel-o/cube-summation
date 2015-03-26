import unittest

from app.cube_summation.matrix3d import Cube


class TestCubeSummation(unittest.TestCase):

    def setUp(self):
        self.n = 4
        self.matrix3d = Cube(self.n)

    def test_size_matrix(self):
        cube = self.matrix3d.get()
        assert (len(cube) * len(cube[0]) * self.n) == self.n**3

    def test_1_update_and_query_matrix(self):
        self.matrix3d.update(x=2, y=2, z=2, value=4)

        assert 4 == self.matrix3d.query(x_1=1, y_1=1, z_1=1, x_2=3, y_2=3, z_2=3)

        self.matrix3d.update(x=1, y=1, z=1, value=23)

        assert 4 == self.matrix3d.query(x_1=2, y_1=2, z_1=2, x_2=4, y_2=4, z_2=4)
        assert 27 == self.matrix3d.query(x_1=1, y_1=1, z_1=1, x_2=3, y_2=3, z_2=3)

    def test_2_update_and_query_matrix(self):
        self.matrix3d.update(x=2, y=2, z=2, value=1)

        assert 0 == self.matrix3d.query(x_1=1, y_1=1, z_1=1, x_2=1, y_2=1, z_2=1)
        assert 1 == self.matrix3d.query(x_1=1, y_1=1, z_1=1, x_2=2, y_2=2, z_2=2)
        assert 1 == self.matrix3d.query(x_1=2, y_1=2, z_1=2, x_2=2, y_2=2, z_2=2)


if __name__ == '__main__':
    unittest.main()