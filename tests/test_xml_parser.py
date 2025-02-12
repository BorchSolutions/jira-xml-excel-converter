import pytest
import os
from src.utils.xml_parser import XMLParser, XMLParseError

class TestXMLParser:
    @pytest.fixture
    def parser(self):
        """Fixture que proporciona una instancia del parser."""
        return XMLParser()

    @pytest.fixture
    def sample_xml_path(self):
        """Fixture que proporciona la ruta al XML de prueba."""
        return os.path.join('tests', 'data', 'sample.xml')

    def test_read_xml_file(self, parser, sample_xml_path):
        """Prueba la lectura correcta de un archivo XML."""
        content = parser.read_file(sample_xml_path)
        assert content is not None
        assert isinstance(content, str)
        assert len(content) > 0

    def test_read_invalid_file(self, parser):
        """Prueba el manejo de archivo inválido."""
        with pytest.raises(XMLParseError):
            parser.read_file("invalid_file.xml")

    def test_parse_xml_content(self, parser):
        """Prueba el parsing de contenido XML válido."""
        xml_content = """
        <?xml version="1.0" encoding="UTF-8"?>
        <rss version="0.92">
            <channel>
                <item>
                    <title>Test Issue</title>
                    <key>TEST-1</key>
                    <type>Bug</type>
                </item>
            </channel>
        </rss>
        """
        root = parser.parse_content(xml_content)
        assert root is not None
        assert root.tag == "rss"
        assert root.attrib["version"] == "0.92"

    def test_parse_invalid_content(self, parser):
        """Prueba el manejo de contenido XML inválido."""
        with pytest.raises(XMLParseError):
            parser.parse_content("<invalid>XML<<<")

    def test_extract_items(self, parser):
        """Prueba la extracción de items del XML."""
        xml_content = """
        <?xml version="1.0" encoding="UTF-8"?>
        <rss version="0.92">
            <channel>
                <item>
                    <title>Issue 1</title>
                    <key>TEST-1</key>
                </item>
                <item>
                    <title>Issue 2</title>
                    <key>TEST-2</key>
                </item>
            </channel>
        </rss>
        """
        root = parser.parse_content(xml_content)
        items = parser.extract_items(root)
        assert len(items) == 2
        assert items[0].find("key").text == "TEST-1"
        assert items[1].find("key").text == "TEST-2"

    def test_extract_no_items(self, parser):
        """Prueba el manejo de XML sin items."""
        xml_content = """
        <?xml version="1.0" encoding="UTF-8"?>
        <rss version="0.92">
            <channel>
            </channel>
        </rss>
        """
        root = parser.parse_content(xml_content)
        items = parser.extract_items(root)
        assert len(items) == 0

    def test_get_field_value(self, parser):
        """Prueba la obtención de valores de campos."""
        xml_content = """
        <item>
            <title>Test Issue</title>
            <key>TEST-1</key>
            <type>Bug</type>
        </item>
        """
        root = parser.parse_content(f"<rss><channel>{xml_content}</channel></rss>")
        item = root.find(".//item")
        assert parser.get_field_value(item, "key") == "TEST-1"
        assert parser.get_field_value(item, "type") == "Bug"
        assert parser.get_field_value(item, "nonexistent") == ""

    def test_validate_xml_structure(self, parser):
        """Prueba la validación de la estructura XML."""
        valid_xml = """
        <?xml version="1.0" encoding="UTF-8"?>
        <rss version="0.92">
            <channel>
                <item>
                    <title>Test</title>
                </item>
            </channel>
        </rss>
        """
        assert parser.validate_structure(parser.parse_content(valid_xml))

        invalid_xml = "<wrongroot></wrongroot>"
        assert not parser.validate_structure(parser.parse_content(invalid_xml))

    def test_clean_field_value(self, parser):
        """Prueba la limpieza de valores de campos."""
        assert parser.clean_field_value(" Test Value ") == "Test Value"
        assert parser.clean_field_value("Test\nValue") == "Test Value"
        assert parser.clean_field_value("Test\t\rValue") == "Test Value"
        assert parser.clean_field_value(None) == ""