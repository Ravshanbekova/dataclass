from dataclasses import dataclass

@dataclass
class Transport:
    model: str
    rang: str
    tezlik: float
    yil: int

@dataclass
class Moshina(Transport):
    uzunlik: int

gentra = Moshina("Gentra 1.6", "Qora", 180, 2024, 4)

print(f"Moshina: {gentra.model}")
print(f"Moshina rangi: {gentra.rang}")
print(f"Moshina tezligi: {gentra.tezlik} km/s")
print(f"Moshina ishlab chiqarilgan yil: {gentra.yil}")
print(f"Moshina uzunligi: {gentra.uzunlik}")