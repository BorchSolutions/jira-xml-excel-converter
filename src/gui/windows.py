"""
Módulo de interfaz gráfica para el conversor XML a Excel.
"""

import tkinter as tk
from tkinter import ttk, filedialog
import threading

class MainWindow:
    """Ventana principal de la aplicación."""

    def __init__(self, process_callback):
        """
        Inicializa la ventana principal.

        Args:
            process_callback (callable): Función para procesar el archivo XML
        """
        self.root = tk.Tk()
        self.root.title("Conversor XML Jira a Excel")
        self.root.geometry("600x350")
        self.process_callback = process_callback
        self.setup_ui()

    def setup_ui(self):
        """Configura los elementos de la interfaz gráfica."""
        # Configuración de estilo
        style = ttk.Style()
        style.configure("Custom.TButton", padding=10)
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Título
        title_label = ttk.Label(
            main_frame, 
            text="Conversor de XML Jira a Excel",
            font=("Helvetica", 14, "bold")
        )
        title_label.pack(pady=10)

        # Botón de selección
        self.select_button = ttk.Button(
            main_frame,
            text="Seleccionar archivo XML",
            command=self.select_file,
            style="Custom.TButton"
        )
        self.select_button.pack(pady=20)

        # Barra de progreso
        self.progress = ttk.Progressbar(
            main_frame,
            orient="horizontal",
            length=400,
            mode="determinate"
        )
        self.progress.pack(pady=20)

        # Etiquetas de estado y error
        self.status_label = ttk.Label(
            main_frame,
            text="Esperando archivo...",
            font=("Helvetica", 10),
            wraplength=500
        )
        self.status_label.pack(pady=10)

        self.error_label = ttk.Label(
            main_frame,
            text="",
            foreground="red",
            font=("Helvetica", 10),
            wraplength=500
        )
        self.error_label.pack(pady=10)

    def select_file(self):
        """Maneja la selección de archivo y inicia el procesamiento."""
        file_path = filedialog.askopenfilename(
            filetypes=[("XML files", "*.xml")]
        )
        if file_path:
            self.select_button["state"] = "disabled"
            self.error_label["text"] = ""
            thread = threading.Thread(
                target=self.process_callback, 
                args=(file_path,)
            )
            thread.start()

    def update_progress(self, value, status_text, error_text=None):
        """
        Actualiza la barra de progreso y mensajes.

        Args:
            value (int): Valor del progreso (0-100)
            status_text (str): Texto de estado
            error_text (str, optional): Texto de error
        """
        self.progress["value"] = value
        self.status_label["text"] = status_text
        if error_text:
            self.error_label["text"] = f"Error: {error_text}"
            self.select_button["state"] = "normal"
        elif value == 100:
            self.select_button["state"] = "normal"
        self.root.update_idletasks()

    def run(self):
        """Inicia el loop principal de la aplicación."""
        self.root.mainloop()