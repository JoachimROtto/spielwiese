Marschbefehl: alle Beispiele ausser jax laufen, CUDA-Threads fixen, Papers und Buch (nur Profiler) lesen, jax fixen, zeiten nehmen, Paper deepln, drucken, odenpaper 
# ToDo
- Im Beispiel wurde auf erste Tricks wie float3 verzichtet
- Beispiel wurde verändert ->Paper
- CUDA-Beispiel die Threaderzeugung überlegen. Oh nein n=1 Mio. verpufft weil i<n nur einmal geprüft wird!!!!
- Zeit CUDA: user ,018 s sys ,260s =>mit 10.000.000 wiederholen ->Grütze
- In der JAX-Variante erzwingt ein Versionskonflikt CPU-Ausführung und es funktioniert nur innnerhalb VSCode
- INsgesamt immer nur die CUDA-Variante nehmen (ausser NumPy und Python-only) denn darum geht es ja: CUDA
- Alles in ein Skript und dann excel!
- np.cross in numba (und auch sonst?) langsamer als loop (aus speichergründen):https://numba.discourse.group/t/numba-with-cross-product-is-10x-slow-than-numba-with-loop/145/3
- Das macht alles überhaupt keinen Sinn, bereits die fast leere Datei mit import kostet 1,6 s ->in MEthoden packen und nen Profiler drüber, genauer pyNaive 1,15 same + import numpy 2,5
- numba/cuda ohne numpy 
naiv: 1,2s
numpy: 1,5s
cupy: 2,1s
jax/jit: 1,77
numba mit cuda und numpy: 1,8
numba mit cuda ohne numpy: (zickt bei result, typfehler?)
numba mit cuda und cupy?: 2
dask: timout bzw. 6s für 10.000(lazy ev, Ausführung bei result.compute())
Ubuntu 2X.XX.XX, Python 3.1X, cuda, nvcc, compiler?
# notizen
- CUDA startet man mit Abwandlungen von nvcc <<Name>>.cu -arch=sm_86 & ./a.out, aber Achtung: das & sorgt dafür dass nicht aufeinander gewartet wird! Naja irgendwie wohl doch...
- time ./<<Name>> wirft real(gesamt) user  (programm) sys(darin steckende syscalls)
- insgesamt an dinge wie print("Ergebnis stimmt überein:", np.allclose(result, np.cross(a, b))) zur Qualitätskontrolle denken



# links
Da waren noch tabs offen
- https://software.intel.com/sites/landingpage/pintool/docs/99977/Pin/doc/html/index.html#SimpleCount
- https://www.intel.com/content/dam/develop/external/us/en/documents/asplos2008-handson-256675.pdf
- https://en.wikipedia.org/wiki/Pin_(computer_program)

# github

## github-zugang (cert etc.)

wenn der push halt nicht läuft
ssh-keygen -t ed25519 -C "githubr@gfed.de"
\*.pub im WebGui reintippern

Anleitung für Keychain folgen? https://docs.github.com/de/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

Wichtig ist dem adden zu folgen und immer git als Username in den links zu benutzen. Die eigentlich Zuordnung erfolgt dann mit dem Zertifikat. 

Token Im WebGui generieren und diesen als Passwort benutzen(Benutzername ohne Emaildomain)

evtl.: 

git config --global user.email "githubr@gfed.de"

git config --global user.name "JoachimROtto"

## bestehendes migrieren

1. Repository auf GitHub erstellen und wähle die Sichtbarkeit (Public oder Private).
2. Lass README, .gitignore und License zunächst unmarkiert, um Konflikte mit deinen lokalen Dateien zu vermeiden.
3. Klicke auf Create repository und kopiere die angezeigte Repository-URL.

Öffne ein Terminal in deinem Projektverzeichnis und führe folgende Befehle aus:

git init

git add .

git commit -m "Initial commit"

git branch -M main

git remote add origin https://JoachimROtto@github.com/JoachimROtto/....

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

Wird nach Usernam/Password gefragt hilft 

git remote set-url origin git@github.com:JoachimROtto/spielwiese

Ist ein Secret drin und wird nicht gepusht oder sollen andere lokale commits verworfen werden: git reset --hard HEAD~1 dreht die lokalen Commits um je eine Stufe zurück.

War das viel des Guten (denn es wird wirklich zurückgedreht!!!) dann mit git reflog den Hash des Wunschcommits finden und mit git reset --Hard <<Hash>> entsprechend zurückkehren

Fragt Ubuntu (also das GUI) nach einem PW wenn gepusht wird ist damit kein sudo oder so gemeint sondern der Schlüssel des Zertifikates