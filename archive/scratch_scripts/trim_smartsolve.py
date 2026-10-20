def trim_resume(tex_path):
    with open(tex_path, 'r') as f:
        lines = f.readlines()

    out = []
    skip = False
    for i, line in enumerate(lines):
        if r"{Artificial Intelligence \& Computer Science Intern}" in line:
            skip = True
            # Also remove the previous \resumeSubheading which is at line i-1
            if out and r"\resumeSubheading" in out[-1]:
                out.pop()
        
        if skip and r"\resumeSubheading" in line and not r"{Artificial Intelligence \& Computer Science Intern}" in line:
            skip = False
            
        if not skip:
            out.append(line)
            
    content = "".join(out)
    
    with open(tex_path, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    trim_resume("application-packages/Seagate/Embedded-Software-Engineer/resume.tex")
