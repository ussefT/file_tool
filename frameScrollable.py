import customtkinter

class MyScrollableCheckboxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title,  width=350, height=360)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        
    def add_label(self,text='0'):
        label = customtkinter.CTkLabel(
            self, text=text)
        label.pack(pady=3, anchor="w")
    #     self.checkboxes = []

    #     for i, value in enumerate(self.values):
    #         checkbox = customtkinter.CTkCheckBox(self, text=value)
    #         checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
    #         self.checkboxes.append(checkbox)

    # def get(self):
    #     checked_checkboxes = []
    #     for checkbox in self.checkboxes:
    #         if checkbox.get() == 1:
    #             checked_checkboxes.append(checkbox.cget("text"))
    #     return checked_checkboxes