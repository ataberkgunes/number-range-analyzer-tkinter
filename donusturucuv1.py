from tkinter import *
from tkinter import messagebox


def sayilari_listele():
    try:
        baslangic = int(entry_baslangic.get())
        bitis = int(entry_bitis.get())
        
        if baslangic > bitis:
            messagebox.showerror("Hata", "Başlangıç sayısı, bitiş sayısından küçük olmalıdır.")
            return
        
        sayilar = list(range(baslangic, bitis + 1))
        
        text_sonuclari.delete("1.0", END)
        for sayi in sayilar:
            text_sonuclari.insert(END, f"{sayi}\n")
        
        toplam = sum(sayilar)
        adet = len(sayilar)
        
        
        text_sonuclari2.delete("1.0", END)
        text_sonuclari2.insert(END, f"{toplam}")
        
        text_sonuclari1.delete("1.0", END)
        text_sonuclari1.insert(END, f"{adet}")

        text_sonuclari3.delete("1.0", END)
        text_sonuclari3.insert(END, "Sayıları Listele")
        
    except ValueError:
        messagebox.showerror("Hata", "Lütfen başlangıç ve bitiş sayılarınızı kontrol ediniz ve geçerli bir sayı giriniz.")

def bolen_2():
    try:
        baslangic = int(entry_baslangic.get())
        bitis = int(entry_bitis.get())
        
        if baslangic > bitis:
            messagebox.showerror("Hata", "Başlangıç sayısı, bitiş sayısından küçük olmalıdır.")
            return
        
        sayilar = list(range(baslangic, bitis + 1))

        bolenler = [sayi for sayi in sayilar if sayi % 2 == 0]

        
        text_sonuclari.delete("1.0", END)
        for sayi in bolenler:
            text_sonuclari.insert(END, f"{sayi}\n")
        
        
        toplam = sum(bolenler)
        adet = len(bolenler)
        
        text_sonuclari2.delete("1.0", END)
        text_sonuclari2.insert(END, f"{toplam}")
        
        text_sonuclari1.delete("1.0", END)
        text_sonuclari1.insert(END, f"{adet}")

        text_sonuclari3.delete("1.0", END)
        text_sonuclari3.insert(END, "2'ye Bölünenler")
        

    except ValueError:
        messagebox.showerror("Hata", "Lütfen başlangıç ve bitiş sayılarınızı kontrol ediniz ve geçerli bir sayı giriniz.")

def bolen_3():
    try:
        baslangic = int(entry_baslangic.get())
        bitis = int(entry_bitis.get())
        
        if baslangic > bitis:
            messagebox.showerror("Hata", "Başlangıç sayısı, bitiş sayısından küçük olmalıdır.")
            return
        
        sayilar = list(range(baslangic, bitis + 1))

        bolenler = [sayi for sayi in sayilar if sayi % 3 == 0]

        
        text_sonuclari.delete("1.0", END)
        for sayi in bolenler:
            text_sonuclari.insert(END, f"{sayi}\n")
        
        
        toplam = sum(bolenler)
        adet = len(bolenler)
        
        text_sonuclari2.delete("1.0", END)
        text_sonuclari2.insert(END, f"{toplam}")
        
        text_sonuclari1.delete("1.0", END)
        text_sonuclari1.insert(END, f"{adet}")

        text_sonuclari3.delete("1.0", END)
        text_sonuclari3.insert(END, "3'e Bölünenler")
        

    except ValueError:
        messagebox.showerror("Hata", "Lütfen başlangıç ve bitiş sayılarınızı kontrol ediniz ve geçerli bir sayı giriniz.")

def bolen_4():
    try:
        baslangic = int(entry_baslangic.get())
        bitis = int(entry_bitis.get())
        
        if baslangic > bitis:
            messagebox.showerror("Hata", "Başlangıç sayısı, bitiş sayısından küçük olmalıdır.")
            return
        
        sayilar = list(range(baslangic, bitis + 1))

        bolenler = [sayi for sayi in sayilar if sayi % 4 == 0]

        
        text_sonuclari.delete("1.0", END)
        for sayi in bolenler:
            text_sonuclari.insert(END, f"{sayi}\n")
        
        
        toplam = sum(bolenler)
        adet = len(bolenler)
        
        text_sonuclari2.delete("1.0", END)
        text_sonuclari2.insert(END, f"{toplam}")
        
        text_sonuclari1.delete("1.0", END)
        text_sonuclari1.insert(END, f"{adet}")

        text_sonuclari3.delete("1.0", END)
        text_sonuclari3.insert(END, "4'e Bölünenler")
        

    except ValueError:
        messagebox.showerror("Hata", "Lütfen başlangıç ve bitiş sayılarınızı kontrol ediniz ve geçerli bir sayı giriniz.")

def bolen_5():
    try:
        baslangic = int(entry_baslangic.get())
        bitis = int(entry_bitis.get())
        
        if baslangic > bitis:
            messagebox.showerror("Hata", "Başlangıç sayısı, bitiş sayısından küçük olmalıdır.")
            return
        
        sayilar = list(range(baslangic, bitis + 1))

        bolenler = [sayi for sayi in sayilar if sayi % 5 == 0]

        
        text_sonuclari.delete("1.0", END)
        for sayi in bolenler:
            text_sonuclari.insert(END, f"{sayi}\n")
        
        
        toplam = sum(bolenler)
        adet = len(bolenler)
        
        text_sonuclari2.delete("1.0", END)
        text_sonuclari2.insert(END, f"{toplam}")
        
        text_sonuclari1.delete("1.0", END)
        text_sonuclari1.insert(END, f"{adet}")

        text_sonuclari3.delete("1.0", END)
        text_sonuclari3.insert(END, "5'e Bölünenler")
        

    except ValueError:
        messagebox.showerror("Hata", "Lütfen başlangıç ve bitiş sayılarınızı kontrol ediniz ve geçerli bir sayı giriniz.")

def bolen_9():
    try:
        baslangic = int(entry_baslangic.get())
        bitis = int(entry_bitis.get())
        
        if baslangic > bitis:
            messagebox.showerror("Hata", "Başlangıç sayısı, bitiş sayısından küçük olmalıdır.")
            return
        
        sayilar = list(range(baslangic, bitis + 1))

        bolenler = [sayi for sayi in sayilar if sayi % 9 == 0]

        
        text_sonuclari.delete("1.0", END)
        for sayi in bolenler:
            text_sonuclari.insert(END, f"{sayi}\n")
        
        
        toplam = sum(bolenler)
        adet = len(bolenler)
        
        text_sonuclari2.delete("1.0", END)
        text_sonuclari2.insert(END, f"{toplam}")
        
        text_sonuclari1.delete("1.0", END)
        text_sonuclari1.insert(END, f"{adet}")

        text_sonuclari3.delete("1.0", END)
        text_sonuclari3.insert(END, "9'a Bölünenler")
        

    except ValueError:
        messagebox.showerror("Hata", "Lütfen başlangıç ve bitiş sayılarınızı kontrol ediniz ve geçerli bir sayı giriniz.")

def asal_listele():
    try:
        baslangic = int(entry_baslangic.get())
        bitis = int(entry_bitis.get())
        
        if baslangic > bitis:
            messagebox.showerror("Hata", "Başlangıç sayısı, bitiş sayısından küçük olmalıdır.")
            return
        if baslangic < 0:
            messagebox.showerror("Hata", "Başlangıç sayısı negatif olmamalıdır.")
            return

        sayilar = list(range(baslangic, bitis + 1))

        asal_sayilar = []

        text_sonuclari.delete("1.0", END)
        for sayi in sayilar:
            if sayi < 2:
                continue
            for i in range(2, sayi):
                if sayi % i == 0:
                    break
            else:
                asal_sayilar.append(sayi)
                text_sonuclari.insert(END, f"{sayi}\n")
        
        
        toplam = sum(asal_sayilar)
        adet = len(asal_sayilar)
        
        text_sonuclari2.delete("1.0", END)
        text_sonuclari2.insert(END, f"{toplam}")
        
        text_sonuclari1.delete("1.0", END)
        text_sonuclari1.insert(END, f"{adet}")

        text_sonuclari3.delete("1.0", END)
        text_sonuclari3.insert(END, "Asal Sayılar")

    except ValueError:
        messagebox.showerror("Hata", "Lütfen başlangıç ve bitiş sayılarınızı kontrol ediniz ve geçerli bir sayı giriniz.")

def sifirla():
    text_sonuclari.delete("1.0", END)
    text_sonuclari1.delete("1.0", END)
    text_sonuclari2.delete("1.0", END)
    text_sonuclari3.delete("1.0", END)
    entry_baslangic.delete(0, END)
    entry_bitis.delete(0, END)

pencere = Tk()
pencere.title("Dönüştürücü v1")
pencere.geometry("854x480")
pencere.config(bg="#dcf3ff")

label_baslangic = Label(pencere, bg="#dcf3ff")
label_baslangic.pack(pady=5)
Label(label_baslangic, text="Başlangıç Sayısı:", bg="#dcf3ff", fg="#301934", width=12, anchor="e").pack(side="left", padx=5)
entry_baslangic = Entry(label_baslangic, bd=2)
entry_baslangic.pack(side="right")

label_bitis = Label(pencere, bg="#dcf3ff")
label_bitis.pack(pady=5)
Label(label_bitis, text="Bitiş Sayısı:", bg="#dcf3ff", fg="#301934", width=12, anchor="e").pack(side="left", padx=5)  #anchor e sağa hizalar
entry_bitis = Entry(label_bitis, bd=2)
entry_bitis.pack(side="right")

frame_butonlar = Frame(pencere, bg="#dcf3ff")
frame_butonlar.pack(pady=10)

buton_1 = Button(frame_butonlar, text="2'ye Bölünenler", bg="#0047AB", fg="#FFFFFF", command=bolen_2)
buton_1.pack(side='left', padx=2)
buton_2 = Button(frame_butonlar, text="3'e Bölünenler", bg="#0047AB", fg="#FFFFFF", command=bolen_3)
buton_2.pack(side='left', padx=2)
buton_3 = Button(frame_butonlar, text="4'e Bölünenler", bg="#0047AB", fg="#FFFFFF", command=bolen_4)
buton_3.pack(side='left', padx=2)
buton_4 = Button(frame_butonlar, text="5'e Bölünenler", bg="#0047AB", fg="#FFFFFF", command=bolen_5)
buton_4.pack(side='left', padx=2)
buton_5 = Button(frame_butonlar, text="9'a Bölünenler", bg="#0047AB", fg="#FFFFFF", command=bolen_9)
buton_5.pack(side='left', padx=2)

buton_6 = Button(frame_butonlar, text="Asal Sayıları Listele", bg="#0047AB", fg="#FFFFFF", command=asal_listele)
buton_6.pack(side='left', padx=2)

buton_7 = Button(frame_butonlar, text="Aradaki Sayıları Listele", bg="#0047AB", fg="#FFFFFF", command=sayilari_listele)
buton_7.pack(side='left', padx=2)

buton_8 = Button(frame_butonlar, text="Sıfırla", bg="#811331", fg="#FFFFFF", command=sifirla)
buton_8.pack(side='left', padx=2)

text_sonuclari = Text(pencere, height=15, width=40)
text_sonuclari.pack(pady=5)
scrollbar = Scrollbar(pencere, command=text_sonuclari.yview, bg="#dcf3ff")
scrollbar.pack(side="right", fill="y")
text_sonuclari.config(yscrollcommand=scrollbar.set)



frame_toplamsayi = Frame(pencere, bg="#dcf3ff")
frame_toplamsayi.pack()

label_toplamsayi = Label(frame_toplamsayi, bg="#dcf3ff")
label_toplamsayi.pack(pady=5)
Label(label_toplamsayi, text="Sayı Adedi:", bg="#dcf3ff", fg="#301934", width=12, anchor="e").pack(side="left", padx=5)
text_sonuclari1 = Text(label_toplamsayi, height=1, width=20, bd=2)
text_sonuclari1.pack()

frame_sonuc = Frame(pencere, bg="#dcf3ff")
frame_sonuc.pack()

label_sonuc = Label(frame_sonuc, bg="#dcf3ff")
label_sonuc.pack(pady=5)
Label(label_sonuc, text="Toplam:", bg="#dcf3ff", fg="#301934", width=12, anchor="e").pack(side="left", padx=5)
text_sonuclari2 = Text(label_sonuc, height=1, width=20, bd=2)
text_sonuclari2.pack()

frame_islem = Frame(pencere, bg="#dcf3ff")
frame_islem.pack()

label_islem = Label(frame_islem, bg="#dcf3ff")
label_islem.pack(pady=5)
Label(label_islem, text="İşlem:", bg="#dcf3ff", fg="#301934", width=12, anchor="e").pack(side="left", padx=5)
text_sonuclari3 = Text(label_islem, height=1, width=20, bd=2)
text_sonuclari3.pack()


pencere.mainloop()
#hesap makinesi iphonedeki gibi önce standart sonra bilimsel