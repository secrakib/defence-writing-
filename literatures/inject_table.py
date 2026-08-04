import re

def insert_table():
    with open(r'e:\Writing Defence\my.tex', 'r', encoding='utf-8') as f:
        content = f.read()

    with open(r'e:\Writing Defence\literatures\table.tex', 'r', encoding='utf-8') as f:
        table_content = f.read()

    # Insert usepackage
    if r'\usepackage{longtable}' not in content:
        content = content.replace(r'\usepackage{colortbl}', r'\usepackage{colortbl}' + '\n' + r'\usepackage{longtable}' + '\n' + r'\usepackage{pdflscape}')

    # Insert subsection and table
    insertion = r"""
\subsection{Summary of Dialectal Resources}
Table \ref{tab:literature_summary} summarizes the major dialectal datasets and resources reviewed in this section, detailing their coverage, architecture, evaluation metrics, and state-of-the-art performance.

""" + table_content

    # Target point
    target = r"direct, multi-directional, poly-dialectal translation within a single, unified neural architecture."
    
    if target in content and r'\subsection{Summary of Dialectal Resources}' not in content:
        content = content.replace(target, target + '\n\n' + insertion)
    
    with open(r'e:\Writing Defence\my.tex', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    insert_table()
