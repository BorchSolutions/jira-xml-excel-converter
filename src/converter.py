"""
Módulo principal del conversor XML de Jira a Excel.
"""

import os
from datetime import datetime
import pandas as pd
from .utils import XMLParser, ExcelFormatter
from .gui.windows import MainWindow

class JiraXMLConverter:
    """Clase principal para la conversión de XML de Jira a Excel."""

    def __init__(self):
        """Inicializa el conversor y la interfaz gráfica."""
        self.xml_parser = XMLParser()
        self.window = MainWindow(self.process_file)
        self.current_file = None

    def process_file(self, file_path):
        """
        Procesa el archivo XML y genera el Excel.
        
        Args:
            file_path (str): Ruta al archivo XML de Jira
        """
        self.current_file = file_path
        try:
            # Lectura y procesamiento del XML
            self.window.update_progress(20, "Procesando archivo XML...")
            items, links = self.xml_parser.parse_file(file_path)
            
            if not items:
                raise ValueError("No se encontraron datos para procesar")

            # Creación del DataFrame
            self.window.update_progress(50, "Creando DataFrame...")
            df = pd.DataFrame(items)

            # Configuración del archivo Excel
            self.window.update_progress(70, "Generando archivo Excel...")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = os.path.join(
                os.path.dirname(file_path),
                f'jira_export_{timestamp}.xlsx'
            )

            # Formateo y guardado del Excel
            self.window.update_progress(80, "Aplicando formato...")
            formatter = ExcelFormatter(df, output_path, links)
            if formatter.format_excel():
                self.window.update_progress(
                    100,
                    f"¡Proceso completado!\nArchivo guardado como:\n{output_path}"
                )
            else:
                raise Exception("Error al formatear el archivo Excel")

        except Exception as e:
            self.window.update_progress(
                0,
                "Error en el proceso",
                str(e)
            )

    def run(self):
        """Inicia la aplicación."""
        self.window.run()

if __name__ == "__main__":
    app = JiraXMLConverter()
    app.run()