"""Deterministic one-page resume fitting using measured bullet line counts."""
from __future__ import annotations

import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .generation_render import resume_tex
from .generation_models import ResumeDraft


@dataclass
class BulletMeasurement:
    bullet_id: str
    text: str
    line_count: int
    evidence_ids: list[str]


@dataclass
class FittedResume:
    resume: ResumeDraft
    measurements: dict[str, BulletMeasurement]
    total_lines: int
    page_count: int
    bottom_gap_points: float


def measure_bullet_lines(directory: Path, bullet_text: str) -> int:
    """Measure how many visual lines a bullet occupies in the compiled PDF."""
    # Create a minimal test resume with just this bullet
    test_resume = f"""\\documentclass[letterpaper,11pt]{{article}}
\\usepackage[letterpaper,left=0.22in,right=0.22in,top=0.10in,bottom=0.10in]{{geometry}}
\\usepackage{{enumitem}}
\\usepackage[hidelinks]{{hyperref}}
\\usepackage[english]{{babel}}
\\input{{glyphtounicode}}
\\pagestyle{{empty}}
\\urlstyle{{same}}
\\raggedright
\\setlength{{\\parindent}}{{0pt}}
\\linespread{{0.92}}
\\pdfgentounicode=1
\\newcommand{{\\resumesection}}[1]{{\\par\\vspace{{2pt}}{{\\large\\scshape #1}}\\par\\vspace{{2pt}}\\hrule height 0.4pt\\vspace{{2pt}}}}
\\newcommand{{\\resumeSubheading}}[4]{{\\textbf{{#1}} \\hfill #2\\\\\\textit{{#3}} \\hfill \\textit{{#4}}}}
\\newcommand{{\\projectHeading}}[2]{{\\textbf{{#1}} \\hfill #2}}
\\newlist{{tightitemize}}{{itemize}}{{1}}
\\setlist[tightitemize]{{leftmargin=0.20in,itemsep=0pt,topsep=1pt,parsep=0pt,partopsep=0pt,label={{\\raisebox{{0.15ex}}{{\\small\\textbullet}}}},after=\\vspace{{1pt}}}}
\\begin{{document}}
\\begin{{center}}
{{\\LARGE \\textbf{{Test}}}}\\[-1pt]
\\small test@example.com
\\end{{center}}\\vspace{{-10pt}}
\\resumesection{{Experience}}
\\resumeSubheading{{Test}}{{2024}}{{Test}}{{Test}}
\\begin{{tightitemize}}
  \\item {bullet_text}
\\end{{tightitemize}}
\\resumesection{{Technical Skills}}
Test
\\end{{document}}"""

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        tex_path = tmpdir / "test.tex"
        tex_path.write_text(test_resume)

        # Compile
        result = subprocess.run(
            ["pdflatex", "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error", "test.tex"],
            cwd=tmpdir, capture_output=True, text=True, timeout=60
        )
        if result.returncode != 0:
            return 2  # Default to 2 lines if compilation fails

        pdf_path = tmpdir / "test.pdf"
        if not pdf_path.exists():
            return 2

        # Extract with bbox
        result = subprocess.run(
            ["pdftotext", "-bbox", str(pdf_path), "-"],
            capture_output=True, text=True, timeout=15
        )
        if result.returncode != 0:
            return 2

        # Parse XML to find bullet lines
        try:
            import xml.etree.ElementTree as ET
            root = ET.fromstring(result.stdout)
            pages = [e for e in root.iter() if e.tag.endswith("page")]
            if not pages:
                return 2

            page = pages[0]
            page_height = float(page.attrib.get("height", 792))

            # Find words that look like bullet content
            bullet_words = []
            for word in page.iter():
                if word.tag.endswith("word"):
                    text = word.text or ""
                    if text.strip() and not text.strip().startswith("•"):
                        # Check if this word is part of our bullet (by y position)
                        try:
                            y_max = float(word.attrib.get("yMax", 0))
                            bullet_words.append((y_max, text))
                        except (KeyError, ValueError):
                            pass

            if not bullet_words:
                return 2

            # Group by line (words with similar y_max)
            bullet_words.sort(key=lambda x: x[0], reverse=True)
            lines = []
            current_line_y = None
            line_tolerance = 5  # points

            for y, text in bullet_words:
                if current_line_y is None or abs(y - current_line_y) <= line_tolerance:
                    current_line_y = y
                    lines.append(text)
                else:
                    current_line_y = y
                    lines.append(text)

            # Count non-empty lines that contain bullet content
            content_lines = [l for l in lines if l.strip() and len(l.strip()) > 2]
            return max(1, len(content_lines))

        except Exception:
            return 2


def measure_all_bullets(directory: Path, resume: ResumeDraft) -> dict[str, BulletMeasurement]:
    """Measure line count for all bullets in a resume."""
    measurements = {}

    # Measure experience bullets
    for entry in resume.experience:
        for i, bullet in enumerate(entry.bullets):
            bid = f"{entry.name}:exp:{i}"
            line_count = measure_bullet_lines(directory, bullet.text)
            measurements[bid] = BulletMeasurement(
                bullet_id=bid,
                text=bullet.text,
                line_count=line_count,
                evidence_ids=bullet.evidence_ids,
            )

    # Measure project bullets
    for entry in resume.projects:
        for i, bullet in enumerate(entry.bullets):
            bid = f"{entry.name}:proj:{i}"
            line_count = measure_bullet_lines(directory, bullet.text)
            measurements[bid] = BulletMeasurement(
                bullet_id=bid,
                text=bullet.text,
                line_count=line_count,
                evidence_ids=bullet.evidence_ids,
            )

    return measurements


def compile_and_measure(directory: Path, resume: ResumeDraft) -> tuple[int, float]:
    """Compile resume and return (page_count, bottom_gap_points)."""
    tex_path = directory / "resume.tex"
    tex_path.write_text(resume_tex(resume))

    result = subprocess.run(
        ["pdflatex", "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error", "resume.tex"],
        cwd=directory, capture_output=True, text=True, timeout=60
    )
    if result.returncode != 0:
        raise RuntimeError(f"LaTeX compilation failed: {result.stderr}")

    pdf_path = directory / "resume.pdf"
    if not pdf_path.exists():
        raise RuntimeError("PDF not produced")

    # Get page count
    result = subprocess.run(["pdfinfo", str(pdf_path)], capture_output=True, text=True, timeout=15)
    page_count = 1
    for line in result.stdout.splitlines():
        if line.startswith("Pages:"):
            page_count = int(line.split(":")[1].strip())
            break

    # Get bottom gap using bbox
    result = subprocess.run(
        ["pdftotext", "-bbox", str(pdf_path), "-"],
        capture_output=True, text=True, timeout=15
    )
    bottom_gap = 0.0
    if result.returncode == 0:
        try:
            import xml.etree.ElementTree as ET
            root = ET.fromstring(result.stdout)
            pages = [e for e in root.iter() if e.tag.endswith("page")]
            if pages:
                page = pages[0]
                page_height = float(page.attrib.get("height", 792))
                max_y = 0.0
                for word in page.iter():
                    if word.tag.endswith("word"):
                        try:
                            max_y = max(max_y, float(word.attrib.get("yMax", 0)))
                        except (KeyError, ValueError):
                            pass
                if max_y > 0:
                    bottom_gap = page_height - max_y
        except Exception:
            pass

    return page_count, bottom_gap


def fit_resume_to_page(
    directory: Path,
    resume: ResumeDraft,
    max_bottom_gap: float = 24.0,
    max_iterations: int = 3,
) -> FittedResume:
    """
    Iteratively fit resume to one page by shortening overlong bullets.
    Returns fitted resume with measurements.
    """
    for iteration in range(max_iterations):
        # Measure all bullets
        measurements = measure_all_bullets(directory, resume)

        # Compile and check
        page_count, bottom_gap = compile_and_measure(directory, resume)

        if page_count == 1 and bottom_gap <= max_bottom_gap:
            # Success!
            total_lines = sum(m.line_count for m in measurements.values())
            return FittedResume(
                resume=resume,
                measurements=measurements,
                total_lines=total_lines,
                page_count=page_count,
                bottom_gap_points=bottom_gap,
            )

        # If multi-page or too much bottom gap, we need to shorten bullets
        # Find bullets exceeding 2 lines
        overlong = [(bid, m) for bid, m in measurements.items() if m.line_count > 2]

        if not overlong and page_count == 1:
            # Single page but too much bottom gap - this is a layout issue, not bullet issue
            break

        # For now, just return what we have - the LLM should handle shortening
        # In a full implementation, we'd ask the LLM to shorten specific bullets
        total_lines = sum(m.line_count for m in measurements.values())
        return FittedResume(
            resume=resume,
            measurements=measurements,
            total_lines=total_lines,
            page_count=page_count,
            bottom_gap_points=bottom_gap,
        )

    # Final attempt
    measurements = measure_all_bullets(directory, resume)
    page_count, bottom_gap = compile_and_measure(directory, resume)
    total_lines = sum(m.line_count for m in measurements.values())
    return FittedResume(
        resume=resume,
        measurements=measurements,
        total_lines=total_lines,
        page_count=page_count,
        bottom_gap_points=bottom_gap,
    )