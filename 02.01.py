from threading import Thread, Semaphore
from random import randint, choice
from time import sleep

tocha = Semaphore(1)
pedra = Semaphore(1)
porta_sem = Semaphore(1)

portas = [1, 2, 3, 4]
porta_saida = randint(1, 4)

print(f"Porta vencedora: {porta_saida}")


class Cavaleiro(Thread):
    def __init__(self, id_cavaleiro):
        super().__init__()
        self.id = id_cavaleiro
        self.distancia = 0
        self.velocidade = randint(2, 4)
        self.tem_tocha = False
        self.tem_pedra = False

    def run(self):

        while self.distancia < 2000:

            self.distancia += self.velocidade

            if self.distancia >= 500 and not self.tem_tocha:
                if tocha.acquire(False):
                    self.tem_tocha = True
                    self.velocidade += 2
                    print(
                        f"Cavaleiro {self.id} pegou a TOCHA. Velocidade = {self.velocidade}"
                    )

            if (
                self.distancia >= 1500
                and not self.tem_tocha
                and not self.tem_pedra
            ):
                if pedra.acquire(False):
                    self.tem_pedra = True
                    self.velocidade += 2
                    print(
                        f"Cavaleiro {self.id} pegou a PEDRA. Velocidade = {self.velocidade}"
                    )

            sleep(0.05)

        print(f"Cavaleiro {self.id} chegou ao final.")

        porta_sem.acquire()

        porta = choice(portas)
        portas.remove(porta)

        print(f"Cavaleiro {self.id} escolheu a porta {porta}")

        if porta == porta_saida:
            print(f"Cavaleiro {self.id} ESCAPOU!")
        else:
            print(f"Cavaleiro {self.id} foi DEVORADO!")

        porta_sem.release()


cavaleiros = []

for i in range(4):
    cavaleiro = Cavaleiro(i + 1)
    cavaleiros.append(cavaleiro)
    cavaleiro.start()

for cavaleiro in cavaleiros:
    cavaleiro.join()

print("Fim da simulação.")