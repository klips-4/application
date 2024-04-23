import customtkinter as ctk
from database.connection import ConnectionObject


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Application")
        self.geometry(f"{980}x{525}")
        self.grid_columnconfigure((1, 1), weight=1)
        self.grid_rowconfigure(2, weight=1, minsize=225)
        self.set_frames()

    def set_frames(self):
        self.top_label_frame = TopLabel(self)
        self.top_label_frame.grid(column=0, row=0, padx=10, pady=(10, 0), sticky="nsew")
        self.middle_label_frame = MiddleLabel(master=self)
        self.middle_label_frame.grid(column=0, row=1, padx=10, pady=(10, 0), sticky="nsew")
        self.bottom_label_frame = BottomLabel(self)
        self.bottom_label_frame.grid(column=0, row=2, padx=10, pady=(10, 10), sticky="nsew")


class TopLabel(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.life_cycle_from_db = None
        self.init_top_widget()
        self.drop_down()
        self.grid_columnconfigure((0, 0), weight=1)
        self.product_from_db = []
        self.volume_from_db = []
        self.current_object = None

    def create_engine(self):
        self.engine = ConnectionObject()

    def select_object(self, selected_object):
        self.product_drop_down.configure(state="normal")
        self.create_engine()
        self.product_from_db = self.engine.get_uniq_products(selected_object)
        self.product_drop_down.configure(values=self.product_from_db)

    def select_product(self, selected_product):
        self.volume_drop_down.configure(state="normal")
        self.current_object = self.object_drop_down.get()
        self.create_engine()
        self.volume_from_db = self.engine.get_uniq_volume(selected_product, self.current_object)
        self.volume_drop_down.configure(values=self.volume_from_db)

    def select_volume(self, selected_volume):
        self.construction_drop_down.configure(state="normal")
        self.current_object = self.object_drop_down.get()
        self.create_engine()
        self.method_from_db = self.engine.get_uniq_method_construction(selected_volume, self.current_object)
        self.construction_drop_down.configure(values=self.method_from_db)

    def select_method_construction(self, selected_construction):
        self.life_cycle_drop_down.configure(state="normal")
        self.current_object = self.object_drop_down.get()
        self.current_volume = self.volume_drop_down.get()
        self.create_engine()
        self.life_cycle_from_db = self.engine.get_uniq_life_cycles(self.current_object, self.current_volume)
        self.life_cycle_drop_down.configure(values=self.life_cycle_from_db)
        self.deviations_from_db = self.engine.get_uniq_deviations(self.current_object, self.current_volume)
        self.master.middle_label_frame.deviations_drop_down.configure(values=self.deviations_from_db)

    def init_top_widget(self):
        self.top_label = ctk.CTkFrame(self, fg_color="aliceblue")
        self.top_label.grid(padx=10, pady=(10, 10), sticky="nsew")

    def drop_down(self):
        # Objects

        self.choose_object = ctk.CTkLabel(self.top_label, text="Выбрать объект:")
        self.choose_object.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.object_drop_down = ctk.CTkComboBox(self.top_label, values=['Резервуар', 'Трубопровод'],
                                                command=self.select_object)

        self.object_drop_down.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nsew")

        # Products

        self.choose_product = ctk.CTkLabel(self.top_label, text="Выбрать продукт:")
        self.choose_product.grid(row=0, column=1, padx=50, pady=(10, 0), sticky="nsew")

        self.product_drop_down = ctk.CTkComboBox(self.top_label, state='disabled', command=self.select_product)
        self.product_drop_down.grid(row=1, column=1, padx=10, pady=(10, 10), sticky="nsew")

        # Volume

        self.choose_value = ctk.CTkLabel(self.top_label, text="Диаметр труб-да/объем резервуара:")
        self.choose_value.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="nsew")

        self.volume_drop_down = ctk.CTkComboBox(self.top_label, state='disabled', command=self.select_volume)
        self.volume_drop_down.grid(row=1, column=2, padx=10, pady=(10, 10), sticky="nsew")

        # Construction

        self.choose_construction = ctk.CTkLabel(self.top_label, text="Способ строительства:")
        self.choose_construction.grid(row=0, column=3, padx=10, pady=(10, 0), sticky="nsew")

        self.construction_drop_down = ctk.CTkComboBox(self.top_label, state='disabled',
                                                      command=self.select_method_construction)
        self.construction_drop_down.grid(row=1, column=3, padx=10, pady=(10, 10), sticky="nsew")

        # Life_cycle

        self.choose_life_cycle = ctk.CTkLabel(self.top_label, text="Этап жизненного цикла:")
        self.choose_life_cycle.grid(row=0, column=4, padx=10, pady=(10, 0), sticky="nsew")

        self.life_cycle_drop_down = ctk.CTkComboBox(self.top_label, state='disabled')
        self.life_cycle_drop_down.grid(row=1, column=4, padx=10, pady=(10, 10), sticky="nsew")


class BottomLabel(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.init_bottom_widget()
        self.grid_columnconfigure((0, 0), weight=1)
        self.grid_rowconfigure(1, weight=1, minsize=225)

    def init_bottom_widget(self):
        self.bottom_label = ctk.CTkFrame(self, fg_color="white")
        self.bottom_label.grid(column=0, row=1, padx=10, pady=(10, 10), sticky="nsew")

        self.text = ctk.CTkLabel(self.bottom_label, text="")
        self.text.grid(column=0, row=1, padx=10, pady=(10, 10), sticky="nw")




class MiddleLabel(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.init_middle_widget()
        self.grid_columnconfigure((0, 0), weight=1)
        self.grid_rowconfigure(0, weight=1, minsize=10)
        self.drop_down()
        self.event = None

    def init_middle_widget(self):
        self.middle_label = ctk.CTkFrame(self, fg_color="aliceblue")
        self.middle_label.grid(padx=10, pady=(10, 10), sticky="nsew")

        self.button = ctk.CTkButton(self.middle_label, text="Выполнить", command=self.get_events)
        self.button.grid(column=3, row=1, padx=10, pady=(10, 10), sticky="nsew")

    def drop_down(self):
        # Deviations
        self.choose_deviation = ctk.CTkLabel(self.middle_label, text="Отступление от требований:")
        self.choose_deviation.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.deviations_drop_down = ctk.CTkComboBox(self.middle_label, values=[''], command=self.select_deviations)
        self.deviations_drop_down.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nsew")

        # Deviations_object

        self.choose_deviation_object = ctk.CTkLabel(self.middle_label,
                                                    text="Объект, относительно которого происходит отступление:")
        self.choose_deviation_object.grid(row=0, column=1, padx=50, pady=(10, 0), sticky="nsew")

        self.deviation_object_drop_down = ctk.CTkComboBox(self.middle_label, state='disabled')
        self.deviation_object_drop_down.grid(row=1, column=1, padx=10, pady=(10, 10), sticky="nsew")

    def select_deviations(self, selected_deviation):
        self.deviation_object_drop_down.configure(state="normal")
        self.current_object = self.master.top_label_frame.object_drop_down.get()
        self.engine = ConnectionObject()
        self.deviation_object_from_db = self.engine.get_uniq_deviation_object(self.current_object, selected_deviation)
        self.deviation_object_drop_down.configure(values=self.deviation_object_from_db)

    def get_events(self):
        self.current_deviation_object = self.deviation_object_drop_down.get()
        self.engine = ConnectionObject()
        self.event = self.engine.get_uniq_event(self.current_object, self.current_deviation_object)
        self.master.bottom_label_frame.text.configure(text=self.event)




if __name__ == "__main__":
    app = App()
    app.mainloop()
