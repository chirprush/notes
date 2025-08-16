template = """
\\section{Chapter %d}

\\subsection{Summary}

\\subsection{Analysis}
""".strip()

for i in range(1, 136):
    with open(f"chapters/chapter{i}.tex", "w") as f:
        f.write(template % i)
