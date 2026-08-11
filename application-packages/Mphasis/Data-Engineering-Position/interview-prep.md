# Mphasis Data Engineering Interview Prep

Date researched: 2026-08-11

## Source Reliability Note

These notes are based on public candidate-report and interview-prep sources, not an official Mphasis interview rubric. Treat them as preparation signals. The exact referred role may differ by client, location, and level.

Sources checked:

- Glassdoor Mphasis interview page, updated August 2026: https://www.glassdoor.com/Interview/Mphasis-Interview-Questions-E29275.htm
- Dataford Mphasis Data Engineer guide, updated July 2026: https://dataford.io/interview-guides/mphasis/data-engineer
- InterviewQuery Mphasis Data Engineer guide, published March 2026: https://www.interviewquery.com/interview-guides/mphasis-data-engineer
- AmbitionBox Mphasis Data Engineer fresher interview page, updated April 2025: https://www.ambitionbox.com/interviews/mphasis-interview-questions/data-engineer/fresher-candidates
- LinkedIn candidate/prep posts about Mphasis data engineering interviews, crawled in 2026.

## What To Expect

Likely interview shape:

- Recruiter or referral screen about role fit, availability, location, experience, and compensation.
- One or two technical rounds, often direct and practical.
- Possible client interview because Mphasis is an IT services / consulting company.
- HR round after technical fit.

Likely technical focus:

- SQL query writing, especially joins, aggregations, window functions, ranking, duplicates, and query optimization.
- PySpark syntax, DataFrame operations, transformations vs. actions, joins, deduplication, null handling, repartitioning, and performance basics.
- ETL/ELT concepts, data quality checks, pipeline debugging, batch loads, incremental loads, and late-arriving data.
- Data warehousing and data modeling: fact/dimension tables, star vs. snowflake schema, SCD Type 1 vs. Type 2.
- Cloud and big-data stack: AWS/Azure, S3/ADLS, Glue/ADF, Spark/Databricks, data lakes, partitioning, orchestration, and pipeline monitoring.
- Resume deep dives, especially previous data engineering projects.

## Highest-Priority Questions To Practice

### SQL

- Write a query to find the second-highest salary overall and per department.
- Explain `RANK()` vs. `DENSE_RANK()` vs. `ROW_NUMBER()`.
- Find duplicate records in a table and keep only the latest row per business key.
- Write month-over-month growth using `LAG()`.
- Explain `UNION` vs. `UNION ALL`.
- Explain inner, left, right, full outer, cross, and self joins.
- Explain `GROUP BY` vs. `HAVING`.
- Optimize a slow query joining two large tables.
- Explain when indexes help and when they do not.

AAIS answer anchor:

Use the 160+ table profiling and MDM migration story. Say you used SQL to inspect source-table structures, validate outputs, compare cross-system patterns, and support mapping into cleaner MDM domains.

### PySpark / Spark

- Drop duplicate rows in a PySpark DataFrame based on specific columns.
- Add a conditional column using `when().otherwise()`.
- Convert a string column to a timestamp.
- Group by a column and calculate max/count/sum.
- Read CSV data with schema inference and bad-record handling.
- Explain transformations vs. actions and lazy evaluation.
- Explain `repartition()` vs. `coalesce()`.
- Explain broadcast joins and when to use them.
- Explain how to handle skewed data.
- Explain how to debug a failed Spark job.

AAIS answer anchor:

Use the 20+ TB billing workflow. Say PySpark was appropriate because the billing data was too large for local/Pandas-style processing, and Glue let the job run as a managed Spark-based workflow.

### ETL / Pipeline Design

- Describe an ETL pipeline you built.
- Explain full load vs. incremental load.
- How would you design an incremental load with a watermark?
- How do you handle late-arriving data?
- What data quality checks do you add?
- How do you log failures and bad records?
- How do you validate source-to-target counts?
- How do you decide file partitioning?

AAIS answer anchor:

Use billing automation, Pentaho-to-Glue modernization, reverse ETL, and validation workflows. Keep the story practical: extract from enterprise sources, transform with business logic, store in S3/MDM-ready structures, validate outputs, and control access.

### Data Modeling / Warehousing

- What is a fact table?
- What is a dimension table?
- Star schema vs. snowflake schema.
- SCD Type 1 vs. Type 2.
- What is MDM and why does it matter?
- What is a data lake vs. a data warehouse?
- Why are Parquet/columnar formats useful for big data?

AAIS answer anchor:

Use the 25-domain MDM migration. Explain that MDM is about creating trusted, standardized views of important business entities across systems. Your role was profiling and mapping messy source tables into a maintainable domain taxonomy.

### Cloud / AWS / Security

- What did you use AWS Glue for?
- What is S3's role in data pipelines?
- What is IAM and why is it important?
- What is Lambda useful for in data engineering?
- How do you secure sensitive data in a pipeline?
- How do you explain PII tokenization?

AAIS answer anchor:

Use Glue for ETL orchestration, S3 for durable pipeline outputs, IAM for controlled access, Lambda for event-driven validation, and hashing/tokenization for safer handling of PII before downstream movement.

## Resume Deep-Dive Answers To Prepare

### Billing Automation

Short answer:

At AAIS, I automated a manual SQL billing workflow using Python, PySpark, and AWS Glue. The pipeline processed 20+ TB of golden-table insurance data and calculated charges for 700+ member companies. The main value was making the workflow repeatable, scalable, and less dependent on manual SQL execution.

Follow-up details to know:

- What were the inputs?
- What business rules determined charges?
- How did you validate counts, totals, or output correctness?
- What made PySpark/Glue better than manual SQL?
- How would you improve the pipeline now?

### 160+ Table Profiling / MDM Migration

Short answer:

I profiled 160+ MySQL, Oracle, and Impala tables using Python, Pandas, SQL, and JDBC. The goal was to understand source-system relationships and map similar fields into a 25-domain MDM taxonomy so the migration could be more maintainable.

Follow-up details to know:

- How did you compare source tables?
- What kinds of schema or naming differences appeared?
- How did you decide two fields were similar?
- What did the 25-domain taxonomy represent?
- How did this support Semarchy MDM?

### Pentaho To AWS Glue

Short answer:

AAIS had many legacy Pentaho ETL jobs. I helped replace 160+ of those workflows with AWS Glue ETL jobs and partitioned S3 pipelines for Semarchy MDM. The benefit was more maintainable, cloud-native data movement.

Follow-up details to know:

- What did Pentaho do in the old process?
- How did Glue jobs differ from the legacy jobs?
- Why partition S3 outputs?
- How did Semarchy consume or use the outputs?

### Reverse ETL / Validation / IAM

Short answer:

I worked on reverse-ETL and validation workflows where processed data needed to be made available back to downstream users or systems. IAM roles helped control who or what could access the data, and validation helped reduce manual errors and support 24-hour latency.

Follow-up details to know:

- What data moved back downstream?
- What validation checks ran?
- What did IAM restrict?
- What did 24-hour latency mean operationally?

### Software Internship SQL Generation

Short answer:

In my earlier AAIS software internship, I used Python and JSON-based generation logic to parse insurance taxonomies and generate 1,000+ production SQL tables across MySQL, Oracle, PostgreSQL, and 10+ insurance lines. That helped standardize data-model delivery instead of manually creating each table.

Follow-up details to know:

- What was the input JSON/taxonomy structure?
- How did the script generate table definitions?
- How did you handle database-specific SQL differences?
- How did you validate generated SQL?

## One-Week Prep Order

1. SQL window functions, joins, duplicates, CTEs, ranking, and query optimization.
2. PySpark DataFrame syntax: read, select, filter, withColumn, groupBy, joins, dropDuplicates, null handling.
3. ETL storytelling from AAIS: billing automation, MDM profiling, Pentaho-to-Glue, reverse ETL.
4. Data modeling: fact/dimension, star/snowflake, SCD, MDM, data lake vs. warehouse.
5. Cloud/AWS: Glue, S3, IAM, Lambda, partitioning, validation, security.
6. Mock interview: answer each AAIS resume bullet out loud in 60-90 seconds.

## Questions To Ask Mphasis

- Is this role tied to a specific client or internal Mphasis data platform team?
- What is the main stack: AWS Glue/Spark, Azure Data Factory/Databricks, Snowflake, dbt, Airflow, or something else?
- Is the work mostly migration, batch ETL, streaming, data warehousing, or analytics enablement?
- How much of the role is SQL/PySpark development versus orchestration/support?
- What does a successful first 90 days look like for this data engineering role?
