from application.views import *

blueprint = Blueprint('general', __name__)

@blueprint.route('/')
def index():
    return render_template('general/index.html')
