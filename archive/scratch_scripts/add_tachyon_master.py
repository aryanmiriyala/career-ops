import re

with open("master-documents/master-resume/resume.tex", "r") as f:
    content = f.read()

tachyon_project = r"""\projectHeading{TachyonMesh - Cloud-Native Traffic Proxy}{Go, Kubernetes, Envoy, Prometheus, Grafana}
\begin{tightitemize}
  \item Built a cloud-native traffic routing system by deploying a containerized Golang backend on Kubernetes and configuring an Envoy proxy to manage load balancing and service networking.
  \item Instrumented the cluster with Prometheus and Grafana, scraping proxy metrics to profile request latency, debug bottlenecks, and optimize throughput under heavy concurrent load.
\end{tightitemize}

"""

# Insert it before the Diff-Grounded project
content = content.replace(
    r"\projectHeading{Diff-Grounded PR Description Generation}",
    tachyon_project + r"\projectHeading{Diff-Grounded PR Description Generation}"
)

# Also add Go, Envoy, Prometheus, Kubernetes, Grafana to the master Technical Skills
content = content.replace(
    "\\textbf{Languages \\& Frameworks:} Python, TypeScript/JavaScript, SQL, Java, C++, C, C\\#, React, Next.js, Angular, Node.js, Express, REST APIs, Firebase\\\\",
    "\\textbf{Languages \\& Frameworks:} Go, Python, TypeScript/JavaScript, SQL, Java, C++, C, C\\#, React, Next.js, Angular, Node.js, Express, REST APIs, Firebase\\\\"
)

content = content.replace(
    "\\textbf{Security, Testing \\& Tools:} Vercel, Vitest, Testing Library, Docker, Git, Linux, SSO, JWT, RBAC, Auth0, anti-CSRF, audit logging, PII tokenization, Codex, Claude Code",
    "\\textbf{Security, Testing \\& Tools:} Kubernetes, Docker, Envoy Proxy, Prometheus, Grafana, Vercel, Vitest, Testing Library, Git, Linux, SSO, JWT, RBAC, Auth0, anti-CSRF, audit logging, PII tokenization"
)

with open("master-documents/master-resume/resume.tex", "w") as f:
    f.write(content)
