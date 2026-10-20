import re

files_to_fix = [
    "templates/canonical-resume.tex",
    "master-documents/master-resume/resume.tex",
    "application-packages/eBay/Software-Engineer-Recent-Grad-Traffic/resume.tex"
]

for file_path in files_to_fix:
    with open(file_path, "r") as f:
        content = f.read()

    # Revert to tighter spacing
    content = content.replace("\\par\\vspace{3pt}%", "\\par\\vspace{2pt}%")
    content = content.replace("\\hrule height 0.4pt\\vspace{3pt}%", "\\hrule height 0.4pt\\vspace{2pt}%")
    
    # Try \vspace{-6pt} in header
    content = content.replace("\\end{center}\\vspace{-2pt}", "\\end{center}\\vspace{-6pt}")

    with open(file_path, "w") as f:
        f.write(content)

