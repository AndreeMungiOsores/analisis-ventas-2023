import tkinter as tk
from tkinter import messagebox
import random
import string

class GeneradorContraseñasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Contraseñas")

        # Estilos para la interfaz
        self.root.configure(background="#f0f0f0")
        self.estilo_fuente = ("Arial", 12)
        self.estilo_boton = {"font": self.estilo_fuente, "bg": "#4caf50", "fg": "white"}

        # Widgets
        self.longitud_label = tk.Label(root, text="Longitud de la Contraseña:", font=self.estilo_fuente, bg="#f0f0f0")
        self.longitud_label.grid(row=0, column=0, padx=10, pady=5)
        self.longitud_entry = tk.Entry(root, font=self.estilo_fuente)
        self.longitud_entry.grid(row=0, column=1, padx=10, pady=5)

        self.generar_boton = tk.Button(root, text="Generar Contraseña", command=self.generar_contraseña, **self.estilo_boton)
        self.generar_boton.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.contraseña_label = tk.Label(root, text="Contraseña Generada:", font=self.estilo_fuente, bg="#f0f0f0")
        self.contraseña_label.grid(row=2, column=0, padx=10, pady=5)
        self.contraseña_entry = tk.Entry(root, font=self.estilo_fuente, show="*")
        self.contraseña_entry.grid(row=2, column=1, padx=10, pady=5)

        self.ver_ocultar_var = tk.BooleanVar()
        self.ver_ocultar_var.set(False)
        self.ver_ocultar_checkbox = tk.Checkbutton(root, text="Mostrar Contraseña", variable=self.ver_ocultar_var, font=self.estilo_fuente, bg="#f0f0f0", command=self.mostrar_ocultar_contraseña)
        self.ver_ocultar_checkbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.marca_agua_label = tk.Label(root, text="De Andree Mungi", font=("Arial", 8), fg="gray", bg="#f0f0f0")
        self.marca_agua_label.place(relx=1.0, rely=1.0, anchor="se")

    def generar_contraseña(self):
        longitud = self.longitud_entry.get()

        if longitud.isdigit():
            longitud = int(longitud)
            if longitud > 0:
                contraseña = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=longitud))
                self.contraseña_entry.delete(0, tk.END)
                self.contraseña_entry.insert(0, contraseña)
            else:
                messagebox.showerror("Error", "La longitud de la contraseña debe ser mayor que 0.")
        else:
            messagebox.showerror("Error", "Por favor, ingresa un valor numérico para la longitud.")

    def mostrar_ocultar_contraseña(self):
        if self.ver_ocultar_var.get():
            self.contraseña_entry.config(show="")
        else:
            self.contraseña_entry.config(show="*")

if __name__ == "__main__":
    root = tk.Tk()
    app = GeneradorContraseñasApp(root)
    root.mainloop()
