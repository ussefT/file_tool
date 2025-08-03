import customtkinter
import frameScrollable


class App(customtkinter.CTk):
    """
    Class app custome tkinter
    
    """
    def __init__(self):
        super().__init__()

        # title window
        self.title('ffiles')

        # size of window
        self.geometry("500x500")


        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Button add files
        self.btn_add_files=customtkinter.CTkButton(
            self,text="Add file",command=self.btn_add_file_callback
        )
        # Button add files grid
        self.btn_add_files.grid(
            row=0,column=0,padx=10,pady=10,sticky='ew'
        )


        self.btn_add_folders=customtkinter.CTkButton(
            self,text="Add folders",command=self.btn_add_folders_callback
        )

        self.btn_add_folders.grid(
            row=0,column=1,padx=0,pady=0,sticky='ew'
        )

       
      
        

        self.scrollable_checkbox_frame = frameScrollable.MyScrollableCheckboxFrame(
            self, title="Files", values=['1','2','3'])
        self.scrollable_checkbox_frame.grid(
            row=1, column=1, padx=10, pady=0, columnspan=1,sticky="w")

        self.scrollable_checkbox_frame.add_label(text='1')
        self.scrollable_checkbox_frame.add_label(text='2')

         # Button exit app
        self.btn_exit = customtkinter.CTkButton(
            self, text="Exit", command=self.button_exit_callbck
            )
        
        # Button exit app grid
        self.btn_exit.grid(
            row=3,column=3,padx=10,pady=10,sticky="ew")
        

    # Command call back 
    def btn_add_file_callback(self):
        pass

    def btn_add_folders_callback(self):
        pass
    def button_exit_callbck(self):
        app.destroy()

app = App()
app.mainloop()