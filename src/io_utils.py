def load_data(file_path):
    """
    Ladda data från en CSV-fil.

    Args:
        file_path (str): Sökvägen till CSV-filen.
    """
    import pandas as pd

    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Filen ej hittad: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"Ingen data: {file_path} är tom.")
        return None
    except pd.errors.ParserError:
        print(f"Parserfel: Kunde inte tolka {file_path}.")
        return None
    except Exception as e:
        print(f"Något gick fel: {e}")
        return None