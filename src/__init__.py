"""
Jira XML to Excel Converter Package
---------------------------------
Este paquete proporciona funcionalidad para convertir archivos XML exportados de Jira
a formato Excel con formato específico y manejo de campos personalizados.
"""

from .converter import JiraXMLConverter
from .utils import XMLParseError

__version__ = '1.0.0'
__author__ = 'Bryan Ramírez'

__all__ = ['JiraXMLConverter', 'XMLParseError']