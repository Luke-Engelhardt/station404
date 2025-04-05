### Spiel: Verlassene Raumstation

#### Abgabe: 07.04.2025

- Konsolenbasiertes Spiel in Python
- Dokumentation mit Spiellogik und Metriken

#### Spielablauf

##### Spielfeld

Das Spielbrett stellt verschiedene Bereiche einer verlassenen Raumstation dar, auf
denen sich versteckte Gefahren befinden, z.B. mechanische Fallen.
##### Aufdecken

Jeder Zug besteht darin, einen Bereich zu "scannen". Ist der Bereich ungefährlich,
erscheint eine Zahl, die anzeigt, wie viele benachbarte Bereiche Fallen enthalten.
##### Spielziel

Das Ziel ist, alle sicheren Bereiche aufzudecken, ohne dabei einen Bereich mit einer
Gefahr zu aktivieren. Wird ein gefährlicher Bereich aufgedeckt, endet das Spiel sofort.


#### Anforderungen
##### Technische Anforderungen

- Konsolenspiel
- Lauffähig unter Python3.13.1 unter Ubuntu 20.04 LTS
- Nutzerfreundliche Kommandozeilenschnittstelle
- Zulässige Module:
	- os
	- sys
	- random
	- unittest
- Zulässige Bibliotheken:
	- pylint
	- coverage
	- mypy

- Alle Bibliotheken müssen in der Datei `requirements.txt` verwaltet werden.
- Die Ordnerstruktur des Projektes muss folgendermaßen aussehen:

```
.
├── mypy.ini
├── README.md
├── requirements.txt
├── documentation
│ ├── documentation.pdf
├── source
│ ├── main.py
│ └── example.py
└── tests
├── test_main.py
└── test_example.py
```


##### Funktionale Anforderungen
- Zu Spielbeginn soll ein zufälliges neues Spielbrett generiert werden
- zufällig verteilte freie Felder und Fallenfelder auf dem Spielbrett
- Mindestbrettgröße 5x5
- Verdecktes Feld soll auf der Kommandozeile angezeigt werden
- Spieler soll ein Feld scannen dürfen
	- Falle gescannt -> Spielende
	- Freies Feld -> Anzeige Summe benachbarter Zahlen im gescannten Feld

##### Nicht-funktionale Anforderungen

- Zuverlässigkeit:
	- Stabile Funktionalität ohne Abstürze
	- Fehlertolerante Handhabung von ungültigen Eingaben
- Benutzerfreundlichkeit
	- Einfache Bedienung auch für Benutzer ohne technische Vorkenntnisse


#### Testing

##### Robuste Entwicklung

- Es müssen automatisierte Unittests entwickelt werden
- Bibliothek unittest muss genutzt werden
- Pro Datei Testabdeckung von mind. 75% (Prüfung über coverage)
- Tests müssen logisch sinnvoll entwickelt sein

##### Statische Code-Analyse - Pylint

- Pylint muss auf **jeder** Datei ausgeführt werden
- Alle Pylint Warnungen müssen behoben werden
- Meldungen können mit guter Begründung unterdrückt werden
- Keine Dokumentation der Test-Dateien nötig `(#pylint: disable=C)`

##### Type Checker - MyPy

- Alle Python Dateien müssen von MyPy überprüft werden
- Alle MyPy Warnungen müssen behoben werden
- Folgende `mypy.ini` muss genutzt werden:

```
[mypy]
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
disallow_untyped_calls = True
disallow_incomplete_defs = True
```


#### Dokumentation & Bewertung
##### Dokumentation

- Abzugeben als PDF
- Alle Funktionen und der grundlegende Aufbau muss beschrieben werden
- Es muss die Version aller genutzten Bibliotheken dokumentiert sein
- Architekturbeschreibung muss vorhanden sein
- Nutzerinterface muss beschrieben werden
- Programmablauf muss dokumentiert werden
- Ergebnisse aller statischen und dynamischen Tools muss vorhanden sein (Unittest, Coverage, Pylint, MyPy)

##### Bewertung 

- Über Exceltabelle 
- Selbsteinschätzung muss eingetragen sein

Author: Luke Engelhardt
Version: 1.0