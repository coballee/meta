from tempfile import NamedTemporaryFile

from flask import render_template, request, send_file, g
from flask.views import MethodView
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
import toml

from webservice.service.hybit_encoder import hyBitMetaEncoder


class MetaForm(FlaskForm):
    owner_name = StringField("Name*")
    owner_email = StringField("E-Mail*")
    owner_phone = StringField("Telefon")
    owner_company = StringField("Unternehmen/Institut/AG")

    source_name = StringField("Name")
    source_email = StringField("E-Mail")
    source_phone = StringField("Telefon")
    source_company = StringField("Unternehmen/Institut/AG")

    contact_name = StringField("Name")
    contact_email = StringField("E-Mail")
    contact_phone = StringField("Telefon")
    contact_company = StringField("Unternehmen/Institut/AG")

    filename = StringField("Dateiname")
    title = StringField("Titel*")
    access = SelectField("Zugriffsberechtigung*", choices=((None, 'wie definiert in root/folder/L0'), ('0_public', '0 - öffentlich'), ('1_open', '1 - vollständig offen'), ('2_internal', '2 - Projektintern offen'), ('3_conditional', '3 - Konditionell offen'), ('4_closed', '4 - geschlossen')), default='4_closed')
    description = TextAreaField("Beschreibung")
    hybit_cluster = StringField("hyBit Cluster")

    format = TextAreaField("Datenformat")

    def check_value(self, data, v_key, d_key):
        if v_key in self.data and self.data.get(v_key) is not None and len(self.data.get(v_key)) > 0:
            data[d_key] = self.data.get(v_key)

    def get_toml_dict(self):
        owner = {}
        contact = {}
        source = {}

        self.check_value(owner, self.owner_name.id, 'name')
        self.check_value(owner, self.owner_email.id, 'email')
        self.check_value(owner, self.owner_phone.id, 'phone')
        self.check_value(owner, self.owner_company.id, 'company')

        self.check_value(contact, self.contact_name.id, 'name')
        self.check_value(contact, self.contact_email.id, 'email')
        self.check_value(contact, self.contact_phone.id, 'phone')
        self.check_value(contact, self.contact_company.id, 'company')
    
        self.check_value(source, self.source_name.id, 'name')
        self.check_value(source, self.source_email.id, 'email')
        self.check_value(source, self.source_phone.id, 'phone')
        self.check_value(source, self.source_company.id, 'company')

        result_dict = {}

        if len(owner) > 0:
            result_dict['owner'] = owner
        if len(contact) > 0:
            result_dict['contact'] = contact
        if len(source) > 0:
            result_dict['source'] = source

        self.check_value(result_dict, self.access.id, 'access')
        if result_dict['access'] == 'None' or result_dict['access'] is 'None':
            del result_dict['access']

        self.check_value(result_dict, self.title.id, 'title')
        self.check_value(result_dict, self.description.id, 'description')
        self.check_value(result_dict, self.hybit_cluster.id, 'cluster')

        return {self.get_filename(): result_dict}

    def get_filename(self):
        return self.filename.data


class StaticHome(MethodView):
    def get(self):
        g.type = ''
        return render_template('home.tpl')


class BaseMetaFileView(MethodView):

    @staticmethod
    def download_toml_file(filename, toml_str):
        with NamedTemporaryFile() as tmp:
            toml_str = '# hyBit Metadata; see meta.hybit.org (hybit-meta.ebroda.de)\n\n' + toml_str
            with open(tmp.name, 'w') as f:
                f.write(toml_str)

            if filename is None:
                filename = ''
            return send_file(tmp.name, download_name=filename + '.metadata.toml', as_attachment=True)

    @staticmethod
    def get_toml_string(form):
        return toml.dumps(form.get_toml_dict(), encoder=hyBitMetaEncoder())


class MetaFileCreation(BaseMetaFileView):

    def get(self, form=None):
        if form is None:
            form = MetaForm()

        g.type = 'file'
        return render_template('file.tpl', form=form, create_update='erstellen', toml=None)

    def post(self):
        form = MetaForm()

        if form.validate_on_submit():
            toml_str = self.get_toml_string(form)

            if request.form['action'] == 'download':
                filename = form.get_filename()
                return self.download_toml_file(filename, toml_str)

            g.type = 'file'
            return render_template('file.tpl', form=form, create_update='bearbeiten', toml=toml_str)

        return self.get(form)

class MetaFolderCreation(BaseMetaFileView):

    def get(self, form=None):
        if form is None:
            form = MetaForm()

        g.type = 'folder'
        return render_template('folder.tpl', form=form, create_update='erstellen', toml=None)



class MetaRootCreation(BaseMetaFileView):

    def get(self, form=None):
        if form is None:
            form = MetaForm()

        g.type = 'root'
        return render_template('root.tpl', form=form, create_update='erstellen', toml=None)

    def post(self):
        form = MetaForm()

        if form.validate_on_submit():
            toml_str = self.get_toml_string(form)

            if request.form['action'] == 'download':
                filename = form.get_filename()
                return self.download_toml_file(filename, toml_str)

            g.type = 'file'
            return render_template('file.tpl', form=form, create_update='bearbeiten', toml=toml_str)

        return self.get(form)
