import tkinter as tk
from tkinter import messagebox, ttk
import pygame
pygame.init()
img  = pygame.image.load(r"D:\deadline\f03ac0c34cedeab3b3fc.jpg")


box1  =pygame.Rect(580,150,400,75)
box2  =pygame.Rect(495,230,500,230)



root = tk.Tk()
root.title("Lời chúc cho thầy cô")


root.geometry("400x300")


label_title = tk.Label(root, text="Chọn thầy hoặc cô:")
label_title.pack(pady=5)


title_combobox = ttk.Combobox(root, values=["Thầy", "Cô"], state="readonly")
title_combobox.pack(pady=5)
title_combobox.current(0) 


frame = tk.Frame(root)
frame.pack(pady=5)


scrollbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
scrollbar.pack(side=tk.BOTTOM, fill=tk.X)


label_teacher = tk.Label(frame, text="Nhập tên thầy/cô:")
label_teacher.pack()

entry_teacher = tk.Entry(frame, width=40, xscrollcommand=scrollbar.set)
entry_teacher.pack(pady=5)
scrollbar.config(command=entry_teacher.xview)
label_message = tk.Label(root, text="Nhập lời chúc:")
label_message.pack(pady=5)
entry_message = tk.Entry(root, width=40)
entry_message.pack(pady=5)





text = "thầy Nguyễn Văn B"
lc = "    zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zip zipzipzipzipzipzipzipzipzipzip zip zip"


def submit_greeting():
     global run, screen,img
     title = title_combobox.get()
     teacher_name = entry_teacher.get().strip()
     message = entry_message.get().strip()
     if not teacher_name or not message:
          messagebox.showerror("Lỗi", "Vui lòng nhập đủ tên thầy/cô và lời chúc!")
     else:
          run = True

          d, c = img.get_size()
          img = pygame.transform.smoothscale(img , (d/1.6, c/1.6))
          d, c = img.get_size()
          screen = pygame.display.set_mode((d,c))
          pyxtkinter()
          print(title,teacher_name)
          messagebox.showinfo("Thành công", f"Lời chúc đã được gửi đến {title} {teacher_name}")
def pyxtkinter():
     def tudongdieuchin(text, box_width, initial_size=45, min_size=10):
          size = initial_size
          font = pygame.font.Font("D:\deadline\SedgwickAve-Regular.ttf", size)
          dai, _ = font.size(text)
          while dai > box_width and size > min_size:
               size -= 1
               font = pygame.font.Font("D:\deadline\SedgwickAve-Regular.ttf", size)
               dai, _ = font.size(text)
          return font    

     def tudongngatdong(lc, box_width, box_height, initial_size=25, min_size=10):
          size = initial_size
          font = pygame.font.Font("D:\deadline\SedgwickAve-Regular.ttf", size)
          while True:
               chu = lc.split(' ')
               lines = []
               current_line = ""
               cao = 0
               for tu in chu:
                    
                    linet = current_line + tu + " "
                    rongt, caot = font.size(linet)
                    
                    if rongt <= box_width:
                         current_line = linet
                    else:
                         lines.append(current_line)
                         current_line = tu + " "
                         cao += caot
               lines.append(current_line)
               cao += caot
               if cao <= box_height or size <= min_size:
                    break
               else:
                    size -= 1
                    font = pygame.font.Font(None, size)

          return font, lines
     while run:
          screen.fill((255,0,0))
          screen.blit(img,(0,0))
          font = tudongdieuchin(text, box1.width)
          font2, lines = tudongngatdong(lc, box2.width, box2.height)
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    submit_greeting()
                    return
          dong1 = pygame.Surface((box1.width, box1.height))
          dong1.set_alpha(0)
          dong1.fill((0,0,0))
          pygame.draw.rect(dong1, (0,0,0), box1)
          #pygame.draw.rect(screen, (0,0,0), box2)
          d1 = font.render(text, True, (166,90,116))
          #d1o = font.render(text1, True,(166,90,116))
          d1r = d1.get_rect()
          #d1r = d1.get_rect(bottom= (box1.x + 5, box1.y + (box1.height - d1.get_height()) // 2))
          #screen.blit(d1o, d1r)
          screen.blit(d1, (box1.x + 5, box1.y + (box1.height - d1.get_height()) // 2))
          y_offset = box2.y + 5
          for line in lines:
               text_surface = font2.render(line, True,(73,31,56))
               line_width = text_surface.get_width()
               x_offset = box2.x + (box2.width - line_width) // 2
               screen.blit(text_surface, (x_offset,y_offset))
               y_offset += text_surface.get_height()


          #pygame.draw.rect(screen, (255,255,255), box2)
          #pygame.image.save(screen, "abc.png",)
          pygame.display.update()
submit_button = tk.Button(root, text="Gửi lời chúc", command=submit_greeting)
submit_button.pack(pady=10)

root.mainloop()