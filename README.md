# Mail-to-Telegram

Dieses Repository enthält ein Python-Skript, das E-Mail-Benachrichtigungen abruft und sie formatiert (Betreff fett, gefolgt von dem E-Mail-Text) als Nachricht an eine Telegram-Gruppe weiterleitet.

## Voraussetzungen

- **Docker:** Zum Erstellen und Ausführen des Containers.
- **Telegram Bot:** Erstelle einen Bot über den [BotFather](https://t.me/botfather) und lade ihn in die Zielgruppe ein.
- **IMAP-fähiges E-Mail-Konto:** Zum Abruf der E-Mails.

## Konfiguration

Das Skript erwartet die folgenden Umgebungsvariablen, die beim Start des Containers einzeln übergeben werden:

- `IMAP_SERVER`: Adresse deines IMAP-Servers (z. B. `imap.example.com`)
- `EMAIL_ACCOUNT`: Deine E-Mail-Adresse
- `EMAIL_PASSWORD`: Dein E-Mail-Passwort
- `TELEGRAM_TOKEN`: Das API-Token deines Telegram Bots
- `TELEGRAM_CHAT_ID`: Die Chat-ID deiner Telegram-Gruppe

## Build und Run

### Docker-Image bauen

Führe folgenden Befehl im Repository-Verzeichnis aus, um das Docker-Image zu bauen:

```bash
docker build -t mail-to-telegram .
