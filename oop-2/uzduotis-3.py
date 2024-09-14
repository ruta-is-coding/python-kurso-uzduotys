# Patobulinti objektinio programavimo 1 pamokos biudžeto programą
from biudzetas import Biudzetas

mano_biudzetas = Biudzetas()

while True:
    while True:
        try:
            veiksmas = int(input("Pasirinkite veiksmą: \n1-pridėti pajamas (€), \n2-pridėti išlaidas (€), "
                                 "\n3 - parodyti balansą, \n4 - parodyti biudžeto ataskaitą, "
                                 "\n5 - išeiti iš programos\n"))
            break
        except ValueError:
            print("Netinkamas pasirinkimas! Bandykite dar kartą")


    match veiksmas:
        case 1:
            suma = abs(float(input("Įveskite sumą (€): ")))
            siuntejas = input("Įveskite siuntėją: ")
            papildoma_info = input("Įveskite papildomą informaciją: ")
            mano_biudzetas.prideti_pajamu_irasa(suma, siuntejas, papildoma_info)
        case 2:
            suma = abs(float(input("Įveskite sumą (€): ")))
            atsiskaitymas = input("Įveskite atsiskaitymo būdą: ")
            pirkinys = input("Įveskite įsigytą prekę/paslaugą: ")
            mano_biudzetas.prideti_islaidu_irasa(suma, atsiskaitymas, pirkinys)
        case 3:
            mano_biudzetas.gauti_balansa()
        case 4:
            mano_biudzetas.parodyti_ataskaita()
        case 5:
            print("Viso geriausio :) !")
            break
        case _:
            print("Netinkamas pasirinkimas! Bandykite dar kartą!")
            continue
