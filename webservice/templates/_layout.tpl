{%- macro getField(field, placeholder = '', offset='mb-2 mt-1') %}
{%- if field.type == 'SelectField' or field.type == 'QuerySelectField' %}
{{ field(placeholder=placeholder, class_="form-select " + offset) }}
{%- else %}
{{ field(placeholder=placeholder, class_="form-control " + offset) }}
{%- endif %}
{%- if field.errors %}
<div class="invalid-feedback" style="display: block;">{{ field.errors|join('<br />') }}</div>
{%- endif %}
{%- endmacro %}
{%- macro formGroup(field, placeholder='', required=False) %}
<div class="form-group">
    {{field.label}}
    {{ getField(field, placeholder, '' if append else 'mb-2 mt-1' ) }}
</div>
{%- endmacro %}

<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>hyBit Metadaten Generator</title>
    <link href="{{ url_for('static', filename='bootstrap.min.css') }}" type="text/css" rel="stylesheet"/>
    <link href="{{ url_for('static', filename='style.css') }}" type="text/css" rel="stylesheet"/>
</head>
<body>
<div class="container-fluid" style="max-width: 1500px;">
    <div class="row">
        <div class="col-12">
            <br />
            <div class="btn-group float-end">
                <a href="{{url_for('meta.root')}}" class="btn btn-{% if g.type == 'root' %}success{% else %}secondary{% endif %}">Root</a>
                <a href="{{url_for('meta.folder')}}" class="btn btn-{% if g.type == 'folder' %}success{% else %}secondary{% endif %}">Ordner</a>
                <a href="{{url_for('meta.file')}}" class="btn btn-{% if g.type == 'file' %}success{% else %}secondary{% endif %}">Datei</a>
            </div>
            <h2><a href="{{url_for('meta.home')}}">hyBit Metadaten Generator</a></h2>
            <br />
        </div>
    </div>

    {% block body %}{% endblock %}
    <br /><br />
</div>
<br /><br />
<footer class="bg-body border-top fixed-bottom-lg py-3 text-center">&copy; hyBit, 2024</footer>
</body>
</html>


