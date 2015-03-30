

class Cube(object):

    def __init__(self, n=0):
        self._items_cube = []
        self.n = n

        if 1 <= n <= 100:
            for z in range(n):
                items_x = []
                for x in range(n):
                    items_y = []
                    for y in range(n):
                        items_y.append(0)
                    items_x.append(items_y)
                self._items_cube.append(items_x)

    def get(self):
        return self._items_cube

    def _in_range(self, axis=0):
        return 1 <= axis <= self.n

    def update(self, x=1, y=1, z=1, value=0):
        if self._in_range(x) and self._in_range(y) and self._in_range(z)\
                and -10**9 <= value <= 10**9:
            x, y, z = x-1, y-1, z-1
            self._items_cube[z][x][y] = value
            return value
        return None

    def _check_axis(self, axis_1=0, axis_2=0):
        return 1 <= axis_1 <= axis_2 <= self.n

    def query(self, x_1=1, y_1=1, z_1=1, x_2=1, y_2=1, z_2=1):
        items_sum = 0
        if self._check_axis(x_1, x_2) and self._check_axis(y_1, y_2) and self._check_axis(z_1, z_2):
            x_1, y_1, z_1 = x_1-1, y_1-1, z_1-1
            x_2, y_2, z_2 = x_2-1, y_2-1, z_2-1

            for id_z, items_z in enumerate(self._items_cube):
                if z_1 <= id_z <= z_2:
                    for id_x, items_x in enumerate(items_z):
                        if x_1 <= id_x <= x_2:
                            for id_y, item in enumerate(items_x):
                                if y_1 <= id_y <= y_2:
                                    items_sum += item
        return items_sum