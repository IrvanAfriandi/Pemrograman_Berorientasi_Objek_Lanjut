import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from tkinter import *
from Userlog import *
from PIL import Image, ImageTk
class FrmUserlog:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("900x600+200+33")
        self.parent.title(title)
        self.parent.resizable(0,0)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        gmbr1=Image.open("Gambar/LupassBG.jpg")
        photo1= ImageTk.PhotoImage(gmbr1)
        label2 = Label(mainFrame, 
                       image=photo1,
                       border=0,
                       justify=CENTER)
        label2.image = photo1
        label2.pack(fill="both", expand=True)
        label2.place(x=-10, y=-10)

        F1=('Consolas',12)
        B = '#0a233a'
        Label(mainFrame,text='Lengkapi Data',bg='#0a233a', fg='white', font=('Consolas',25)).place(x=80,y=105)
        Label(mainFrame,text='Nama Lengkap',bg='#0a233a', fg='white', font=F1).place(x=40,y=170)
        Label(mainFrame,text='Nomor Telepon',bg='#0a233a', fg='white', font=F1).place(x=40,y=240)
        Label(mainFrame,text='Email',bg='#0a233a', fg='white', font=F1).place(x=40,y=320)

        self.txtNama= Entry(mainFrame,width=36,border=0, background='white', insertbackground='red', fg=B)
        self.txtNama.config(font=F1)
        self.txtNama.place(x=40,y=200)
        self.txtNama.focus_set()

        self.txtNomorTelepon= Entry(mainFrame,width=36,border=0, background='white', insertbackground='red', fg=B)
        self.txtNomorTelepon.config(font=F1)
        self.txtNomorTelepon.place(x=40,y=270)

        self.txtEmail= Entry(mainFrame,width=36,border=0, background='white', insertbackground='red', fg=B)
        self.txtEmail.config(font=F1)
        self.txtEmail.place(x=40,y=350)
        def btnVerif(x,y,text,ecolor,lcolor):
                def on_entera(e):
                    self.btnSimpan['background'] = ecolor
                    self.btnSimpan['foreground']= lcolor
                def on_leavea(e):
                    self.btnSimpan['background'] = lcolor
                    self.btnSimpan['foreground']= ecolor
                self.btnSimpan = Button(mainFrame,text=text,
                            width=13,
                            height=1,
                            font='Consolas',
                            fg=ecolor,
                            border=0,
                            bg=lcolor,
                            activeforeground=lcolor,
                            activebackground=ecolor,
                            command=self.onCari)
                self.btnSimpan.bind("<Enter>", on_entera)
                self.btnSimpan.bind("<Leave>", on_leavea)
                self.btnSimpan.place(x=x,y=y)
        btnVerif(130,430,'Verifikasi','#0a233a', 'white')

    def onCari(self, event=None):
        NoTelp = self.txtNomorTelepon.get()
        if not NoTelp or NoTelp == "0":
            messagebox.showinfo("Maaf", "Data Yang Anda Masukkan Tidak Ditemukan")
        elif not NoTelp.isdigit():
            messagebox.showwarning("Peringatan", "Nomor telepon harus berupa angka.")
        else:
            NomorTelepon = self.txtNomorTelepon.get()
            obj = Userlog()
            a = obj.get_by_NomorTelepon(NomorTelepon)
            Password = obj.KataSandi
            if(len(a)>0):
                self.onKeluar()
                messagebox.showinfo("Data Ditemukan", "Password Anda Adalah : " +Password)
            else:
                messagebox.showinfo("showinfo", "Data Tidak Ditemukan")


    def onKeluar(self, event=None):
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmUserlog(root2, "Aplikasi Data Userlog")
    root2.mainloop()
