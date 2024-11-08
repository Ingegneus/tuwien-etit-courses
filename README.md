> **🚧 Achtung**
dieses repo ist ein work in progress (wip). es wird definitiv noch unvollständigkeiten oder fehler geben 

# was ist das hier
in diesem logseq grafen, versuche ich so gut es geht die stärken von logseq zu verwenden, um verständliche resourcen für studierende zu bieten. das system dass ich aufgesetzt habe ist bestimmt noch ausbaufähig, aber es ist mal ein anfang.

mir ist klar, dass in unserem studium git nicht wirklich thema ist und daher die bar of entry, um hier mitzumachen höher ist, als zur fachschaft zu gehen und ein pdf abzugeben. ich bin der überzeugung, dass das hier langlebiger ist. stellt euch vor es gäbe nicht 20 ausarbeitungen, sondern eine quelle die immer den letzten stand hat und ziemlich sicher auf richtigheit kontrolliert wurde.

## motivation
ich hasse die art und weise wie lehrmaterial organisiert und präsentiert wird. das ist ein ansatz, beziehungsweise experiment, es besser zu machen

# wie nutze ich das hier
es gibt zwei arten wie du diese ausarbeitung verwenden kannst.
## variante 1: installation (windows)
hierfür brauchst du erstmal [logseq](https://github.com/logseq/logseq). was ist logseq? Das ist eine Plattform für Wissensmanagement und Zusammenarbeit. Sie legt den Fokus auf Privatsphäre, Langlebigkeit und Benutzerkontrolle. mehr infos findest du [hier](https://logseq.com/).
als nächstes empfehle ich dir [git](https://git-scm.com/downloads) zu installieren. damit kannst du recht einfach updates zu diesem material herunter laden und auch kollaborieren. sobald du das installiert hast, such dir einen folder aus wo du deinen "grafen" speichern möchtest, dann öffne ein terminal (command prompt, powershell, ...) 
`cd dein/pfad/zum/grafen` 
und verwende 
`git clone https://github.com/Ingegneus/tuwien-etit-courses.git`

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

## variante 2: statische HTML
lade dir den html.zip ordner runter. entpacke ihn und öffne die `index.html` datei (sollte sich automatisch im browser öffnen).