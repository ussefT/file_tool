import customtkinter
import tkinter as tk

class MyScrollableCheckboxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title,  width=400, height=300)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []
        
    def add_label(self,path_file='',row_counter=0,text='0'):
        """Add to checkBox in to Frame"""
        # label = customtkinter.CTkLabel(
        #     self, text=text)
        # label.pack(pady=3, anchor="w")

       
        self.checkbox_var = tk.IntVar()

        # for i in enumerate(self.values):
        checkbox = customtkinter.CTkCheckBox(
            self,font=customtkinter.CTkFont(size=10),
            hover=True,checkbox_height=20,checkbox_width=20,
            text=text,textvariable=path_file,
            variable=self.checkbox_var,command=self.check_get
            )
        
        checkbox.grid(
            row=row_counter, column=0,
            padx=10, pady=(10, 0), sticky="w"
                    )
        
        print(self.checkboxes)
        self.checkboxes.append(checkbox)

    def check_get(self):
        """return item checked"""
        return self.checkbox_var.get()


    def check_list(self):
        """ return list of checkBox """
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get():
                checked_checkboxes.append(checkbox._textvariable)
            
        return checked_checkboxes

    def check_remove(self):
        """remove item checkBox"""
        if self.checkboxes:
            checked = [cb for cb in self.checkboxes if cb.get() == 1]
            for check in checked:
                    self.checkboxes.remove(check)
                    check.destroy()

    
    
    