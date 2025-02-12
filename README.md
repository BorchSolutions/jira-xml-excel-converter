# Jira XML to Excel Converter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Made with Pandas](https://img.shields.io/badge/Made%20with-Pandas-1f425f.svg)](https://pandas.pydata.org/)

A Python GUI application that converts Jira XML exports to Excel (.xlsx) with custom field support, date formatting, and hyperlink preservation. Features progress tracking, error handling, and automated column formatting.

<img src="/api/placeholder/800/400" alt="Application Screenshot">

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/jira-xml-excel-converter.git

# Navigate to the project directory
cd jira-xml-excel-converter

# Install required packages
pip install -r requirements.txt

# Run the application
python jira-to-excel.py
```

## ✨ Features

- **User-Friendly GUI**
  - Simple and intuitive window interface
  - Progress bar for tracking conversion status
  - Status and error messages
  - File selection button

- **Data Processing**
  - XML parsing with encoding handling
  - Standard and custom field extraction
  - Date conversion to dd/mm/yyyy format
  - Date and time column separation

- **Excel Formatting**
  - Active hyperlinks to Jira tasks
  - Numeric formatting for hours
  - Automatic column width adjustment
  - Visual styles for better readability

## 📋 Processed Fields

- Task Code (with active hyperlink)
- Type
- Priority
- Company (custom field)
- Task Type (custom field)
- Hours Used (numeric field)
- Status
- Summary
- Assignee
- Reporter
- Creation and Update dates/times

## 🛠 Requirements

### Dependencies
```bash
pip install pandas openpyxl
```

### Libraries Used
- `xml.etree.ElementTree`: XML processing
- `pandas`: Data handling and Excel export
- `tkinter`: GUI interface
- `openpyxl`: Advanced Excel formatting
- `datetime`: Date and time handling
- `codecs`: File encoding management
- `threading`: Background processing

## 📖 Usage

1. Run the application:
   ```python
   python jira-to-excel.py
   ```

2. Follow these steps:
   - Click "Select XML File"
   - Choose your Jira XML export
   - Wait for processing to complete
   - Find the Excel file in the same location

3. Output:
   - Excel file named: `jira_export_[TIMESTAMP].xlsx`
   - All processed columns included
   - Optimized format for filtering and analysis

## 🏗 Code Structure

### Main Class: `JiraXMLConverter`

#### Interface Methods
- `__init__`: Window initialization
- `setup_ui`: Visual elements configuration
- `run`: Application startup

#### Processing Methods
- `process_file`: File selection handling
- `process_xml`: Main XML processing
- `parse_jira_date`: Date conversion
- `clean_xml_content`: XML cleaning

#### Extraction Methods
- `get_text`: XML element text extraction
- `get_customfield_value`: Custom fields processing
- `get_assignee`: Assignee retrieval
- `get_reporter`: Reporter retrieval

## ⚠️ Important Notes

- XML must be a valid Jira export
- Custom fields must exist in the XML
- Dates are processed considering timezone
- Hours are formatted with one decimal place
- Hyperlinks point to Jira tasks

## 🐛 Error Handling

- XML file validation
- Special character handling
- Safe numeric data conversion
- Descriptive error messages
- Error logging recovery

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

Bryan Ramírez - [Your GitHub Profile](https://github.com/ezzeker)

## 🙏 Acknowledgments

- Jira for the XML export functionality
- Python community for the amazing libraries
- All contributors who help improve this tool

## 📝 To-Do

- [ ] Add support for multiple XML files
- [ ] Implement custom field mapping
- [ ] Add export templates
- [ ] Support for different date formats
- [ ] Dark mode for GUI
