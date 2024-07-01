import os
import re
import docx
from PyPDF2 import PdfReader
from datetime import datetime

# Regular expression pattern to match SSNs
ssn_pattern = re.compile(r'\b\d{3}-\d{2}-\d{4}\b')

def search_ssn_in_text(text):
    ssns = ssn_pattern.findall(text)
    redacted_ssns = [re.sub(r'\d{2}-\d{4}', 'XX-XXXX', ssn) for ssn in ssns]
    return redacted_ssns

def search_ssn_in_docx(file_path):
    try:
        doc = docx.Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return search_ssn_in_text(' '.join(full_text))
    except Exception as e:
        print(f"Error reading DOCX file {file_path}: {e}")
        return []

def search_ssn_in_pdf(file_path):
    ssns = []
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            text = page.extract_text()
            ssns.extend(search_ssn_in_text(text))
    except Exception as e:
        print(f"Error reading PDF file {file_path}: {e}")
    return ssns

def search_ssn_in_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
        return search_ssn_in_text(text)
    except Exception as e:
        print(f"Error reading TXT file {file_path}: {e}")
        return []

def is_hidden(filepath):
    name = os.path.basename(os.path.abspath(filepath))
    return name.startswith('~$') or name.startswith('.')

def scan_current_folder():
    current_folder = os.getcwd()
    results = []

    for root, _, files in os.walk(current_folder):
        for file in files:
            if is_hidden(file):
                continue

            file_path = os.path.join(root, file)
            if file.endswith('.docx'):
                ssns = search_ssn_in_docx(file_path)
                if ssns:
                    results.append((file_path, ssns))
            elif file.endswith('.pdf'):
                ssns = search_ssn_in_pdf(file_path)
                if ssns:
                    results.append((file_path, ssns))
            elif file.endswith('.txt'):
                ssns = search_ssn_in_txt(file_path)
                if ssns:
                    results.append((file_path, ssns))
    
    return results

if __name__ == "__main__":
    ssn_results = scan_current_folder()
    output_lines = []
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    output_lines.append(f"Scan performed on: {current_time}\n")

    if ssn_results:
        for file_path, ssns in ssn_results:
            line = f"SSNs found in {file_path}: {ssns}"
            print(line)
            output_lines.append(line + "\n")
    else:
        line = "No SSNs found in the current folder."
        print(line)
        output_lines.append(line + "\n")
    
    output_filename = f"ssn_scan_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(output_filename, 'w') as f:
        f.writelines(output_lines)
