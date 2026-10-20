def trim_resume(tex_path):
    with open(tex_path, 'r') as f:
        lines = f.readlines()

    out = []
    skip = False
    for i, line in enumerate(lines):
        if r"{Artificial Intelligence \& Computer Science Intern}" in line:
            skip = True
        
        if skip and r"\resumeSubheading" in line and not r"{Artificial Intelligence \& Computer Science Intern}" in line:
            skip = False
            
        if not skip:
            out.append(line)
            
    content = "".join(out)
    
    # Remove some bullets from AAIS Data Eng
    content = content.replace(
        r"  \item Delivered reverse-ETL and data-validation workflows with custom AWS IAM roles, giving users controlled self-service access to validated insurance data while maintaining 24-hour latency." + "\n",
        ""
    )
    # Remove a bullet from AAIS SWE
    content = content.replace(
        r"  \item Implemented RBAC and JWT patterns in a React/Node.js modernization, replacing broad employee-wide visibility with role-specific controls for about 110 internal users." + "\n",
        ""
    )
    
    with open(tex_path, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    trim_resume("application-packages/Seagate/Embedded-Software-Engineer/resume.tex")
