import tkinter as tk
from tkinter import *
import json
from PIL import Image, ImageTk
from datetime import date
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Userlog import *
from Kamar import *

class UserlogFrm:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("900x600+200+33")
        self.parent.title(title)
        self.parent.resizable(0,0)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        self.mainFrame = Frame(self.parent, bd=10)
        self.mainFrame.pack(fill=BOTH, expand=YES)
        self.mainFrame = self.mainFrame
        gmbr1=Image.open("Gambar/SignInBG.jpg")
        photo1= ImageTk.PhotoImage(gmbr1)
        label2 = Label(self.mainFrame, 
                       image=photo1,
                       border=0,
                       justify=CENTER)
        label2.image = photo1
        label2.pack(fill="both", expand=True)
        label2.place(x=-10, y=-10)
        self.SignUp()

    def SignUp(self):
        mainFrame = self.mainFrame
        Frame(mainFrame, width=400, height=530, bg='#0a233a', relief='ridge', border=3).place(x=470,y=30)
        Frame(mainFrame,width=147,height=2, bg='white').place(x=520,y=195)
        Frame(mainFrame,width=147,height=2, bg='white').place(x=680,y=195)
        Frame(mainFrame,width=308,height=2, bg='white').place(x=520,y=265)
        Frame(mainFrame,width=308,height=2, bg='white').place(x=520,y=335)
        Frame(mainFrame,width=147,height=2, bg='white').place(x=520,y=405)
        Frame(mainFrame,width=147,height=2, bg='white').place(x=520,y=475)
        F1=('Consolas',12)
        Label(mainFrame,text='SIGN UP',bg='#0a233a', fg='white', font=('Consolas',25)).place(x=599,y=65)
        Label(mainFrame,text='Nama Depan',bg='#0a233a', fg='white', font=F1).place(x=520,y=140)
        Label(mainFrame,text='Nama Belakang',bg='#0a233a', fg='white', font=F1).place(x=680,y=140)
        Label(mainFrame,text='Email',bg='#0a233a', fg='white', font=F1).place(x=520,y=210)
        Label(mainFrame,text='Alamat',bg='#0a233a', fg='white', font=F1).place(x=520,y=280)
        Label(mainFrame,text='Nomor Telepon',bg='#0a233a', fg='white', font=F1).place(x=520,y=350)
        Label(mainFrame,text='Password',bg='#0a233a', fg='white', font=F1).place(x=520,y=420)
        Label(mainFrame,text='Jenis Kelamin',bg='#0a233a', fg='white', font=F1).place(x=715,y=380)
        self.txtNama1= Entry(mainFrame,width=16,border=0, background='#0a233a', insertbackground='white', fg='white')
        self.txtNama1.config(font=F1)
        self.txtNama1.place(x=520,y=170)
        self.txtNama1.focus_set()
        self.txtNama1.bind("<Return>",self.N1)
        self.txtNama2= Entry(mainFrame,width=16,border=0, background='#0a233a', insertbackground='white', fg='white')
        self.txtNama2.config(font=F1)
        self.txtNama2.place(x=680,y=170)
        self.txtNama2.bind("<Return>",self.N2)
        self.txtEmail= Entry(mainFrame,width=35,border=0, background='#0a233a', insertbackground='white', fg='white')
        self.txtEmail.config(font=F1)
        self.txtEmail.place(x=520,y=240)
        self.txtEmail.bind("<Return>",self.N3)
        self.txtAlamat= Entry(mainFrame,width=16,border=0, background='#0a233a', insertbackground='white', fg='white')
        self.txtAlamat.config(font=F1)
        self.txtAlamat.place(x=520,y=310)
        self.txtAlamat.bind("<Return>",self.N4)
        self.txtNomorTelepon= Entry(mainFrame,width=16,border=0, background='#0a233a', insertbackground='white', fg='white')
        self.txtNomorTelepon.config(font=F1)
        self.txtNomorTelepon.place(x=520,y=380)
        self.txtNomorTelepon.bind("<Return>",self.N5)
        self.txtPassword= Entry(mainFrame,width=16,border=0, background='#0a233a', insertbackground='white', fg='white')
        self.txtPassword.config(font=F1)
        self.txtPassword.place(x=520,y=450)
        self.txtPassword.bind("<Return>",self.N6)
        self.txtRolename = StringVar()
        self.Tamu = Radiobutton(mainFrame, text='Tamu', font=F1, fg='white', selectcolor='#0a233a', background="#0a233a", borderwidth=4, value='Tamu', variable=self.txtRolename)
        self.Tamu.place(x=720, y=410)
        self.Tamu.select()
        self.txtGender = StringVar()
        self.L = Radiobutton(mainFrame, text='Laki-laki', font=F1, fg='white', selectcolor='#0a233a', background="#0a233a", borderwidth=4, value='Laki-Laki', variable=self.txtGender)
        self.L.place(x=720, y=410)
        self.L.select()
        self.P = Radiobutton(mainFrame, text='Perempuan', font=F1, fg='white', selectcolor='#0a233a', background="#0a233a", borderwidth=4, value='Perempuan', variable=self.txtGender)
        self.P.place(x=720, y=440)
        def btnKamar(x,y,text,ecolor,lcolor):
            def on_entera(e):
                btnSimpan['background'] = ecolor
                btnSimpan['foreground']= lcolor
            def on_leavea(e):
                btnSimpan['background'] = lcolor
                btnSimpan['foreground']= ecolor
            btnSimpan = Button(mainFrame,text=text,
                        width=15,
                        height=1,
                        font='Consolas',
                        fg=ecolor,
                        border=0,
                        bg=lcolor,
                        activeforeground=lcolor,
                        activebackground=ecolor,
                        command=self.PilihKamar)
            btnSimpan.bind("<Enter>", on_entera)
            btnSimpan.bind("<Leave>", on_leavea)
            btnSimpan.place(x=x,y=y)
        btnKamar(590,500,'Pilih Kamar','#0a233a', 'white')

    def PilihKamar(self):
        Frame(self.mainFrame, width=400, height=530, bg='#0a233a', relief='ridge', border=3).place(x=470,y=30)
        Label(self.mainFrame, text='Silahkan Pilih Kamar',bg='#0a233a', fg='white', font=('Consolas',15)).place(x=560,y=75)
        def btn1001(x,y,text,ecolor,lcolor):
            def on_entera(e):
                btn1['background'] = ecolor
                btn1['foreground']= lcolor
                btn1['borderwidth']= 3
                btn1['relief']= 'groove'
            def on_leavea(e):
                btn1['background'] = lcolor
                btn1['foreground']= ecolor
                btn1['borderwidth']= 0
            btn1 = Button(self.mainFrame,text=text,
                        width=15,
                        height=1,
                        font='arial',
                        fg=ecolor,
                        border=0,
                        bg=lcolor,
                        activeforeground=lcolor,
                        activebackground=ecolor,
                        command=self.Tampil1)
            btn1.bind("<Enter>", on_entera)
            btn1.bind("<Leave>", on_leavea)
            btn1.place(x=x,y=y)
        btn1001(495,140,1001,'#0a233a', 'white')
        def btn1002(x,y,text,ecolor,lcolor):
            def on_entera(e):
                btn2['background'] = ecolor
                btn2['foreground']= lcolor
                btn2['borderwidth']= 3
                btn2['relief']= 'groove'
            def on_leavea(e):
                btn2['background'] = lcolor
                btn2['foreground']= ecolor
                btn2['borderwidth']= 0
            btn2 = Button(self.mainFrame,text=text,
                        width=15,
                        height=1,
                        font='arial',
                        fg=ecolor,
                        border=0,
                        bg=lcolor,
                        activeforeground=lcolor,
                        activebackground=ecolor,
                        command=self.Tampil2)
            btn2.bind("<Enter>", on_entera)
            btn2.bind("<Leave>", on_leavea)
            btn2.place(x=x,y=y)
        btn1002(495,190,1002,'#0a233a', 'white')
        def btn1003(x,y,text,ecolor,lcolor):
            def on_entera(e):
                btn3['background'] = ecolor
                btn3['foreground']= lcolor
                btn3['borderwidth']= 3
                btn3['relief']= 'groove'
            def on_leavea(e):
                btn3['background'] = lcolor
                btn3['foreground']= ecolor
                btn3['borderwidth']= 0
            btn3 = Button(self.mainFrame,text=text,
                        width=15,
                        height=1,
                        font='arial',
                        fg=ecolor,
                        border=0,
                        bg=lcolor,
                        activeforeground=lcolor,
                        activebackground=ecolor,
                        command=self.Tampil3)
            btn3.bind("<Enter>", on_entera)
            btn3.bind("<Leave>", on_leavea)
            btn3.place(x=x,y=y)
        btn1003(495,240,1003,'#0a233a', 'white')
        def btn1004(x,y,text,ecolor,lcolor):
            def on_entera(e):
                btn4['background'] = ecolor
                btn4['foreground']= lcolor
                btn4['borderwidth']= 3
                btn4['relief']= 'groove'
            def on_leavea(e):
                btn4['background'] = lcolor
                btn4['foreground']= ecolor
                btn4['borderwidth']= 0
            btn4 = Button(self.mainFrame,text=text,
                        width=15,
                        height=1,
                        font='arial',
                        fg=ecolor,
                        border=0,
                        bg=lcolor,
                        activeforeground=lcolor,
                        activebackground=ecolor,
                        command=self.Tampil4)
            btn4.bind("<Enter>", on_entera)
            btn4.bind("<Leave>", on_leavea)
            btn4.place(x=x,y=y)
        btn1004(495,290,1004,'#0a233a', 'white')
        def btn1005(x,y,text,ecolor,lcolor):
            def on_entera(e):
                btn5['background'] = ecolor
                btn5['foreground']= lcolor
                btn5['borderwidth']= 3
                btn5['relief']= 'groove'
            def on_leavea(e):
                btn5['background'] = lcolor
                btn5['foreground']= ecolor
                btn5['borderwidth']= 0
            btn5 = Button(self.mainFrame,text=text,
                        width=15,
                        height=1,
                        font='arial',
                        fg=ecolor,
                        border=0,
                        bg=lcolor,
                        activeforeground=lcolor,
                        activebackground=ecolor,
                        command=self.Tampil5)
            btn5.bind("<Enter>", on_entera)
            btn5.bind("<Leave>", on_leavea)
            btn5.place(x=x,y=y)
        btn1005(495,340,1005,'#0a233a', 'white')

        def btn1006(x,y,text,ecolor,lcolor):
            def on_entera(e):
                btn6['background'] = ecolor
                btn6['foreground']= lcolor
                btn6['borderwidth']= 3
                btn6['relief']= 'groove'
            def on_leavea(e):
                btn6['background'] = lcolor
                btn6['foreground']= ecolor
                btn6['borderwidth']= 0
            btn6 = Button(self.mainFrame,text=text,
                        width=15,
                        height=1,
                        font='arial',
                        fg=ecolor,
                        border=0,
                        bg=lcolor,
                        activeforeground=lcolor,
                        activebackground=ecolor,
                        command=self.Tampil6)
            btn6.bind("<Enter>", on_entera)
            btn6.bind("<Leave>", on_leavea)
            btn6.place(x=x,y=y)
        btn1006(675,140,1006,'#0a233a', 'white')
        def btn1007(x,y,text,ecolor,lcolor):
            def on_entera(e):
                btn7['background'] = ecolor
                btn7['foreground']= lcolor
                btn7['borderwidth']= 3
                btn7['relief']= 'groove'
            def on_leavea(e):
                btn7['background'] = lcolor
                btn7['foreground']= ecolor
                btn7['borderwidth']= 0
            btn7 = Button(self.mainFrame,text=text,
                        width=15,
                        height=1,
                        font='arial',
                        fg=ecolor,
                        border=0,
                        bg=lcolor,
                        activeforeground=lcolor,
                        activebackground=ecolor,
                        command=self.Tampil7)
            btn7.bind("<Enter>", on_entera)
            btn7.bind("<Leave>", on_leavea)
            btn7.place(x=x,y=y)
        btn1007(675,190,1007,'#0a233a', 'white')
        def btn1008(x,y,text,ecolor,lcolor):
            def on_entera(e):
                btn8['background'] = ecolor
                btn8['foreground']= lcolor
                btn8['borderwidth']= 3
                btn8['relief']= 'groove'
            def on_leavea(e):
                btn8['background'] = lcolor
                btn8['foreground']= ecolor
                btn8['borderwidth']= 0
            btn8 = Button(self.mainFrame,text=text,
                        width=15,
                        height=1,
                        font='arial',
                        fg=ecolor,
                        border=0,
                        bg=lcolor,
                        activeforeground=lcolor,
                        activebackground=ecolor,
                        command=self.Tampil8)
            btn8.bind("<Enter>", on_entera)
            btn8.bind("<Leave>", on_leavea)
            btn8.place(x=x,y=y)
        btn1008(675,240,1008,'#0a233a', 'white')
        def btn1009(x,y,text,ecolor,lcolor):
            def on_entera(e):
                btnv9['background'] = ecolor
                btnv9['foreground']= lcolor
                btnv9['borderwidth']= 3
                btnv9['relief']= 'groove'
            def on_leavea(e):
                btnv9['background'] = lcolor
                btnv9['foreground']= ecolor
                btnv9['borderwidth']= 0
            btnv9 = Button(self.mainFrame,text=text,
                        width=15,
                        height=1,
                        font='arial',
                        fg=ecolor,
                        border=0,
                        bg=lcolor,
                        activeforeground=lcolor,
                        activebackground=ecolor,
                        command=self.Tampil9)
            btnv9.bind("<Enter>", on_entera)
            btnv9.bind("<Leave>", on_leavea)
            btnv9.place(x=x,y=y)
        btn1009(675,290,1009,'#0a233a', 'white')
        def btn1010(x,y,text,ecolor,lcolor):
            def on_entera(e):
                btn10['background'] = ecolor
                btn10['foreground']= lcolor
                btn10['borderwidth']= 3
                btn10['relief']= 'groove'
            def on_leavea(e):
                btn10['background'] = lcolor
                btn10['foreground']= ecolor
                btn10['borderwidth']= 0
            btn10 = Button(self.mainFrame,text=text,
                        width=15,
                        height=1,
                        font='arial',
                        fg=ecolor,
                        border=0,
                        bg=lcolor,
                        activeforeground=lcolor,
                        activebackground=ecolor,
                        command=self.Tampil10)
            btn10.bind("<Enter>", on_entera)
            btn10.bind("<Leave>", on_leavea)
            btn10.place(x=x,y=y)
        btn1010(675,340,1010,'#0a233a', 'white')


    def Tampil1(self,  event=None):
        IDKamar = '1001'
        self.txtIDKamar = IDKamar
        obj = Kamar()
        a = obj.get_by_IDKamar(IDKamar)
        IDKamar = obj.IDKamar
        KelasKamar = obj.KelasKamar 
        HargaPerMalam = obj.HargaPerMalam
        StatusKamar = obj.StatusKamar
        if(len(a)>0):
            Label(self.mainFrame, text="Status\t\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=400)
            Label(self.mainFrame, text="Class\t\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=430)
            Label(self.mainFrame, text="Harga / Malam\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=460)

            Label(self.mainFrame, text=StatusKamar, width=11, anchor=W, justify=LEFT,bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=400)
            Label(self.mainFrame, text=KelasKamar, width=11, anchor=W, justify=LEFT, bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=430)
            Label(self.mainFrame, text=HargaPerMalam, bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=460)
            def btnKamar(x,y,text,ecolor,lcolor):
                def on_entera(e):
                    btnSimpan['background'] = ecolor
                    btnSimpan['foreground']= lcolor
                def on_leavea(e):
                    btnSimpan['background'] = lcolor
                    btnSimpan['foreground']= ecolor
                btnSimpan = Button(self.mainFrame,text=text,
                            width=15,
                            height=1,
                            font='Consolas',
                            fg=ecolor,
                            border=0,
                            bg=lcolor,
                            activeforeground=lcolor,
                            activebackground=ecolor,
                            command=self.onSimpan)
                btnSimpan.bind("<Enter>", on_entera)
                btnSimpan.bind("<Leave>", on_leavea)
                btnSimpan.place(x=x,y=y)
            btnKamar(590,505,'Check IN','#0a233a', 'white')
        else:
            None
    def Tampil2(self,  event=None):
        IDKamar = '1002'
        self.txtIDKamar = IDKamar
        obj = Kamar()
        a = obj.get_by_IDKamar(IDKamar)
        IDKamar = obj.IDKamar
        KelasKamar = obj.KelasKamar 
        HargaPerMalam = obj.HargaPerMalam
        StatusKamar = obj.StatusKamar
        if(len(a)>0):
            Label(self.mainFrame, text="Status\t\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=400)
            Label(self.mainFrame, text="Class\t\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=430)
            Label(self.mainFrame, text="Harga / Malam\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=460)

            Label(self.mainFrame, text=StatusKamar, width=11, anchor=W, justify=LEFT,bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=400)
            Label(self.mainFrame, text=KelasKamar, width=11, anchor=W, justify=LEFT, bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=430)
            Label(self.mainFrame, text=HargaPerMalam, bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=460)
            def btnKamar(x,y,text,ecolor,lcolor):
                def on_entera(e):
                    btnSimpan['background'] = ecolor
                    btnSimpan['foreground']= lcolor
                def on_leavea(e):
                    btnSimpan['background'] = lcolor
                    btnSimpan['foreground']= ecolor
                btnSimpan = Button(self.mainFrame,text=text,
                            width=15,
                            height=1,
                            font='Consolas',
                            fg=ecolor,
                            border=0,
                            bg=lcolor,
                            activeforeground=lcolor,
                            activebackground=ecolor,
                            command=self.onSimpan)
                btnSimpan.bind("<Enter>", on_entera)
                btnSimpan.bind("<Leave>", on_leavea)
                btnSimpan.place(x=x,y=y)
            btnKamar(590,505,'Check IN','#0a233a', 'white')
        else:
            None
    def Tampil3(self,  event=None):
        IDKamar = '1003'
        self.txtIDKamar = IDKamar
        obj = Kamar()
        a = obj.get_by_IDKamar(IDKamar)
        IDKamar = obj.IDKamar
        KelasKamar = obj.KelasKamar 
        HargaPerMalam = obj.HargaPerMalam
        StatusKamar = obj.StatusKamar
        if(len(a)>0):
            Label(self.mainFrame, text="Status\t\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=400)
            Label(self.mainFrame, text="Class\t\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=430)
            Label(self.mainFrame, text="Harga / Malam\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=460)

            Label(self.mainFrame, text=StatusKamar, width=11, anchor=W, justify=LEFT,bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=400)
            Label(self.mainFrame, text=KelasKamar, width=11, anchor=W, justify=LEFT, bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=430)
            Label(self.mainFrame, text=HargaPerMalam, bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=460)
            def btnKamar(x,y,text,ecolor,lcolor):
                def on_entera(e):
                    btnSimpan['background'] = ecolor
                    btnSimpan['foreground']= lcolor
                def on_leavea(e):
                    btnSimpan['background'] = lcolor
                    btnSimpan['foreground']= ecolor
                btnSimpan = Button(self.mainFrame,text=text,
                            width=15,
                            height=1,
                            font='Consolas',
                            fg=ecolor,
                            border=0,
                            bg=lcolor,
                            activeforeground=lcolor,
                            activebackground=ecolor,
                            command=self.onSimpan)
                btnSimpan.bind("<Enter>", on_entera)
                btnSimpan.bind("<Leave>", on_leavea)
                btnSimpan.place(x=x,y=y)
            btnKamar(590,505,'Check IN','#0a233a', 'white')
        else:
            None
    def Tampil4(self,  event=None):
        IDKamar = '1004'
        self.txtIDKamar = IDKamar
        obj = Kamar()
        a = obj.get_by_IDKamar(IDKamar)
        IDKamar = obj.IDKamar
        KelasKamar = obj.KelasKamar 
        HargaPerMalam = obj.HargaPerMalam
        StatusKamar = obj.StatusKamar
        if(len(a)>0):
            Label(self.mainFrame, text="Status\t\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=400)
            Label(self.mainFrame, text="Class\t\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=430)
            Label(self.mainFrame, text="Harga / Malam\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=460)

            Label(self.mainFrame, text=StatusKamar, width=11, anchor=W, justify=LEFT,bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=400)
            Label(self.mainFrame, text=KelasKamar, width=11, anchor=W, justify=LEFT, bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=430)
            Label(self.mainFrame, text=HargaPerMalam, bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=460)
            def btnKamar(x,y,text,ecolor,lcolor):
                def on_entera(e):
                    btnSimpan['background'] = ecolor
                    btnSimpan['foreground']= lcolor
                def on_leavea(e):
                    btnSimpan['background'] = lcolor
                    btnSimpan['foreground']= ecolor
                btnSimpan = Button(self.mainFrame,text=text,
                            width=15,
                            height=1,
                            font='Consolas',
                            fg=ecolor,
                            border=0,
                            bg=lcolor,
                            activeforeground=lcolor,
                            activebackground=ecolor,
                            command=self.onSimpan)
                btnSimpan.bind("<Enter>", on_entera)
                btnSimpan.bind("<Leave>", on_leavea)
                btnSimpan.place(x=x,y=y)
            btnKamar(590,505,'Check IN','#0a233a', 'white')
        else:
            None
    def Tampil5(self,  event=None):
        IDKamar = '1005'
        self.txtIDKamar = IDKamar
        obj = Kamar()
        a = obj.get_by_IDKamar(IDKamar)
        IDKamar = obj.IDKamar
        KelasKamar = obj.KelasKamar 
        HargaPerMalam = obj.HargaPerMalam
        StatusKamar = obj.StatusKamar
        if(len(a)>0):
            Label(self.mainFrame, text="Status\t\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=400)
            Label(self.mainFrame, text="Class\t\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=430)
            Label(self.mainFrame, text="Harga / Malam\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=460)

            Label(self.mainFrame, text=StatusKamar, width=11, anchor=W, justify=LEFT,bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=400)
            Label(self.mainFrame, text=KelasKamar, width=11, anchor=W, justify=LEFT, bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=430)
            Label(self.mainFrame, text=HargaPerMalam, bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=460)
            def btnKamar(x,y,text,ecolor,lcolor):
                def on_entera(e):
                    btnSimpan['background'] = ecolor
                    btnSimpan['foreground']= lcolor
                def on_leavea(e):
                    btnSimpan['background'] = lcolor
                    btnSimpan['foreground']= ecolor
                btnSimpan = Button(self.mainFrame,text=text,
                            width=15,
                            height=1,
                            font='Consolas',
                            fg=ecolor,
                            border=0,
                            bg=lcolor,
                            activeforeground=lcolor,
                            activebackground=ecolor,
                            command=self.onSimpan)
                btnSimpan.bind("<Enter>", on_entera)
                btnSimpan.bind("<Leave>", on_leavea)
                btnSimpan.place(x=x,y=y)
            btnKamar(590,505,'Check IN','#0a233a', 'white')
        else:
            None
    def Tampil6(self,  event=None):
        IDKamar = '1006'
        self.txtIDKamar = IDKamar
        obj = Kamar()
        a = obj.get_by_IDKamar(IDKamar)
        IDKamar = obj.IDKamar
        KelasKamar = obj.KelasKamar 
        HargaPerMalam = obj.HargaPerMalam
        StatusKamar = obj.StatusKamar
        if(len(a)>0):
            Label(self.mainFrame, text="Status\t\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=400)
            Label(self.mainFrame, text="Class\t\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=430)
            Label(self.mainFrame, text="Harga / Malam\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=460)

            Label(self.mainFrame, text=StatusKamar, width=11, anchor=W, justify=LEFT,bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=400)
            Label(self.mainFrame, text=KelasKamar, width=11, anchor=W, justify=LEFT, bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=430)
            Label(self.mainFrame, text=HargaPerMalam, bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=460)
            def btnKamar(x,y,text,ecolor,lcolor):
                def on_entera(e):
                    btnSimpan['background'] = ecolor
                    btnSimpan['foreground']= lcolor
                def on_leavea(e):
                    btnSimpan['background'] = lcolor
                    btnSimpan['foreground']= ecolor
                btnSimpan = Button(self.mainFrame,text=text,
                            width=15,
                            height=1,
                            font='Consolas',
                            fg=ecolor,
                            border=0,
                            bg=lcolor,
                            activeforeground=lcolor,
                            activebackground=ecolor,
                            command=self.onSimpan)
                btnSimpan.bind("<Enter>", on_entera)
                btnSimpan.bind("<Leave>", on_leavea)
                btnSimpan.place(x=x,y=y)
            btnKamar(590,505,'Check IN','#0a233a', 'white')
        else:
            None
    def Tampil7(self,  event=None):
        IDKamar = '1007'
        self.txtIDKamar = IDKamar
        obj = Kamar()
        a = obj.get_by_IDKamar(IDKamar)
        IDKamar = obj.IDKamar
        KelasKamar = obj.KelasKamar 
        HargaPerMalam = obj.HargaPerMalam
        StatusKamar = obj.StatusKamar
        if(len(a)>0):
            Label(self.mainFrame, text="Status\t\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=400)
            Label(self.mainFrame, text="Class\t\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=430)
            Label(self.mainFrame, text="Harga / Malam\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=460)

            Label(self.mainFrame, text=StatusKamar, width=11, anchor=W, justify=LEFT,bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=400)
            Label(self.mainFrame, text=KelasKamar, width=11, anchor=W, justify=LEFT, bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=430)
            Label(self.mainFrame, text=HargaPerMalam, bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=460)
            def btnKamar(x,y,text,ecolor,lcolor):
                def on_entera(e):
                    btnSimpan['background'] = ecolor
                    btnSimpan['foreground']= lcolor
                def on_leavea(e):
                    btnSimpan['background'] = lcolor
                    btnSimpan['foreground']= ecolor
                btnSimpan = Button(self.mainFrame,text=text,
                            width=15,
                            height=1,
                            font='Consolas',
                            fg=ecolor,
                            border=0,
                            bg=lcolor,
                            activeforeground=lcolor,
                            activebackground=ecolor,
                            command=self.onSimpan)
                btnSimpan.bind("<Enter>", on_entera)
                btnSimpan.bind("<Leave>", on_leavea)
                btnSimpan.place(x=x,y=y)
            btnKamar(590,505,'Check IN','#0a233a', 'white')
        else:
            None
    def Tampil8(self,  event=None):
        IDKamar = '1008'
        self.txtIDKamar = IDKamar
        obj = Kamar()
        a = obj.get_by_IDKamar(IDKamar)
        IDKamar = obj.IDKamar
        KelasKamar = obj.KelasKamar 
        HargaPerMalam = obj.HargaPerMalam
        StatusKamar = obj.StatusKamar
        if(len(a)>0):
            Label(self.mainFrame, text="Status\t\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=400)
            Label(self.mainFrame, text="Class\t\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=430)
            Label(self.mainFrame, text="Harga / Malam\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=460)

            Label(self.mainFrame, text=StatusKamar, width=11, anchor=W, justify=LEFT,bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=400)
            Label(self.mainFrame, text=KelasKamar, width=11, anchor=W, justify=LEFT, bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=430)
            Label(self.mainFrame, text=HargaPerMalam, bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=460)
            def btnKamar(x,y,text,ecolor,lcolor):
                def on_entera(e):
                    btnSimpan['background'] = ecolor
                    btnSimpan['foreground']= lcolor
                def on_leavea(e):
                    btnSimpan['background'] = lcolor
                    btnSimpan['foreground']= ecolor
                btnSimpan = Button(self.mainFrame,text=text,
                            width=15,
                            height=1,
                            font='Consolas',
                            fg=ecolor,
                            border=0,
                            bg=lcolor,
                            activeforeground=lcolor,
                            activebackground=ecolor,
                            command=self.onSimpan)
                btnSimpan.bind("<Enter>", on_entera)
                btnSimpan.bind("<Leave>", on_leavea)
                btnSimpan.place(x=x,y=y)
            btnKamar(590,505,'Check IN','#0a233a', 'white')
        else:
            None
    def Tampil9(self,  event=None):
        IDKamar = '1009'
        self.txtIDKamar = IDKamar
        obj = Kamar()
        a = obj.get_by_IDKamar(IDKamar)
        IDKamar = obj.IDKamar
        KelasKamar = obj.KelasKamar 
        HargaPerMalam = obj.HargaPerMalam
        StatusKamar = obj.StatusKamar
        if(len(a)>0):
            Label(self.mainFrame, text="Status\t\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=400)
            Label(self.mainFrame, text="Class\t\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=430)
            Label(self.mainFrame, text="Harga / Malam\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=460)

            Label(self.mainFrame, text=StatusKamar, width=11, anchor=W, justify=LEFT,bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=400)
            Label(self.mainFrame, text=KelasKamar, width=11, anchor=W, justify=LEFT, bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=430)
            Label(self.mainFrame, text=HargaPerMalam, bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=460)
            def btnKamar(x,y,text,ecolor,lcolor):
                def on_entera(e):
                    btnSimpan['background'] = ecolor
                    btnSimpan['foreground']= lcolor
                def on_leavea(e):
                    btnSimpan['background'] = lcolor
                    btnSimpan['foreground']= ecolor
                btnSimpan = Button(self.mainFrame,text=text,
                            width=15,
                            height=1,
                            font='Consolas',
                            fg=ecolor,
                            border=0,
                            bg=lcolor,
                            activeforeground=lcolor,
                            activebackground=ecolor,
                            command=self.onSimpan)
                btnSimpan.bind("<Enter>", on_entera)
                btnSimpan.bind("<Leave>", on_leavea)
                btnSimpan.place(x=x,y=y)
            btnKamar(590,505,'Check IN','#0a233a', 'white')
        else:
            None
    def Tampil10(self,  event=None):
        IDKamar = '1010'
        self.txtIDKamar = IDKamar
        obj = Kamar()
        a = obj.get_by_IDKamar(IDKamar)
        IDKamar = obj.IDKamar
        KelasKamar = obj.KelasKamar 
        HargaPerMalam = obj.HargaPerMalam
        StatusKamar = obj.StatusKamar
        if(len(a)>0):
            Label(self.mainFrame, text="Status\t\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=400)
            Label(self.mainFrame, text="Class\t\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=430)
            Label(self.mainFrame, text="Harga / Malam\t=", bg='#0a233a', fg='white', font=('Consolas',13)).place(x=535,y=460)

            Label(self.mainFrame, text=StatusKamar, width=11, anchor=W, justify=LEFT,bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=400)
            Label(self.mainFrame, text=KelasKamar, width=11, anchor=W, justify=LEFT, bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=430)
            Label(self.mainFrame, text=HargaPerMalam, bg='#0a233a', fg='white', font=('Consolas',13)).place(x=700,y=460)
            def btnKamar(x,y,text,ecolor,lcolor):
                def on_entera(e):
                    btnSimpan['background'] = ecolor
                    btnSimpan['foreground']= lcolor
                def on_leavea(e):
                    btnSimpan['background'] = lcolor
                    btnSimpan['foreground']= ecolor
                btnSimpan = Button(self.mainFrame,text=text,
                            width=15,
                            height=1,
                            font='Consolas',
                            fg=ecolor,
                            border=0,
                            bg=lcolor,
                            activeforeground=lcolor,
                            activebackground=ecolor,
                            command=self.onSimpan)
                btnSimpan.bind("<Enter>", on_entera)
                btnSimpan.bind("<Leave>", on_leavea)
                btnSimpan.place(x=x,y=y)
            btnKamar(590,505,'Check IN','#0a233a', 'white')
        else:
            None

    def N1(self, event=None):
            a = str(self.txtNama1.get())
            if (a==''):
                messagebox.showinfo("Pemberitahuan", "Mohon Lengkapi datanya dulu")
                self.txtNama1.focus_set()
            else:
                self.txtNama2.focus_set() 
    def N2(self, event=None):
            a = str(self.txtNama2.get())
            if (a==''):
                messagebox.showinfo("Pemberitahuan", "Mohon Lengkapi datanya dulu")
                self.txtNama2.focus_set()
            else:
                self.txtEmail.focus_set() 
    def N3(self, event=None):
            a = str(self.txtEmail.get())
            if (a==''):
                messagebox.showinfo("Pemberitahuan", "Mohon Lengkapi datanya dulu")
                self.txtEmail.focus_set()
            else:
                self.txtAlamat.focus_set() 
    def N4(self, event=None):
            a = str(self.txtAlamat.get())
            if (a==''):
                messagebox.showinfo("Pemberitahuan", "Mohon Lengkapi datanya dulu")
                self.txtAlamat.focus_set()
            else:
                self.txtNomorTelepon.focus_set() 
    def N5(self, event=None):
            a = str(self.txtNomorTelepon.get())
            if (a==''):
                messagebox.showinfo("Pemberitahuan", "Mohon Lengkapi datanya dulu")
                self.txtNomorTelepon.focus_set()
            else:
                self.txtPassword.focus_set() 
    def N6(self, event=None):
            a = str(self.txtPassword.get())
            if (a==''):
                messagebox.showinfo("Pemberitahuan", "Mohon Lengkapi datanya dulu")
                self.txtPassword.focus_set()
            else:
                self.onCari()
        
    def onReload(self, event=None):
        obj = Userlog()
        result = obj.get_all()
        parsed_data = json.loads(result)
        self.ditemukan = False
    def onCari(self, event=None):
        NomorTelepon = self.txtNomorTelepon.get()
        obj = Userlog()
        a = obj.get_by_NomorTelepon(NomorTelepon)
        if(len(a)>0):
            self.ditemukan = True
            messagebox.showinfo("Info", "Nomor Telepn Sudah Digunakan" )
            self.txtNomorTelepon.focus_set()
        else:
            self.ditemukan = False
            self.onSimpan()
    def Tanggal(self):
        self.sekarang = date.today() 
        return self.sekarang
    def onSimpan(self, event=None):
        Nama1 = self.txtNama1.get()
        Nama2 = self.txtNama2.get()
        self.Nama = Nama1+" "+Nama2
        Nama = self.Nama
        NomorTelepon = self.txtNomorTelepon.get()
        Gender = self.txtGender.get()
        Email = self.txtEmail.get()
        Alamat = self.txtAlamat.get()
        Rolename = self.txtRolename.get()
        Pass = self.txtPassword.get()
        obj = Userlog()
        obj.Nama = Nama
        obj.NomorTelepon = NomorTelepon
        obj.JenisKelamin = Gender
        obj.Email = Email
        obj.Alamat = Alamat
        obj.Rolename = Rolename
        obj.KataSandi = Pass
        res = obj.simpan()
        json.loads(res)
        self.CheckIN()
        self.onKeluar()
        messagebox.showinfo("Data Berhasil Disimpan", "Selamat Datang "+Nama)

    def CheckIN(self):
        Nama = self.Nama
        KamarID = self.txtIDKamar
        kmr = Kamar()
        kmr.get_by_IDKamar(KamarID)
        KmrID = kmr.IDKamar
        KlsKmr = kmr.KelasKamar
        Harga = kmr.HargaPerMalam
        StatusKmr = "Isi"
        Pnyewa = Nama
        ChIn = self.Tanggal()
        
        kmr.IDKamar = KmrID
        kmr.KelasKamar = KlsKmr
        kmr.HargaPerMalam = Harga
        kmr.Penyewa = Pnyewa
        kmr.StatusKamar = StatusKmr
        kmr.CheckIN = ChIn
        kmr.update_by_IDKamar(KmrID)

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = UserlogFrm(root2, "Aplikasi Data Datahotel")
    root2.mainloop()