import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    new_lines = []
    for i in range(len(lines)):
        line = lines[i]
        if i < 450 or '\\includegraphics' in line or '\\url' in line or 'bibliography' in line or 'bibliographystyle' in line:
            new_lines.append(line)
            continue
        line = re.sub(r'chrF\+\+(?!\s*\\cite)', r'chrF++ \\cite{popovic2015chrf}', line)
        new_lines.append(line)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

if __name__ == '__main__':
    process_file(r'e:\Writing Defence\my.tex')
