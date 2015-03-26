

class Cube(object):

    def __init__(self, n=0):
        self._items_cube = []

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

    def update(self, x=1, y=1, z=1, value=0):
        x, y, z = x-1, y-1, z-1
        try:
            self._items_cube[z][x][y] = value
        except IndexError as e:
            pass

    def query(self, x_1=1, y_1=1, z_1=1, x_2=1, y_2=1, z_2=1):
        x_1, y_1, z_1 = x_1-1, y_1-1, z_1-1
        x_2, y_2, z_2 = x_2-1, y_2-1, z_2-1
        items_sum = 0

        for id_z, items_z in enumerate(self._items_cube):
            if z_1 <= id_z <= z_2:
                for id_x, items_x in enumerate(items_z):
                    if x_1 <= id_x <= x_2:
                        for id_y, item in enumerate(items_x):
                            if y_1 <= id_y <= y_2:
                                items_sum += item
        return items_sum