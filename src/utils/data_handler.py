"""
Módulo para el manejo y procesamiento de datos.
"""

from datetime import datetime
import html

class DataHandler:
    """Clase para procesar y transformar datos."""

    @staticmethod
    def parse_jira_date(date_str):
        """
        Convierte una fecha de Jira al formato deseado.
        
        Args:
            date_str (str): Fecha en formato Jira
                
        Returns:
            tuple: (fecha en formato dd/mm/yyyy, hora en formato HH:MM:SS)
        """
        if not date_str:
            return "", ""
            
        try:
            formats = [
                "%a, %d %b %Y %H:%M:%S %z", #Formato Estandar
                "%a, %d %b %Y %H:%M:%S +0000", #Formato Alternativo
                "%Y-%m-%d %H:%M:%S", #Formato ISO
            ]
            
            for date_format in formats:
                try:
                    dt = datetime.strptime(date_str, date_format)
                    return dt.strftime("%d/%m/%Y"), dt.strftime("%H:%M:%S")
                except ValueError:
                    continue
                    
            return "", ""
        except Exception:
            return "", ""
    @staticmethod
    def clean_field_value(value):
        """
        Limpia y formatea un valor de campo.
        
        Args:
            value: Valor a limpiar
            
        Returns:
            str: Valor limpio y formateado
        """
        if value is None:
            return ""
        return str(value).strip()

    @staticmethod
    def decode_html_entities(text):
        """
        Decodifica entidades HTML en el texto.
        
        Args:
            text (str): Texto con entidades HTML
            
        Returns:
            str: Texto decodificado
        """
        if text:
            return html.unescape(text)
        return text

    @staticmethod
    def process_numeric_field(value, default=0.0):
        """
        Procesa un campo numérico.
        
        Args:
            value: Valor a procesar
            default: Valor por defecto si hay error
            
        Returns:
            float: Valor numérico procesado
        """
        try:
            return float(value or default)
        except (ValueError, TypeError):
            return default

    @staticmethod
    def format_field_value(value, field_type):
        """
        Formatea un valor según su tipo.
        
        Args:
            value: Valor a formatear
            field_type (str): Tipo de campo ('text', 'number', 'date', 'time')
            
        Returns:
            str: Valor formateado
        """
        if field_type == 'number':
            return f"{float(value):.1f}"
        elif field_type == 'date':
            return value.strftime("%d/%m/%Y") if isinstance(value, datetime) else value
        elif field_type == 'time':
            return value.strftime("%H:%M:%S") if isinstance(value, datetime) else value
        return str(value)