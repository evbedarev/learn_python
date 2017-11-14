from tkinter import *
import Port-sec


class Application(Frame):
    """docstring for Application"""

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid(row=5, column=5)
        self.create_widgets()

    def create_widgets(self):
        self.lbl_path_utc = Label(self, text='mac адресс ')
        self.lbl_path_utc.grid(row=2, column=0, columnspan=4, sticky=W)
        self.mac = Entry(self, width=55)
        self.mac.grid(row=3, column=0, columnspan=2, sticky=W)

        self.ip_com = Label(self, text='ip комутатора:')
        self.ip_com.grid(row=4, column=0, columnspan=4, sticky=W)
        self.ip_com = Entry(self, width=55)
        self.ip_com.grid(row=5, column=0, columnspan=2, sticky=W)

        # self.ok_bttn = Button(self, text="Start", command=self.findUser)
        # self.ok_bttn.grid(row=7, column=1, sticky=W)

    # def findUser(self):
    #     import Port-sec
    #
    #     fp = FindIp.Run_command(self.ent_utc.get())
    #
    #     self.ent_uname.insert(0, fp)


root = Tk()
root.title("Clear interface")
root.geometry("350x130")
app = Application(root)
root.mainloop()