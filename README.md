# hyBit Datastructure
Definition von Datei-Struktur und Berechtigungsebenen für die Datenakquise und -nutzung in hyBit

## Basic
Grundsätzlich wird jede Datei als öffentlich (Level 0) betrachtet, es seie denn, es wird ein strengeres Dateilevel
durch eine Metadatei definiert.

## Metadaten
Eine Textdatei (TOML; see example) mit Metadaten ist **unbedingt erforderlich** und für **jede Datei** zu
erstellen (entweder einzeln, oder im sinnvollen Format für alle zusammengehörigen Dateien).
Nur hier können/dürfen die Datenlevel angegeben werden.

Die Metadata-Datei muss mindestens die folgenden Felder enthalten (see example):
- Titel [title]
- Besitzer:in [owner]
- Access-Level (siehe unten) [access-level]
- Beschreibung

Zusätzlich werden automatisch aus der Besitzer:in abgeleitet:
- Quelle [source] (optional; if not specified: same as owner)
- Ansprechpartner:in [contact] (optional; if not specified: same as owner)

Weitere optionale Felder (Beispiele)
- Datenformat [format]
- Bearbeitung [how-processed] (was data cleaned or processed otherwise?)
- Beschreibung [description]
- Startdatum [start] (bei Zeitreihen)
- Enddatum [end] (bei Zeitreihen)
- Auflösung [resolution] (bei Zeitreihen)
- Lizenz (sowas wie GPL, CC-BY-ND 4.0 usw.)

## Generelle Anmerkungen
1. Sämtliche Berechtigungen beziehen sich auf Lese-Rechte.
   Berechtigungen nach Manipulation der Datensätze ist mit den Daten-Eignern abzustimmen
2. Datensätze **ohne** Levelangabe gelten als **L0** (siehe unten)

## Festlegen der Ordner – und Dateibenennung (bindend!)
YYYY-MM-DD.beispielhafter-dateiname.endung  
YYYY-MM-DD.beispielhafter-dateiname.endung.metadata.toml

YYYY-MM-DD_beispielhafter-dateiname.endung  
YYYY-MM-DD_beispielhafter-dateiname.endung.metadata.toml

YYYY_MM_DD_beispielhafter-dateiname.endung  
YYYY_MM_DD_beispielhafter-dateiname.endung.metadata.toml

## Offene Punkte
Wie mehrere Dateien handlen?

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

## Acess-Level
| Level | L0 | L1 | L2 | L3 | L4 |
| ----- | -- | -- | -- | -- | -- |
| Titel | Vollständig offen &  bereits publik | Vollständig offen |  Projektintern offen |  Konditionell offen | Geschlossen |
| Erläuterung | Referenz zu   Daten bereits  vorhanden   und zu   nutzen |  Publizierbar, jedoch (noch)  keine   Referenz  vorhanden;  Wechsel zuL0, wenn Referenz vorhanden | Keine Restriktionen  innerhalb des  Konsortiums;  aber Rücksprache vor Veröffentlichung oder Weitergabe an Dritte |Konditionen +    Datenverantwortlichkeit  (Partner,    Mitarbeiter:innen) sind    in Metadaten  aufzuführen   Bei gruppenbezogenen   Konditionen werden  Rechte von   Systemadmin vergeben | dürfen   NICHT (auch   nicht in   geschützten   Bereichen)   auf dem   Server   hochgeladen   werden   Metadaten-   Info auf   Server| 