import xml.etree.ElementTree as ET
from docx import Document

# Abra o arquivo XML
tree = ET.parse('arq.xml')
root = tree.getroot()

# Crie um novo documento DOCX
document = Document()

# Adicione os elementos do XML ao documento
for element in root:
    document.add_paragraph(element.text)

# Salve o documento
document.save('novo_documento.docx')
