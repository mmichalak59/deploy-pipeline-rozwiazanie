from app import dodaj, odejmij, pomnoz, poteguj

def test_dodaj():
    assert dodaj(2, 3) == 5
    assert dodaj(-1, 1) == 0

def test_odejmij():
    assert odejmij(10, 4) == 6
    assert odejmij(0, 5) == -5

def test_pomnoz():
    assert pomnoz(3, 5) == 15
    assert pomnoz(0, 99) == 0

def test_poteguj():
    assert poteguj(2, 8) == 256
    assert poteguj(3, 3) == 27
    assert poteguj(5, 0) == 1

if __name__ == "__main__":
    test_dodaj()
    test_odejmij()
    test_pomnoz()
    test_poteguj()
    print("Wszystkie testy OK")
