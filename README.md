> **🚧 Achtung**
dieses repo ist ein work in progress (wip). es wird definitiv noch unvollständigkeiten oder fehler geben. wenn dir etwas auffällt dann melde es bitte über ein [issue](https://github.com/Ingegneus/tuwien-etit-courses/issues) oder öffne vielleicht gleich ein [pull request](https://github.com/Ingegneus/tuwien-etit-courses/pulls), damit das hier so gut werden kann wie möglich.

## übersicht
- [was ist das hier](https://github.com/Ingegneus/tuwien-etit-courses?tab=readme-ov-file#was-ist-das-hier)
  - [hier ein paar screenshots](https://github.com/Ingegneus/tuwien-etit-courses?tab=readme-ov-file#hier-ein-paar-screenshots)
  - [motivation](https://github.com/Ingegneus/tuwien-etit-courses?tab=readme-ov-file#motivation)
- [wie nutze ich das hier](https://github.com/Ingegneus/tuwien-etit-courses?tab=readme-ov-file#wie-nutze-ich-das-hier)
  - [variante 1](https://github.com/Ingegneus/tuwien-etit-courses?tab=readme-ov-file#variante-1-installation-explizit-windows-aber-sollte-f%C3%BCr-macos-und-linux-gleich-finktionieren)
  - [variante 2](https://github.com/Ingegneus/tuwien-etit-courses?tab=readme-ov-file#variante-2-statische-html)
  - [variante 3](https://github.com/Ingegneus/tuwien-etit-courses?tab=readme-ov-file#variante-3-github-pages)
  - [wie nutze ich das hier](https://github.com/Ingegneus/tuwien-etit-courses?tab=readme-ov-file#mein-logseq-setup)
- [TODOs](https://github.com/Ingegneus/tuwien-etit-courses?tab=readme-ov-file#todos)


## was ist das hier
in diesem logseq grafen, versuche ich so gut es geht die stärken von logseq zu verwenden, um verständliche resourcen für studierende zu bieten. das system dass ich aufgesetzt habe ist bestimmt noch ausbaufähig, aber es ist mal ein anfang.

mir ist klar, dass in unserem studium git nicht wirklich thema ist und daher die bar of entry, um hier mitzumachen höher ist, als zur fachschaft zu gehen und ein pdf abzugeben. ich bin der überzeugung, dass das hier langlebiger ist. stell dir vor es gäbe nicht 20 ausarbeitungen, sondern eine quelle die immer auf dem letzten stand ist und ziemlich sicher auf richtigkeit kontrolliert wurde.

### hier ein paar screenshots  
geteilte fenster für einfacheres referenzieren von material. unten sieht man auch einen ausführbaren code block (ähnlich zu jupyter) der das beispiel durchrechnen kann
![img](https://raw.githubusercontent.com/ingegneus/tuwien-etit-courses/refs/heads/main/assets/storages/uni-git-assets/ls-uni-screenshot-1.webp)

links: beispiele mit verlinkten formeln + erklärung im pop up fenster; rechts: vorlesung mit transcript und timestamps für die leichtere suche
![img](https://raw.githubusercontent.com/ingegneus/tuwien-etit-courses/refs/heads/main/assets/storages/uni-git-assets/ls-uni-screenshot-2.webp)

automatische formelsammlung die gefiltert werden kann
![img](https://raw.githubusercontent.com/ingegneus/tuwien-etit-courses/refs/heads/main/assets/storages/uni-git-assets/ls-uni-screenshot-3.webp)


### motivation
ich hasse die art und weise wie lehrmaterial organisiert und präsentiert wird. das ist ein ansatz, beziehungsweise experiment, es besser zu machen

## wie nutze ich das hier
es gibt drei arten wie du diese ausarbeitung verwenden kannst.
### variante 1: installation (explizit windows, aber sollte für macos und linux gleich finktionieren)
hierfür brauchst du erstmal [logseq](https://github.com/logseq/logseq). was ist logseq? Das ist eine Plattform für Wissensmanagement und Zusammenarbeit. Sie legt den Fokus auf Privatsphäre, Langlebigkeit und Benutzerkontrolle. mehr infos findest du [hier](https://logseq.com/).  
als nächstes empfehle ich dir [git](https://git-scm.com/downloads) zu installieren. damit kannst du recht einfach updates zu diesem material herunter laden und auch kollaborieren. sobald du das installiert hast, such dir einen folder aus wo du deinen "grafen" speichern möchtest, dann öffne ein terminal (command prompt, powershell, ...)  
`cd dein/pfad/zum/grafen`  
und verwende  
`git clone https://github.com/Ingegneus/tuwien-etit-courses.git`
jetzt musst du die anleitung [hier](https://github.com/Ingegneus/logseq-plugin-config) befolgen. damit hast du alle plugins sowie meine konfiguration kopiert. das wichtigste sind dort die KaTeX definitionen.  
  
solltest du git nicht installieren wollen/können/was auch immer, dann kannst du den inhalt dieses repos mit diesem [link](https://github.com/Ingegneus/tuwien-etit-courses/archive/refs/heads/main.zip) herunterladen. entpacke ihn und verschiebe den `tuwien-etit-courses` ordner in deinen ordner für den grafen.  

jetzt sollte dein folder so ausschauen:
```
logseq-graf/
├─ assets/
├─ draws/
├─ journals/
├─ logseq/
├─ pages/
├─ tuwien-etit-courses/
├─ whiteboards/
```

nun kopiere/verschiebe den inhalt von `tuwien-etit-courses/` nach `logdeq-graf/`. jetzt kannst du in logseq deinen grafen neu [indexieren](https://docs.logseq.com/#/page/63500411-87b0-4d62-a9ac-5b5418bc3201) und du kannst sie in logseq bearbeiten.

Die häufigsten git befehle die du brauchen wirst sind:  
- `git add ./path/to/file.ext` - fügt eine datei zur staging area hinzu. bedeutet, dass die änderungen an dieser datei (oder falls die datei neu ist, die datei selbst) zum upload freigegeben sind  
- `git commit -m "meaningful commit message"` - fügt die änderungen die in der staging area sind dem aktuellen branch hinzu. dadurch sind die bearbeitungen durchgegangen  
- `git push` -  lädt deine änderungen auf guthub hoch  
- `git pull` - zieht den zustand von github und vereint es mit deiner lokalen version  

### variante 2: statische HTML
lade dir die `html.zip` datei von [hier](https://github.com/Ingegneus/tuwien-etit-courses/releases) runter, entpacke sie und öffne die `index.html` datei (sollte sich automatisch im browser öffnen). bedenke, dass einiges im browser nicht funktionieren wird, da es nur eine statische html datei ist. das heißt alles was mit plugins zu tun hat wird nicht gehen

### variante 3: github pages
diese methode ist sehr ähnlich zu 2, nur online. es gibt allerdings ein paar einschränkungen, ist aber im zweifelsfall praktisch. nutze diesen link öffnest [link](https://ingegneus.github.io/tuwien-etit-courses/). bedenke, dass einiges im browser nicht funktionieren wird, da es nur eine statische html datei ist. das heißt alles was mit plugins zu tun hat wird nicht gehen

### mein logseq setup
ich verwende logseq für so ziemlich alles und habe einige workflows entwickelt. für die uni nutze ich diese plugins:  
- live math (einfachere eingabe von latex)  
- display math (wendet \displaystyle überall and und man kann custom macros definiern)  
- logseq anki sync (damit kann man logseq flashcards mit anki synchronisieren und lernen)  
- helium (wenn man ein video schaut dann "floatet" es beim scrollen und bleibt immer sichtbar, auch wenn man notizen zu einem video macht)  
- media timestamp (die ganzen vo transcript timestamps sind mittels media timestamp eingetragen)  

[hier](https://docs.logseq.com/#/page/plugins) ist eine anleitung wie man plugins installiert

### TODOs
- [contribution guidelines](https://github.com/Ingegneus/tuwien-etit-courses/blob/main/UNI-CONTRIBUTION.md)
- wenn du einen fehler finden solltest dann, öffne bitte hier einen issue.
- wie sollen die uni unterlagen organisiert und verteilt werden?