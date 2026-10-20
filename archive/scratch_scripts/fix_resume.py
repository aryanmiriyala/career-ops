import re

def fix():
    with open('application-packages/Seagate/Embedded-Software-Engineer/resume.tex', 'r') as f:
        content = f.read()

    # Replace consecutive resumeSubheading
    content = re.sub(r'\\resumeSubheading\s*\\resumeSubheading', r'\\resumeSubheading', content)

    with open('application-packages/Seagate/Embedded-Software-Engineer/resume.tex', 'w') as f:
        f.write(content)

if __name__ == "__main__":
    fix()
