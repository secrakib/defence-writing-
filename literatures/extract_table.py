import zipfile
import xml.etree.ElementTree as ET
import json

z = zipfile.ZipFile(r'e:\Writing Defence\literatures\Literature Index Table.docx')
doc = ET.fromstring(z.read('word/document.xml'))
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

tables = doc.findall('.//w:tbl', ns)
rows = []
if tables:
    for row in tables[0].findall('.//w:tr', ns):
        row_data = []
        for cell in row.findall('.//w:tc', ns):
            paragraphs = cell.findall('.//w:p', ns)
            cell_text = []
            for p in paragraphs:
                texts = [node.text for node in p.iter() if node.tag == f"{{{ns['w']}}}t" and node.text]
                cell_text.append(''.join(texts))
            row_data.append('\n'.join(cell_text).strip())
        rows.append(row_data)

with open(r'e:\Writing Defence\literatures\table_output.json', 'w', encoding='utf-8') as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)
