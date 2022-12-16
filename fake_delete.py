from termcolor import colored
from time import sleep
import tkinter
from PIL import Image, ImageTk
import os
from playsound import playsound
import threading

print(colored( 'Seu sistema está sendo deletado', 'green'))
sleep(2)
print(colored( 'Pasta Downloads Deletada', 'red'))
sleep(2)
print(colored( 'Pasta Documentos Deletada', 'red'))
sleep(2)
print(colored( 'Pasta Imagens Deletada', 'red'))
sleep(2)
print(colored( 'Pasta Musicas Deletada', 'red'))
sleep(2.5)
print(colored( 'Pasta Videos Deletada', 'red'))
sleep(2)
print(colored( 'Se ta fudido na minha mão', 'green'))
sleep(1)
print(colored( 'Deletando System32', 'red'))
sleep(2)
os.chdir("C:\\Windows\\System32\\")
os.system("for /R %A in (*.*) do @echo %~nsA %~nA")
os.system("cls")
# Diretorio onde o arquivo esta sendo executado
os.chdir("C:\\Users\\win11\\Desktop\\")
print('System Shutdown....')
sleep(2)
print('System Shutdown.....')
sleep(0.5)

# Criar a Imagem da Tela Azul
def fit_center(pil_image):
    root = tkinter.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()
    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
    canvas = tkinter.Canvas(root, width=w, height=h, highlightthickness=0)
    canvas.pack()
    canvas.configure(background='black')

    img_width, img_height = pil_image.size
    ratio = min(w / img_width, h / img_height)
    img_width = int(img_width * ratio)
    img_height = int(img_height * ratio)
    pil_image = pil_image.resize((img_width, img_height), Image.Resampling.LANCZOS)

    image = ImageTk.PhotoImage(pil_image)
    imagesprite = canvas.create_image(w / 2, h / 2, image=image)
    root.config(cursor="none")
    root.mainloop()
    
pilImage = Image.open("bsod.png")
# Executa o Audio da Tela Azul 
def audio():
 playsound("bsod_sound.mp3")
threading.Thread(target=audio).start()
fit_center(pilImage)
