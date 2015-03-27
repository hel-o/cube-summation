# coding=utf-8
from flask import Blueprint, render_template, request


from .forms import ConfigCubeForm


cube_views = Blueprint('cube_views', __name__)


@cube_views.route('/', methods=['GET', 'POST'])
def home():
    error_message = None
    # lazy validation:
    if request.method == 'POST':
        try:
            test_cases = int(request.form.get('test-cases', 0))
        except ValueError:
            test_cases = 0
        if 1 <= test_cases <= 50:
            return render_template('cube-summation/config-cube.html', test_cases=test_cases)
        else:
            error_message = u'Nro. inválido, debe estar entre 1 y 50'

    return render_template('cube-summation/home.html', error_message=error_message)


@cube_views.route('/config-cube', methods=['POST'])
def config_cube():
    data = request.form
    form = ConfigCubeForm(data)
    if form.is_valid():
        return render_template(
            'cube-summation/do-operations.html',
            matrix_size=form.matrix_size,
            operations=form.operations
        )
    else:
        return render_template(
            'cube-summation/config-cube.html',
            errors=form.get_errors()
        )


@cube_views.route('/do-operation', methods=['POST'])
def do_operation():
    pass