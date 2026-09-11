# 🐢 Turtle Crossing

Ein kleines Arcade-Spiel mit Python's `turtle`-Modul: Bringe die Schildkröte sicher über die Straße, ohne von den Autos erwischt zu werden. Jede erfolgreiche Überquerung erhöht das Level – und damit die Geschwindigkeit der Autos.

## 🎮 Spielprinzip

- Die Schildkröte startet am unteren Bildschirmrand.
- Drücke die **Pfeiltaste nach oben**, um vorwärts zu laufen.
- Erreicht die Schildkröte die obere Bildschirmkante, steigt das Level und sie kehrt zum Start zurück.
- Autos fahren zufällig von rechts nach links über den Bildschirm.
- Kollidiert die Schildkröte mit einem Auto, ist das Spiel vorbei.

## 🛠️ Voraussetzungen

- Python 3.x
- Das `turtle`-Modul (Teil der Python-Standardbibliothek, keine Installation nötig)

## 🚀 Installation & Start

```bash
git clone https://github.com/<dein-username>/<dein-repo>.git
cd <dein-repo>
python main.py
```

## 📁 Projektstruktur

```
.
├── main.py            # Hauptspiel-Loop
├── player.py           # Schildkröten-Klasse (Spieler)
├── car_manager.py       # Erzeugt und bewegt die Autos
├── scoreboard.py         # Zeigt Level und Game-Over-Meldung an
└── README.md
```

## 🕹️ Steuerung

| Taste | Aktion |
|-------|--------|
| ↑     | Schildkröte vorwärts bewegen |

## 📄 Lizenz

Dieses Projekt steht unter der MIT-Lizenz – frei nutzbar und veränderbar.
