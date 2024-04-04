#Einleitung
Auf diesem Dokument stehen Informationen zu Metadaten und Security Levels in hyBit. Ab jetzt werden alle Projektpartner Zugang zum Server bekommen und es ist wichtig, neue Datensätze direkt mit dem entsprechenden Metadaten und mit dem richtigen Security Level Information hochzuladen.
Mehr Informationen über den Serven auf dem Dokument "ServerEinrichtung.pdf".

Anmerkung: die Informationen und Beispiele hier sind ausschließlich für NextCloud relevant. Es wird in die Zukunft ein Database geben, wo die Datensätze einfliessen sollten, aber weitere Informationen dazu, wenn es soweit ist. 

Bei den Security Levels gibt es Einiges zu berücksichtigen:
 - Metadaten müssen immer offen für alle sein, sogar wenn die entsprechende Datensätze vertraulich sind. Projektpartner, die vertrauliche Daten haben oder bekommen, sind dafür verantwortlich, diese Metadaten für all bereitzustellen.
 - Security Levels sind in NextCloud keine vorliegende Struktur, sondern müssen bei jeder Hochladung berücksichtigen werden. Das heißt: Wenn eine Datei im hyBit Ordner (oder entsprechenden Cluster Ordner) hochgeladen wird, ist sie automatisch für das ganze Konsortium zugänglich. Wenn es nicht der Fall sein sollte, muss die Datei nicht im hyBit Ordner, sondern im persönlichen Ordner hochgeladen werden und extra Zugang zu entsprechenden Partner gegeben werden. Dabei kann man bei NextCloud auswählen, welcher Art von Zugang man geben möchte (lesen, schreiben bzw. aktualisieren, herunterladen, teilen, etc.). Auf dieser Art und Weise können auch Stakeholder, die Projektpartner sind, auch Zugang zum Server bekommen und sie selbst ihre Datensätze hochladen und entsprechende Zugänge definieren und geben.
 - Wenn es Datensätzen im hyBit Ordner auf dem Server liegen, wo keine Security Level Informationen vorhanden sind, darf man automatisch davon ausgehen, dass sie Level 0 sind, und damit kompett offen.
 
 Bei Fragen zum allgemeinen Server Zugang und Einrichtung, kann man sich bei unserem IT Mitarbeiter Bennet Petznik melden. Bei Fragen zu Metadaten und Security Levels, kann man sich bei den Daten Managers melden, die eine Schulung zum Thema bekommen werden:
 Bennet Petznik, bpetznik@uni-bremen.de
 Cluster 1: Olga Masyutina, masyutina@uni-bremen.de
 Cluster 2: Felix Dittmar, felix.dittmar@ict.fraunhofer.de
 Cluster 3: Eike Broda, brd@biba.uni-bremen.de
 Cluster 4: Leander Kimmer, leander.kimmer@ifam.fraunhofer.de
 Cluster 5: Larissa Doré, larissa.dore@wupperinst.org
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
| Daten     | DateTime-Format   | time_format   | str      | Falls abweichend von "%Y-%m-%dT%H:%M:%S" bzw. "%Y-%m-%dT%H:%M:%S.%f"                               |
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

Diese Menge ist sicherlich nicht vollständig. Um einen einheitlichen Standard zu haben, wollen wir diese Liste weiterführen.
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
Die Datei- und Ordnernamen sollen als Präfix das Erstelldatum im Format [ISO 8601](https://xkcd.com/1179/) enthalten. Ausnahmen sind Datei- und Ordnernamen nach Konventionen, wie z.B. ``README.md`` oder Quellcode unter Versionskontrolle.

### Beispiele
YYYY-MM-DD_dateiname.endung  
YYYY-MM-DD_dateiname.endung.hyBit-meta.toml

2024-02-29_myPaper.pdf  
2024-02-29_myPaper.pdf.hyBit-meta.toml

README.md  
README.md.hyBit-meta.toml

root.hyBit-meta.toml

## Generierung der hyBit-meta.toml-Dateien
Die hyBit-meta.toml-Dateien können mittels eines Generators erstellt werden. Hier werden die benötigten und optionalen Attribute abgefragt 
und können von den Nutzer:innen einfach eingetragen werden.

Eine aktuelle Instanz ist unter [hybit-meta.ebroda.de](https://hybit-meta.ebroda.de) verfügbar (perspektivisch [meta.hybit.org](https://meta.hybit.org)).

### Beispiele
Ein Beispiel für eine README.md.hyBit-meta.toml findet sich nachfolgend.

```toml
["README.md"]
owner.name = "Eike Broda"
owner.email = "mail@example.com"
owner.company = "BIBA"
access = "0_public"
title = "hyBit Dateiberechtigungen"
description = "Beschreibung der verschiedenen Zugriffslevel"
cluster = "3"
```

Dateinamen zur Kategorisierung sollen nach Möglichkeit nur einmalig definiert werden, um Fehler bei Änderungen zu vermeiden. Die alternative toml-Definition, z.B. ``["README.md".owner]``, ist auch valide, aber nicht empfohlen.

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
