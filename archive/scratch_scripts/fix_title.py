import re

files_to_fix = [
    "templates/canonical-resume.tex",
    "master-documents/master-resume/resume.tex",
    "application-packages/eBay/Software-Engineer-Recent-Grad-Traffic/resume.tex"
]

for file_path in files_to_fix:
    with open(file_path, "r") as f:
        content = f.read()

    # The title extraction failed and injected `{}` and newlines.
    content = re.sub(r"\{\}\s*Software Engineer \| Distributed Systems \\& Performance", "Software Engineer | Distributed Systems \\& Performance", content, flags=re.DOTALL)
    content = re.sub(r"\{\}\s*Software Engineer", "Software Engineer", content, flags=re.DOTALL)
    
    with open(file_path, "w") as f:
        f.write(content)
