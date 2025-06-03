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

- Python 3.8 lub nowszy
- Zainstalowana gra **Rocket League**
- Biblioteka `rlgym` umożliwiająca komunikację gry z Pythonem

## Instalacja

1. Sklonuj repozytorium i przejdź do katalogu `RocketLeagueRLBot`.
2. Zainstaluj zależności komendą:

   ```bash
   pip install -r requirements.txt
   ```

## Użycie

1. Uruchom Rocket League w trybie treningu.
2. Następnie w terminalu wykonaj:

   ```bash
   python -m src.main
   ```

## Trening Bota

Parametry treningu znajdują się w pliku `config/settings.json` w sekcji
`training_params`. Domyślnie bot trenuje przez 10 epizodów. Możesz zmienić tę
wartość na dowolną liczbę. Po uruchomieniu skryptu `python -m src.main` bot
rozpocznie prostą sesję treningową w przygotowanym środowisku.

## TODO

- [ ] Zdefiniowanie interfejsu komunikacji z grą Rocket League.
- [ ] Implementacja podstawowego modelu AI.
- [ ] Stworzenie pętli treningowej.
- [ ] ... i wiele więcej! 
