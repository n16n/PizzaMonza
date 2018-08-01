import socket
import time
from tkinter import *
from tkinter import font
from tkinter import messagebox
import re

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))

def posalji():
    poruka = ""
    vrsta = "Vrsta: "
    prilog = "Dodaci ("
    velicina = "Velicina: "
    if v_vrsta.get() == 1:  vrsta += "CAPRICCIOSA"
    elif v_vrsta.get() == 2:  vrsta += "PEPPERONI"
    elif v_vrsta.get() == 3:  vrsta += "VESUVIO"
    elif v_vrsta.get() == 4:  vrsta += "MEXICANA"

    if v_velicina.get() == 1:  velicina += "25"
    elif v_velicina.get() == 2:  velicina += "32"
    elif v_velicina.get() == 3:  velicina += "50"

    if v_feferone.get() == 1:  prilog += "feferone"
    if v_masline.get() == 1:  prilog += "," + "masline"
    if v_ceri.get() == 1:  prilog += "," + "ceri"

    telefon = "Telefon: " + broj.get()
    isporuci = "Adresa: " + adresa.get()
    zahtevam = "Napomena: " + napomena.get()
    poruka = vrsta + "; " + velicina + "; " + prilog + "); " + telefon + "; " + isporuci + "; " + zahtevam

    s.send(poruka.encode())
    odgovor = s.recv(1024).decode()
    messagebox.showinfo("Narudžbina", odgovor)
    if messagebox.OK:
        root.destroy()
    print(poruka)
    s.close()

def nmz():
    messagebox.showinfo("NE", "679,7 kcal i 75g masti / 100g proizvoda!")
    cb_d4.config(state = DISABLED)


root = Tk()
root.title("Pizza Monza")
root.config(height = 1000, width = 600, bg = "#8B0000")
root.geometry("450x500")
root.resizable(False, False)

#kontrolne promenljive
v_vrsta = IntVar()
v_velicina = IntVar()
v_feferone = IntVar()
v_masline = IntVar()
v_ceri = IntVar()
v_majonez = IntVar()
v_broj = StringVar()
v_adresa = StringVar()
v_napomena = StringVar()

#fontovi
fNaslov = font.Font(family = "Verdana", size = 30, weight = "bold")
fOstalo = font.Font(family = "Verdana", size = 15, weight = "bold")
fTekst = font.Font(family = "Verdana", size = 10, weight = "bold")

#naslov
l_naslov = Label(root, text = "Pizza Monza", font = fNaslov, fg = "white")
#l_naslov.place(x = 500, y = 5)
l_naslov.pack(anchor = N)
l_naslov['bg'] = l_naslov.master['bg']

l_prazno0 = Label(root, text = "NISTA", font = fOstalo, fg = "#8B0000", bg = "#8B0000")
l_prazno0.pack()

frm = Frame(root, bg = "#8B0000")
frm.pack(anchor = W)

#vrsta
l_vrsta = Label(frm, text = "Vrsta:", font = fOstalo, fg = "white")
l_vrsta.grid(row = 0, column = 0)
l_vrsta["bg"] = l_vrsta.master["bg"]
rb_p1 = Radiobutton(frm, text = "CAPRICCIOSA", font = fTekst, variable = v_vrsta, value = 1)
rb_p1.grid(row = 1, column = 0)
rb_p1["bg"] = rb_p1.master["bg"]
rb_p2 = Radiobutton(frm, text = "PEPPERONI", font = fTekst, variable = v_vrsta, value = 2)
rb_p2.grid(row = 1, column = 1)
rb_p2["bg"] = rb_p2.master["bg"]
rb_p3 = Radiobutton(frm, text = "VESUVIO", font = fTekst, variable = v_vrsta, value = 3)
rb_p3.grid(row = 2, column = 0)
rb_p3["bg"] = rb_p3.master["bg"]
rb_p4 = Radiobutton(frm, text = "MEXICANA", font = fTekst, variable = v_vrsta, value = 4)
rb_p4.grid(row = 2, column = 1)
rb_p4["bg"] = rb_p4.master["bg"]

l_prazno1 = Label(frm, text = "NISTA", font = fOstalo, fg = "#8B0000", bg = "#8B0000")
l_prazno1.grid(row = 3, column = 0)

#velicina
l_velicina = Label(frm, text = "Velicina:", font = fOstalo, fg = "white")
l_velicina.grid(row = 4, column = 0)
l_velicina["bg"] = l_velicina.master["bg"]
rb_v1 = Radiobutton(frm, text = "25", font = fTekst, variable = v_velicina, value = 1)
rb_v1.grid(row = 5, column = 0)
rb_v1["bg"] = rb_v1.master["bg"]
rb_v2 = Radiobutton(frm, text = "32", font = fTekst, variable = v_velicina, value = 2)
rb_v2.grid(row = 5, column = 1)
rb_v2["bg"] = rb_v2.master["bg"]
rb_v3 = Radiobutton(frm, text = "50", font = fTekst, variable = v_velicina, value = 3)
rb_v3.grid(row = 5, column = 3)
rb_v3["bg"] = rb_v3.master["bg"]

l_prazno2 = Label(frm, text = "NISTA", font = fOstalo, fg = "#8B0000", bg = "#8B0000")
l_prazno2.grid(row = 6, column = 0)

#dodaci
l_dodaci = Label(frm, text = "Dodaci:", font = fOstalo, fg = "white")
l_dodaci.grid(row = 7, column = 0)
l_dodaci["bg"] = l_dodaci.master["bg"]
cb_d1 = Checkbutton(frm, text = "Feferone", font = fTekst, variable = v_feferone)
cb_d1.grid(row = 8, column = 0)
cb_d1["bg"] = cb_d1.master["bg"]
cb_d2 = Checkbutton(frm, text = "Masline", font = fTekst, variable = v_masline)
cb_d2.grid(row = 8, column = 1)
cb_d2["bg"] = cb_d2.master["bg"]
cb_d3 = Checkbutton(frm, text = "Čeri", font = fTekst, variable = v_ceri)
cb_d3.grid(row = 9, column = 0)
cb_d3["bg"] = cb_d3.master["bg"]
cb_d4 = Checkbutton(frm, text = "Majonez", font = fTekst, variable = v_majonez, command = nmz)
cb_d4.grid(row = 9, column = 1)
cb_d4["bg"] = cb_d4.master["bg"]

l_prazno3 = Label(frm, text = "NISTA", font = fOstalo, fg = "#8B0000", bg = "#8B0000")
l_prazno3.grid(row = 10, column = 0)

#broj, adresa, napomena
l_broj = Label(frm, text = "Broj telefona: ", font = fOstalo, fg = "white")
l_broj.grid(row = 11, column = 0)
l_broj["bg"] = l_broj.master["bg"]
broj = Entry(frm, textvariable = v_broj, font = fTekst, fg = "white")
broj.grid(row = 11, column = 1)
broj["bg"] = broj.master["bg"]
l_adresa = Label(frm, text = "Adresa: ", font = fOstalo, fg = "white")
l_adresa.grid(row = 12, column = 0)
l_adresa["bg"] = l_adresa.master["bg"]
adresa = Entry(frm, textvariable = v_adresa, font = fTekst, fg = "white")
adresa.grid(row = 12, column = 1)
adresa["bg"] = adresa.master["bg"]
l_napomena = Label(frm, text = "Napomena: ", font = fOstalo, fg = "white")
l_napomena.grid(row = 13, column = 0)
l_napomena["bg"] = l_napomena.master["bg"]
napomena = Entry(frm, textvariable = v_napomena, font = fTekst, fg = "white")
napomena.grid(row = 13, column = 1)
napomena["bg"] = napomena.master["bg"]

l_prazno4 = Label(frm, text = "NISTA", font = fOstalo, fg = "#8B0000", bg = "#8B0000")
l_prazno4.grid(row = 14, column = 0)

#dugme
dugme = Button(frm, text = "Pošalji", font = fTekst, bg = "white", command = posalji)
dugme.grid(row = 15, column = 0, columnspan = 3)

root.mainloop()


#telefon
#brojTel = re.sub(r'\D',"",brojTel)
#if brojTel == "":
#    brojTel="GRESKA_TELEFON"
# poklapanjeTelefona = re.match(r'\d{9}', telefon)
# poklapanjeMejla = re.match(r'^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$', mail)