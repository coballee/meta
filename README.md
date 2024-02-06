# hyBit Datastructure
Definition von Datei-Struktur und Berechtigungsebenen für die Datenakquise und -nutzung in hyBit

## Metadaten
Eine Textdatei (TOML; see example) mit Metadaten ist **unbedingt erforderlich** und für **jede Datei** zu
erstellen (entweder einzeln, oder im sinnvollen Format für alle zusammengehörigen Dateien).
Nur hier können/dürfen die Datenlevel angegeben werden.

Die Metadata-Datei muss mindestens die folgenden Felder enthalten (see example):
- Titel [title]
- Besitzer:in [owner]
- Quelle [source] (optional; if not specified: same as owner)
- Ansprechpartner:in [contact] (optional; if not specified: same as owner)
- Access-Level (siehe unten) [access-level]
- Datenformat [format]

Weitere optionale Felder (Beispiele)
- Bearbeitung [how-processed] (was data cleaned or processed otherwise?)
- Beschreibung [description]
- Startdatum [start] (bei Zeitreihen)
- Enddatum [end] (bei Zeitreihen)
- Auflösung [resolution] (bei Zeitreihen)

## Generelle Anmerkungen
1. Sämtliche Berechtigungen beziehen sich auf Lese-Rechte.
   Berechtigungen nach Manipulation der Datensätze ist mit den Daten-Eignern abzustimmen
2. Datensätze **ohne** Levelangabe gelten als **L0** (siehe unten)

## Festlegen der Ordner – und Dateibenennung (bindend!)
YYYY-MM-DD.beispielhafter-dateiname.endung  
YYYY-MM-DD.beispielhafter-dateiname.metadata.toml

## Acess-Level
| Level | L0 | L1 | L2 | L3 | L4 |
| ----- | -- | -- | -- | -- | -- |
| Titel | Vollständig offen &  bereits publik | Vollständig offen |  Projektintern offen |  Konditionell offen | Geschlossen |
| Erläuterung | Referenz zu   Daten bereits  vorhanden   und zu   nutzen |  Publizierbar, jedoch (noch)  keine   Referenz  vorhanden;  Wechsel zuL0, wenn Referenz vorhanden | Keine Restriktionen  innerhalb des  Konsortiums;  aber Rücksprache vor Veröffentlichung oder Weitergabe an Dritte |Konditionen +    Datenverantwortlichkeit  (Partner,    Mitarbeiter:innen) sind    in Metadaten  aufzuführen   Bei gruppenbezogenen   Konditionen werden  Rechte von   Systemadmin vergeben | dürfen   NICHT (auch   nicht in   geschützten   Bereichen)   auf dem   Server   hochgeladen   werden   Metadaten-   Info auf   Server| 