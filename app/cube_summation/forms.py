# coding=utf-8


class ConfigCubeForm(object):

    matrix_size = 0
    operations = 0
    _errors = None

    def __init__(self, form):
        self._errors = []
        try:
            self.matrix_size = int(form.get('matrix-size', 0))
        except ValueError:
            self.matrix_size = 0

        try:
            self.operations = int(form.get('operations', 0))
        except ValueError:
            self.operations = 0

    def is_valid(self):
        if not 1 <= self.matrix_size <= 100:
            self._errors.append(u'El tamaño de la matriz debe estar entre 1 y 100')

        if not 1 <= self.operations <= 1000:
            self._errors.append(u'El nro. de operaciones debe estar entre 1 y 1000')

        return 0 == len(self._errors)

    def get_errors(self):
        return self._errors


class DoOperationForm(object):
    pass

