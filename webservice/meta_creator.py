from tempfile import NamedTemporaryFile

from flask import Flask, render_template, request, send_file
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
import toml
from wtforms.validators import InputRequired

app = Flask(__name__, template_folder='.')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'avneiobneroibrneropibo2hz0892hv0eravbo'
app.debug = True


class MetaForm(FlaskForm):
    owner_name = StringField("Name*", validators=[InputRequired()])
    owner_email = StringField("E-Mail*", validators=[InputRequired()])

    source_name = StringField("Name")
    source_email = StringField("E-Mail")

    contact_name = StringField("Name")
    contact_email = StringField("E-Mail")

    filename = StringField("Dateiname")
    title = StringField("Titel*", validators=[InputRequired()])
    access = SelectField("Zugriffsberechtigung*", choices=(('0_public', '0 - öffentlich'), ('1_open', '1 - vollständig offen'), ('2_internal', '2 - Projektintern offen'), ('3_conditional', '3 - Konditionell offen'), ('4_closed', '4 - geschlossen')), default='4_closed')
    description = TextAreaField("Beschreibung")

    format = TextAreaField("Datenformat")

    def get_toml_dict(self):
        dict = {
            'owner': {
                'name': self.owner_name.data,
                'contact': self.owner_email.data
            },
            'meta': {
                'access': self.access.data,
                'title': self.title.data,
                'description': self.description.data,
            }
        }

        if self.source_email.data or self.source_name.data:
            dict['source'] = {'name': self.source_name.data, 'email': self.source_email.data}

        if self.contact_email.data or self.contact_name.data:
            dict['contact'] = {'name': self.contact_name.data, 'email': self.contact_email.data}

        return dict

    def get_filename(self):
        return self.filename.data


@app.route('/', methods=['GET', 'POST'])
def create_meta():
    form = MetaForm()

    toml_str = None
    create_update = 'erstellen'
    if form.validate_on_submit():
        create_update = 'bearbeiten'

        toml_dict = form.get_toml_dict()
        toml_str = toml.dumps(toml_dict)

        if request.form['action'] == 'download':
            with NamedTemporaryFile() as tmp:
                toml_str = '# hyBit Metadata; see meta.hybit.org for more information about format\n# File created by hyBit Metadata Creator\n\n' + toml_str
                with open(tmp.name, 'w') as f:
                    f.write(toml_str)

                filename = form.get_filename()

                if filename is None and len(filename) == 0:
                    filename = ''
                return send_file(tmp.name, download_name=filename + '.metadata.toml', as_attachment=True)

    return render_template('page.tpl', form=form, create_update=create_update, toml=toml_str)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2345, debug=True)
