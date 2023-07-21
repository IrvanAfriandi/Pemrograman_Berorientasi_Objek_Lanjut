import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,CENTER,END,Tk,W,StringVar,messagebox, Menu
from PIL import Image, ImageTk
from UserMenuForm import *
from User import *
from UserlogForm import *
from UserlogForm1 import *
from FrmKamar import *
from FrmMakan import *
from FrmMinum import *
from FrmPesanan import *


class Dashboard:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("900x600+200+33")
        self.parent.title(title)
        self.parent.resizable(0,0)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.my_w_child = None
        self.bio = None
        self.editbio = None
        self.gantipaswd = None
        self.infkamar = None
        
        self.aturKomponen()
        
    def new_window( self, number, _class):
        new = tk.Toplevel()
        new.transient()
        new.grab_set()
        _class(new, number)
          
    def aturKomponen(self):
        mainFrame = Frame(self.parent, 
                          borderwidth=7, 
                          background='#43060b', 
                          relief='ridge')
        mainFrame.pack(fill=BOTH, expand=YES)
        
        gmbr = Image.open("Gambar/LoginBG.jpg")
        photo = ImageTk.PhotoImage(gmbr)
        label1 = Label(mainFrame, image=photo)
        label1.image = photo
        label1.pack(fill="both", expand=True)
        Frame(mainFrame, width=355, height=589, bg='white', borderwidth=9, relief='ridge').place(x=533,y=-3)
        F=('Consolas',16)
        l1=Label(mainFrame,text='Username',bg='white')
        l1.config(font=F)
        l1.place(x=600,y=180)
        l2=Label(mainFrame,text='Nomor Telepon',bg='white')
        l2.config(font=F)
        l2.place(x=600,y=245)
        l3=Label(mainFrame,text='Password',bg='white')
        l3.config(font=F)
        l3.place(x=600,y=310)
        l4=Label(mainFrame,text='Nomor Kamar',bg='white')
        l4.config(font=F)
        l4.place(x=600,y=375)
        self.txtUsername= Entry(mainFrame,width=20, fg='red', border=0)
        self.txtUsername.config(font=F)
        self.txtUsername.place(x=600,y=210)
        self.txtUsername.focus_set()
        self.txtUsername.bind("<Return>",self.Enter1)
        self.txtNomorTelepon= Entry(mainFrame,width=20, fg='red',border=0)
        self.txtNomorTelepon.config(font=F)
        self.txtNomorTelepon.place(x=600,y=275)
        self.txtPassword= Entry(mainFrame,width=20, fg='red',border=0)
        self.txtPassword.config(font=F, show='*')
        self.txtPassword.place(x=600,y=340)
        self.txtPassword.bind("<Return>",self.Enter2)
        self.txtNoKamar = StringVar()
        NoKamar = ttk.Combobox(mainFrame, width = 10, font=F, foreground='red', textvariable = self.txtNoKamar) 
        NoKamar.place(x=600,y=410)
        NoKamar['values'] = ('1001','1002','1003','1004','1005','1006','1007','1008','1009','1010')
        NoKamar.current()
        Frame(mainFrame,width=240,height=2,bg='#141414').place(x=600,y=240)
        Frame(mainFrame,width=240,height=2,bg='#141414').place(x=600,y=305)
        Frame(mainFrame,width=240,height=2,bg='#141414').place(x=600,y=370)
        gmbr1=Image.open("Gambar/Orang.jpg")
        photo1= ImageTk.PhotoImage(gmbr1)
        label2 = Label(image=photo1,
                    border=0,
                    justify=CENTER)
        label2.image = photo1
        label2.pack(fill="both", expand=True)
        label2.place(x=665, y=30)
        def btnlogin(x,y,text,ecolor,lcolor):
            def on_entera(e):
                myButton1['background'] = ecolor
                myButton1['foreground']= lcolor
            def on_leavea(e):
                myButton1['background'] = lcolor
                myButton1['foreground']= ecolor
            myButton1 = Button(mainFrame,text=text,
                        width=20,
                        height=2,
                        fg=ecolor,
                        border=0,
                        bg=lcolor,
                        activeforeground=lcolor,
                        activebackground=ecolor,
                        command=self.onLogin)
            myButton1.bind("<Enter>", on_entera)
            myButton1.bind("<Leave>", on_leavea)
            myButton1.place(x=x,y=y)
        btnlogin(650,490,'L O G I N','white','#6f1317') 

        def daftar(x,y,text,ecolor,lcolor):
            def on_entera(e):
                myButton1['background'] = 'white'
                myButton1['foreground']= lcolor
            def on_leavea(e):
                myButton1['background'] = 'white'
                myButton1['foreground']= ecolor
            myButton1 = Button(mainFrame,text=text,
                        width=30,
                        height=2,
                        fg=ecolor,
                        border=0,
                        bg='white',
                        activeforeground=lcolor,
                        activebackground='white',
                        command=self.menuSignIn)
            myButton1.bind("<Enter>", on_entera)
            myButton1.bind("<Leave>", on_leavea)
            myButton1.place(x=x,y=y)
        daftar(640,440,'Belum punya akun? Daftar Sekarang','blue','red')

        def lupa(x,y,text,ecolor,lcolor):
            def on_entera(e):
                myButton1['background'] = 'white'
                myButton1['foreground']= lcolor
            def on_leavea(e):
                myButton1['background'] = 'white'
                myButton1['foreground']= ecolor
            myButton1 = Button(mainFrame,text=text,
                        width=20,
                        height=2,
                        fg=ecolor,
                        border=0,
                        bg='white',
                        activeforeground=lcolor,
                        activebackground='white',
                        command=self.menuLupaPassword)
            myButton1.bind("<Enter>", on_entera)
            myButton1.bind("<Leave>", on_leavea)
            myButton1.place(x=x,y=y)
        lupa(650,530,'Lupa Password?','blue','red')

    def MenuUser(self):
        if (self.my_w_child==True):
            self.my_w_child = False
            self.my_w_child.destroy()
        else:
            self.my_w_child=tk.Toplevel(root)
            self.my_w_child.geometry("900x600+200+33")
            self.my_w_child.resizable(0,0)

            Nama = self.txtUsername.get()


            gmbr1=Image.open("Gambar/BGKamar1.jpg")
            photo1= ImageTk.PhotoImage(gmbr1)
            label1 = Label(self.my_w_child, image=photo1, border=0, justify=CENTER)
            label1.image = photo1
            label1.pack(fill="both", expand=True)
            label1.place(x=0, y=0)


            gmbr2=Image.open("Gambar/User1.png")
            photo2= ImageTk.PhotoImage(gmbr2)
            label2 = Label(self.my_w_child, image=photo2, background='#c69c6d', justify=CENTER)
            label2.image = photo2
            label2.place(x=26, y=0)

            UserNm = Label(self.my_w_child, width=22, border=0, text=Nama, font=('Consolas',15), bg='white', fg='#c69c6d')
            UserNm.pack(fill="both", expand=True)
            UserNm.place(x=1, y=160)

            gmbr3=Image.open("Gambar/Bio2.png")
            photo3= ImageTk.PhotoImage(gmbr3)
            label3 = Label(self.my_w_child, image=photo3, background='#c69c6d', justify=CENTER)
            label3.image = photo3
            label3.place(x=13, y=240)
        
            gmbr4=Image.open("Gambar/Change.png")
            photo4= ImageTk.PhotoImage(gmbr4)
            label4 = Label(self.my_w_child, image=photo4, background='#c69c6d', justify=CENTER)
            label4.image = photo4
            label4.place(x=13, y=290)

            gmbr5=Image.open("Gambar/ChgPassword.png")
            photo5= ImageTk.PhotoImage(gmbr5)
            label5 = Label(self.my_w_child, image=photo5, background='#c69c6d', justify=CENTER)
            label5.image = photo5
            label5.place(x=13, y=340)

            gmbr10=Image.open("Gambar/Info.png")
            photo10= ImageTk.PhotoImage(gmbr10)
            label10 = Label(self.my_w_child, image=photo10, background='#c69c6d', justify=CENTER)
            label10.image = photo10
            label10.place(x=13, y=390)

            gmbr7=Image.open("Gambar/MakananOrMinuman.png")
            photo7= ImageTk.PhotoImage(gmbr7)
            label7 = Label(self.my_w_child, image=photo7, background='#c69c6d', justify=CENTER)
            label7.image = photo7
            label7.place(x=13, y=440)
            
            gmbr6=Image.open("Gambar/Exit1.png")
            photo6= ImageTk.PhotoImage(gmbr6)
            label6 = Label(self.my_w_child, image=photo6, background='#c69c6d', justify=CENTER)
            label6.image = photo6
            label6.place(x=13, y=490)

            def btnBio(x,y,text,ecolor,lcolor):
                def on_entera(e):
                    myButton1['background'] = '#c69c6d'
                    myButton1['foreground']= lcolor
                def on_leavea(e):
                    myButton1['background'] = '#c69c6d'
                    myButton1['foreground']= ecolor
                myButton1 = Button(self.my_w_child ,text=text,
                            width=7,
                            height=2,
                            fg=ecolor,
                            font=('Consolas',15),
                            border=0,
                            bg='#c69c6d',
                            activeforeground=lcolor,
                            activebackground='#c69c6d',
                            command=self.inBiodata)
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
                myButton1 = Button(self.my_w_child,text=text,
                            width=12,
                            height=2,
                            fg=ecolor,
                            font=('Consolas',15),
                            border=0,
                            bg='#c69c6d',
                            activeforeground=lcolor,
                            activebackground='#c69c6d',
                            command=self.inEditBiodata)
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
                myButton1 = Button(self.my_w_child,text=text,
                            width=14,
                            height=2,
                            fg=ecolor,
                            font=('Consolas',15),
                            border=0,
                            bg='#c69c6d',
                            activeforeground=lcolor,
                            activebackground='#c69c6d',
                            command=self.GantiPasswd)
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
                myButton1 = Button(self.my_w_child,text=text,
                            width=10,
                            height=2,
                            fg=ecolor,
                            font=('Consolas',15),
                            border=0,
                            bg='#c69c6d',
                            activeforeground=lcolor,
                            activebackground='#c69c6d',
                            command=self.inInfoKamar)
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
                myButton1 = Button(self.my_w_child, text=text,
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
                myButton1 = Button(self.my_w_child, text=text,
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
    def Makan(self):
        self.new_window("", FrmMakan)
    def Minun(self):
        self.new_window("", FrmMinum)
    def MakananMinuman(self, event=None):
        if (self.roti==True):
            Frame(self.my_w_child, width=240, height=150, bg='#c69c6d', relief='ridge', border=0).place(x=0,y=475)
            Label(self.my_w_child, text='Makanan',bg='#c69c6d', fg='white', font=('Consolas',13)).place(x=65,y=535)
            Label(self.my_w_child, text='Minuman',bg='#c69c6d', fg='white', font=('Consolas',13)).place(x=145,y=535)

            gmbr8=Image.open("Gambar/Makanan.png")
            photo8= ImageTk.PhotoImage(gmbr8)
            label8 = Button(self.my_w_child, image=photo8, command=self.Makan, activebackground='#c69c6d', border=0, background='#c69c6d')
            label8.image = photo8
            label8.place(x=75, y=485)

            gmbr9=Image.open("Gambar/Minuman.png")
            photo9= ImageTk.PhotoImage(gmbr9)
            label9 = Button(self.my_w_child,image=photo9, command=self.Minun, activebackground='#c69c6d', border=0, background='#c69c6d')
            label9.image = photo9
            label9.place(x=150, y=480)

            gmbr6=Image.open("Gambar/Exit1.png")
            photo6= ImageTk.PhotoImage(gmbr6)
            label6 = Button(self.my_w_child, image=photo6, border=0, activebackground='#c69c6d', command=self.onKeluar, background='#c69c6d', justify=CENTER)
            label6.image = photo6
            label6.place(x=12, y=550)

            gmbr11=Image.open("Gambar/Panah2.png")
            photo11= ImageTk.PhotoImage(gmbr11)
            label11 = Button(self.my_w_child, image=photo11, activebackground='#c69c6d', border=0, command=self.Tutup, background='#c69c6d')
            label11.image = photo11
            label11.place(x=210, y=475)

        else:
            Frame(self.my_w_child, width=235, height=150, bg='#c69c6d', relief='ridge', border=0).place(x=0,y=480)
            gmbr6=Image.open("Gambar/Exit1.png")
            photo6= ImageTk.PhotoImage(gmbr6)
            label6 = Label(self.my_w_child, image=photo6, background='#c69c6d', justify=CENTER)
            label6.image = photo6
            label6.place(x=13, y=490)

            def btnExit(x,y,text,ecolor,lcolor):
                def on_entera(e):
                    myButton1['background'] = '#c69c6d'
                    myButton1['foreground']= lcolor
                def on_leavea(e):
                    myButton1['background'] = '#c69c6d'
                    myButton1['foreground']= ecolor
                myButton1 = Button(self.my_w_child, text=text,
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

    def menuSignIn(self):
        self.new_window("Sign In", UserlogFrm)

    def menuLupaPassword(self):
        self.new_window("Verifikasi", FrmUserlog)

    def onSimpan(self):
        self.new_window("Menu Buku", FrmUserlog)
        
        
    def Enter1(self, event=None):
            a = str(self.txtUsername.get())
            if (a==''):
                messagebox.showinfo("Pemberitahuan", "Mohon Lengkapi datanya dulu")
                self.txtUsername.focus_set()
            else:
                self.txtPassword.focus_set() 
    def Enter2(self, event=None):
            b = str(self.txtPassword.get())
            if (b==''):
                messagebox.showinfo("Pemberitahuan", "Mohon Lengkapi datanya dulu")
                self.txtPassword.focus_set()
            else:
                self.onLogin()

    def inEditBiodata(self):
        if (self.bio==True):
            self.my_w_child1.destroy()
        if (self.gantipaswd==True):
            self.my_w_child3.destroy()
        if (self.infkamar==True):
            self.my_w_child4.destroy()
        if (self.editbio==True):
            self.editbio = False
            self.my_w_child2.destroy()
            self.inBiodata()
        else:
            self.editbio = True
            self.my_w_child2=tk.Toplevel(self.parent, border=2)
            self.my_w_child2.geometry("600x390+475+200")
            self.my_w_child2.resizable(0,0)
            NomorTelepon = self.txtNomorTelepon.get()
            obj = Userlog()
            obj.get_by_NomorTelepon(NomorTelepon)

            Label(self.my_w_child2, text="Edit Biodata", font=('Consolas',25), fg='black').place(x=215, y=0)
            Label(self.my_w_child2, text="Nama :", font=('Consolas',15), fg='black').place(x=218, y=60)
            Label(self.my_w_child2, text="Nomor Telepon :", font=('Consolas',15), fg='black').place(x=118, y=95)
            Label(self.my_w_child2, text="Email :", font=('Consolas',15), fg='black').place(x=207, y=128)
            Label(self.my_w_child2, text="Jenis Kelamin :", font=('Consolas',15), fg='black').place(x=118, y=165)
            Label(self.my_w_child2, text="Alamat :", font=('Consolas',15), fg='black').place(x=194, y=230)

            self.editNama= Entry(self.my_w_child2, font=('Consolas',15),border=0, background='#f0f0f0', fg='black')
            self.editNama.place(x=290, y=60)
            self.editNama.insert(0,obj.Nama)
            self.editNomor = Entry(self.my_w_child2, font=('Consolas',15),border=0, background='#f0f0f0', fg='black')
            self.editNomor.place(x=290, y=95)
            self.editNomor.insert(0,obj.NomorTelepon)
            self.editEmail = Entry(self.my_w_child2, font=('Consolas',15),border=0, background='#f0f0f0', fg='black')
            self.editEmail.place(x=290, y=130)
            self.editEmail.insert(0,obj.Email)
            self.editAlamat = Entry(self.my_w_child2, font=('Consolas',15),border=0, background='#f0f0f0', fg='black')
            self.editAlamat.place(x=290, y=230)
            self.editAlamat.insert(0,obj.Alamat)
            self.editPass = Entry(self.my_w_child2, font=('Consolas',15),border=0, background='#f0f0f0', fg='black')
            self.editPass.place(x=290, y=2030)
            self.editPass.insert(0,obj.KataSandi)
            self.editRole = Entry(self.my_w_child2, font=('Consolas',15),border=0, background='#f0f0f0', fg='black')
            self.editRole.place(x=290, y=2030)
            self.editRole.insert(0,obj.Rolename)
            self.editGender = StringVar()
            self.L = Radiobutton(self.my_w_child2, text='Laki-laki', font=('Consolas',11), fg='black', selectcolor='white', borderwidth=4, value='Laki-Laki', variable=self.editGender)
            self.L.place(x=290, y=165)
            self.P = Radiobutton(self.my_w_child2, text='Perempuan', font=('Consolas',11), fg='black', selectcolor='white', borderwidth=4, value='Perempuan', variable=self.editGender)
            self.P.place(x=290, y=195)
            gen = obj.JenisKelamin
            if(gen=="Perempuan"):
                self.P.select()
            else:
                self.L.select() 
            def btnKamar(x,y,text,ecolor,lcolor):
                def on_entera(e):
                    btnSimpan['background'] = ecolor
                    btnSimpan['foreground']= lcolor
                def on_leavea(e):
                    btnSimpan['background'] = lcolor
                    btnSimpan['foreground']= ecolor
                btnSimpan = Button(self.my_w_child2,text=text,
                            width=15,
                            height=1,
                            font='Consolas',
                            fg=ecolor,
                            border=0,
                            bg=lcolor,
                            activeforeground=lcolor,
                            activebackground=ecolor,
                            command=self.SimpanBio)
                btnSimpan.bind("<Enter>", on_entera)
                btnSimpan.bind("<Leave>", on_leavea)
                btnSimpan.place(x=x,y=y)
            btnKamar(220,290,'Simpan','white', 'grey')

    def inBiodata(self):
        if (self.editbio==True):
            self.my_w_child2.destroy()
        if (self.gantipaswd==True):
            self.my_w_child3.destroy()
        if (self.infkamar==True):
            self.my_w_child4.destroy()
        if (self.bio==True):
            self.bio = False
            self.my_w_child1.destroy()
            self.inBiodata()
        else:
            self.bio = True
            self.my_w_child1=tk.Toplevel(root, border=2)
            self.my_w_child1.geometry("600x390+475+200")
            self.my_w_child1.resizable(0,0)
            Label(self.my_w_child1, text="Biodata", font=('Consolas',25), fg='black').place(x=255, y=0)
            NomorTelepon = self.txtNomorTelepon.get()
            IDKamar = self.txtNoKamar.get()
            obj = Userlog()
            obj.get_by_NomorTelepon(NomorTelepon)
            ojb = Kamar()
            ojb.get_by_IDKamar(IDKamar)
            Label(self.my_w_child1, text="Nama :", font=('Consolas',15), fg='black').place(x=248, y=60)
            Label(self.my_w_child1, text="Nomor Telepon :", font=('Consolas',15), fg='black').place(x=148, y=95)
            Label(self.my_w_child1, text="Email :", font=('Consolas',15), fg='black').place(x=237, y=128)
            Label(self.my_w_child1, text="Jenis Kelamin :", font=('Consolas',15), fg='black').place(x=148, y=165)
            Label(self.my_w_child1, text="Alamat :", font=('Consolas',15), fg='black').place(x=224, y=200)
            Label(self.my_w_child1, text="Nomor Kamar :", font=('Consolas',15), fg='black').place(x=171, y=235)
            Label(self.my_w_child1, text="Jenis Kamar :", font=('Consolas',15), fg='black').place(x=171, y=270)
            Label(self.my_w_child1, text="Tanggal Check IN :", font=('Consolas',15), fg='black').place(x=116, y=305)

            Label(self.my_w_child1, text=obj.Nama, font=('Consolas',15), fg='black').place(x=320, y=60)
            Label(self.my_w_child1, text=obj.NomorTelepon, font=('Consolas',15), fg='black').place(x=320, y=95)
            Label(self.my_w_child1, text=obj.Email, font=('Consolas',15), fg='black').place(x=320, y=130)
            Label(self.my_w_child1, text=obj.JenisKelamin, font=('Consolas',15), fg='black').place(x=320, y=165)
            Label(self.my_w_child1, text=obj.Alamat, font=('Consolas',15), fg='black').place(x=320, y=200)
            Label(self.my_w_child1, text=ojb.IDKamar, font=('Consolas',15), fg='black').place(x=320, y=235)
            Label(self.my_w_child1, text=ojb.KelasKamar, font=('Consolas',15), fg='black').place(x=320, y=270)
            Label(self.my_w_child1, text=ojb.CheckIN, font=('Consolas',15), fg='black').place(x=320, y=305)

    def inInfoKamar(self):
        if (self.editbio==True):
            self.my_w_child2.destroy()
        if (self.gantipaswd==True):
            self.my_w_child3.destroy()
        if (self.bio==True):
            self.my_w_child1.destroy()
        if (self.infkamar==True):
            self.infkamar = False
            self.my_w_child4.destroy()
            self.inInfoKamar()
        else:
            self.infkamar = True
            self.my_w_child4=tk.Toplevel(root, border=2)
            self.my_w_child4.geometry("600x390+475+200")
            self.my_w_child4.resizable(0,0)
            IDKamar = self.txtNoKamar.get()
            ojb = Kamar()
            ojb.get_by_IDKamar(IDKamar)
            Label(self.my_w_child4, text="Info Kamar", font=('Consolas',25), fg='black').place(x=235, y=0)
            Label(self.my_w_child4, text="Nomor Kamar\t:", font=('Consolas',15), fg='black').place(x=128, y=60)
            Label(self.my_w_child4, text="Kelas Kamar\t:", font=('Consolas',15), fg='black').place(x=128, y=95)
            Label(self.my_w_child4, text="Nama Tamu\t:", font=('Consolas',15), fg='black').place(x=128, y=128)
            Label(self.my_w_child4, text="Harga / Malam\t:", font=('Consolas',15), fg='black').place(x=128, y=165)
            Label(self.my_w_child4, text="Checkn IN\t:", font=('Consolas',15), fg='black').place(x=128, y=200)

            Label(self.my_w_child4, text=ojb.IDKamar, font=('Consolas',15), fg='black').place(x=330, y=60)
            Label(self.my_w_child4, text=ojb.KelasKamar, font=('Consolas',15), fg='black').place(x=330, y=95)
            Label(self.my_w_child4, text=ojb.Penyewa, font=('Consolas',15), fg='black').place(x=330, y=130)
            Label(self.my_w_child4, text=ojb.HargaPerMalam, font=('Consolas',15), fg='black').place(x=330, y=165)
            Label(self.my_w_child4, text=ojb.CheckIN, font=('Consolas',15), fg='black').place(x=330, y=200)

            self.editKelasKamar= Entry(self.my_w_child4)
            self.editKelasKamar.place(x=1090, y=60)
            self.editKelasKamar.insert(0,ojb.KelasKamar)
            self.editHarga= Entry(self.my_w_child4)
            self.editHarga.place(x=1090, y=60)
            self.editHarga.insert(0,ojb.HargaPerMalam)
            self.editStatusKamar= Entry(self.my_w_child4)
            self.editStatusKamar.place(x=1090, y=60)
            self.editStatusKamar.insert(0, "Kosong")

            def btnKamar(x,y,text,ecolor,lcolor):
                def on_entera(e):
                    btnSimpan['background'] = ecolor
                    btnSimpan['foreground']= lcolor
                def on_leavea(e):
                    btnSimpan['background'] = lcolor
                    btnSimpan['foreground']= ecolor
                btnSimpan = Button(self.my_w_child4,text=text,
                            width=15,
                            height=1,
                            font='Consolas',
                            fg=ecolor,
                            border=0,
                            bg=lcolor,
                            activeforeground=lcolor,
                            activebackground=ecolor,
                            command=self.inCheckOut)
                btnSimpan.bind("<Enter>", on_entera)
                btnSimpan.bind("<Leave>", on_leavea)
                btnSimpan.place(x=x,y=y)
            btnKamar(220,290,'Check OUT?','white', 'grey')

    def inCheckOut(self):
        IDKamar = self.txtNoKamar.get()
        KelasKamar = self.editKelasKamar.get()
        HargaPerMalam = self.editHarga.get()
        StatusKamar = self.editStatusKamar.get()
        Penyewa = None
        CheckIN = None
        obj = Kamar()
        obj.get_by_IDKamar(IDKamar)
        obj.IDKamar = IDKamar
        obj.KelasKamar = KelasKamar
        obj.HargaPerMalam = HargaPerMalam
        obj.StatusKamar = StatusKamar
        obj.Penyewa = Penyewa
        obj.CheckIN = CheckIN
        obj.update_by_IDKamar(IDKamar)
        messagebox.showinfo("","Berhasil Check Out")
        self.my_w_child.destroy()
  

    
    def GantiPasswd(self):
        if (self.editbio==True):
            self.my_w_child2.destroy()
        if (self.bio==True):
            self.my_w_child1.destroy()
        if (self.infkamar==True):
            self.my_w_child4.destroy()
        if (self.gantipaswd==True):
            self.gantipaswd = False
            self.my_w_child3.destroy()
            self.GantiPasswd()
        else:
            self.gantipaswd = True
            self.my_w_child3=tk.Toplevel(self.parent, border=2)
            self.my_w_child3.geometry("600x390+475+200")
            self.my_w_child3.resizable(0,0)
            NomorTelepon = self.txtNomorTelepon.get()
            obj = Userlog()
            obj.get_by_NomorTelepon(NomorTelepon)

            Label(self.my_w_child3, text="Ganti Password", font=('Consolas',25), fg='black').place(x=205, y=0)
            Label(self.my_w_child3, text="Password Sekarang", font=('Consolas',15), fg='black').place(x=120, y=80)
            Label(self.my_w_child3, text="Ulangi Password", font=('Consolas',15), fg='black').place(x=120, y=170)
            Frame(self.my_w_child3, width=240,height=2,bg='#141414').place(x=120,y=145)
            Frame(self.my_w_child3, width=240,height=2,bg='#141414').place(x=120,y=235)
            self.Verif1= Entry(self.my_w_child3, font=('Consolas',15),border=0, background='#f0f0f0', fg='black')
            self.Verif1.place(x=120, y=115)
            self.Verif2= Entry(self.my_w_child3, font=('Consolas',15),border=0, background='#f0f0f0', fg='black')
            self.Verif2.place(x=120, y=205)

            def btnVerif(x,y,text,ecolor,lcolor):
                def on_entera(e):
                    btnSimpan['background'] = ecolor
                    btnSimpan['foreground']= lcolor
                def on_leavea(e):
                    btnSimpan['background'] = lcolor
                    btnSimpan['foreground']= ecolor
                btnSimpan = Button(self.my_w_child3,text=text,
                            width=15,
                            height=1,
                            font='Consolas',
                            fg=ecolor,
                            border=0,
                            bg=lcolor,
                            activeforeground=lcolor,
                            activebackground=ecolor,
                            command=self.MenuVerifikasi)
                btnSimpan.bind("<Enter>", on_entera)
                btnSimpan.bind("<Leave>", on_leavea)
                btnSimpan.place(x=x,y=y)
            btnVerif(220,290,'Verifikasi','white', 'grey')
    
    def MenuVerifikasi(self):
        NomorTelepon = self.txtNomorTelepon.get()
        verif1 = self.Verif1.get()
        verif2 = self.Verif2.get()
        if (verif2==verif1):
            obj = Userlog()
            obj.get_by_NomorTelepon(NomorTelepon)
            Pwd = obj.KataSandi
            if (verif2==Pwd):
                Frame(self.my_w_child3, width=900 ,height=500, background='#f0f0f0').place(x=0, y=0)
                Label(self.my_w_child3, text="Ganti Password", font=('Consolas',25), fg='black').place(x=205, y=0)
                Label(self.my_w_child3, text="Password Baru", font=('Consolas',15), fg='black').place(x=120, y=80)
                Label(self.my_w_child3, text="Ulangi Password", font=('Consolas',15), fg='black').place(x=120, y=170)
                Frame(self.my_w_child3, width=240,height=2,bg='#141414').place(x=120,y=145)
                Frame(self.my_w_child3, width=240,height=2,bg='#141414').place(x=120,y=235)
                self.Pw1= Entry(self.my_w_child3, font=('Consolas',15),border=0, background='#f0f0f0', fg='black')
                self.Pw1.place(x=120, y=115)
                self.Pw2= Entry(self.my_w_child3, font=('Consolas',15),border=0, background='#f0f0f0', fg='black')
                self.Pw2.place(x=120, y=205)

                self.editNama= Entry(self.my_w_child3)
                self.editNama.place(x=2090, y=60)
                self.editNama.insert(0,obj.Nama)
                self.editNomor = Entry(self.my_w_child3)
                self.editNomor.place(x=2090, y=95)
                self.editNomor.insert(0,obj.NomorTelepon)
                self.editEmail = Entry(self.my_w_child3)
                self.editEmail.place(x=2090, y=130)
                self.editEmail.insert(0,obj.Email)
                self.editAlamat = Entry(self.my_w_child3)
                self.editAlamat.place(x=2090, y=230)
                self.editAlamat.insert(0,obj.Alamat)
                self.editGender = Entry(self.my_w_child3)
                self.editGender.place(x=2090, y=230)
                self.editGender.insert(0,obj.JenisKelamin)
                self.editRole = Entry(self.my_w_child3)
                self.editRole.place(x=2090, y=2030)
                self.editRole.insert(0,obj.Rolename)
                def btnVerif1(x,y,text,ecolor,lcolor):
                    def on_entera(e):
                        btnSimpan['background'] = ecolor
                        btnSimpan['foreground']= lcolor
                    def on_leavea(e):
                        btnSimpan['background'] = lcolor
                        btnSimpan['foreground']= ecolor
                    btnSimpan = Button(self.my_w_child3,text=text,
                                width=15,
                                height=1,
                                font='Consolas',
                                fg=ecolor,
                                border=0,
                                bg=lcolor,
                                activeforeground=lcolor,
                                activebackground=ecolor,
                                command=self.SimpanPasswd)
                    btnSimpan.bind("<Enter>", on_entera)
                    btnSimpan.bind("<Leave>", on_leavea)
                    btnSimpan.place(x=x,y=y)
                btnVerif1(220,290,'Simpan','white', 'grey')
            else:
                messagebox.showwarning("", "Password Salah")
        else:
            messagebox.showwarning("", "Password Tidak Valid")

    def SimpanPasswd(self):
        obj = Userlog()
        NomorTelepon = self.editNomor.get()
        Nama = self.editNama.get()
        Email = self.editEmail.get()
        JenisKelamin = self.editGender.get()
        Alamat = self.editAlamat.get()
        KataSandi = self.Pw2.get()
        Rolename = self.editRole.get()
        obj.NomorTelepon = NomorTelepon
        obj.Nama = Nama
        obj.Email = Email
        obj.JenisKelamin = JenisKelamin
        obj.KataSandi = KataSandi
        obj.Rolename = Rolename
        obj.Alamat = Alamat
        obj.update_by_NomorTelepon(NomorTelepon)
        self.my_w_child.destroy()
        self.my_w_child3.destroy()
        messagebox.showinfo("","Password Berhasil Diganti")
        self.MenuUser()

    def SimpanBio(self, event=None):
        obj = Userlog()
        NomorTelepon = self.editNomor.get()
        Nama = self.editNama.get()
        Email = self.editEmail.get()
        JenisKelamin = self.editGender.get()
        Alamat = self.editAlamat.get()
        KataSandi = self.editPass.get()
        Rolename = self.editRole.get()
        obj.NomorTelepon = NomorTelepon
        obj.Nama = Nama
        obj.Email = Email
        obj.JenisKelamin = JenisKelamin
        obj.KataSandi = KataSandi
        obj.Rolename = Rolename
        obj.Alamat = Alamat
        obj.update_by_NomorTelepon(NomorTelepon)
        self.my_w_child.destroy()
        self.my_w_child4.destroy()
        messagebox.showinfo("","Berhasil Menyimpan")
        self.MenuUser()
    
    def onLogin(self, event=None):
        u = self.txtUsername.get()
        p = self.txtPassword.get()
        A = User()
        B =[]
        A.Username = u
        A.Passwrd = p
        res = A.Login()
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        if(status=="success"):
            if(msg=="Tamu"):
                messagebox.showinfo("Horeee", "Login Berhasil")
                self.MenuUser()
            elif(msg=="Petugas"):
                messagebox.showwarning("Comingsoon", "Program masih dalam tahap pengembangan, Terimakasih")
            else:
                messagebox.showinfo("Maaf :(", "User Tidak Dikenal")
            
        else:
            messagebox.showinfo("Maaf :(", "Login tidak valid")
 
    def onLogout(self):
        self.aturKomponen()
                    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
if __name__ == '__main__':
    root = tk.Tk()
    my_str = tk.StringVar()
    aplikasi = Dashboard(root, "")
    root.mainloop() 