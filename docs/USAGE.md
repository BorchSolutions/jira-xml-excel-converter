# Guía de Uso: Jira XML to Excel Converter

Esta guía detalla cómo utilizar el conversor de XML de Jira a Excel, incluyendo instalación, configuración y casos de uso comunes.

## Tabla de Contenidos
- [Instalación](#instalación)
- [Uso Básico](#uso-básico)
- [Configuración de Jira](#configuración-de-jira)
- [Procesamiento de Archivos](#procesamiento-de-archivos)
- [Formato del Archivo de Salida](#formato-del-archivo-de-salida)
- [Solución de Problemas](#solución-de-problemas)
- [Preguntas Frecuentes](#preguntas-frecuentes)

## Instalación

### Requisitos Previos
- Python 3.6 o superior
- pip (gestor de paquetes de Python)
- Acceso a Jira para exportar archivos XML

### Pasos de Instalación
1. Clone el repositorio:
   ```bash
   git clone https://github.com/yourusername/jira-xml-excel-converter.git
   cd jira-xml-excel-converter
   ```

2. Instale las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Verifique la instalación:
   ```bash
   python main.py
   ```

## Uso Básico

1. **Iniciar la Aplicación**
   - Ejecute `python main.py`
   - Se abrirá una ventana con interfaz gráfica

2. **Seleccionar Archivo**
   - Haga clic en "Seleccionar archivo XML"
   - Navegue hasta su archivo XML exportado de Jira
   - Seleccione el archivo y haga clic en "Abrir"

3. **Procesamiento**
   - La barra de progreso mostrará el avance
   - Espere a que se complete el proceso
   - El archivo Excel se guardará automáticamente

## Configuración de Jira

### Exportar XML desde Jira
1. En Jira, vaya a la vista de issues deseada
2. Haga clic en "Exportar"
3. Seleccione "XML"
4. Configure los campos deseados
5. Descargue el archivo

### Campos Soportados
- Campos Estándar:
  - Código de tarea
  - Tipo
  - Prioridad
  - Estado
  - Resumen
  - Asignado
  - Reportado por
  - Fechas de creación/actualización

- Campos Personalizados:
  - Empresa
  - Tipo Tarea
  - Horas Utilizadas

## Procesamiento de Archivos

### Características del Procesamiento
- Conversión automática de fechas a formato dd/mm/yyyy
- Separación de fecha y hora en columnas diferentes
- Formateo de horas con un decimal
- Creación de hipervínculos activos
- Ajuste automático de anchos de columna

### Limitaciones
- Tamaño máximo de archivo: No especificado
- Tipos de campos personalizados soportados: texto, número
- Codificación de archivo soportada: UTF-8

## Formato del Archivo de Salida

### Nombre del Archivo
- Formato: `jira_export_YYYYMMDD_HHMMSS.xlsx`
- Ejemplo: `jira_export_20250212_143022.xlsx`

### Estructura del Excel
- Hoja única llamada "Tareas"
- Columnas ordenadas según campos estándar
- Formato especial para hipervínculos y números
- Anchos de columna optimizados

## Solución de Problemas

### Errores Comunes

1. **Error de Lectura XML**
   - Causa: XML mal formado o codificación incorrecta
   - Solución: Verificar la exportación de Jira

2. **Campos Faltantes**
   - Causa: Campo personalizado no encontrado
   - Solución: Verificar la configuración de exportación

3. **Error de Permisos**
   - Causa: No hay acceso de escritura en el directorio
   - Solución: Verificar permisos de carpeta

### Logs de Error
- Los errores se muestran en la interfaz
- Revise la consola para más detalles

## Preguntas Frecuentes

**P: ¿Puedo procesar múltiples archivos a la vez?**
R: No, actualmente solo se procesa un archivo por vez.

**P: ¿Se pueden personalizar los campos?**
R: No en esta versión. Se procesarán los campos predefinidos.

**P: ¿Se mantiene el formato de los campos personalizados?**
R: Sí, se respeta el formato numérico y de texto según corresponda.

**P: ¿Dónde se guarda el archivo Excel?**
R: En la misma ubicación que el archivo XML de origen.

**P: ¿Se pueden modificar los formatos de fecha?**
R: No en esta versión. Se usa el formato dd/mm/yyyy por defecto.