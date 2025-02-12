# Guía de Contribución

¡Gracias por tu interés en contribuir al Conversor XML de Jira a Excel! Esta guía te ayudará a entender el proceso de contribución y los estándares que seguimos.

## Tabla de Contenidos
- [Código de Conducta](#código-de-conducta)
- [¿Cómo Puedo Contribuir?](#cómo-puedo-contribuir)
- [Estilo de Código](#estilo-de-código)
- [Proceso de Pull Request](#proceso-de-pull-request)
- [Desarrollo Local](#desarrollo-local)
- [Pruebas](#pruebas)
- [Documentación](#documentación)

## Código de Conducta

Este proyecto y todos sus participantes están bajo un Código de Conducta. Al contribuir, te comprometes a mantener un ambiente respetuoso y colaborativo.

- Usa lenguaje inclusivo
- Respeta diferentes puntos de vista y experiencias
- Acepta críticas constructivas
- Enfócate en lo mejor para la comunidad
- Muestra empatía hacia otros miembros

## ¿Cómo Puedo Contribuir?

### Reportando Bugs
1. Verifica que el bug no haya sido reportado antes
2. Crea un issue usando la plantilla de bugs
3. Incluye:
   - Descripción clara del problema
   - Pasos para reproducirlo
   - Comportamiento esperado
   - Capturas de pantalla si aplica
   - Entorno (OS, Python version, etc.)

### Sugiriendo Mejoras
1. Revisa las mejoras ya sugeridas
2. Crea un issue usando la plantilla de mejoras
3. Describe detalladamente la mejora
4. Explica por qué sería útil
5. Considera implicaciones de implementación

### Pull Requests
1. Crea un fork del repositorio
2. Crea una rama para tu feature/fix
3. Implementa tus cambios
4. Asegúrate de seguir el estilo de código
5. Añade pruebas si es necesario
6. Actualiza la documentación
7. Crea el pull request

## Estilo de Código

### Python
- Seguimos PEP 8
- Usamos type hints cuando es posible
- Docstrings en formato Google
- Líneas máximo de 88 caracteres
- Imports organizados según:
  1. Stdlib
  2. Third-party
  3. Local

### Ejemplo de Estilo
```python
from typing import List, Optional
import xml.etree.ElementTree as ET

import pandas as pd

from .utils import parse_date


class XMLProcessor:
    """Procesa archivos XML de Jira.

    Args:
        file_path: Ruta al archivo XML.
        encoding: Codificación del archivo.

    Attributes:
        path: Ruta al archivo.
        tree: Árbol XML parseado.
    """

    def __init__(self, file_path: str, encoding: str = "utf-8") -> None:
        self.path = file_path
        self.tree = None

    def process_file(self) -> Optional[pd.DataFrame]:
        """Procesa el archivo XML y retorna un DataFrame.

        Returns:
            DataFrame con los datos procesados o None si hay error.

        Raises:
            XMLParseError: Si hay error al parsear el XML.
        """
        try:
            self.tree = ET.parse(self.path)
            return self._process_tree()
        except ET.ParseError as e:
            raise XMLParseError(f"Error parsing XML: {str(e)}")
```

## Proceso de Pull Request

1. **Preparación**
   - Actualiza tu fork
   - Crea una rama descriptiva
   - Implementa tus cambios
   - Ejecuta las pruebas

2. **Creación del PR**
   - Título claro y descriptivo
   - Descripción detallada
   - Referencias a issues relacionados
   - Lista de cambios realizados

3. **Revisión**
   - Responde a los comentarios
   - Realiza los cambios solicitados
   - Mantén actualizada la rama

4. **Merge**
   - El equipo principal revisará
   - Se solicitarán cambios si es necesario
   - Se aprobará cuando esté listo

## Desarrollo Local

1. **Configuración**
   ```bash
   git clone https://github.com/yourusername/jira-xml-excel-converter.git
   cd jira-xml-excel-converter
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

2. **Estructura del Proyecto**
   ```
   src/               # Código fuente
   ├── converter.py   # Clase principal
   ├── utils/        # Utilidades
   └── gui/          # Interfaz gráfica
   
   tests/            # Pruebas
   docs/             # Documentación
   examples/         # Ejemplos
   ```

## Pruebas

### Ejecutar Pruebas
```bash
pytest tests/
pytest tests/test_converter.py -v
pytest tests/ -k "test_xml"
```

### Escribir Pruebas
```python
def test_xml_parsing():
    """Test que el parser XML maneja correctamente los datos."""
    processor = XMLProcessor("tests/data/sample.xml")
    df = processor.process_file()
    assert df is not None
    assert len(df) > 0
    assert "Código" in df.columns
```

## Documentación

### Docstrings
- Usar formato Google
- Incluir Args, Returns, Raises
- Ejemplos si son útiles

### Documentación del Proyecto
- README.md: Visión general
- USAGE.md: Guía detallada
- Comentarios en código cuando necesario
- Documentar cambios en CHANGELOG.md