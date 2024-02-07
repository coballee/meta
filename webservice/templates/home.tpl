{% extends "_layout.tpl" %}

{% block body %}
<div class="p-5 text-center bg-body-tertiary rounded-3">
    <h1 class="text-body-emphasis">hyBit Metadaten Generator</h1>
    <p class="col-lg-8 mx-auto fs-5 text-muted">
        Dieses Tool unterstützt bei der Erstellung der verschiedenen Metadateien für hyBit-Projektdateien.
    </p>
    <div class="d-inline-flex gap-2">
        <a href="https://gitlab.ips.biba.uni-bremen.de/hyBit/meta-datarights#hybit-datastructure" class="d-inline-flex align-items-center btn btn-primary btn-lg px-4 rounded-pill" type="button">
            Format-Beschreibung (GitHub)
        </a>
    </div>
</div>
<div class="row">
    <div class="col-12">
        <br />
    </div>
    <div class="col-12 col-md-4">
        <div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative p-3">
            <h3>Root</h3>
            <p class="card-text">Hier werden die grundsätzlichen Informationen über die Dateistruktur abgelegt. Diese Datei stellt die Basis für alle (ungeordneten) Dateien und Ordner.</p>
            <a href="{{url_for('meta.root')}}" class="btn btn-outline-secondary stretched-link">
Metadatei erstellen
            </a>
        </div>
    </div>

    <div class="col-12 col-md-4  h-100">
        <div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative p-3">
            <h3>Ordner</h3>
            <p class="card-text">Zusätzlich können auf Ordnerlevel noch abweichende Berechtigungen definiert werden, auch für mehrere Dateien.</p>
            <a href="{{url_for('meta.folder')}}" class="btn btn-outline-secondary stretched-link">
                Metadatei erstellen
            </a>
        </div>
    </div>

    <div class="col-12 col-md-4">
        <div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative p-3">
            <h3>Datei</h3>
            <p class="card-text">Zudem ist die Definition der Informationen auch spezifisch für eine einzelne Datei möglich.<br /><br /> </p>
            <a href="{{url_for('meta.file')}}" class="btn btn-outline-secondary stretched-link">
                Metadatei erstellen
            </a>
        </div>
    </div>
</div>

{% endblock %}
