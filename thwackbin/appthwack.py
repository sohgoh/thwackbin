"""
    thwackbin.appthwack
    ~~~~~~~~~~~~~~~~~~~

    Contains the /api blueprint handling all the routes.
"""
__author__ = 'Andrew Hawker <andrew@appthwack.com>'


from flask import abort, request, Blueprint, send_from_directory, current_app, redirect
from thwackbin import mocks, utils


api = Blueprint('api', __name__, url_prefix='/api')

#Super secret!
API_KEY = 'DTOZZNWeCNWFWtuqqJEm14nnonVJMDXA9flmdvzg'


@api.before_request
def authorize():
    """
    Authorize the client API KEY which comes in as basic auth username.
    """
    auth = request.authorization
    if not auth or not auth.username == API_KEY:
        return abort(401)


@api.route('/project')
def project():
    """
    Returns JSON response containing mock project data.
    """
    return utils.jsonify(mocks.project())


@api.route('/project', methods=['POST'])
def new_project():
    """
    Returns JSON response containing mock response to creating
    an AppThwack project.
    """
    name = request.form.get('name')
    project_type = request.form.get('type')
    if not all((name, project_type)):
        abort(400)
    return utils.jsonify(mocks.new_project())


@api.route('/devicepool/<int:project_id>')
def devicepool(project_id):
    """
    Returns JSON response containing mock devicepool data.
    """
    return utils.jsonify(mocks.devicepool())


@api.route('/device')
def devices():
    """
    Returns JSON response containing mock list of devices.
    """
    return utils.jsonify(mocks.devices())


@api.route('/file', methods=['POST'])
def upload_file():
    """
    Returns JSON response containing mock file upload data.
    Validates:
        Form Data:
            - file: (file) File being uploaded is .apk or .ipa.
            - name: (string) File name used by AppThwack.
    """
    f = request.files.get('file')
    if not f or not utils.valid_ext(f.filename):
        abort(400)
    name = request.form.get('name')
    if not name:
        abort(400)
    return utils.jsonify(mocks.file_id())


@api.route('/run', methods=['POST'])
def schedule_run():
    """
    Returns JSON response containing mock run data.
    Validates:
        Form Data:
            - project: (int) project id which we're running
            - name: (string) name of run
            - app: (int) file_id returned from /file upload
    """
    project = request.form.get('project')
    name = request.form.get('name')
    app = request.form.get('app')
    if not all((project, name, app)):
        abort(400)
    return utils.jsonify(mocks.run_id())


@api.route('/run/<int:project_id>/<int:run_id>/cancel', methods=['PUT'])
def cancel_run(project_id, run_id):
    """
    Returns JSON response containing mock cancellation result.
    """
    return utils.jsonify(mocks.cancellation())


@api.route('/run/<int:project_id>/<int:run_id>', methods=['PUT'])
def publish_run(project_id, run_id):
    """
    Return JSON response containing mock publish data.
    """
    state = request.args.get('public')
    if not state:
        abort(400)
    return utils.jsonify(mocks.publish())


@api.route('/run/<int:project_id>/<int:run_id>')
def results(project_id, run_id):
    """
    Returns JSON response containing mock run results.
    Supports:
        - ?format=archive: Download generic results archive.
    """
    fmt = request.args.get('format')
    if fmt and fmt == 'archive':
        directory = current_app.config['DOWNLOAD_FOLDER']
        return send_from_directory(directory, 'results.zip')
    return utils.jsonify(mocks.results())


@api.route('/run/<int:project_id>/<int:run_id>/status')
def results_status(project_id, run_id):
    """
    Returns JSON response containing mock run status.
    """
    results = mocks.results()
    status = results['summary']['status']
    return utils.jsonify(dict(status=status))


@api.route('/run/<int:project_id>/<int:run_id>/summary')
def results_summary(project_id, run_id):
    """
    Returns JSON response containing mock run status.
    """
    results = mocks.results()
    summary = results['summary']
    return utils.jsonify(summary)


@api.route('/run/<int:project_id>')
def runs(project_id):
    """
    Returns JSON response containing mock list of all runs of a project.
    """
    return utils.jsonify(mocks.runs())


@api.route('/run/compatibility')
def compatibility():
    """
    Returns JSON response containing mock compatibility information
    regarding a test upload and device pool.
    """
    return utils.jsonify(mocks.compatibility())
