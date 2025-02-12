import os
import pytest
from datetime import datetime
from src.converter import JiraXMLConverter
from src.utils.xml_parser import XMLParseError

class TestJiraXMLConverter:
    @pytest.fixture
    def converter(self):
        """Fixture que proporciona una instancia del conversor."""
        return JiraXMLConverter()

    @pytest.fixture
    def sample_xml_path(self):
        """Fixture que proporciona la ruta al XML de prueba."""
        return os.path.join('tests', 'data', 'sample.xml')

    def test_initialization(self, converter):
        """Prueba la inicialización correcta del conversor."""
        assert converter.root is not None
        assert converter.progress is not None
        assert converter.status_label is not None
        assert converter.error_label is not None

    def test_parse_jira_date(self, converter):
        """Prueba la conversión de fechas de Jira."""
        test_date = "Wed, 5 Feb 2025 12:30:00 -0500"
        fecha, hora = converter.parse_jira_date(test_date)
        assert fecha == "05/02/2025"
        assert hora == "12:30:00"

    def test_parse_invalid_date(self, converter):
        """Prueba el manejo de fechas inválidas."""
        test_date = "Invalid Date"
        fecha, hora = converter.parse_jira_date(test_date)
        assert fecha == ""
        assert hora == ""

    def test_clean_xml_content(self, converter):
        """Prueba la limpieza de contenido XML."""
        test_content = "Test\x00Content\x1FWith\x08Invalid\x0BChars"
        cleaned = converter.clean_xml_content(test_content)
        assert "\x00" not in cleaned
        assert "\x1F" not in cleaned
        assert "\x08" not in cleaned
        assert "\x0B" not in cleaned
        assert cleaned == "TestContentWithInvalidChars"

    def test_decode_html_entities(self, converter):
        """Prueba la decodificación de entidades HTML."""
        test_text = "Test &amp; Example &lt;tag&gt;"
        decoded = converter.decode_html_entities(test_text)
        assert decoded == "Test & Example <tag>"

    def test_get_customfield_value_numeric(self, converter, mocker):
        """Prueba la obtención de campos personalizados numéricos."""
        mock_item = mocker.Mock()
        mock_customfield = mocker.Mock()
        mock_name = mocker.Mock(text="Horas utilizadas")
        mock_value = mocker.Mock(text="8.5")
        
        mock_customfield.find.side_effect = [mock_name, mock_value]
        mock_item.findall.return_value = [mock_customfield]
        
        value = converter.get_customfield_value(mock_item, "Horas utilizadas")
        assert value == 8.5

    def test_get_customfield_value_text(self, converter, mocker):
        """Prueba la obtención de campos personalizados de texto."""
        mock_item = mocker.Mock()
        mock_customfield = mocker.Mock()
        mock_name = mocker.Mock(text="Empresa")
        mock_value = mocker.Mock(text="Test Company")
        
        mock_customfield.find.side_effect = [mock_name, mock_value]
        mock_item.findall.return_value = [mock_customfield]
        
        value = converter.get_customfield_value(mock_item, "Empresa")
        assert value == "Test Company"

    def test_get_assignee(self, converter, mocker):
        """Prueba la obtención del asignado."""
        mock_item = mocker.Mock()
        mock_assignee = mocker.Mock(text="John Doe")
        mock_item.find.return_value = mock_assignee
        
        assignee = converter.get_assignee(mock_item)
        assert assignee == "John Doe"

    def test_get_assignee_not_found(self, converter, mocker):
        """Prueba el manejo de asignado no encontrado."""
        mock_item = mocker.Mock()
        mock_item.find.return_value = None
        
        assignee = converter.get_assignee(mock_item)
        assert assignee == "No asignado"

    def test_get_reporter(self, converter, mocker):
        """Prueba la obtención del reportero."""
        mock_item = mocker.Mock()
        mock_reporter = mocker.Mock(text="Jane Doe")
        mock_item.find.return_value = mock_reporter
        
        reporter = converter.get_reporter(mock_item)
        assert reporter == "Jane Doe"

    def test_get_reporter_not_found(self, converter, mocker):
        """Prueba el manejo de reportero no encontrado."""
        mock_item = mocker.Mock()
        mock_item.find.return_value = None
        
        reporter = converter.get_reporter(mock_item)
        assert reporter == "No especificado"