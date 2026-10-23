# Application Questions - Quora Full Stack Software Engineer, New Grad

## Question 1
Describe one full-stack application or feature you built (internship or personal project). What does it do, and why did you build it? What was one technical challenge or tradeoff you worked through? How did you use AI while building it and how did it help? Add a link (repo, paper, or demo) if you have one.

## Draft Answer
I built Diff-Grounded PR Description Generation an LLM pipeline that turns commits diffs linked issues and repository metadata into structured pull request descriptions. The system collects commits file diffs linked issues and repository metadata builds structured PR context improves weak commit messages summarizes file-level changes and generates reviewer-ready descriptions under grounding constraints. It was accepted at IEEE ICSME 2025 and evaluated across 1450 pull requests showing stronger grounding and reviewer preference than current AI-generated and human-written baselines.

I built it because PR descriptions are often missing or low quality which slows down code review. Reviewers waste time reconstructing context from raw diffs. An automated pipeline that produces evidence-grounded descriptions directly from repository artifacts reduces that friction.

The main technical challenge was keeping the generated descriptions grounded in actual code changes rather than hallucinating. LLMs tend to invent details when commit messages are weak or diffs are large. I designed a structured context construction phase that extracts file-level summaries from diffs links them to issue tracker data and feeds only verified artifacts into the generation prompt. I added a grounding constraint that forces the model to cite specific diff hunks and issue references for every claim. The evaluation pipeline compared generated descriptions against raw code-change evidence using LLM-as-judge and human review across correctness coverage and clarity metrics.

I used AI throughout the research workflow. I used Claude Code to scaffold the GitHub API ingestion layer and the prompt engineering iterations for the grounding constraint. It helped design the evaluation harness that computes correctness coverage and clarity scores across the 1450 PR test set. I also used it to generate the initial LaTeX structure for the ICSME paper and to iterate on the experimental results tables. The AI assistance accelerated the experimentation cycle so I could focus on the core contribution the grounding constraint and the evaluation methodology.

Paper https://conf.researchr.org/details/icsme-2026/icsme-2026-papers/16/Diff-Grounded-Pull-Request-Description-Generation-with-Structured-Evidence
Repo https://github.com/aryanmiriyala/Diff-Grounded-PR-Generation