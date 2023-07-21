import tkinter as tk
from tkinter import *
import json
from PIL import Image, ImageTk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Userlog import *

class UserMenu:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("900x600+200+33")
        self.parent.title(title)
        self.parent.resizable(0,0)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        self.roti = None
        
    def aturKomponen(self):
        self.mainFrame = Frame(self.parent, bd=10)
        self.mainFrame.pack(fill=BOTH, expand=YES)

        obj = Userlog()
        obj.get_all()
        Nama = obj.Nama

        Label(self.mainFrame, text=Nama, font=('Consolas',15), fg='black').place(x=100, y=0)
        
        gmbr1=Image.open("Gambar/BGKamar1.jpg")
        photo1= ImageTk.PhotoImage(gmbr1)
        label1 = Label(self.mainFrame, image=photo1, border=0, justify=CENTER)
        label1.image = photo1
        label1.pack(fill="both", expand=True)
        label1.place(x=-10, y=-10)

        gmbr2=Image.open("Gambar/User1.png")
        photo2= ImageTk.PhotoImage(gmbr2)
        label2 = Label(self.mainFrame, image=photo2, background='#c69c6d', justify=CENTER)
        label2.image = photo2
        label2.place(x=26, y=0)

        gmbr3=Image.open("Gambar/Bio2.png")
        photo3= ImageTk.PhotoImage(gmbr3)
        label3 = Label(self.mainFrame, image=photo3, background='#c69c6d', justify=CENTER)
        label3.image = photo3
        label3.place(x=13, y=240)
    
        gmbr4=Image.open("Gambar/Change.png")
        photo4= ImageTk.PhotoImage(gmbr4)
        label4 = Label(self.mainFrame, image=photo4, background='#c69c6d', justify=CENTER)
        label4.image = photo4
        label4.place(x=13, y=290)

        gmbr5=Image.open("Gambar/ChgPassword.png")
        photo5= ImageTk.PhotoImage(gmbr5)
        label5 = Label(self.mainFrame, image=photo5, background='#c69c6d', justify=CENTER)
        label5.image = photo5
        label5.place(x=13, y=340)

        gmbr10=Image.open("Gambar/Info.png")
        photo10= ImageTk.PhotoImage(gmbr10)
        label10 = Label(self.mainFrame, image=photo10, background='#c69c6d', justify=CENTER)
        label10.image = photo10
        label10.place(x=13, y=390)

        gmbr7=Image.open("Gambar/MakananOrMinuman.png")
        photo7= ImageTk.PhotoImage(gmbr7)
        label7 = Label(self.mainFrame, image=photo7, background='#c69c6d', justify=CENTER)
        label7.image = photo7
        label7.place(x=13, y=440)
        
        gmbr6=Image.open("Gambar/Exit1.png")
        photo6= ImageTk.PhotoImage(gmbr6)
        label6 = Label(self.mainFrame, image=photo6, background='#c69c6d', justify=CENTER)
        label6.image = photo6
        label6.place(x=13, y=490)

        def btnBio(x,y,text,ecolor,lcolor):
            def on_entera(e):
                myButton1['background'] = '#c69c6d'
                myButton1['foreground']= lcolor
            def on_leavea(e):
                myButton1['background'] = '#c69c6d'
                myButton1['foreground']= ecolor
            myButton1 = Button(self.mainFrame,text=text,
                        width=7,
                        height=2,
                        fg=ecolor,
                        font=('Consolas',15),
                        border=0,
                        bg='#c69c6d',
                        activeforeground=lcolor,
                        activebackground='#c69c6d',
                        command=self.onSimpan)
            myButton1.bind("<Enter>", on_entera)
            myButton1.bind("<Leave>", on_leavea)
            myButton1.place(x=x,y=y)
        btnBio(55,225,'Biodata','white','#BDC3C7') 

        def btnGantiBio(x,y,text,ecolor,lcolor):
            def on_entera(e):
                myButton1['background'] = '#c69c6d'
                myButton1['foreground']= lcolor
            def on_leavea(e):
                myButton1['background'] = '#c69c6d'
                myButton1['foreground']= ecolor
            myButton1 = Button(self.mainFrame,text=text,
                        width=12,
                        height=2,
                        fg=ecolor,
                        font=('Consolas',15),
                        border=0,
                        bg='#c69c6d',
                        activeforeground=lcolor,
                        activebackground='#c69c6d',
                        command=self.onSimpan)
            myButton1.bind("<Enter>", on_entera)
            myButton1.bind("<Leave>", on_leavea)
            myButton1.place(x=x,y=y)
        btnGantiBio(54,279,'Edit Biodata','white','#BDC3C7') 

        def btnGantiPass(x,y,text,ecolor,lcolor):
            def on_entera(e):
                myButton1['background'] = '#c69c6d'
                myButton1['foreground']= lcolor
            def on_leavea(e):
                myButton1['background'] = '#c69c6d'
                myButton1['foreground']= ecolor
            myButton1 = Button(self.mainFrame,text=text,
                        width=14,
                        height=2,
                        fg=ecolor,
                        font=('Consolas',15),
                        border=0,
                        bg='#c69c6d',
                        activeforeground=lcolor,
                        activebackground='#c69c6d',
                        command=self.onSimpan)
            myButton1.bind("<Enter>", on_entera)
            myButton1.bind("<Leave>", on_leavea)
            myButton1.place(x=x,y=y)
        btnGantiPass(54,328,'Ganti Password','white','#BDC3C7') 

        def btnInfoKamar(x,y,text,ecolor,lcolor):
            def on_entera(e):
                myButton1['background'] = '#c69c6d'
                myButton1['foreground']= lcolor
            def on_leavea(e):
                myButton1['background'] = '#c69c6d'
                myButton1['foreground']= ecolor
            myButton1 = Button(self.mainFrame,text=text,
                        width=10,
                        height=2,
                        fg=ecolor,
                        font=('Consolas',15),
                        border=0,
                        bg='#c69c6d',
                        activeforeground=lcolor,
                        activebackground='#c69c6d',
                        command=self.onSimpan)
            myButton1.bind("<Enter>", on_entera)
            myButton1.bind("<Leave>", on_leavea)
            myButton1.place(x=x,y=y)
        btnInfoKamar(54,377,'Info Kamar','white','#BDC3C7')

        def btnExit(x,y,text,ecolor,lcolor):
            def on_entera(e):
                myButton1['background'] = '#c69c6d'
                myButton1['foreground']= lcolor
            def on_leavea(e):
                myButton1['background'] = '#c69c6d'
                myButton1['foreground']= ecolor
            myButton1 = Button(self.mainFrame, text=text,
                        width=6,
                        height=2,
                        fg=ecolor,
                        font=('Consolas',15),
                        border=0,
                        bg='#c69c6d',
                        activeforeground=lcolor,
                        activebackground='#c69c6d',
                        command=self.onKeluar)
            myButton1.bind("<Enter>", on_entera)
            myButton1.bind("<Leave>", on_leavea)
            myButton1.place(x=x,y=y)
        btnExit(54,477,'Keluar','white','#BDC3C7')

        def btnOrder(x,y,text,ecolor,lcolor):
            def on_entera(e):
                myButton1['background'] = '#c69c6d'
                myButton1['foreground']= lcolor
            def on_leavea(e):
                myButton1['background'] = '#c69c6d'
                myButton1['foreground']= ecolor
            myButton1 = Button(self.mainFrame, text=text,
                        width=14,
                        height=2,
                        fg=ecolor,
                        font=('Consolas',15),
                        border=0,
                        bg='#c69c6d',
                        activeforeground=lcolor,
                        activebackground='#c69c6d',
                        command=self.Buka)
            myButton1.bind("<Enter>", on_entera)
            myButton1.bind("<Leave>", on_leavea)
            myButton1.place(x=x,y=y)
        btnOrder(55,425,'Delivery Order','white','#BDC3C7')

    def MakananMinuman(self, event=None):
        if (self.roti==True):
            Frame(self.mainFrame, width=240, height=150, bg='#c69c6d', relief='ridge', border=0).place(x=0,y=475)
            Label(self.mainFrame, text='Makanan',bg='#c69c6d', fg='white', font=('Consolas',13)).place(x=65,y=535)
            Label(self.mainFrame, text='Minuman',bg='#c69c6d', fg='white', font=('Consolas',13)).place(x=145,y=535)

            gmbr8=Image.open("Gambar/Makanan.png")
            photo8= ImageTk.PhotoImage(gmbr8)
            label8 = Button(self.mainFrame, image=photo8, activebackground='#c69c6d', border=0, background='#c69c6d')
            label8.image = photo8
            label8.place(x=75, y=485)

            gmbr9=Image.open("Gambar/Minuman.png")
            photo9= ImageTk.PhotoImage(gmbr9)
            label9 = Button(self.mainFrame,image=photo9, activebackground='#c69c6d', border=0, background='#c69c6d')
            label9.image = photo9
            label9.place(x=150, y=480)

            gmbr6=Image.open("Gambar/Exit1.png")
            photo6= ImageTk.PhotoImage(gmbr6)
            label6 = Button(self.mainFrame, image=photo6, border=0, activebackground='#c69c6d', command=self.onKeluar, background='#c69c6d', justify=CENTER)
            label6.image = photo6
            label6.place(x=12, y=550)

            gmbr11=Image.open("Gambar/Panah2.png")
            photo11= ImageTk.PhotoImage(gmbr11)
            label11 = Button(self.mainFrame, image=photo11, activebackground='#c69c6d', border=0, command=self.Tutup, background='#c69c6d')
            label11.image = photo11
            label11.place(x=210, y=475)

        else:
            Frame(self.mainFrame, width=235, height=150, bg='#c69c6d', relief='ridge', border=0).place(x=0,y=480)
            gmbr6=Image.open("Gambar/Exit1.png")
            photo6= ImageTk.PhotoImage(gmbr6)
            label6 = Label(self.mainFrame, image=photo6, background='#c69c6d', justify=CENTER)
            label6.image = photo6
            label6.place(x=13, y=490)

            def btnExit(x,y,text,ecolor,lcolor):
                def on_entera(e):
                    myButton1['background'] = '#c69c6d'
                    myButton1['foreground']= lcolor
                def on_leavea(e):
                    myButton1['background'] = '#c69c6d'
                    myButton1['foreground']= ecolor
                myButton1 = Button(self.mainFrame, text=text,
                            width=6,
                            height=2,
                            fg=ecolor,
                            font=('Consolas',15),
                            border=0,
                            bg='#c69c6d',
                            activeforeground=lcolor,
                            activebackground='#c69c6d',
                            command=self.onKeluar)
                myButton1.bind("<Enter>", on_entera)
                myButton1.bind("<Leave>", on_leavea)
                myButton1.place(x=x,y=y)
            btnExit(54,477,'Keluar','white','#BDC3C7')

    def Tutup(self):
        self.roti = False
        self.MakananMinuman()
    def Buka(self):
        self.roti = True
        self.MakananMinuman()     
        
    def onClear(self, event=None):
        self.txtNomorTelepon.delete(0,END)
        self.txtNomorTelepon.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")
        self.txtEmail.delete(0,END)
        self.txtEmail.insert(END,"")
        self.txtJenisKelamin.set("")
        self.txtKataSandi.delete(0,END)
        self.txtKataSandi.insert(END,"")
        self.txtRolename.set("")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data userlog
        obj = Userlog()
        result = obj.get_all()
        parsed_data = json.loads(result)
    def onCari(self, event=None):
        NomorTelepon = self.txtNomorTelepon.get()
        obj = Userlog()
        a = obj.get_by_NomorTelepon(NomorTelepon)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        NomorTelepon = self.txtNomorTelepon.get()
        obj = Userlog()
        res = obj.get_by_NomorTelepon(NomorTelepon)
        self.txtNomorTelepon.delete(0,END)
        self.txtNomorTelepon.insert(END,obj.NomorTelepon)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,obj.Nama)
        self.txtEmail.delete(0,END)
        self.txtEmail.insert(END,obj.Email)
        self.txtJenisKelamin.set(obj.JenisKelamin)
        self.txtKataSandi.delete(0,END)
        self.txtKataSandi.insert(END,obj.KataSandi)
        self.txtRolename.set(obj.Rolename)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        NomorTelepon = self.txtNomorTelepon.get()
        Nama = self.txtNama.get()
        Email = self.txtEmail.get()
        JenisKelamin = self.txtJenisKelamin.get()
        KataSandi = self.txtKataSandi.get()
        Rolename = self.txtRolename.get()
        # create new Object
        obj = Userlog()
        obj.NomorTelepon = NomorTelepon
        obj.Nama = Nama
        obj.Email = Email
        obj.JenisKelamin = JenisKelamin
        obj.KataSandi = KataSandi
        obj.Rolename = Rolename
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_NomorTelepon(NomorTelepon)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        NomorTelepon = self.txtNomorTelepon.get()
        obj = Userlog()
        obj.NomorTelepon = NomorTelepon
        if(self.ditemukan==True):
            res = obj.delete_by_NomorTelepon(NomorTelepon)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = UserMenu(root2, "Aplikasi Data Userlog")
    root2.mainloop()
