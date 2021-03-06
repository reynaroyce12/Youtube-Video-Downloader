from tkinter import *
from downloader import *

SAVE_LOCATION = r"C:\Users\REYNA ROYCE\Desktop"
BG_COLOR = '#181818'
FG_COLOR = '#ffffff'
BT_BG = '#373737'
BT_FG = '#828282'


class Setup:
    def sent_file(self):
        try:
            file_url = fr'{self.file_entry.get()}'
            file_path = self.path_entry.get()
            obj = Download(file_url, file_path)
            if len(self.path_entry.get()) != 0:
                obj.download_file()
                self.message.config(text=f"'{obj.video_title}' downloaded.")
            else:
                self.message.config(text=f"Enter the location to save.")
        except:
            self.message.config(text="Oops! Something went wrong.Try again")

    def clear_content(self):
        self.file_entry.delete(0, END)
        self.path_entry.delete(0, END)
        self.message.config(text="")

    def __init__(self):
        self.window = Tk()
        self.window.title("YouTube Video Downloader")
        self.window.geometry('550x550')
        self.window.config(padx=60, pady=10, bg=BG_COLOR)

        self.image_canvas = Canvas(width=350, height=300, bg=BG_COLOR, highlightthickness=0)
        img = PhotoImage(file='image/yt_logo.png')
        self.image_canvas.create_image(150, 150, image=img)
        self.image_canvas.grid(row=1, column=2, columnspan=2)

        self.file_label = Label(text="Video URL", font=('Open Sans Condensed', 10, 'bold'), bg=BG_COLOR, fg=FG_COLOR)
        self.file_label.grid(row=2, column=1)

        self.file_entry = Entry(width=45, bg='#202020', fg='white')
        self.file_entry.grid(row=2, column=2, padx=30)

        self.path_label = Label(text="Location", font=('Open Sans Condensed', 10, 'bold'), bg=BG_COLOR, fg=FG_COLOR)
        self.path_label.grid(row=3, column=1, pady=20)

        self.path_entry = Entry(width=45, bg='#202020', fg='white')
        self.path_entry.insert(0, SAVE_LOCATION)
        self.path_entry.grid(row=3, column=2, padx=30, pady=20)

        self.download_bt = Button(text="Download", font=('Open Sans Condensed', 10, 'bold'), bg=BT_BG, fg=BT_FG
                                  , command=self.sent_file)
        self.download_bt.grid(row=5, column=1, columnspan=2, pady=5)

        self.clear_bt = Button(text="Clear", font=('Open Sans Condensed', 10, 'bold'), width=8, bg=BT_BG, fg=BT_FG
                               , command=self.clear_content)
        self.clear_bt.grid(row=6, column=1, columnspan=2, pady=15)

        self.message = Label(text="", font=('Open Sans Condensed', 10, 'bold'),
                             bg=BG_COLOR, fg=FG_COLOR, wraplength=400)
        self.message.grid(row=7, column=1, columnspan=2)

        self.window.mainloop()
