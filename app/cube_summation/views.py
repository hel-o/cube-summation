# coding=utf-8
from flask import Blueprint, render_template, request, session


from .forms import ConfigCubeForm, DoOperationForm
from .matrix3d import Cube


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
    form = ConfigCubeForm(request.form)
    if form.is_valid():
        # da error, TODO fix --> para tener un objeto en memoria:
        # session['cube'] = Cube(form.matrix_size)
        session['matrix-size'] = form.matrix_size
        session['n-operations'] = form.operations
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
    form = DoOperationForm(request.form)
    result = 0
    if form.is_valid():
        session['n-operations'] = int(session['n-operations']) - 1
        # esto da error, lo dejo, problemas para tener un objeto en memoria
        # cube = session['cube']
        if form.operation == 'update':
            # result = cube.update(form.x, form.y, form.z, form.value)
            result = form.value
        else:
            # result = cube.query(f{% endblock %}orm.x, form.y, form.z, form.x_2, form.y_2, form.z_2)
            result = form.value
    return render_template(
        'cube-summation/do-operations.html',
        matrix_size=session['matrix-size'],
        operations=session['n-operations'],
        operation_name=form.operation,
        operation_result=result,
        form_axis=form,
        errors=form.get_errors()
    )