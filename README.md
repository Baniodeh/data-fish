# Daten-Fische
In diesem Reporitory findet ihr alles zum DataScience Kurs.

## Getting started


### Python

In diesem Kurs werden wir Python 3 als Programmiersprache verwenden. Ein einfacher Weg den Python-Interpreter und alle
benötigten Packete zu installieren ist mit Hilfe von Anaconda. Dazu müsst ihr euch einfach nur Anaconda herunterladen und
installieren.

https://www.anaconda.com/download/


### PyCharm

Programm-Code ist im Prinzip in jedem Text-Editor möglich. Um uns die Dinge etwas einfacher zu machen wollen wir
jedoch eine IDE ("Integrated development environment") benutzen. Von Jetbrains gibt es eine sehr gute IDE als Community-Edition kostenlos:

https://www.jetbrains.com/pycharm/


### GitKraken

GitKraken ist ein Git Client (UI) für Git. So ein User Interface erleichtert die Arbeit und ist eine Alternative zum Command Line Interface (CLI):

https://www.gitkraken.com/download


## Setup

```sh
git clone https://github.com/neuefische/data-fish.git
```

```sh
conda env create --file environment.yml
source activate data-fish
```

## Usage

```sh
conda env update --file environment.yml
source activate data-fish
jupyter notebook
```
