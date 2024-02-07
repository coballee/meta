from flask import Blueprint

from webservice.service.meta_creator import MetaFileCreation, StaticHome, MetaRootCreation, MetaFolderCreation

meta_blueprint = Blueprint('meta', __name__)

meta_blueprint.add_url_rule('/', view_func=StaticHome.as_view('home'))
meta_blueprint.add_url_rule('/file', view_func=MetaFileCreation.as_view('file'))
meta_blueprint.add_url_rule('/root', view_func=MetaRootCreation.as_view('root'))
meta_blueprint.add_url_rule('/folder', view_func=MetaFolderCreation.as_view('folder'))
