import customtkinter
from customtkinter import filedialog as fd
import frameScrollable
from tools import file_name,folder_name,file_is

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
        self.path_list=[]
        self.row_counter=0

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

        # Button add folders
        self.btn_add_folders=customtkinter.CTkButton(
            self,text="Add folders",command=self.btn_add_folders_callback
        )

        # Button add folders grid
        self.btn_add_folders.grid(
            row=0,column=1,padx=0,pady=0,sticky='ew'
        )

        # Button remove item on list
        self.btn_remove_checkbx=customtkinter.CTkButton(
            self,text='Remove',command=self.btn_remove_checkbx_callback
        )

        # Button remove item on list grid
        self.btn_remove_checkbx.grid(
            row=0,column=2,padx=10,pady=0,sticky='ew'
        )

        # Class Frame and CheckBox
        self.scrollable_checkbox_frame = frameScrollable.MyScrollableCheckboxFrame(
            self, title="Files", values=['1','2','3'])
        
        # Class Frame and CheckBox grid
        self.scrollable_checkbox_frame.grid(
            row=1, column=0, padx=10, pady=0, columnspan=5,sticky="w")

        

         # Button exit app
        self.btn_exit = customtkinter.CTkButton(
            self, text="Exit", command=self.btn_exit_callbck
            )
        
        # Button exit app grid
        self.btn_exit.grid(
            row=3,column=3,padx=10,pady=10,sticky="ew")
        

    # Command call back 
    

    def btn_add_folders_callback(self):
        """Add folder"""
        print(self.scrollable_checkbox_frame.check_list())
    def btn_exit_callbck(self):
        """Exit App"""
        app.destroy()

    def btn_add_file_callback(self):
        """Button open dialog file add """
        filetypes = (
        ('JPG file', '*.jpg'),
        ('PNG file', '*.png'),
        ('WEB file', '*.web'),
        ('All file', '*.*')
            )

        self.path_list = fd.askopenfilenames(
        title='Open a file',
        initialdir='/Users/usef/Desktop',
        filetypes=filetypes)
        
        
        for i in self.path_list:
            if file_is(i):
                print(i)
                name_of_path=file_name(i)
                self.scrollable_checkbox_frame.add_label(text=name_of_path,path_file=i,row_counter=self.row_counter)
                self.row_counter+=1
    
    def path_remove(self):
        """Remove item on the list when is checked"""
        
        self.scrollable_checkbox_frame.check_remove()
          
    def btn_remove_checkbx_callback(self):
        """Button remove callback"""
        self.path_remove()


if __name__=='__main__':
    app = App()
    app.mainloop()