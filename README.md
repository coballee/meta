# hyBit Datastructure
Definition von Datei-Struktur und Berechtigungsebenen für die Datenakquise und -nutzung in hyBit

## Basic
Grundsätzlich wird jede Datei als öffentlich (Level 0) betrachtet, außer, es wird ein strengeres Dateilevel durch eine Metadatei definiert.

Die Evaluation erfolgt absteigend und wird spezifischer pro Datei (ebenso in der einzelnen Datei, sofern mehrere Dateien definiert sind):
- Default: Level 0
- root.hyBit-meta.toml
- folder.hyBit-meta.toml
- file.ext.hyBit-meta.toml (definiert für genau 1 Datei die Metadaten)

### Beispiel
Das folgende Beispiel soll die Definition und den Ablauf dieser Dateien anhand eines einfachen Beispiels und den Zugriffsleveln
beispielhaft darstellen. Dazu wird folgende Dateistruktur angenommen, 4 Dateien, teilweise in Unterordnern:
```plain
data/dataset.csv
figures/fig1.png
figures/fig2.png
paper-draft.pdf
```

In den Ordnern werden zudem die folgenden Zugriffslevel für einzelne Dateien und Verzeichnisse definiert.

| Meta-Datei                       | Dateipfad        | Zugriffslevel |
|----------------------------------|------------------|---------------|
| _Default_                        | **               | L0            |
| root.hyBit-meta.toml             | **               | L2            |
| root.hyBit-meta.toml             | figures/         | L1            |
| data/folder.hyBit-meta.toml      | data/**          | L3            | 
| figures/fig1.png.hyBit-meta.toml | figures/fig1.png | L0            |

Basierend auf diesen Metadaten verfügen die Dateien über folgende Berechtigungen:

| Datei            | Zugriffslevel |
|------------------|---------------|
| data/data1.csv   | L3            |
| figures/fig1.png | L0            |
| figures/fig2.png | L1            |
| paper-draft.pdf  | L2            |

## Metadaten
Eine Textdatei (TOML; see example) mit Metadaten ist **unbedingt erforderlich** und für **jede Datei** zu
erstellen (entweder einzeln, oder im sinnvollen Format für alle zusammengehörigen Dateien).
Nur hier wird das Zugriffslevel angegeben.

Die Metadata-Datei muss mindestens die nachfolgenden Felder enthalten. Die Typen Contact und AccessLevel sind unterhalb ([Typen](#typen)) definiert.

| Name                 | Attribut     | Typ             | Beschreibung                                                     |
|----------------------|--------------|-----------------|------------------------------------------------------------------|
| Titel                | title        | str             | Titel des Datensatzes                                            |
| Beschreibung         | description  | str             | Beschreibung der Daten                                           |
| Zugriffslevel        | access-level | AccessLevel/str | Zugriffsberechtigungen für diese Daten                           |
| Besitzer:in          | owner        | Contact         | Wer ist verantwortlich für diese Daten?                          |
| _Quelle_             | source       | Contact         | Herkunft der Daten (sofern nicht angegeben: owner)               |
| _Ansprechpartner:in_ | contact      | Contact         | Ansprechpartner:in für die Daten (sofern nicht angegeben: owner) | 

Weitere optionale Felder, die bisher definiert sind.
Von diesen kann eine beliebige Menge für einzelne Dateien definiert werden. 

| Kategorie | Name              | Attribut      | Typ      | Beschreibung                                                                                          |
|-----------|-------------------|---------------|----------|-------------------------------------------------------------------------------------------------------|
| Daten     | Auflösung         | resolution    | str      | Welche (z.B. zeitliche) Auflösung haben die Daten, ggf. inkl Einheit?                                 |
| Daten     | Einheit           | unit          | str      | Welche Einheit haben die Daten? (z.B. kWh, Sekunden, ...)                                             |
| Daten     | Aufnahmezeitpunkt | snapshot_time | datetime | In welchem Moment wurden die Daten aufgenommen/exportiert?                                            |
| Daten     | Beginn            | time_begin    | datetime | Beginn des Zeitraums der Daten                                                                        |
| Daten     | Ende              | time_end      | datetime | Ende des Zeitraums der Daten                                                                          |
| Daten     | Zeitzone          | timezone      | str      | Zeitzone, sofern relevant (gilt für alle Zeitwerte)                                                   |
| Daten     | DateTime-Format   | time_format   | str      | Falls abweichend von "%Y-%m-%dT%H:%M:%S.%f" bzw. "%Y-%m-%dT%H:%M:%S.%f"                               |
| Daten     | Vorbereitung      | preprocessing | str      | Beschreibung, welche Aktionen auf den Daten ausgeführt wurden                                         |
| Daten     | Rohdaten          | raw_data      | Path/str | Link auf die Originaldaten, sofern diese hier zusammengefasst/bearbeitet sind                         |
| Technisch | Speicherort       | location      | str      | Bei Level L4 sollte hier ein Hinweis sein, wo die Daten liegen (z.B. Dateipfad / interner Serverlink) |
| Technisch | Format            | format        | str      | In welchem Dateiformat sind die Daten?                                                                |
| Technisch | Encoding          | encoding      | str      | Standard: UTF-8, falls abweichend entsprechend angeben.                                               | 
| Referenz  | Referenz          | reference     | str      | Verweis auf eine Publikation, die zu diesen Daten gehört                                              |
| Referenz  | DOI               | doi           | str      | DOI, sofern vorhanden                                                                                 |
| Referenz  | URL               | url           | str      | URL auf eine Webseite mit den Daten bzw. mehr Informationen dazu                                      |
| Referenz  | Repository        | repository    | str      | Verweis auf ein Repository, z.B. Git, welches die Daten oder Material dazu enthält                    |
| Referenz  | Lizenz            | licence       | str      | Lizenz, unter der die Daten genutzt werden können (z.B. GPL, CC-BY-ND 4.0, ...)                       | 

Diese Menge ist sicherlich nicht vollständig. Um einen einheitlichen Standard zu haben, wollen wir diese Liste weiter führen.
Dazu bitte für zusätzliche Felder bitte einen [Issue hier im Repository](https://github.com/hyBit-project/meta/issues) erstellen.

### Typen
Nachfolgend sind zwei oben verwendete Datentypen näher beschrieben.
Ansonsten sind alle Werte als String ausgeführt ohne spezifisches Format. 
Die Annahme des Datumsformats für Datetime ist `%Y-%m-%dT%H:%M:%S.%f` bzw. `%Y-%m-%dT%H:%M:%S`
(in Anlehnung an [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) und [datetime.isoformat()](https://docs.python.org/3/library/datetime.html#datetime.datetime.isoformat)).

#### Contact

| Name          | Attribut | Typ | Beschreibung                               |
|---------------|----------|-----|--------------------------------------------|
| Name          | name     | str | Name der Person                            |
| E-mail        | mail     | str | E-Mail-Adresse der Person                  |
| _Telefon_     | phone    | str | Telefonnummer der Person (optional)        |
| _Unternehmen_ | company  | str | Unternehmen/Institut der Person (optional) |

#### AccessLevel
Es sind fünf AccessLevel definiert. Diese sind in der folgenden Tabelle aufgelistet.
Ebenso die String-Konstanten, die für die Datenlevel genutzt werden sollen.

| Level | Konstante     | Titel                              | Erläuterung                                                                                                                                                               |
|-------|---------------|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| L0    | 0_public      | Vollständig offen & bereits publik | Referenz zu Daten bereits vorhanden und zu nutzen                                                                                                                         |
| L1    | 1_open        | Vollständig offen                  | Publizierbar, jedoch (noch) keine Referenz vorhanden; Wechsel zu L0, wenn Referenz vorhanden                                                                              | 
| L2    | 2_internal    | Projektintern offen                | Keine Restriktionen innerhalb des Konsortiums; aber Veröffentlichung oder Weitergabe an Dritte nur nach Rücksprache!                                                      | 
| L3    | 3_conditional | Konditionell offen                 | Konditionen + Datenverantwortlichkeit (Partner, Mitarbeiter:innen) sind in Metadaten aufzuführen. Bei gruppenbezogenen Konditionen werden Rechte von Systemadmin vergeben | 
| L4    | 4_closed      | Geschlossen                        | dürfen **NICHT** (auch nicht in geschützten Bereichen) auf dem Server hochgeladen werden; nur Metadaten-Info auf Server                                                   |

## Generelle Anmerkungen
1. Sämtliche Berechtigungen beziehen sich auf Lese-Rechte.
   Berechtigungen nach Manipulation der Datensätze ist mit den Daten-Eignern abzustimmen
2. Datensätze **ohne** Levelangabe gelten als **L0**.

## Festlegen der Ordner – und Dateibenennung (bindend!)
YYYY_MM_DD_dateiname.endung  
YYYY_MM_DD_dateiname.endung.hyBit-meta.toml

## Generierung der hyBit-meta.toml-Dateien
Die hyBit-meta.toml-Dateien können mittels eines Generators erstellt werden. Hier werden die benötigten und optionalen Attribute abgefragt 
und können von den Nutzer:innen einfach eingetragen werden.

Eine aktuelle Instanz ist unter [hybit-meta.ebroda.de](https://hybit-meta.ebroda.de) verfügbar (perspektivisch [meta.hybit.org](https://meta.hybit.org)).

Ein Beispiel für eine hyBit-meta.toml findet sich nachfolgend.
```toml
...
t.b.a.
```

## Offene Punkte
Wie mehrere Dateien handlen?

No `..`s allowed in the path.

```toml
# This is my proposal on how to handle complex cases: allow optional
# tables for each file, specified with a relative path, to override
# metadata items on a per file basis. The path will be interpreted as
# being rooted at the directory, to which the metadata file applies. No
# `..`s allowed in the path.
["foo/bar/file.one"]
owner.name = "Foo Bar"
owner.contact = "foo@bar.foobar"
format.name = "The hilarious foobar format."

# Last but not least: maybe we want to allow people to specify directory
# metadata with a `.hyBit-metadata.toml` file inside the directory? This
# would lead to less clutter and the file can be versioned, if the
# directory contains a Git repository.
```

Darstellung in hyBit Datenspeicher (NextCloud?)  
-> z.B. basierend auf MetaData-Plugin (https://github.com/gino0631/nextcloud-metadata/)