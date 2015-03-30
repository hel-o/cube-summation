# coding=utf-8


def _parse_value(value):
    try:
        return int(value)
    except ValueError:
        return 0


class ConfigCubeForm(object):

    matrix_size = 0
    operations = 0
    _errors = None

    def __init__(self, form):
        self._errors = []
        self.matrix_size = _parse_value(form.get('matrix-size', 0))
        self.operations = _parse_value(form.get('operations', 0))

    def is_valid(self):
        if not 1 <= self.matrix_size <= 100:
            self._errors.append(u'El tamaño de la matriz debe estar entre 1 y 100')

        if not 1 <= self.operations <= 1000:
            self._errors.append(u'El nro. de operaciones debe estar entre 1 y 1000')

        return 0 == len(self._errors)

    def get_errors(self):
        return self._errors


class DoOperationForm(object):

    def __init__(self, form):
        self._errors = []
        self.operation = form.get('operation', None)

        if self.operation == 'update':
            self.x = _parse_value(form.get('update-x', 0))
            self.y = _parse_value(form.get('update-y', 0))
            self.z = _parse_value(form.get('update-z', 0))
            self.value = _parse_value(form.get('update-value', 0))
        elif self.operation == 'query':
            self.x = _parse_value(form.get('query-x1', 0))
            self.y = _parse_value(form.get('query-y1', 0))
            self.z = _parse_value(form.get('query-z1', 0))

            self.x_2 = _parse_value(form.get('query-x2', 0))
            self.y_2 = _parse_value(form.get('query-y2', 0))
            self.z_2 = _parse_value(form.get('query-z2', 0))

    def is_valid(self):
        if self.operation == 'update':
            if not -10**9 <= self.value <= 10**9:
                self._errors.append(u'El valor a actualizar está fuera del rango')
            if not self.x or not self.y or not self.z:
                self._errors.append(u'Verifique que el valor de la coordenada debe ser un nro.')
        elif self.operation == 'query':
            if not self.x or not self.y or not self.z\
                    or not self.x_2 or not self.y_2 or not self.z_2:
                self._errors.append(u'Verifique que el valor de la coordenada debe ser un nro.')
        else:
            self._errors.append(u'seleccione un tipo de operación válida')

        print self._errors

        return 0 == len(self._errors)

    def get_errors(self):
        return self._errors
