# Automation

Validation and local helper scripts for the application pipeline.

- `validate_application_package.py`: checks that a selected application package has the expected files, one-page resume PDF, internal alignment notes, explicit pass/waiver verification gates, placeholder-free resume and cover-letter sources, cover-letter artifact, ATS-safe canonical resume source structure, extractable PDF text, bottom-page utilization when `pdftotext -bbox` is available, conservative artifact size, and clean generated LaTeX state.
- `analyze_application_keywords.py`: reports exact job-description term coverage in the selected resume artifact. Use it during the alignment pass as deterministic support, not as an employer ATS score.
- `upsert_application_tracker.py`: appends or updates one tracker row without printing or loading the full tracker into model context.

This folder should stay focused on repo/application validation only.
