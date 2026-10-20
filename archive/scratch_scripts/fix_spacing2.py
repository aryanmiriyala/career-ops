import re

files_to_fix = [
    "templates/canonical-resume.tex",
    "master-documents/master-resume/resume.tex",
    "application-packages/eBay/Software-Engineer-Recent-Grad-Traffic/resume.tex"
]

for file_path in files_to_fix:
    with open(file_path, "r") as f:
        content = f.read()

    # Revert to tighter spacing so it fits on one page.
    content = content.replace("\\par\\vspace{6pt}%", "\\par\\vspace{3pt}%")
    content = content.replace("\\hrule height 0.4pt\\vspace{4pt}%", "\\hrule height 0.4pt\\vspace{3pt}%")

    with open(file_path, "w") as f:
        f.write(content)

