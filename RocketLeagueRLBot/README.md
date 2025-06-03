# RocketLeagueRLBot

## Opis Projektu

Ten projekt ma na celu stworzenie bota opartego na sztucznej inteligencji (AI), zdolnego do nauki i gry w Rocket League. Bot będzie wykorzystywał techniki uczenia maszynowego, prawdopodobnie uczenia przez wzmacnianie (Reinforcement Learning), aby doskonalić swoje umiejętności w grze.

## Struktura Projektu

- \`config/\`: Pliki konfiguracyjne.
- \`data/\`: Dane treningowe, zapisane modele itp.
- \`docs/\`: Dokumentacja projektu.
- \`src/\`: Główny kod źródłowy bota.
  - \`agent/\`: Komponenty agenta AI (model, logika treningu).
  - \`env/\`: Interfejs do środowiska gry Rocket League.
  - \`utils/\`: Narzędzia i funkcje pomocnicze.
- \`tests/\`: Testy jednostkowe.
- \`main.py\`: Główny skrypt uruchomieniowy.
- \`requirements.txt\`: Zależności projektu.

## Wymagania Wstępne

- Python 3.12 lub nowszy
- (Opcjonalnie) Zainstalowana gra Rocket League wraz z BakkesMod, jeśli chcesz
  trenować bezpośrednio w grze.

Projekt zawiera uproszczone środowisko testowe pozwalające uruchomić trening
bez posiadania gry.

## Instalacja

```bash
pip install -r requirements.txt
```

Jeżeli planujesz używać prawdziwego środowiska z grą Rocket League, zapoznaj się
z instrukcjami na stronie [rlgym](https://rlgym.org) dotyczącymi konfiguracji
gry i BakkesMod.

## Użycie

Do uruchomienia przykładowego treningu wystarczy komenda:

```bash
python -m src.main
```

Domyślnie skrypt uruchamia krótki trening w wbudowanym środowisku testowym.
Parametr `num_episodes` w funkcji `main` można zmienić, aby wydłużyć trening.

## Trening Bota

Aktualnie projekt udostępnia jedynie przykładową implementację pętli
treningowej korzystającą z prostego środowiska losowego. Kod można rozbudować o
pełną integrację z `rlgym`, aby trenować bota na prawdziwych meczach
Rocket League.

## TODO

- [ ] Zdefiniowanie interfejsu komunikacji z grą Rocket League.
- [ ] Implementacja podstawowego modelu AI.
- [ ] Stworzenie pętli treningowej.
- [ ] ... i wiele więcej! 