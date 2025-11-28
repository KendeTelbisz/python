def ellenoriz_kor(kor):
    if kor < 0:
        raise ValueError("A kör nem lehet negatív!")
    return True

try:
    ellenoriz_kor(-5)
except ValueError as h:
    print("hiba:", h)