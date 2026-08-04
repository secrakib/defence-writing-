import codecs
import re

file_path = 'e:/Writing Defence/xelatex.tex'

with codecs.open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert Graph 1: Topology
graph1_latex = r"""
\begin{figure}[htbp]
  \centering
  \includegraphics[width=\textwidth]{graphics/topology_comparison.pdf}
  \caption{Structural comparison between the traditional pivot translation approach (routing through Standard Bangla) and the proposed direct poly-dialectal mapping topology.}
  \label{fig:topology}
\end{figure}
"""
content = content.replace(
    "paradigm shift from uni-dialectal modeling to a holistic, poly-dialectal approach.",
    "paradigm shift from uni-dialectal modeling to a holistic, poly-dialectal approach.\n" + graph1_latex
)

# 2. Insert Graph 6: Timeline
graph6_latex = r"""
\begin{figure}[htbp]
  \centering
  \includegraphics[width=\textwidth]{graphics/dataset_timeline.pdf}
  \caption{Evolution of Bangla regional dialect datasets and resources over time, highlighting the scale and dialectal coverage of the proposed corpus.}
  \label{fig:timeline}
\end{figure}
"""
content = content.replace(
    "deploying the resulting system as a publicly accessible web application.",
    "deploying the resulting system as a publicly accessible web application.\n" + graph6_latex
)

# 3. Insert Graph 3: LoRA Efficiency
graph3_latex = r"""
\begin{figure}[htbp]
  \centering
  \includegraphics[width=\textwidth]{graphics/lora_efficiency.pdf}
  \caption{Parameter efficiency of LoRA fine-tuning across the three evaluated model architectures, demonstrating over 98\% reduction in trainable parameters.}
  \label{fig:lora_efficiency}
\end{figure}
"""
content = content.replace(
    "approximately 4.7M for BanglaT5 and 9.8M for NLLB-200 and mBART-50.",
    "approximately 4.7M for BanglaT5 and 9.8M for NLLB-200 and mBART-50.\n" + graph3_latex
)

# 4. Insert Graph 2: Proximity vs BLEU
graph2_latex = r"""
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.9\textwidth]{graphics/proximity_vs_bleu.pdf}
  \caption{Scatter plot illustrating the inverse relationship between a dialect's linguistic proximity to Standard Bangla and the resulting translation quality (BLEU score).}
  \label{fig:proximity_bleu}
\end{figure}
"""
# Use regex to insert after \end{enumerate} in the directionality section
pattern = r"(\\end\{enumerate\}\s*\\begin\{figure\}\[htbp\]\s*\\centering\s*\\includegraphics\[width=0\.85\\textwidth\]\{graphics/directionality\.png\})"
content = re.sub(pattern, lambda m: "\\end{enumerate}\n\n" + graph2_latex + "\n\\begin{figure}[htbp]\n  \\centering\n  \\includegraphics[width=0.85\\textwidth]{graphics/directionality.png}", content)

# 5. Replace Graph 4: Error Taxonomy
content = content.replace(
    r"\includegraphics[width=0.75\textwidth]{graphics/error_analysis.png}",
    r"\includegraphics[width=0.9\textwidth]{graphics/error_taxonomy.pdf}"
)

# 6. Insert Graph 5: Quantization
graph5_latex = r"""
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.65\textwidth]{graphics/quantization_radar.pdf}
  \caption{Multidimensional performance trade-off (Radar chart) demonstrating the advantages of INT8 quantization in reducing latency and memory footprint while preserving translation quality.}
  \label{fig:quantization}
\end{figure}
"""
content = re.sub(
    r"(\\end\{table\}\s*\\subsection\{User Interface and Translation Demonstrations\})",
    lambda m: "\\end{table}\n\n" + graph5_latex + "\n\\subsection{User Interface and Translation Demonstrations}",
    content
)

with codecs.open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated xelatex.tex")
