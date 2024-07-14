from tkinter import *
from tkinter import filedialog,messagebox

def manipulate():
    img=filedialog.askopenfile(mode='r')
    if img is not None:
        img_name=img.name
        key=entry.get(1.0,END)
        fi=open(img_name,'rb')
        img_byte=fi.read()
        fi.close()
        img_byte=bytearray(img_byte)
        for index,values in enumerate(img_byte):
            img_byte[index]=values^int(key)
        man_img=open(img_name,'wb')
        man_img.write(img_byte)
        man_img.close()
        messagebox.showinfo("info","Image encrypted/decrypted successfully")



if __name__=="__main__":
    root=Tk()
    root.geometry("300x150")
    root.title("Pixel Manipulation")
    b1=Button(root,text="Encrypt/Decrypt",command=manipulate)
    b1.pack(pady=30)
    lbl=Label(root,text="Enter key to encrypt/decrypt")
    lbl.pack()
    entry=Text(root,height=1,width=10)
    entry.pack()
    root.mainloop()
