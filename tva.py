from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

root = Tk()
root.geometry("900x400")
root.title("Gestion des articles")

def afficher2():
    v = paiement.get()

    if v == 3:
        label_ttc.config(text="1%")
    elif v == 6:
        label_ttc.config(text="2%")
    elif v == 1:
        label_ttc.config(text="3%")
    else:
        label_ttc.config(text="")


def calculer():
    montant_brut = float(entry.get())
    taux_tva = float(comb.get()) / 100

    montant_tva = montant_brut * taux_tva


    if paiement.get()==3:
        taux_remise=0.01
    elif paiement.get()==6:   
        taux_remise=0.02
    elif paiement.get()==1:   
        taux_remise=0.03


    label_vstock.config(text=f"{taux_tva} DH")
    label6.config(text=f"{montant_tva} DH")

    montant_remise=montant_tva*taux_remise
    label_vstock.config(text=f"{montant_remise} DH")
    montant_ttc=montant_brut + montant_remise
    label8.config(text=f"{montant_ttc} DH")

    




def delete():
    entry.delete(0,END)
    comb.set("")
    label6.config(text="")
    label8.config(text="")
    label_vstock.config(text="")
    paiement.set(0)
    afficher2()


def destroy():
    if messagebox.askyesno("Fermer", "Voulez-vous fermer ?"):
        root.destroy()


label1 = Label(root, text="montant brut")
label1.place(x=10, y=10)

entry = Entry(root)
entry.place(x=10, y=40)

label2 = Label(root, text="tva")
label2.place(x=500, y=10)
comb = Combobox(root, values=["7", "10", "20"], state="readonly")
comb.place(x=500, y=30, width=150)


label4 = Label(root, text="montant tva")
label4.place(x=10, y=100)
label6 = Label(root, text="", bg="lightblue")
label6.place(x=10, y=130, width=150)

label7 = Label(root, text="montant ttc")
label7.place(x=200, y=230)
label8 = Label(root, text="", bg="lightblue")
label8.place(x=300, y=230, width=150)

label9 = Label(root, text="paiement")
label9.place(x=30, y=160)

paiement = IntVar()
Radiobutton(root, text="3 mois", variable=paiement, value=3, command=afficher2).place(x=30, y=180)
Radiobutton(root, text="6 mois", variable=paiement, value=6, command=afficher2).place(x=30, y=200)
Radiobutton(root, text="1 an", variable=paiement, value=1, command=afficher2).place(x=30, y=220)

label10 = Label(root, text="taux remise")
label10.place(x=440, y=160)
label_ttc = Label(root, text="", bg="lightblue")
label_ttc.place(x=550, y=160, width=150)

label11 = Label(root, text="mont.remise")
label11.place(x=440, y=195)
label_vstock = Label(root, text="", bg="lightblue")
label_vstock.place(x=550, y=200, width=150)

Button(root, text="Nouveau", command=delete).place(x=250, y=320, width=120)
Button(root, text="calculer", command=calculer).place(x=420, y=320, width=120)
Button(root, text="Fermer", command=destroy).place(x=600, y=320, width=120)

afficher2()

root.mainloop()
