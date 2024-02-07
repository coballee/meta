{% extends "_layout.tpl" %}

{% block body %}
<form method="post" action="{{url_for('meta.file')}}">
    <div class="row">
        {{form.csrf_token()}}
        <div class="col-12 col-lg-6 offset-lg-3">
            <div class="card">
                <div class="card-header">Berechtigungen festlegen für Datei</div>
                <div class="card-body">
                    {{formGroup(form.filename)}}
                    <div class="form-text">Dateiname inkl. Dateiendung, z.B. hyBit.png</div>
                </div>
            </div>
            <br />
        </div>
        <div class="col-12 col-lg-6">
            <div class="card">
                <div class="card-header">Notwendige Attribute (sofern nicht in folder/root-Datei definiert)</div>
                <div class="card-body">
                    <div class="row">
                        <div class="col-5">{{formGroup(form.access)}}</div>
                    </div>
                    <hr />
                    {{formGroup(form.title)}}
                    {{formGroup(form.description)}}
                    <hr/>
                    <strong>Besitzer:in</strong>
                    <div class="row mt-1">

                        <div class="col-6">{{formGroup(form.owner_name)}}</div>
                        <div class="col-6">{{formGroup(form.owner_company)}}</div>
                        <div class="col-6">{{formGroup(form.owner_email)}}</div>
                        <div class="col-6">{{formGroup(form.owner_phone)}}</div>
                    </div>
                    <div class="form-text">Die Angaben "Name", "E-Mail", "Telefon" und "Unternehmen" werden für die folgenden Attribute übernommen, sofern sie im Folgenden nicht eingetragen werden.</div>
                    <br />

                    <strong>Quelle</strong>
                    <div class="row mt-1">
                        <div class="col-6">{{formGroup(form.source_name)}}</div>
                        <div class="col-6">{{formGroup(form.source_company)}}</div>
                        <div class="col-6">{{formGroup(form.source_email)}}</div>
                        <div class="col-6">{{formGroup(form.source_phone)}}</div>
                    </div>
                    <br />

                    <strong>Ansprechpartner:in</strong>
                    <div class="row mt-1">
                        <div class="col-6">{{formGroup(form.contact_name)}}</div>
                        <div class="col-6">{{formGroup(form.contact_company)}}</div>
                        <div class="col-6">{{formGroup(form.contact_email)}}</div>
                        <div class="col-6">{{formGroup(form.contact_phone)}}</div>
                    </div>
                    <div class="row">
                        <hr />
                        <div class="col-5">{{formGroup(form.hybit_cluster)}}</div>
                        <div class="form-text">Die Nummer des hyBit Clusters (1, 2, 3, 4, 5, Q1) oder eine komma-getrennte Liste, z.B. 1, 2.</div>
                    </div>

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
        {% if toml %}
        <div class="col-12">
            <div class="card">
                <div class="card-header">Ergebnis</div>
                <div class="card-body"><pre>{{toml}}</pre></div>
                <div class="card-footer"><button class="btn btn-primary" type="submit" name="action" value="download">Download</button></div>
            </div>
        </div>
        {% endif %}
    </div>
</form>
{% endblock %}
