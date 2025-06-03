# Ten plik będzie zawierał różne funkcje pomocnicze,
# które mogą być używane w różnych częściach projektu.

import json

def load_config(config_path="config/settings.json"):
    """Wczytuje plik konfiguracyjny JSON."""
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        print(f"Konfiguracja wczytana z {config_path}")
        return config
    except FileNotFoundError:
        print(f"BŁĄD: Plik konfiguracyjny nie został znaleziony w {config_path}")
        return None
    except json.JSONDecodeError:
        print(f"BŁĄD: Błąd dekodowania pliku JSON w {config_path}")
        return None

# Możesz tu dodać inne funkcje pomocnicze, np.:
# - funkcje do przetwarzania danych
# - funkcje do logowania
# - funkcje do obsługi wyjątków 