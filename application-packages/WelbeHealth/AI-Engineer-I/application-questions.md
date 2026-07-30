# WelbeHealth AI Engineer I Application Questions

## Python Experience

Question: Please describe your experience with Python. Include examples of applications, scripts, APIs, or automation projects you have built or contributed to.

Answer:

I have used Python mostly for data engineering, backend automation, and AI/RAG work.

At AAIS, I built Python and PySpark workflows to automate a manual SQL billing process over 20+ TB of insurance data for 700+ member companies. I also used Python, Pandas, SQL, and JDBC to profile 160+ MySQL, Oracle, and Impala tables and map them into 25 MDM domains for a cloud migration.

For AI projects, I used Python in FalconGraph Search, a RAG system that cleaned and chunked documents, generated embeddings, retrieved evidence with FAISS, and served source-grounded answers through FastAPI. I also built a Python LLM research pipeline using the OpenAI API and GitHub API to generate pull request descriptions from commits, diffs, linked issues, and repository metadata.

I have also used Python for automation around SQL generation, validation, and secure data movement, including scripts that generated 1,000+ production SQL tables and AWS Lambda workflows that tokenized PII before sending structured JSON to S3.

## Artificial Intelligence And Machine Learning Experience

Question: Please describe your experience with artificial intelligence or machine learning. Include any coursework, bootcamps, internships, personal projects, or professional experience.

Answer:

My AI experience comes from a mix of internships, research, and personal projects.

At SmartSolve, I use Codex and Claude Code as part of my day-to-day engineering workflow for planning, debugging, implementation, and code review. I still treat the final output as my responsibility, so I focus a lot on checking the code, understanding the tradeoffs, and keeping AI-assisted work isolated around company source code.

I have also built several AI applications myself. FalconGraph Search was a RAG project where I processed campus webpages and documents, generated embeddings, used FAISS for retrieval, and returned cited answers through a FastAPI and Next.js interface. Travel Health Advisor used a Mistral chatbot with health-profile context to answer travel-health questions and generate vaccination checklist PDFs. RocketGrader used LangChain and Mistral AI to parse student submissions and return structured feedback, scores, strengths, and improvement areas.

On the research side, I built an LLM pipeline that generated pull request descriptions from commits, diffs, linked issues, and repository metadata, then evaluated the output against the actual code-change evidence. I have also worked on reinforcement learning through a MarioRL project comparing PPO and DQN agents with PyTorch, Stable-Baselines3, Gym, and TensorBoard.

## LLM Project

Question: Please describe a project where you used an LLM to solve a problem. What was your role, what tools did you use, and what was the outcome?

Answer:

One project I would use is FalconGraph Search, a RAG-based campus answer engine I built for BGSU resources.

The problem was that useful campus information was spread across webpages, PDFs, and documents, so a normal search experience could still leave users digging through a lot of disconnected material. My role was to build the pipeline that turned those sources into something an LLM could answer from with evidence.

I used Python for document processing, chunking, and retrieval logic, FAISS for vector search, OpenAI embeddings and LLM calls for source-grounded answers, FastAPI for the backend endpoint, and Next.js for the interface. The system retrieved relevant chunks, generated an answer, and showed citations so the user could trace the response back to the original source instead of just trusting a generated paragraph.

The outcome was a working prototype that made the LLM more useful by grounding it in retrieved documents. It also taught me that the hard part is not only calling the model. A lot of the real work is cleaning the data, choosing useful chunks, checking retrieval quality, and designing the answer flow so a person can verify what the AI is saying.

## WelbeHealth Interest

Question: Why are you interested in the AI Engineer I opportunity at WelbeHealth, and how has your background prepared you to contribute to AI-powered solutions in healthcare?

Answer:

I am interested in WelbeHealth because the AI work is tied to real care and operations, not just building a flashy model demo. The PACE setting stands out to me because AI has to be useful for people making decisions around vulnerable seniors. That means the system needs to be grounded, secure, and explainable enough for teams to trust.

My background prepared me for that kind of work through a mix of AI projects and healthcare-adjacent software experience. I built FalconGraph Search, a RAG system that processed documents, generated embeddings, retrieved evidence with FAISS, and returned cited answers through FastAPI and Next.js. I also built Travel Health Advisor, a health AI prototype that used disease data, health-profile context, and a Mistral chatbot to answer travel-health questions.

I have also worked in environments where reliability and data protection mattered. At the Alliance for Paired Kidney Donation, I helped improve an AWS-hosted healthcare workflow platform with anti-CSRF protection, audit logging, protected routing, and form reliability updates. At AAIS, I worked on Python, AWS, and data-validation workflows, including PII tokenization before sending structured data to S3.

That combination is why the role feels like a strong fit. I can contribute to prototypes, RAG pipelines, prompt and retrieval testing, documentation, and secure workflow thinking while continuing to learn from senior AI engineers.
