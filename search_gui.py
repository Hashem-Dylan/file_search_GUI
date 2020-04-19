import tkinter as tki
import os
from tkinter import Entry


class SearchGUI:



    def __init__(self):
        # create the main window
        self.main_window = tki.Tk()

        # Create top and bottom frame
        self.frame_1 = tki.Frame(self.main_window)
        self.frame_4 = tki.Frame(self.main_window)
        self.frame_5 = tki.Frame(self.main_window)



        # Create a Button widget. Button will trigger convert callback
        self.search_button = tki.Button(self.frame_5,
                                        text='Search',
                                        command=self.search)
        self.exit_button = tki.Button(self.frame_5,
                                      text='Exit',
                                      command=self.main_window.destroy)
        # Create Entry widgets
        self.entry_file_name = tki.Entry(self.frame_1,
                                    width=10)
        # Create labels in corresponding frames
        self.search_label = tki.Label(self.frame_1,
                                text='Enter file name: ')

        self.label4 = tki.Label(self.frame_4,
                                text='File Location: ')
        self.path = tki.StringVar()
        self.path_label = tki.Label(self.frame_4,
                                       textvariable=self.path)

        # pack labels in corresponding frames
        self.label4.pack(side='left')
        self.search_label.pack(side='left')
        # pack frames
        self.frame_1.pack()
        self.frame_4.pack()
        self.frame_5.pack()
        # pack buttons and entries
        self.exit_button.pack(side='left')
        self.search_button.pack(side='left')
        self.entry_file_name.pack(side='right')
        self.path_label.pack(side='left')



        # Enter the main loop
        tki.mainloop()


    def search(self):

        i = 0
        file_count = 1
        directory = r'C:\Users'
        os.chdir(directory)
        key_file = self.entry_file_name.get()
        for dirpath, dirnames, filenames in os.walk(directory):
            for file in filenames:
                file_count += 1
                if os.path.splitext(file)[0] == os.path.splitext(key_file)[0]:
                    self.path.set(dirpath)
                    os.startfile(dirpath)
                    break
                else:
                    i += 1

        i += 1
        if i == file_count:
            self.path.set('file not found')


search_gui = SearchGUI

search_gui()
