# Mphasis Data Engineering Referral Prep

Date created: 2026-08-11

## Intake Status

Status: Referral prep only - not a full application package yet.

Application package folder: `application-packages/Mphasis/Data-Engineering-Position/`

User-provided context:

- Aryan spoke with an executive at Mphasis.
- The executive referred Aryan for a data engineering position.
- Aryan wants the new one-page resume and expanded CV source material used appropriately for data engineering roles.

## Resume / CV Use Decision

Use by default: `master-documents/ready-to-send/Aryan_Miriyala_Resume.pdf`.

Use only if requested: `master-documents/ready-to-send/Aryan_Miriyala_Curriculum_Vitae.pdf`.

Reason: The one-page resume is the right default for a corporate data engineering referral or ATS application. The CV is useful if the executive, recruiter, or hiring team wants a fuller inventory of internships, projects, research, and skills.

The root-level PDFs `Aryan_Miriyala_Resume.pdf` and `Aryan_Miriyala_Curriculum_Vitae.pdf` are ignored by git. The tracked ready-to-send copies already live under `master-documents/ready-to-send/`.

## Required Before Final Package

- Exact job title.
- Posting URL or pasted job description.
- Location and remote/hybrid/on-site expectation.
- Employment type, especially full-time, internship, contract, or client-site consulting.
- Required years of experience.
- Required stack, especially Snowflake, Spark, Databricks, Airflow, dbt, Kafka, AWS, Azure, GCP, SQL, Python, and ETL/ELT tooling.
- Work authorization, E-Verify, OPT/STEM OPT, and future sponsorship stance.
- Whether the executive already submitted the referral or expects Aryan to apply first and then share an application ID.

## Preliminary Fit Summary

Strongest verified fit areas:

- Production data engineering internship at AAIS using Python, SQL, PySpark, AWS Glue, Glue Workflows, S3, IAM, MySQL, Oracle, Impala, PostgreSQL, JDBC, Semarchy MDM, billing workflows, reverse ETL, data validation, and large insurance datasets.
- Production-scale evidence: 20+ TB of golden-table insurance data, 700+ member companies, 160+ source tables, and 25 MDM domains.
- Data-adjacent software engineering at AAIS, including Python/JSON automation that generated 1,000+ production SQL tables and AWS Lambda/S3 validation with PII tokenization.
- HealthTrend project evidence for Spark, PySpark, Kafka, Hadoop HDFS, Apache NiFi, Docker Compose, structured CSV ingestion, semi-structured JSON events, and downstream analytics.
- SmartSolve and Actual Reality evidence for internal/customer workflow software, authentication, PostgreSQL, Next.js/TypeScript, and AI-assisted development.

Preliminary risk areas to verify:

- If the referred role is senior, contract-only, or client-site with 8-10+ years required, position it carefully and confirm whether the referral is for an early-career/new-grad fit.
- If the role requires Snowflake, Databricks, Airflow, dbt, or cloud tooling beyond AWS, treat those as gaps unless Aryan can verify additional source material.
- Do not mention F-1, OPT, STEM OPT, future sponsorship, E-Verify, or Form I-983 in submitted artifacts unless Aryan explicitly asks. Keep those details internal.

## Preliminary Resume Direction

Primary angle: Early-career data engineer with production Python, SQL, PySpark, AWS Glue, S3, IAM, MDM, data profiling, ETL, validation, and large-scale insurance data experience.

Target Professional Title Clause: Do not add until the exact posted title is known. If the role title is simply `Data Engineer`, use `Data Engineer-aligned software engineer...` in the summary. If it is `Senior Data & Platform Engineer`, do not claim senior alignment without clear recruiter guidance.

Strongest evidence to lead:

- AAIS Data Engineering Intern: production PySpark and AWS Glue billing automation over 20+ TB of golden-table insurance data for 700+ member companies.
- AAIS Data Engineering Intern: profiling 160+ MySQL, Oracle, and Impala tables with Python, Pandas, SQL, and JDBC to support 25-domain MDM migration.
- AAIS Data Engineering Intern: replacing 160+ Pentaho jobs with AWS Glue ETL workflows and partitioned S3 pipelines for Semarchy MDM.
- AAIS Software Engineering Intern: Python/JSON generation of 1,000+ production SQL tables and AWS Lambda/S3 data validation with PII tokenization.
- HealthTrend: Spark/PySpark, Kafka, Hadoop HDFS, NiFi, Docker Compose, batch plus streaming ingestion.

## Preliminary Keyword Map

Supported - add/use now:

- Python
- SQL
- PySpark
- Spark
- AWS Glue
- AWS Glue Workflows
- AWS S3
- AWS IAM
- AWS Lambda
- ETL
- ELT, only if framed broadly as ETL/ELT and not tied to a specific unsupported tool
- Data validation
- Data profiling
- Data modeling
- Data migration
- MDM
- Semarchy MDM / xDM
- JDBC
- MySQL
- Oracle
- PostgreSQL
- Impala
- Kafka
- Hadoop HDFS
- Apache NiFi
- Docker
- Large-scale data processing
- Insurance data platforms
- Cross-source data mapping

Unsupported - omit unless Aryan verifies source material:

- Snowflake production engineering
- Snowflake Cortex
- Databricks production work
- Airflow
- dbt
- Scala
- Azure Data Factory
- GCP Dataflow / BigQuery production work
- Formal data warehouse administration
- Senior platform ownership
- 8-10+ years of experience
- Production AI agent development on enterprise data platforms

Likely built but undocumented - ask/update source:

- Parquet, schema evolution, CloudWatch, CI/CD, and production monitoring may have appeared adjacent to AWS/data work, but they should not be claimed until Aryan confirms specifics.
- Any Mphasis/client-specific domain context should wait for the exact role or recruiter details.

## F-1 Work Authorization Gate

Preliminary status: Proceed with caution - company has public U.S. hiring and historical visa/LCA signals, but exact role eligibility is unknown.

Internal checks still needed:

- Confirm whether the role is full-time W-2, contract, internship, client-site, or staffing/consulting placement.
- Confirm E-Verify and STEM OPT Form I-983 support for the U.S. entity and the specific role.
- Confirm future sponsorship path and whether the team/client imposes separate authorization restrictions.
- Confirm whether any application form asks for permanent unrestricted work authorization, current/future sponsorship, or authorization to work for any employer.

## Interview / Referral Prep

Short pitch:

I am finishing my M.S. in Computer Science at BGSU and have production data engineering experience from AAIS, where I built Python, SQL, PySpark, and AWS Glue workflows over large insurance datasets. My strongest project automated a manual billing process across 20+ TB of golden-table data for 700+ member companies, and I also worked on profiling 160+ source tables for an MDM migration. I am looking for a data engineering role where I can keep building reliable pipelines, validation workflows, and cloud data systems.

Stories to prepare:

- AAIS billing automation: manual SQL workflow, PySpark/AWS Glue design, 20+ TB scale, 700+ member companies, validation, and how correctness was checked.
- AAIS MDM migration: 160+ tables, MySQL/Oracle/Impala sources, JDBC profiling, 25-domain taxonomy, and how source-system differences were mapped.
- Legacy replacement: Pentaho-to-AWS Glue/S3 modernization, partitioning decisions, maintainability, and handoff.
- Secure data movement: IAM-controlled access, reverse ETL, validation workflows, and PII tokenization with Lambda/S3.
- HealthTrend: Kafka/HDFS/Spark/NiFi architecture and what would need to change for a production version.

Questions to ask recruiter or hiring team:

- Is this role attached to a specific client, internal Mphasis team, or platform group?
- What are the main data sources and target platforms?
- Is the core stack AWS Glue/Spark, Snowflake, Databricks, Airflow, dbt, or another orchestration platform?
- Is this full-time employment, contract, or contract-to-hire?
- What level is the role calibrated for?
- Does the U.S. entity support STEM OPT training plans and future sponsorship for this role?

## External Research Notes

- Mphasis careers site: https://careers.mphasis.com/home/hot-jobs.html
- Public search result observed on 2026-08-11 for a Mphasis Data Engineer / Senior Data & Platform Engineer posting in Dallas, TX, but this may not be the referred role and should not be treated as the source of truth without confirmation.
- Public visa/LCA databases show Mphasis has recent U.S. LCA/H-1B filing history, but historical filings do not guarantee the referred role supports OPT, STEM OPT, H-1B, or future sponsorship.
