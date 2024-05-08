import customtkinter as ctk
from modules.logics.app import App


class UI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self._set_appearance_mode('system')
        self.geometry('600x400')
        self.title("BoolMin")
        self.rowconfigure(index=(0, 1, 2, 3, 4), weight=1)
        self.columnconfigure(index=0, weight=1)
        
        self.topbox = ctk.CTkTextbox(master=self, corner_radius=5, width=600, height=100, font=('Helvetica', 24))
        self.bottombox = ctk.CTkTextbox(master=self, width=600, height=100, font=('Helvetica', 24))
        calculate_btn = ctk.CTkButton(master=self, width=70, height=30, 
                                      corner_radius=2, text="Calculate", 
                                      font=('Helvetica', 20),
                                      anchor="center", 
                                      command=self.generate_result)
        
        top_label= ctk.CTkLabel(master=self, width=200, height=20, font=('Helvetica', 25), text="Enter expression:", anchor="sw")
        bottom_label= ctk.CTkLabel(master=self, width=200, height=20, font=('Helvetica', 25), text="Result:", anchor="w")
        
        self.topbox.grid(row=1, column=0, columnspan=3, padx=5, pady=0, sticky='sw')
        self.bottombox.grid(row=3, columnspan=3, padx=5)
        top_label.grid(row=0, column=0, padx=2, pady=0, sticky='sw')
        bottom_label.grid(row=2, column=0, padx=5, pady=5, sticky='sw')
        calculate_btn.grid(row=4, column=0)
        
    
    def generate_result(self):
        expression = self.topbox.get("1.0", ctk.END)
        result = App(bool_exp=expression)
        result = result.generate_result()
        
        self.bottombox.delete("1.0", ctk.END)
        
        if expression:
            self.bottombox.insert("end", result)
            
if __name__=="__main__":
    app = UI()
    app.mainloop()
