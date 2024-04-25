import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class AdministradorTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Administrador de Tareas")

        self.tareas = []

        # Estilos para la interfaz
        self.root.configure(background="#f0f0f0")
        self.estilo_fuente = ("Arial", 12)
        self.estilo_boton = {"font": self.estilo_fuente, "bg": "#4caf50", "fg": "white"}

        # Widgets para agregar una nueva tarea
        self.etiqueta_titulo = tk.Label(root, text="Título de la Tarea:", font=self.estilo_fuente, bg="#f0f0f0")
        self.etiqueta_titulo.grid(row=0, column=0, padx=10, pady=5)
        self.entrada_titulo = tk.Entry(root, font=self.estilo_fuente)
        self.entrada_titulo.grid(row=0, column=1, padx=10, pady=5)

        self.etiqueta_descripcion = tk.Label(root, text="Descripción de la Tarea:", font=self.estilo_fuente, bg="#f0f0f0")
        self.etiqueta_descripcion.grid(row=1, column=0, padx=10, pady=5)
        self.entrada_descripcion = tk.Entry(root, font=self.estilo_fuente)
        self.entrada_descripcion.grid(row=1, column=1, padx=10, pady=5)

        self.boton_agregar = tk.Button(root, text="Agregar Tarea", command=self.agregar_tarea, **self.estilo_boton)
        self.boton_agregar.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        # Lista de tareas
        self.marco_tareas = tk.Frame(root)
        self.marco_tareas.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
        self.lista_tareas = tk.Listbox(self.marco_tareas, width=50, font=self.estilo_fuente)
        self.lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar = tk.Scrollbar(self.marco_tareas, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.lista_tareas.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.lista_tareas.yview)

        # Botones para administrar tareas
        self.boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea, **self.estilo_boton)
        self.boton_eliminar.grid(row=4, column=0, padx=5, pady=5)

        self.boton_editar = tk.Button(root, text="Editar Tarea", command=self.editar_tarea, **self.estilo_boton)
        self.boton_editar.grid(row=4, column=1, padx=5, pady=5)

        # Crédito "De Andree Mungi" como marca de agua
        self.marca_de_agua = tk.Label(root, text="De Andree Mungi", font=("Arial", 8), bg="#f0f0f0", fg="gray")
        self.marca_de_agua.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

        # Configuración inicial
        self.actualizar_lista_tareas()

    def agregar_tarea(self):
        titulo = self.entrada_titulo.get()
        descripcion = self.entrada_descripcion.get()
        if titulo and descripcion:
            self.tareas.append((titulo, descripcion, False))  # False indica que la tarea no está completada
            self.actualizar_lista_tareas()
        else:
            messagebox.showerror("Error", "Por favor ingresa tanto el título como la descripción de la tarea.")

    def eliminar_tarea(self):
        # Verificar si hay algún elemento seleccionado
        if self.lista_tareas.curselection():
            indice_tarea_seleccionada = self.lista_tareas.curselection()[0]
            del self.tareas[indice_tarea_seleccionada]
            self.actualizar_lista_tareas()
        else:
            messagebox.showerror("Error", "Ninguna tarea seleccionada.")

    def editar_tarea(self):
        # Verificar si hay algún elemento seleccionado
        if self.lista_tareas.curselection():
            indice_tarea_seleccionada = self.lista_tareas.curselection()[0]
            titulo, descripcion, completada = self.tareas[indice_tarea_seleccionada]

            # Mostrar ventana de edición
            ventana_edicion = tk.Toplevel(self.root)
            ventana_edicion.title("Editar Tarea")
            ventana_edicion.configure(background="#f0f0f0")

            etiqueta_titulo = tk.Label(ventana_edicion, text="Título de la Tarea:", font=self.estilo_fuente, bg="#f0f0f0")
            etiqueta_titulo.grid(row=0, column=0, padx=10, pady=5)
            entrada_titulo = tk.Entry(ventana_edicion, font=self.estilo_fuente)
            entrada_titulo.grid(row=0, column=1, padx=10, pady=5)
            entrada_titulo.insert(tk.END, titulo)

            etiqueta_descripcion = tk.Label(ventana_edicion, text="Descripción de la Tarea:", font=self.estilo_fuente, bg="#f0f0f0")
            etiqueta_descripcion.grid(row=1, column=0, padx=10, pady=5)
            entrada_descripcion = tk.Entry(ventana_edicion, font=self.estilo_fuente)
            entrada_descripcion.grid(row=1, column=1, padx=10, pady=5)
            entrada_descripcion.insert(tk.END, descripcion)

            # Checkbox para marcar la tarea como completada
            completada_var = tk.BooleanVar()
            completada_var.set(completada)
            completada_checkbox = tk.Checkbutton(ventana_edicion, text="Completada", variable=completada_var, bg="#f0f0f0")
            completada_checkbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

            # Función para aplicar cambios
            def aplicar_cambios():
                nuevo_titulo = entrada_titulo.get()
                nueva_descripcion = entrada_descripcion.get()
                nueva_completada = completada_var.get()
                self.tareas[indice_tarea_seleccionada] = (nuevo_titulo, nueva_descripcion, nueva_completada)
                self.actualizar_lista_tareas()
                ventana_edicion.destroy()

            boton_aplicar_cambios = tk.Button(ventana_edicion, text="Aplicar Cambios", command=aplicar_cambios, **self.estilo_boton)
            boton_aplicar_cambios.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        else:
            messagebox.showerror("Error", "Ninguna tarea seleccionada.")

    def actualizar_lista_tareas(self):
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            titulo = f"{tarea[0]}: {tarea[1]}"
            if tarea[2]:  # Si la tarea está completada, añadir un símbolo de check
                titulo += " \u2713"  # Símbolo de check Unicode
            self.lista_tareas.insert(tk.END, titulo)

if __name__ == "__main__":
    root = tk.Tk()
    app = AdministradorTareasApp(root)
    root.mainloop()
