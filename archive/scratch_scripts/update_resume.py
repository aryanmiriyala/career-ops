import re

with open("application-packages/eBay/Software-Engineer-Recent-Grad-Traffic/resume.tex", "r") as f:
    content = f.read()

tachyon_project = r"""\projectHeading{TachyonMesh - Cloud-Native Traffic Proxy}{Go, Kubernetes, Envoy, Prometheus, Grafana}
\begin{tightitemize}
  \item Built a cloud-native traffic routing system by deploying a containerized Golang backend on Kubernetes and configuring an Envoy proxy to manage load balancing.
  \item Instrumented the cluster with Prometheus and Grafana, scraping proxy metrics to profile request latency, debug bottlenecks, and optimize throughput under load.
\end{tightitemize}"""

content = re.sub(r"\\projectHeading\{HealthTrend - Distributed Streaming Pipeline\}.*?\\end\{tightitemize\}", lambda m: tachyon_project, content, flags=re.DOTALL)

content = content.replace(
    "\\textbf{Languages \\& Frameworks:} Java, C++, Python, JavaScript, TypeScript, SQL, Node.js, Express, REST APIs\\\\",
    "\\textbf{Languages \\& Frameworks:} Go (Golang), Java, C++, Python, TypeScript, SQL, Node.js, REST APIs\\\\"
)
content = content.replace(
    "\\textbf{Infrastructure \\& Cloud:} Linux, Docker containers, Apache Kafka, Spark, PySpark, AWS S3, AWS Lambda, IAM, DynamoDB\\\\",
    "\\textbf{Infrastructure \\& Cloud:} Kubernetes, Docker, Envoy Proxy, Prometheus, Grafana, Apache Kafka, Linux, AWS\\\\"
)

with open("application-packages/eBay/Software-Engineer-Recent-Grad-Traffic/resume.tex", "w") as f:
    f.write(content)

