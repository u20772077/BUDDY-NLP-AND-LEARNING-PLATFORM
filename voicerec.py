
from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import mpg123
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
import math
from PIL import ImageTk, Image, ImageOps
'''
# function user/system speech interaction  
def buddy_talk(audio):
    print('audio')
    tts= gTTS(text=audio , lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')
    #capture command
def myCommand():
    r  = sr.Recognizer()
    with sr.Microphone() as source:
      print(' I am at your service , what is your command')
 
 #this is not going to work ...try defining them in terms of variables

    r.pause_threshold = 1
    r.adjust_for_ambient_noise(source,duration = 1)
    audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print('did you say  ' +command+ '/n')
        #loop back to listen for command
    except sr.UnknownValueError:
            assistant(myCommand())
    return command
            #if statement for execution command
def assistant(command):
     if 'open youtube ' in command:
         browser_path = 'Program Files (x86)\Mozilla Firefox\firefox.exe'
         url  = 'https://www.youtube.com/'
         webbrowser.get(browser_path).open(url)

     if 'morning buddy ' in command:
         talkToMe('top of the morning to ya ')

     if ' how is my day looking' in command:
        buddy_talk('well  lets take a look ' )
        buddy_talk(' command completed')

buddy_talk(' ready for new you command')
while True:
 assistant(myCommand())
 '''                 
#   GRAPHICS SUPPORT 
'''
def create_circle():
    circle = plt.Circle((0,0), radius=5)
    return create_circle



def show_shape(patch):
    ax = plt.gca()
    ax.add_patch(patch)
    plt.axis('scaled')
    plt.show()

if __name__ =='__main__':

            c = create_circle()
            show_shape(c)
'''
'''
circle = plt.Circle((5.5,5.5),4, color ='red')
ax = plt.gca()
#triangle
'''
'''
points = np.array([[2,2],[6,5],[3,np.sqrt(5**2 - 2**2)]])
polygon = Polygon(points,closed= False,color = 'blue')
ax.add_patch(points)
# line tangent
'''
'''
x1,y1 = [-1,12], [1,2]
plt.plot(x1,y1,marker="o")
ax.add_artist(circle)
ax.set_xlim(0,10)
ax.set_ylim(0,10)
#plt.axis('scaled')

plt.show()

'''

#################### theme functions


def font_change_default(self):
           self.text_box.config(font="Verdana 10")
           self.entry_field.config(font="Verdana 10")
           self.font = "Verdana 10"

def font_change_times(self):
    self.text_box.config(font="Times")
    self.entry_field.config(font="Times")
    self.font = "Times"

def font_change_system(self):
    self.text_box.config(font="System")
    self.entry_field.config(font="System")
    self.font = "System"

def font_change_helvetica(self):
    self.text_box.config(font="helvetica 10")
    self.entry_field.config(font="helvetica 10")
    self.font = "helvetica 10"

def font_change_fixedsys(self):
    self.text_box.config(font="fixedsys")
    self.entry_field.config(font="fixedsys")
    self.font = "fixedsys"

def color_theme_default(self):
    self.master.config(bg="#EEEEEE")
    self.text_frame.config(bg="#EEEEEE")
    self.entry_frame.config(bg="#EEEEEE")
    self.text_box.config(bg="#FFFFFF", fg="#000000")
    self.entry_field.config(bg="#FFFFFF", fg="#000000", insertbackground="#000000")
    self.send_button_frame.config(bg="#EEEEEE")
    self.send_button.config(bg="#FFFFFF", fg="#000000", activebackground="#FFFFFF", activeforeground="#000000")
#self.emoji_button.config(bg="#FFFFFF", fg="#000000", activebackground="#FFFFFF", activeforeground="#000000")
    self.sent_label.config(bg="#EEEEEE", fg="#000000")

    self.tl_bg = "#FFFFFF"
    self.tl_bg2 = "#EEEEEE"
    self.tl_fg = "#000000"



# image theme
def road_image_theme(self):
    global photo

    self.photo = ImageTk.PhotoImage(Image.open("images/w.jpg"))
    
    self.master.config(bg=self.photo)
    self.text_frame.config(bg=self.photo)
    self.text_box.config(bg="#212121", fg="#FFFFFF")
    self.entry_frame.config(bg="#2a2b2d")
    self.entry_field.config(bg="#212121", fg="#FFFFFF", insertbackground=self.back)
    self.send_button_frame.config(bg="#2a2b2d")
    self.send_button.config(bg="#212121", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
# self.emoji_button.config(bg="#212121", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
    self.sent_label.config(bg="#2a2b2d", fg="#FFFFFF")

    self.tl_bg = self.back
    self.tl_bg2 = self.back
    self.tl_fg = "#FFFFFF"












# Dark
def color_theme_dark(self):
    self.master.config(bg="#2a2b2d")
    self.text_frame.config(bg="#2a2b2d")
    self.text_box.config(bg="#212121", fg="#FFFFFF")
    self.entry_frame.config(bg="#2a2b2d")
    self.entry_field.config(bg="#212121", fg="#FFFFFF", insertbackground="#FFFFFF")
    self.send_button_frame.config(bg="#2a2b2d")
    self.send_button.config(bg="#212121", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
# self.emoji_button.config(bg="#212121", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
    self.sent_label.config(bg="#2a2b2d", fg="#FFFFFF")

    self.tl_bg = "#212121"
    self.tl_bg2 = "#2a2b2d"
    self.tl_fg = "#FFFFFF"

# Grey
def color_theme_grey(self):
        self.master.config(bg="#444444")
        self.text_frame.config(bg="#444444")
        self.text_box.config(bg="#4f4f4f", fg="#ffffff")
        self.entry_frame.config(bg="#444444")
        self.entry_field.config(bg="#4f4f4f", fg="#ffffff", insertbackground="#ffffff")
        self.send_button_frame.config(bg="#444444")
        self.send_button.config(bg="#4f4f4f", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")
#self.emoji_button.config(bg="#4f4f4f", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")
        self.sent_label.config(bg="#444444", fg="#ffffff")

        self.tl_bg = "#4f4f4f"
        self.tl_bg2 = "#444444"
        self.tl_fg = "#ffffff"


def color_theme_turquoise(self):
    self.master.config(bg="#003333")
    self.text_frame.config(bg="#003333")
    self.text_box.config(bg="#669999", fg="#FFFFFF")
    self.entry_frame.config(bg="#003333")
    self.entry_field.config(bg="#669999", fg="#FFFFFF", insertbackground="#FFFFFF")
    self.send_button_frame.config(bg="#003333")
    self.send_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
#self.emoji_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
    self.sent_label.config(bg="#003333", fg="#FFFFFF")

    self.tl_bg = "#669999"
    self.tl_bg2 = "#003333"
    self.tl_fg = "#FFFFFF"    

# Blue
def color_theme_dark_blue(self):
    self.master.config(bg="#263b54")
    self.text_frame.config(bg="#263b54")
    self.text_box.config(bg="#1c2e44", fg="#FFFFFF")
    self.entry_frame.config(bg="#263b54")
    self.entry_field.config(bg="#1c2e44", fg="#FFFFFF", insertbackground="#FFFFFF")
    self.send_button_frame.config(bg="#263b54")
    self.send_button.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
#self.emoji_button.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
    self.sent_label.config(bg="#263b54", fg="#FFFFFF")

    self.tl_bg = "#1c2e44"
    self.tl_bg2 = "#263b54"
    self.tl_fg = "#FFFFFF"




# Torque
def color_theme_turquoise(self):
        self.master.config(bg="#003333")
        self.text_frame.config(bg="#003333")
        self.text_box.config(bg="#669999", fg="#FFFFFF")
        self.entry_frame.config(bg="#003333")
        self.entry_field.config(bg="#669999", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.send_button_frame.config(bg="#003333")
        self.send_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
#self.emoji_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#003333", fg="#FFFFFF")

        self.tl_bg = "#669999"
        self.tl_bg2 = "#003333"
        self.tl_fg = "#FFFFFF"

# Hacker
def color_theme_hacker(self):
    self.master.config(bg="#0F0F0F")
    self.text_frame.config(bg="#0F0F0F")
    self.entry_frame.config(bg="#0F0F0F")
    self.text_box.config(bg="#0F0F0F", fg="#33FF33")
    self.entry_field.config(bg="#0F0F0F", fg="#33FF33", insertbackground="#33FF33")
    self.send_button_frame.config(bg="#0F0F0F")
    self.send_button.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
#self.emoji_button.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
    self.sent_label.config(bg="#0F0F0F", fg="#33FF33")

    self.tl_bg = "#0F0F0F"
    self.tl_bg2 = "#0F0F0F"
    self.tl_fg = "#33FF33"



# Default font and color theme
def default_format(self):
    self.font_change_default()
    self.color_theme_default()    


