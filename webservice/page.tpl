{%- macro getField(field, placeholder = '', offset='mb-2 mt-1') %}
{%- if field.type == 'SelectField' or field.type == 'QuerySelectField' %}
{{ field(placeholder=placeholder, class_="form-select " + offset) }}
{%- else %}
{{ field(placeholder=placeholder, class_="form-control " + offset) }}
{%- endif %}
{%- if field.errors %}
<div class="invalid-feedback" style="display: block;">
    {{ field.errors|join('<br />') }}
</div>
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
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="container">
    <div class="row">
        <div class="col-12">
            <br />
            <h2>hyBit Metadaten Generator</h2>
            <br />
        </div>
    </div>
        <form method="post" action="/">
            <div class="row">
        <div class="col-12 col-lg-8">
            <div class="card">
                <div class="card-header">hyBit Metadaten Generator</div>
                <div class="card-body">
                    {{form.csrf_token()}}

                    <div class="row">
                        <div class="col-2"><strong>Besitzer:in</strong></div>
                        <div class="col-5">{{formGroup(form.owner_name)}}</div>
                        <div class="col-5">{{formGroup(form.owner_email)}}</div>
                    </div>
                    <div class="row mt-1">
                        <div class="col-2"><strong>Quelle</strong></div>
                        <div class="col-5">{{formGroup(form.source_name)}}</div>
                        <div class="col-5">{{formGroup(form.source_email)}}</div>
                    </div>
                    <div class="row mt-1">
                        <div class="col-2"><strong>Ansprech-partner:in</strong></div>
                        <div class="col-5">{{formGroup(form.contact_name)}}</div>
                        <div class="col-5">{{formGroup(form.contact_email)}}</div>
                    </div>

                    <div class="row mt-1">
                        <div class="col-2"><strong>Zugriff</strong></div>
                        <div class="col-5">{{formGroup(form.access)}}</div>
                    </div>
                    <br />
                    <strong>Metadaten</strong>
                    <div class="row">
                        <div class="col-6">{{formGroup(form.filename)}}</div>
                        <div class="col-6">{{formGroup(form.title)}}</div>
                    </div>
                    {{formGroup(form.description)}}
                </div>
                <div class="card-footer">
                    <button class="btn btn-primary" name="action" value="show" type="submit">Metadaten {{create_update}}</button>
                </div>
            </div>
            <br />
        </div>

        <div class="col-12 col-lg-4">
            <div class="card">
                <div class="card-header">hyBit Metadaten Generator (optionale Attribute)</div>
                <div class="card-body">
                    <strong>Datenbeschreibung (optional)</strong><br />
                    <i>Felder noch definieren & ergänzen</i>

                </div>
                <div class="card-footer">
                    <button class="btn btn-primary" name="action" value="show" type="submit">Metadaten {{create_update}}</button>
                </div>
            </div>
        </div>
        <br />
            <div class="col-12">
            {% if toml %}

            <div class="card">
                <div class="card-header">Ergebnis</div>
                <div class="card-body"><pre>{{toml}}</pre></div>
                <div class="card-footer"><button class="btn btn-primary" type="submit" name="action" value="download">Download</button></div>
            </div>
            {% endif %}
            </div>
        </div>
    </form>
</div>
</body>
</html>
