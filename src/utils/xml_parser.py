"""
Módulo para el procesamiento de archivos XML.
"""

import xml.etree.ElementTree as ET
import codecs
import re
from .data_handler import DataHandler

class XMLParseError(Exception):
    """Excepción personalizada para errores de parsing XML."""
    pass

class XMLParser:
    """Clase para procesar archivos XML de Jira."""

    def __init__(self):
        """Inicializa el parser XML."""
        self.data_handler = DataHandler()

    def parse_file(self, file_path):
        """
        Parsea un archivo XML de Jira.
        
        Args:
            file_path (str): Ruta al archivo XML
            
        Returns:
            list: Lista de items procesados
            
        Raises:
            XMLParseError: Si hay error en el parsing
        """
        try:
            content = self._read_file(file_path)
            cleaned_content = self._clean_content(content)
            root = ET.fromstring(cleaned_content)
            return self._process_items(root)
        except Exception as e:
            raise XMLParseError(f"Error parsing XML: {str(e)}")

    def _read_file(self, file_path):
        """
        Lee el contenido del archivo XML.
        
        Args:
            file_path (str): Ruta al archivo
            
        Returns:
            str: Contenido del archivo
        """
        try:
            with codecs.open(file_path, 'r', encoding='utf-8', 
                           errors='ignore') as file:
                return file.read()
        except Exception as e:
            raise XMLParseError(f"Error reading file: {str(e)}")

    def _clean_content(self, content):
        """
        Limpia el contenido XML.
        
        Args:
            content (str): Contenido XML
            
        Returns:
            str: Contenido limpio
        """
        return re.sub(r'[\x00-\x08\x0B-\x0C\x0E-\x1F\x7F]', '', content)

    def _process_items(self, root):
        """
        Procesa los items del XML.
        
        Args:
            root: Elemento raíz del XML
            
        Returns:
            tuple: (Lista de diccionarios con datos procesados, Lista de links)
        """
        items = root.findall(".//item")
        processed_items = []
        links = []

        for item in items:
            try:
                processed_item = self._process_single_item(item)
                processed_items.append(processed_item)
                links.append(self._get_text(item, 'link'))
            except Exception as e:
                print(f"Error processing item: {str(e)}")
                continue

        return processed_items, links

    def _process_single_item(self, item):
        """
        Procesa un único item del XML.
        """
        fecha_creacion, hora_creacion = self.data_handler.parse_jira_date(
            self._get_text(item, 'created')
        )
        fecha_actualizacion, hora_actualizacion = self.data_handler.parse_jira_date(
            self._get_text(item, 'updated')
        )
        
        # Obtener fecha de inicio desde el campo personalizado
        fecha_inicio = self._get_customfield_value(item, 'Start date')
        if fecha_inicio:
            fecha_inicio, _ = self.data_handler.parse_jira_date(fecha_inicio)

        return {
            'Código': self._get_text(item, 'key'),
            'Tipo': self._get_text(item, 'type'),
            'Prioridad': self._get_text(item, 'priority'),
            'Empresa': self._get_customfield_value(item, 'Empresa'),
            'Tipo Tarea': self._get_customfield_value(item, 'Tipo tarea'),
            'Horas Utilizadas': self._get_customfield_value(item, 'Horas utilizadas'),
            'Estado': self._get_text(item, 'status'),
            'Resumen': self.data_handler.decode_html_entities(
                self._get_text(item, 'summary')
            ),
            'Asignado': self._get_assignee(item),
            'Reportado por': self._get_reporter(item),
            'Fecha Inicio': fecha_inicio,  # Nueva columna
            'Fecha Creación': fecha_creacion,
            'Hora Creación': hora_creacion,
            'Fecha Actualización': fecha_actualizacion,
            'Hora Actualización': hora_actualizacion
        }
    def _get_text(self, item, tag):
        """
        Obtiene el texto de un elemento XML de forma segura.
        
        Args:
            item: Elemento XML del item
            tag (str): Nombre de la etiqueta
            
        Returns:
            str: Texto del elemento o cadena vacía
        """
        element = item.find(tag)
        return self.data_handler.clean_field_value(
            element.text if element is not None else ''
        )

    def _get_customfield_value(self, item, field_name):
        """
        Obtiene el valor de un campo personalizado por nombre.
        
        Args:
            item: Elemento XML del item
            field_name (str): Nombre del campo personalizado
            
        Returns:
            str/float: Valor del campo personalizado
        """
        for customfield in item.findall(".//customfield"):
            name_elem = customfield.find('customfieldname')
            if name_elem is not None and name_elem.text == field_name:
                value_elem = customfield.find('.//customfieldvalue')
                if value_elem is not None:
                    if field_name == 'Horas utilizadas':
                        return self.data_handler.process_numeric_field(value_elem.text)
                    return self.data_handler.decode_html_entities(value_elem.text)
        return 0.0 if field_name == 'Horas utilizadas' else ''

    def _get_assignee(self, item):
        """
        Obtiene el nombre del asignado de forma segura.
        
        Args:
            item: Elemento XML del item
            
        Returns:
            str: Nombre del asignado o 'No asignado'
        """
        assignee = item.find('assignee')
        if assignee is not None:
            return assignee.text or assignee.attrib.get('accountid', 'No asignado')
        return 'No asignado'

    def _get_reporter(self, item):
        """
        Obtiene el nombre del reportero de forma segura.
        
        Args:
            item: Elemento XML del item
            
        Returns:
            str: Nombre del reportero o 'No especificado'
        """
        reporter = item.find('reporter')
        if reporter is not None:
            return reporter.text or reporter.attrib.get('accountid', 'No especificado')
        return 'No especificado'