from tkinter import *
from tkinter import ttk, messagebox # messagebox จะเป็น pop-up message

GUI = Tk()
GUI.title('โปรแกรมทดลองคำนวณ')
GUI.geometry('700x500')

bg = PhotoImage(file='car.png')
#bg = PhotoImage(file='C:\\Users\\admin\\Documents\\Basic Python//cars.png') #ใช้ path ยาว
BG = Label(GUI,image=bg)
BG.pack()

L = Label(GUI,text = 'กรอกจำนวนปลา (kg)', font=(None,20)) #font=(font-name, font-size)
L.pack()

v_quantity = StringVar() # เป็นตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
e1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None,20)) #textvariable เป็นตัวแปรพิเศษที่สร้างขึ้นมาเพื่อเก็บข้อความ
e1.pack()

def Cal():
	try: #ดักจับ error
		quan = float(v_quantity.get())
		calc = quan * 39 # คำนวณกิโลละ 39 บาท
		messagebox.showinfo('ราคาทั้งหมด', 'ราคาปลาทั้งหมด {} บาท'.format(calc))
		v_quantity.set('0') # ตัวเลข default
	except:
		messagebox.showwarning('Wrong input', 'Input number only')
		v_quantity.set('0') # ตัวเลข default

B = ttk.Button(GUI, text='คำนวณ', command=Cal)
B.pack(ipadx=20, ipady=10) # ipadx ขยายความกว้าง x/y



GUI.mainloop() #เพื่อให้โปรแกรมรันตลอดเวลา