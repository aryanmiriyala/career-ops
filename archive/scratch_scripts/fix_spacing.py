import re
import os

files_to_fix = [
    "templates/canonical-resume.tex",
    "master-documents/master-resume/resume.tex",
    "application-packages/eBay/Software-Engineer-Recent-Grad-Traffic/resume.tex"
]

for file_path in files_to_fix:
    with open(file_path, "r") as f:
        content = f.read()

    # 1. Replace -- with - in date ranges
    content = re.sub(r"([A-Za-z]+\.? \d{4})\s*--\s*([A-Za-z]+\.? \d{4}|Present)", r"\1 - \2", content)

    # 2. Fix the header to use naked URLs and two lines
    # We will just manually replace the center block.
    # Let's extract the title (e.g. Software Engineer ...)
    title_match = re.search(r"github\.com/aryanmiriyala\}\s*(?:\\\$\|\\\$|\||\$\|\$)?\s*(.*?)\n\\end\{center\}", content, re.DOTALL)
    title = title_match.group(1).strip() if title_match else "Software Engineer"
    title = title.replace("$|$", "").replace("GitHub", "").strip()
    if title.startswith("|"): title = title[1:].strip()

    new_header = r"""\begin{center}
  {\LARGE \textbf{Aryan Miriyala}}\\[2pt]
  \small
  +1 419-315-0444 $|$ \href{mailto:aryanmiriyala@gmail.com}{aryanmiriyala@gmail.com} $|$ \href{https://www.linkedin.com/in/aryan-miriyala-7788a21b6/}{linkedin.com/in/aryan-miriyala}\\
  \href{https://github.com/aryanmiriyala}{github.com/aryanmiriyala} $|$ """ + title + r"""
\end{center}\vspace{-2pt}"""

    content = re.sub(r"\\begin\{center\}.*?\\end\{center\}\\vspace\{-10pt\}", lambda m: new_header, content, flags=re.DOTALL)

    # 3. Adjust spacing in \resumesection
    content = content.replace("\\par\\vspace{2pt}%", "\\par\\vspace{6pt}%")
    content = content.replace("\\hrule height 0.4pt\\vspace{2pt}%", "\\hrule height 0.4pt\\vspace{4pt}%")

    with open(file_path, "w") as f:
        f.write(content)

print("Done fixing spacing and formatting.")
