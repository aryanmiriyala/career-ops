"""Render structured, evidence-checked content through fixed local templates."""
import re
import shutil
import subprocess
from pathlib import Path
import yaml


LATEX_ESCAPES = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '$': r'\$', '#': r'\#',
                 '_': r'\_', '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}'}

# Load contact info from central config
_CONTACT_CACHE: dict | None = None


def _load_contact(root: Path) -> dict:
    global _CONTACT_CACHE
    if _CONTACT_CACHE is None:
        contact_path = root / "profile" / "contact.yaml"
        if contact_path.is_file():
            _CONTACT_CACHE = yaml.safe_load(contact_path.read_text())
        else:
            _CONTACT_CACHE = {
                "name": "Aryan Miriyala",
                "phone": "+1 419-315-0444",
                "email": "aryanmiriyala@gmail.com",
                "linkedin": "https://www.linkedin.com/in/aryan-miriyala-7788a21b6/",
                "github": "https://github.com/aryanmiriyala",
                "default_title": "Software Engineer",
            }
    return _CONTACT_CACHE


def tex(value):
    return ''.join(LATEX_ESCAPES.get(char, char) for char in value).replace('\u2014', '--').replace('\u2013', '--')


def markdown_text(value):
    return value.replace('\u2014', '-').replace('\u2013', '-').strip()


def _contact_lines(root: Path, for_resume: bool = True) -> tuple[str, str]:
    """Generate contact lines for resume or cover letter."""
    c = _load_contact(root)
    name = c["name"]
    phone = c["phone"]
    email = c["email"]
    linkedin = c["linkedin"]
    github = c["github"]
    title = c.get("default_title", "Software Engineer")

    if for_resume:
        line1 = r"{\LARGE \textbf{" + tex(name) + r"}}\\[2pt]"
        line2 = r"\small"
        line3 = (tex(phone) + r" $|$ \href{mailto:" + tex(email) +
                 r"}{" + tex(email) + r"} $|$ \href{" + tex(linkedin) +
                 r"}{" + tex(linkedin) + r"}\\")
        line4 = r"\href{" + tex(github) + r"}{" + tex(github) + r"} $|$ " + tex(title)
        return line1, line2, line3, line4
    else:
        line1 = r"{\Large\textbf{" + tex(name) + r"}}"
        line2 = (tex(phone) + r" $|$ \href{mailto:" + tex(email) + r"}{" + tex(email) + r"} $|$ \href{" + tex(linkedin) + r"}{" + tex(linkedin) + r"}")
        return line1, line2


def resume_tex(draft, root: Path | None = None):
    if root is None:
        root = Path.cwd()
    summary = ''
    if draft.summary:
        summary = '\\resumesection{Professional Summary}\n' + tex(draft.summary[0].text) + '\n\n'
    def entries(values, projects=False):
        output = []
        for entry in values:
            if projects:
                output.append(f'\\projectHeading{{{tex(entry.name)}}}{{{tex(entry.title)}}}')
            else:
                output.extend([f'\\resumeSubheading', f'{{{tex(entry.title)}}}{{{tex(entry.dates)}}}',
                               f'{{{tex(entry.name)}}}{{{tex(entry.location)}}}'])
            output.append('\\begin{tightitemize}')
            output.extend(f'  \\item {tex(bullet.text)}' for bullet in entry.bullets)
            output.append('\\end{tightitemize}')
        return '\n'.join(output)
    project_section = ''
    if draft.projects:
        project_section = '\n\\resumesection{Projects}\n' + entries(draft.projects, True) + '\n'
    skills = '\\\n'.join(tex(claim.text) for claim in draft.skills)

    line1, line2, line3, line4 = _contact_lines(root, for_resume=True)

    return r'''\documentclass[letterpaper,11pt]{article}
\usepackage[letterpaper,left=0.22in,right=0.22in,top=0.10in,bottom=0.10in]{geometry}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage[english]{babel}
\input{glyphtounicode}
\pagestyle{empty}
\urlstyle{same}
\raggedright
\setlength{\parindent}{0pt}
\linespread{0.92}
\pdfgentounicode=1
\newcommand{\resumesection}[1]{\par\vspace{2pt}{\large\scshape #1}\par\vspace{2pt}\hrule height 0.4pt\vspace{2pt}}
\newcommand{\resumeSubheading}[4]{\textbf{#1} \hfill #2\\\textit{#3} \hfill \textit{#4}}
\newcommand{\projectHeading}[2]{\textbf{#1} \hfill #2}
\newlist{tightitemize}{itemize}{1}
\setlist[tightitemize]{leftmargin=0.20in,itemsep=0pt,topsep=1pt,parsep=0pt,partopsep=0pt,label={\raisebox{0.15ex}{\small\textbullet}},after=\vspace{1pt}}
\begin{document}
\begin{center}
%s
%s
%s
%s
\end{center}\vspace{-6pt}
\resumesection{Education}
\resumeSubheading{Bowling Green State University}{Bowling Green, OH}{M.S. in Computer Science, GPA: 4.00/4.00}{Aug. 2024 -- Aug. 2026}
\resumeSubheading{Bowling Green State University}{Bowling Green, OH}{B.S. in Computer Science, GPA: 4.00/4.00}{Jan. 2021 -- Apr. 2024}
%s\resumesection{Experience}
%s%s
\resumesection{Technical Skills}
%s
\end{document}
''' % (line1, line2, line3, line4, summary, entries(draft.experience), project_section, skills)


def cover_letter_markdown(letter):
    return '\n\n'.join(markdown_text(paragraph.text) for paragraph in letter.paragraphs) + '\n'


def cover_letter_tex(letter, company, title, root: Path | None = None):
    if root is None:
        root = Path.cwd()
    paragraphs = '\n\n'.join(tex(paragraph.text) for paragraph in letter.paragraphs)
    line1, line2 = _contact_lines(root, for_resume=False)

    return r'''\documentclass[letterpaper,11pt]{article}
\usepackage[letterpaper,left=0.80in,right=0.80in,top=0.70in,bottom=0.70in]{geometry}
\usepackage[hidelinks]{hyperref}
\usepackage[english]{babel}
\input{glyphtounicode}
\pdfgentounicode=1
\pagestyle{empty}
\setlength{\parindent}{0pt}
\setlength{\parskip}{9pt}
\begin{document}
\begin{center}%s\\
%s
\end{center}
\vspace{8pt}
Hiring Team\\
%s\\
Re: %s

%s

Sincerely,\\[8pt]
Aryan Miriyala
\end{document}
''' % (line1, line2, tex(company), tex(title), paragraphs)


def compile_pdf(directory: Path, source_name: str, output_name: str):
    if not shutil.which('pdflatex'):
        raise ValueError('pdflatex is required to compile application PDFs')
    result = subprocess.run(['pdflatex', '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', source_name],
                            cwd=directory, capture_output=True, text=True, timeout=60)
    produced = directory / (Path(source_name).stem + '.pdf')
    if result.returncode or not produced.is_file():
        tail = '\n'.join((result.stdout + '\n' + result.stderr).splitlines()[-12:])
        raise ValueError('PDF compilation failed: ' + tail)
    target = directory / output_name
    if produced != target:
        produced.replace(target)
    for suffix in ('.aux', '.log', '.out'):
        artifact = directory / (Path(source_name).stem + suffix)
        if artifact.exists():
            artifact.unlink()


def pdf_pages(path):
    result = subprocess.run(['pdfinfo', str(path)], capture_output=True, text=True, timeout=15)
    match = re.search(r'^Pages:\s+(\d+)', result.stdout, re.MULTILINE)
    return int(match.group(1)) if result.returncode == 0 and match else None


def pdf_text(path, layout=False):
    command = ['pdftotext'] + (['-layout'] if layout else []) + [str(path), '-']
    result = subprocess.run(command, capture_output=True, text=True, timeout=15)
    if result.returncode:
        raise ValueError('PDF text extraction failed')
    return result.stdout
