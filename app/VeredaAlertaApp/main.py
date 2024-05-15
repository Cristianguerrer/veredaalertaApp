import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class VeredaAlertaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VeredaAlerta")

        # Crear el marco principal
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(padx=10, pady=10)

        # Título de la aplicación
        self.title_label = tk.Label(self.main_frame, text="VeredaAlerta", font=("Helvetica", 16))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Etiqueta y campo de entrada para el mensaje de alerta
        self.message_label = tk.Label(self.main_frame, text="Mensaje de Alerta:")
        self.message_label.grid(row=1, column=0, sticky="e", pady=5)

        self.message_entry = tk.Entry(self.main_frame, width=40)
        self.message_entry.grid(row=1, column=1, pady=5)

        # Etiqueta y campo de entrada para el nivel de alerta
        self.level_label = tk.Label(self.main_frame, text="Nivel de Alerta:")
        self.level_label.grid(row=2, column=0, sticky="e", pady=5)

        self.level_entry = tk.Entry(self.main_frame, width=40)
        self.level_entry.grid(row=2, column=1, pady=5)

        # Botón para agregar alerta
        self.add_alert_button = tk.Button(self.main_frame, text="Agregar Alerta", command=self.add_alert)
        self.add_alert_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Lista de alertas
        self.alerts_listbox = tk.Listbox(self.main_frame, width=60, height=10)
        self.alerts_listbox.grid(row=4, column=0, columnspan=2, pady=10)

        # Botón para mostrar detalles de la alerta seleccionada
        self.details_button = tk.Button(self.main_frame, text="Mostrar Detalles", command=self.show_details)
        self.details_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.alerts = []

    def add_alert(self):
        message = self.message_entry.get()
        level = self.level_entry.get()

        if not message or not level:
            messagebox.showwarning("Campos Vacíos", "Por favor, completa todos los campos.")
            return

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        alert = {"message": message, "level": level, "timestamp": timestamp}
        self.alerts.append(alert)

        self.alerts_listbox.insert(tk.END, f"{timestamp} - {level}")

        self.message_entry.delete(0, tk.END)
        self.level_entry.delete(0, tk.END)

    def show_details(self):
        selected_index = self.alerts_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Ninguna Selección", "Por favor, selecciona una alerta de la lista.")
            return

        alert = self.alerts[selected_index[0]]
        details = f"Mensaje: {alert['message']}\nNivel: {alert['level']}\nFecha y Hora: {alert['timestamp']}"
        messagebox.showinfo("Detalles de la Alerta", details)


if __name__ == "__main__":
    root = tk.Tk()
    app = VeredaAlertaApp(root)
    root.mainloop()
