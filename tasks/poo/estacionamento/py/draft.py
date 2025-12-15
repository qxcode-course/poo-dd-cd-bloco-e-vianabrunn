from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo
        self.entrada = 0

    def tempo(self, saida):
        return saida - self.entrada

    @abstractmethod
    def calcular_valor(self, saida):
        pass

    def __str__(self):
        id_formatado = self.id.rjust(10, "_")
        return f"{self.tipo} : {id_formatado} : {self.entrada}"
    
class Bike(Veiculo):
    def calcular_valor(self, saida):
        return 3.00
    
    def estacionar(self, tipo, id):
        if tipo == "bike":
            v = Bike(id, "Bike")
        elif tipo == "moto":
            v = Moto(id, "Moto")
        elif tipo == "carro":
            v = Carro(id, "Carro")

        v.entrada = self.tempo_atual
        self.veiculos.append(v)
    
class Moto(Veiculo):
    def calcular_valor(self, saida):
        return self.tempo(saida) / 20
    
    def estacionar(self, tipo, id):
        if tipo == "bike":
            v = Bike(id, "Bike")
        elif tipo == "moto":
            v = Moto(id, "Moto")
        elif tipo == "carro":
            v = Carro(id, "Carro")

        v.entrada = self.tempo_atual
        self.veiculos.append(v)
    
    
class Carro(Veiculo):
    def calcular_valor(self, saida):
        valor = self.tempo(saida) / 10
        return max(valor, 5.00)
    
    def estacionar(self, tipo, id):
        if tipo == "bike":
            v = Bike(id, "Bike")
        elif tipo == "moto":
            v = Moto(id, "Moto")
        elif tipo == "carro":
            v = Carro(id, "Carro")

        v.entrada = self.tempo_atual
        self.veiculos.append(v)

    
class Estacionamento:
    def __init__(self):
        self.veiculos = []
        self.tempo_atual = 0

    def avancar_tempo(self, minutos):
        self.tempo_atual += minutos

    def estacionar(self, tipo, id):
        if tipo == "bike":
            v = Bike(id, "Bike")
            v.entrada = self.tempo_atual
        elif tipo == "moto":
            v = Moto(id, "Moto")
            v.entrada = self.tempo_atual
        elif tipo == "carro":
            v = Carro(id, "Carro")
            v.entrada = self.tempo_atual
        self.veiculos.append(v)

    def pagar(self, id):
        for v in self.veiculos:
            if v.id == id:
                valor = v.calcular_valor(self.tempo_atual)
                print(f"{v.tipo} chegou {v.entrada} saiu {self.tempo_atual}. Pagar R$ {valor:.2f}")
                self.veiculos.remove(v)
                return

    def __str__(self):
        saida = ""
        for v in self.veiculos:
            tipo_formatado = v.tipo.rjust(10, "_")
            saida += f"{tipo_formatado} : {v.id.rjust(10, '_')} : {v.entrada}\n"
        saida += f"Hora atual: {self.tempo_atual}"
        return saida

def main():
    est = Estacionamento()

    while True:
        line = input()
        print("$" + line)

        args = line.split()

        if args[0] == "end":
            break

        if args[0] == "init":
            est = Estacionamento()

        elif args[0] == "show":
            print(est)

        elif args[0] == "estacionar":
            est.estacionar(args[1], args[2])

        elif args[0] == "tempo":
            est.avancar_tempo(int(args[1]))


        elif args[0] == "pagar":
            est.pagar(args[1])

main()

    