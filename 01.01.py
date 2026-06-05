from threading import Thread, Semaphore
from random import randint, choice
from time import sleep

area = Semaphore(2)
pista_norte = Semaphore(1)
pista_sul = Semaphore(1)


class Aviao(Thread):
    def __init__(self, id_aviao):
        super().__init__()
        self.id_aviao = id_aviao

    def run(self):
        print(f"Avião {self.id_aviao} aguardando área de decolagem")

        area.acquire()

        print(f"Avião {self.id_aviao} entrou na área")

        print(f"Avião {self.id_aviao} manobrando")
        sleep(randint(300, 700) / 1000)

        pista = choice(["Norte", "Sul"])

        if pista == "Norte":
            print(f"Avião {self.id_aviao} aguardando pista Norte")
            pista_norte.acquire()

            print(f"Avião {self.id_aviao} taxiando para pista Norte")
            sleep(randint(500, 1000) / 1000)

            print(f"Avião {self.id_aviao} decolando pela pista Norte")
            sleep(randint(600, 800) / 1000)

            pista_norte.release()

        else:
            print(f"Avião {self.id_aviao} aguardando pista Sul")
            pista_sul.acquire()

            print(f"Avião {self.id_aviao} taxiando para pista Sul")
            sleep(randint(500, 1000) / 1000)

            print(f"Avião {self.id_aviao} decolando pela pista Sul")
            sleep(randint(600, 800) / 1000)

            pista_sul.release()

        print(f"Avião {self.id_aviao} afastando-se da área")
        sleep(randint(300, 800) / 1000)

        area.release()

        print(f"Avião {self.id_aviao} concluiu a decolagem")


avioes = []

for i in range(12):
    aviao = Aviao(i + 1)
    avioes.append(aviao)
    aviao.start()

for aviao in avioes:
    aviao.join()

print("Todas as aeronaves decolaram.")