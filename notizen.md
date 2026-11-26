# github

## github-zugang (cert etc.)

wenn der push halt nicht läuft
ssh-keygen -t ed25519 -C "githubr@gfed.de"
\*.pub im WebGui reintippern

Anleitung für Keychain folgen? https://docs.github.com/de/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

Vielleicht war der Fehler auch dass ich Password als Password gelesen habe aber eigentlich der Token gemeint war.

Token Im WebGui generieren und diesen als Passwort benutzen

## bestehendes migrieren

1. Repository auf GitHub erstellen und wähle die Sichtbarkeit (Public oder Private).
2. Lass README, .gitignore und License zunächst unmarkiert, um Konflikte mit deinen lokalen Dateien zu vermeiden.
3. Klicke auf Create repository und kopiere die angezeigte Repository-URL.

Öffne ein Terminal in deinem Projektverzeichnis und führe folgende Befehle aus:

git init

git add .

git commit -m "Initial commit"

git branch -M main

git remote add origin <DEINE-GITHUB-URL>

git push -u origin main

Hinweis: Leere Unterordner werden von Git standardmäßig nicht erfasst. Falls ein Ordner leer bleiben soll, lege darin eine Platzhalterdatei wie .gitkeep an.

## aussem Repo lokal erstellen

ins lokale Verzeichnis (Achtung: es wird ein Unterverzeichnis mit dem Namen erstellt)

git clone https://github.com/JoachimROtto/.....

syncen wie gewohnt (Aber nicht von hier sondern aus dem erstellten Unterverzeichnis)

## syncen im weiteren Sinne

git add .

git commit -m "Kurze, klare Beschreibung"

git push -u origin main

Sind Bilder oso vorhanden, kann es zu einem Fehler (rpc fehlgeschlagen http 400 curl 22) kommen. Es hilft: git config --global http.postBuffer 524288000
git commit -m "Initialisierung"
