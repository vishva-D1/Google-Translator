# from tkinter import *
# import tkinter as tk
# from tkinter import ttk
# from googletrans import Translator  #pip install googletrans==3.1.0a0
# from tkinter import messagebox

# root = tk.Tk()
# root.title('Language Translator')
# root.geometry('590x370')

# def translate():
#     lang_1 = text_entry1.grt("1.0","end-1c")
#     cl = choose_language.get()

#     if lang_1 =='':
#         messagebox.showerror('Language Translator', 'Enter the text to translate!')
#     else:
#         text_entry2.delete(1.0,'end')
#         translator = Translator()
#         output = translator.translate(lang_1,dest=cl)
#         text_entry2.insert('end,output.text') 

# def clear():
#     text_entry1.delete(1.0,'end')
#     text_entry2.delete(1.0,'end')

# a = tk.StringVar()

# frame1 = Frame(root,width=590,height=370,relief=RIDGE,borderwidth=5,bg='#f7DC6F')
# frame1.place(x=0,y=0)

# Label(root,text="Language Translator" ,font=("Helvetica 20 bold"),fg="black",bg='#f7dc6f').pack(pady=10)


# auto_select = ttk.Combobox(frame1, width=27,textvariable=a, state='randomly',font=('verdana',10,'bold'))

# auto_select['values'] =(   
#                              'Auto select',
#                         )

# auto_select.place(x=15,y=60)
# auto_select.current(0)
   
# l = tk.stringvar()
# choose_lanaguage = ttk.Combobox(frame1,width=27, textvariable=l, state='randonly', font=('verdana',10,'bold'))

# choose_lanaguage['values'] =(
                                
#                               'Afrikaans',
# 'Albanian',
# 'Amharic',
# 'Arabic',
# 'Armenian',
# 'Azerbaijani',
# 'Basque',
# 'Belarusian',
# 'Bengali',
# 'Bosnian',
# 'Bulgarian',
# 'Burmese',
# 'Catalan',
# 'Cebuano',
# 'Chinese (Simplified)',
# 'Chinese (Traditional)',
# 'Corsican',
# 'Croatian',
# 'Czech',
# 'Danish',
# 'Dutch',
# 'English',
# 'Esperanto',
# 'Estonian',
# 'Finnish',
# 'French',
# 'Frisian',
# 'Galician',
# 'Georgian',
# 'German',
# 'Greek',
# 'Gujarati',
# 'Haitian Creole',
# 'Hausa',
# 'Hawaiian',
# 'Hebrew',
# 'Hindi',
# 'Hmong',
# 'Hungarian',
# 'Icelandic',
# 'Igbo',
# 'Indonesian',
# 'Irish',
# 'Italian',
# 'Japanese',
# 'Javanese',
# 'Kannada',
# 'Kazakh',
# 'Khmer',
# 'Kinyarwanda',
# 'Korean',
# 'Kurdish',
# 'Kyrgyz',
# 'Lao',
# 'Latin',
# 'Latvian',
# 'Lithuanian',
# 'Luxembourgish',
# 'Macedonian',
# 'Malagasy',
# 'Malay',
# 'Malayalam',
# 'Maltese',
# 'Maori',
# 'Marathi',
# 'Mongolian',
# 'Nepali',
# 'Norwegian',
# 'Nyanja',
# 'Odia (Oriya)',
# 'Pashto',
# 'Persian',
# 'Polish',
# 'Portuguese',
# 'Punjabi',
# 'Romanian',
# 'Russian',
# 'Samoan',
# 'Scots Gaelic',
# 'Serbian',
# 'Sesotho',
# 'Shona',
# 'Sindhi',
# 'Sinhala',
# 'Slovak',
# 'Slovenian',
# 'Somali',
# 'Spanish',
# 'Sundanese',
# 'Swahili',
# 'Swedish',
# 'Tagalog',
# 'Tajik',
# 'Tamil',
# 'Tatar',
# 'Telugu',
# 'Thai',
# 'Turkish',
# 'Turkmen',
# 'Ukrainian',
# 'Urdu',
# 'Uyghur',
# 'Uzbek',
# 'Vietnamese',
# 'Welsh',
# 'Xhosa',
# 'Yiddish',
# 'Yoruba',
# 'Zulu'
#                             )


# choose_lanaguage.place(x=305,y=60)
# choose_lanaguage.cuirrent(0)

# frame1 = Frame(root,width=590,height=370,relief=RIDGE,borderwidth=5,bg='#f7DC6F')
# frame1.place(x=0,y=0)

# Label(root,text="Language Translator" ,font=("Helvetica 20 bold"),fg="black",bg='#f7dc6f').pack(pady=10)

# text_entry1 = Text(frame1,width=20,height=7,borderwidth=5,relief=RIDGE,font=('verdana',15))
# text_entry1.place(x=10,y=100)

# text_entry2 = Text(frame1,width=20,height=7,borderwidth=5,relief=RIDGE,font=('verdana',15))
# text_entry2.place(x=300,y=100)

# btn1 = Button(frame1,text="Translate",relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",cursor="hand2")
# btn1.place(x=185,y=300)

# btn2 = Button(frame1,text="clear",relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",cursor="hand2")
# btn2.place(x=300,y=300)



# root .mainloop()


from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator

root = Tk()
root.title('Language Translator')
root.geometry('590x370')

def translate():
    lang_1 = text_entry1.get("1.0", "end-1c")
    cl = choose_language.get()
    
    if lang_1 == '':
        messagebox.showerror('Language Translator', 'Enter the text to translate!')
    else:
        text_entry2.delete(1.0, 'end')
        translator = Translator()
        output = translator.translate(lang_1, dest=cl)
        text_entry2.insert('end', output.text)

def clear():
    text_entry1.delete(1.0, 'end')
    text_entry2.delete(1.0, 'end')

# Main Frame
frame1 = Frame(root, width=590, height=370, relief=RIDGE, borderwidth=5, bg='#f7DC6F')
frame1.place(x=0, y=0)

Label(root, text="Language Translator", font=("Helvetica 20 bold"), fg="black", bg='#f7dc6f').pack(pady=10)

# Auto Select Combobox
a = StringVar()
auto_select = ttk.Combobox(frame1, width=27, textvariable=a, state='readonly', font=('verdana', 10, 'bold'))
auto_select['values'] = ('Auto select',)
auto_select.place(x=15, y=60)
auto_select.current(0)

# Language Selection Combobox
l = StringVar()
choose_language = ttk.Combobox(frame1, width=27, textvariable=l, state='readonly', font=('verdana', 10, 'bold'))
choose_language['values'] = (
    'Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 'Bengali', 
    'Bosnian', 'Bulgarian', 'Burmese', 'Catalan', 'Cebuano', 'Chinese (Simplified)', 'Chinese (Traditional)', 
    'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Esperanto', 'Estonian', 'Finnish', 'French', 
    'Frisian', 'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian', 
    'Hebrew', 'Hindi', 'Hmong', 'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 
    'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Kinyarwanda', 'Korean', 'Kurdish', 'Kyrgyz', 'Lao', 'Latin', 
    'Latvian', 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori', 
    'Marathi', 'Mongolian', 'Nepali', 'Norwegian', 'Nyanja', 'Odia (Oriya)', 'Pashto', 'Persian', 'Polish', 
    'Portuguese', 'Punjabi', 'Romanian', 'Russian', 'Samoan', 'Scots Gaelic', 'Serbian', 'Sesotho', 'Shona', 
    'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tagalog', 
    'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Turkish', 'Turkmen', 'Ukrainian', 'Urdu', 'Uyghur', 'Uzbek', 
    'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu'
)
choose_language.place(x=305, y=60)
choose_language.current(0)

# Text Entry Boxes
text_entry1 = Text(frame1, width=20, height=7, borderwidth=5, relief=RIDGE, font=('verdana', 15))
text_entry1.place(x=10, y=100)

text_entry2 = Text(frame1, width=20, height=7, borderwidth=5, relief=RIDGE, font=('verdana', 15))
text_entry2.place(x=300, y=100)

# Buttons
btn1 = Button(frame1,  text="Translate", relief=RAISED, borderwidth=2, 
              font=('verdana', 10, 'bold'), bg='#248aa2', fg="black", cursor="hand2", command=translate)
btn1.place(x=185, y=300)

btn2 = Button(frame1, text="Clear", relief=RAISED, borderwidth=2, 
              font=('verdana', 10, 'bold'), bg='#248aa2', fg="black", cursor="hand2", command=clear)
btn2.place(x=300, y=300)

root.mainloop()
