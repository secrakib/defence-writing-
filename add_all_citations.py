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
        line = re.sub(r'\bBanglaT5(?:\'s)?\b(?!\s*\\cite)', r'\g<0> \\cite{bhattacharjee-etal-2023-banglanlg}', line)
        line = re.sub(r'\bNLLB-200(?:\'s)?\b(?!\s*\\cite)', r'\g<0> \\cite{nllb2022}', line)
        line = re.sub(r'\bmBART-50(?:\'s)?\b(?!\s*\\cite)', r'\g<0> \\cite{tang2020multilingual}', line)
        line = re.sub(r'\bLoRA(?:\'s)?\b(?!\s*\\cite)', r'\g<0> \\cite{hu2021lora}', line)
        line = re.sub(r'\bBLEU(?:\'s)?\b(?!\s*\\cite)', r'\g<0> \\cite{papineni2002bleu}', line)
        line = re.sub(r'\bchrF\+\+(?:\'s)?\b(?!\s*\\cite)', r'\g<0> \\cite{popovic2015chrf}', line)
        line = re.sub(r'\bMETEOR(?:\'s)?\b(?!\s*\\cite)', r'\g<0> \\cite{banerjee2005meteor}', line)
        line = re.sub(r'\bTER(?:\'s)?\b(?!\s*\\cite)', r'\g<0> \\cite{snover2006study}', line)
        line = re.sub(r'\bTransformers(?:\'s)?\b(?!\s*\\cite)', r'\g<0> \\cite{vaswani2017attention}', line)
        line = re.sub(r'\bTransformer(?:\'s)?\b(?!\s*\\cite)(?!s\b)', r'\g<0> \\cite{vaswani2017attention}', line)
        new_lines.append(line)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

if __name__ == '__main__':
    process_file(r'e:\Writing Defence\my.tex')
