# coding=utf-8
import unittest

from app import app


class TestWebApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')

        assert 200 == response.status_code
        assert b'Nro. de casos de prueba' in response.data

    def test_home_set_test_cases(self):
        response = self.client.post('/', data={
            'test-cases': 3
        }, follow_redirects=True)

        assert b'Prueba Nro. 1 de 3' in response.data
        assert b'Define la matriz(N x N x N)' in response.data
        assert b'Nro. de operaciones' in response.data

    def test_home_bad_set_tests_cases(self):
        response = self.client.post('/', data={
            'test-cases': 0
        }, follow_redirects=True)
        assert b'Nro. inválido, debe estar entre 1 y 50' in response.data

        response = self.client.post('/', data={
            'test-cases': ''
        }, follow_redirects=True)
        assert b'Nro. inválido, debe estar entre 1 y 50' in response.data

    def test_config_cube(self):
        response = self.client.post('/config-cube', data={
            'matrix-size': 4,
            'operations': 2
        })

        assert b'Matrix de 4x4x4' in response.data
        assert b'Operaci&oacute;n nro. 1 de 2' in response.data

    def test_bad_config_cube(self):
        response = self.client.post('/config-cube', data={
            'matrix-size': 0
        })

        assert b'El tamaño de la matriz debe estar entre 1 y 100' in response.data
        assert b'El nro. de operaciones debe estar entre 1 y 1000' in response.data


if __name__ == '__main__':
    unittest.main()