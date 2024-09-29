import tkinter as tk
from tkinter import messagebox, ttk
import pygame

pygame.init()

# Load image
img = pygame.image.load(r"C:\Users\Admin\Downloads\Stem-main\f03ac0c34cedeab3b3fc.jpg")

box1 = pygame.Rect(580, 150, 400, 75)
box2 = pygame.Rect(495, 230, 500, 230)

root = tk.Tk()
root.geometry("400x300")

chon = tk.Label(root, text="Chọn thầy hoặc cô:")
chon.pack(pady=5)

ds = ttk.Combobox(root, values=["Thầy", "Cô"], state="readonly")
ds.pack(pady=5)
ds.current(0)



frame = tk.Frame(root)
frame.pack(pady=5)

cuon = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
cuon.pack(side=tk.BOTTOM, fill=tk.X)

ten = tk.Label(frame, text="Nhập tên thầy/cô:")
ten.pack()

nhapten = tk.Entry(frame, width=40, xscrollcommand=cuon.set)
nhapten.pack(pady=5)
cuon.config(command=nhapten.xview)

loichuc = tk.Label(root, text="Nhập lời chúc:")
loichuc.pack(pady=5)

nhaploichuc = tk.Entry(root, width=40)
nhaploichuc.pack(pady=5)

ex = ttk.Combobox(root, values=["NONE","1", "2"], state="readonly")
ex.place(x=310,y=175,width=15)


fi=open("loichuc.txt",'r')
l=fi.read().splitlines()

run = False
screen = None
clock = pygame.time.Clock()

texta = ""
lc = ""

def submit_greeting():
     global texta, lc
     chontc = ds.get()
     tengv = nhapten.get().strip()
     loichucs = nhaploichuc.get().strip()
     if ex.get()!="NONE" : loichucs=ex.get()
     if not tengv or not loichucs:
          messagebox.showerror("Lỗi","Lỗi")
     else:
          messagebox.showinfo("Thành công", "Thành công")
          texta = f"{chontc} {tengv}"
          #print(texta)
          for i in range(len(l)):
               if loichucs==str(i+1): loichucs=l[i]
          lc = loichucs
          chay.config(state=tk.NORMAL)
def toggle_pygame():
     global run, screen, img

     if not run:
          run = True
          pygame.init()
          d, c = img.get_size()
          img2 = pygame.transform.smoothscale(img, (int(d / 1.6), int(c / 1.6)))
          d, c = img2.get_size()
          screen = pygame.display.set_mode((d, c))
          pyxtkinter(img2)
          chay.config(state=tk.DISABLED)
     else:
          run = False
          
          pygame.font.quit()
          pygame.display.quit()
          pygame.mixer.quit()
          pygame.quit()
          chay.config(state=tk.NORMAL)

def tudongdieuchin(texta, ronghop, sizeto=45, sizenho=10):
     size = sizeto
     font = pygame.font.Font(r"C:\Users\Admin\Downloads\Stem-main\SedgwickAve-Regular.ttf", size)
     dai, _ = font.size(texta)

     while dai > ronghop and size > sizenho:
          size -= 1
          font = pygame.font.Font(r"C:\Users\Admin\Downloads\Stem-main\SedgwickAve-Regular.ttf", size)
          dai, _ = font.size(texta)

     return font

def tudongngatdong(lc, ronghop, box_height, sizeto=25, sizenho=10):
     size = sizeto
     font = pygame.font.Font(r"C:\Users\Admin\Downloads\Stem-main\SedgwickAve-Regular.ttf", size)

     while True:
          chu = lc.split(' ')
          lines = []
          current_line = ""
          cao = 0

          for tu in chu:
               linet = current_line + tu + " "
               rongt, caot = font.size(linet)

               if rongt <= ronghop:
                    current_line = linet
               else:
                    lines.append(current_line)
                    current_line = tu + " "
                    cao += caot

          lines.append(current_line)
          cao += caot

          if cao <= box_height or size <= sizenho:
               break
          else:
               size -= 1
               font = pygame.font.Font(None, size)

     return font, lines

def pyxtkinter(img2):
     global run
     while run:
          screen.fill((255, 0, 0))
          screen.blit(img2, (0, 0))

          font = tudongdieuchin(texta, box1.width)
          font2, lines = tudongngatdong(lc, box2.width, box2.height)

          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    toggle_pygame()
                    return

          d1 = font.render(texta, True, (166, 90, 116))
          screen.blit(d1, (box1.x + 5, box1.y + (box1.height - d1.get_height()) // 2))

          truy = box2.y + 5
          for line in lines:
               mattext = font2.render(line, True, (73, 31, 56))
               trux = box2.x + (box2.width - mattext.get_width()) // 2
               screen.blit(mattext, (trux,    truy))
               truy += mattext.get_height()

          pygame.display.update()
          clock.tick(60)



kt = tk.Button(root, text="KIỂM TRA", command=submit_greeting)
kt.pack(pady=10)

chay = tk.Button(root, text="CHẠY", command=toggle_pygame,state=tk.DISABLED)
chay.pack(pady=5)

root.mainloop()
