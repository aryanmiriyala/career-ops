def update_resume(tex_path):
    with open(tex_path, 'r') as f:
        content = f.read()

    # Update Title
    content = content.replace("github.com/aryanmiriyala} $|$ Software Engineer", "github.com/aryanmiriyala} $|$ Embedded Software Engineer")

    # String replacement for Projects and Skills
    projects_start = r"\resumesection{Projects}"
    
    projects_replacement = r"""\resumesection{Projects}
\projectHeading{Self-Adaptive Parallelism Runtime Coordination}{C++, OpenMP, Linux}
\begin{tightitemize}
  \item Built a C++/OpenMP adaptive runtime research system that used per-epoch telemetry and a UCB controller to tune scheduling policy, chunk size, and thread count for varying computational loads.
  \item Benchmarked adaptive scheduling against serial and fixed-policy baselines across Mandelbrot, heat diffusion, and reduction workloads to analyze memory management and concurrency efficiency.
  \item Generated paper-ready performance summaries and plots for runtime, speedup, Karp-Flatt behavior, and scheduler decisions to support robust root-cause analysis of parallel system bottlenecks.
\end{tightitemize}

\projectHeading{FalconGraph Multithreaded Search Engine}{C++, OpenMP, Python, FastAPI, Docker}
\begin{tightitemize}
  \item Built a campus answer engine integrating a multithreaded C++/OpenMP crawler, Python document processing, FAISS retrieval, FastAPI RAG, and a Next.js interface into a config-driven pipeline.
  \item Implemented reliable checkpointed cleaning, graph-node and edge reconstruction, document chunking, embeddings, and semantic ranking to ensure maintainable processing of university resources.
\end{tightitemize}

\resumesection{Technical Skills}
\textbf{Languages:} C/C++, Python, Rust, SQL, JavaScript, TypeScript, Java, C\#\\
\textbf{Systems \& Concepts:} Operating Systems, Concurrency, Memory Management, Data Structures, Algorithms, Computer Architecture, Root-Cause Analysis, Resource-Constrained Design, Modular Architecture\\
\textbf{Tools \& Infrastructure:} Linux, Docker, Make, Git, CI/CD, Jenkins, AWS Lambda, DynamoDB, PySpark, FastAPI, Vitest, Testing Library, PII tokenization

\end{document}
"""

    # Slice the content
    idx = content.find(projects_start)
    if idx != -1:
        content = content[:idx] + projects_replacement

    with open(tex_path, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    update_resume("application-packages/Seagate/Embedded-Software-Engineer/resume.tex")
