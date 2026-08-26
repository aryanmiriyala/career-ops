# Master Documents

Canonical reusable documents.

- `master-resume/resume.tex`: canonical one-page ATS/application master resume source.
- `master-resume/resume.pdf`: compiled one-page master resume PDF when intentionally generated.
- `master-resume/resume-expanded.tex`: expanded four-page master resume source preserved for reference and deeper tailoring.
- `master-resume/resume-expanded.pdf`: compiled expanded master resume PDF.
- `master-cover-letter/cover-letter-template.md`: reusable cover-letter structure and language.

When regenerating `master-resume/resume.pdf` or `ready-to-send/Aryan_Miriyala_Resume.pdf`, run `python3 automation/validate_resume_pdf.py master-documents/master-resume/resume.pdf` before committing. This standalone check enforces the same bottom-page utilization expectation as application-package resumes.

Tailored job-specific files belong in `application-packages/<Company>/<Role>/`, not here.
