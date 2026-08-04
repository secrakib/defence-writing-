import json

def json_to_latex(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # We want 7 columns, ignore the 8th (BibTeX)
    headers = data[0][:-1]
    rows = [row[:-1] for row in data[1:]]

    latex_code = r"""
\begin{landscape}
\begin{longtable}{
    >{\raggedright\arraybackslash}p{2.5cm}
    >{\raggedright\arraybackslash}p{3cm}
    >{\raggedright\arraybackslash}p{3.5cm}
    >{\raggedright\arraybackslash}p{3cm}
    >{\raggedright\arraybackslash}p{4cm}
    >{\raggedright\arraybackslash}p{3.5cm}
    >{\raggedright\arraybackslash}p{4.5cm}
}
\caption{Comprehensive Summary of Bangla Regional Dialect NLP Resources and Datasets}
\label{tab:literature_summary} \\
\toprule
"""
    # Header row
    latex_code += " & ".join([f"\\textbf{{{h.replace('&', r'\\&')}}}" for h in headers]) + r" \\" + "\n"
    latex_code += r"\midrule" + "\n"
    latex_code += r"\endfirsthead" + "\n\n"
    
    latex_code += r"""
\multicolumn{7}{c}%
{{\bfseries \tablename\ \thetable{} -- continued from previous page}} \\
\toprule
"""
    latex_code += " & ".join([f"\\textbf{{{h.replace('&', r'\\&')}}}" for h in headers]) + r" \\" + "\n"
    latex_code += r"\midrule" + "\n"
    latex_code += r"\endhead" + "\n\n"
    
    latex_code += r"""
\midrule
\multicolumn{7}{r}{{Continued on next page}} \\
\bottomrule
\endfoot
""" + "\n"
    
    latex_code += r"""
\bottomrule
\endlastfoot
""" + "\n"

    for idx, row in enumerate(rows):
        # Escape LaTeX special characters
        cleaned_row = []
        for cell in row:
            cell = cell.replace('&', r'\&')
            cell = cell.replace('%', r'\%')
            cell = cell.replace('$', r'\$')
            cell = cell.replace('#', r'\#')
            cell = cell.replace('_', r'\_')
            cell = cell.replace('{', r'\{')
            cell = cell.replace('}', r'\}')
            cell = cell.replace('~', r'\textasciitilde')
            cell = cell.replace('^', r'\textasciicircum')
            cell = cell.replace('\n', r' \newline ')
            cell = cell.replace('κ', r'$\kappa$')
            cell = cell.replace('→', r'$\rightarrow$')
            cell = cell.replace('↔', r'$\leftrightarrow$')
            cell = cell.replace('’', "'")
            cell = cell.replace('‘', "'")
            cell = cell.replace('“', "``")
            cell = cell.replace('”', "''")
            cell = cell.replace('–', "--")
            cell = cell.replace('—', "---")
            cell = cell.replace('…', r'\dots')
            cleaned_row.append(cell)
        
        latex_code += " & ".join(cleaned_row) + r" \\" + "\n"
        if idx < len(rows) - 1:
             latex_code += r"\midrule" + "\n"

    latex_code += r"\end{longtable}" + "\n"
    latex_code += r"\end{landscape}" + "\n"

    with open(r'e:\Writing Defence\literatures\table.tex', 'w', encoding='utf-8') as f:
        f.write(latex_code)

if __name__ == '__main__':
    json_to_latex(r'e:\Writing Defence\literatures\table_output.json')
