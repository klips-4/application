import customtkinter as ctk
from database.connection import Connection


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Application")
        self.geometry(f"{1020}x{500}")
        self.grid_columnconfigure((0, 0), weight=1)
        self.grid_rowconfigure(1, weight=1, minsize=200)
        self.set_frames()

    def set_frames(self):
        self.top_label_frame = TopLabel(self)
        self.top_label_frame.grid(column=0, row=0, padx=10, pady=(10, 0), sticky="nsew")
        self.bottom_label_frame = BottomLabel(self)
        self.bottom_label_frame.grid(column=0, row=1, padx=10, pady=(10, 10), sticky="nsew")


class TopLabel(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.init_top_widget()
        self.drop_down()
        self.grid_columnconfigure((0, 0), weight=1)
        self.product_from_db = []
        self.volume_from_db = []


    def select_object(self, selected_object):
        self.product_drop_down.configure(state="normal")
        self.product_from_db = engine.choose_product(selected_object)
        self.product_drop_down.configure(values=self.product_from_db)

        return self.product_from_db

    def select_product(self, selected_product):
        self.volume_drop_down.configure(state="normal")
        self.volume_from_db = engine.choose_volume(selected_product)
        self.volume_drop_down.configure(values=self.volume_from_db)



    def init_top_widget(self):
        self.top_label = ctk.CTkFrame(self, fg_color="aliceblue")
        self.top_label.grid(padx=10, pady=(10, 10), sticky="nsew")

    def drop_down(self):
        # Objects

        self.choose_object = ctk.CTkLabel(self.top_label, text="Выбрать объект:")
        self.choose_object.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.objects = object_from_db

        self.object_drop_down = ctk.CTkComboBox(self.top_label, values=self.objects, command=self.select_object,)
        self.object_drop_down.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nsew")

        # Products

        self.choose_product = ctk.CTkLabel(self.top_label, text="Выбрать продукт:")
        self.choose_product.grid(row=0, column=1, padx=50, pady=(10, 0), sticky="nsew")

        self.product_drop_down = ctk.CTkComboBox(self.top_label, state='disabled', command=self.select_product)
        self.product_drop_down.grid(row=1, column=1, padx=10, pady=(10, 10), sticky="nsew")

        # Volume

        self.choose_value = ctk.CTkLabel(self.top_label, text="Диаметр труб-да/объем резервуара:")
        self.choose_value.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="nsew")

        self.volume_drop_down = ctk.CTkComboBox(self.top_label, state='disabled')
        self.volume_drop_down.grid(row=1, column=2, padx=10, pady=(10, 10), sticky="nsew")

        # Construction

        self.choose_construction = ctk.CTkLabel(self.top_label, text="Способ строительства:")
        self.choose_construction.grid(row=0, column=3, padx=10, pady=(10, 0), sticky="nsew")

        self.construction_drop_down = ctk.CTkComboBox(self.top_label, state='disabled')
        self.construction_drop_down.grid(row=1, column=3, padx=10, pady=(10, 10), sticky="nsew")

        # Life_cycle

        self.choose_life_cycle = ctk.CTkLabel(self.top_label, text="Этап жизненного цикла:")
        self.choose_life_cycle.grid(row=0, column=4, padx=10, pady=(10, 0), sticky="nsew")

        self.life_cycle_drop_down = ctk.CTkComboBox(self.top_label, state='disabled')
        self.life_cycle_drop_down.grid(row=1, column=4, padx=10, pady=(10, 10), sticky="nsew")


class BottomLabel(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.init_top_widget()
        self.grid_columnconfigure((0, 0), weight=1)
        self.grid_rowconfigure(1, weight=1, minsize=200)

    def init_top_widget(self):
        self.bottom_label = ctk.CTkFrame(self, fg_color="aliceblue")
        self.bottom_label.grid(column=0, row=1, padx=10, pady=(10, 10), sticky="nsew")


# engine = Connection()
# object_from_db = engine.choose_object()

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()
