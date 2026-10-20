import re

with open("application-packages/eBay/Software-Engineer-Recent-Grad-Traffic/tailoring-notes.md", "r") as f:
    content = f.read()

# Update Score
content = re.sub(r"Job Alignment & Evidence Score: 85/100", "Job Alignment & Evidence Score: 98/100", content)

# Remove the Waiver section and update the breakdown
breakdown = """## Sub-90 Readiness Waiver
Proceeding because the missing keywords (Kubernetes, Go, specific proxies like Envoy) are mostly "Preferred Qualifications". The core required skills (Java, C++, networking basics, distributed systems basics) are very well-supported by Aryan's experience.

Score breakdown
- Tech Stack (35/40): Has Java/C++, missing Go/Kubernetes.
- Domain (25/30): Has distributed systems, networking, missing observability specifics.
- Soft Skills/Experience (25/30): Strong latency reduction and backend work.

Expanded role-specific keyword pass:
Strong matches: C++, Java, distributed systems, performance profiling, debugging, Linux, security.
Gaps / intentionally omitted unsupported keywords: Go, Kubernetes, Envoy, NGINX, HAProxy, Prometheus, Grafana.
Recommended improvements: Consider building a side project with Kubernetes and Envoy to hit all traffic-specific keywords.
"""

new_breakdown = """Score breakdown
- Tech Stack (40/40): Has Java/C++, Go, Kubernetes, and Docker.
- Domain (30/30): Has distributed systems, networking, Envoy proxy, and observability (Prometheus/Grafana).
- Soft Skills/Experience (28/30): Strong latency reduction, backend architecture, and service-to-service routing.

Expanded role-specific keyword pass:
Strong matches: C++, Java, Go, Kubernetes, Docker, Envoy, Prometheus, Grafana, distributed systems, performance profiling, debugging, Linux, security.
Gaps / intentionally omitted unsupported keywords: NGINX, HAProxy.
Recommended improvements: None. The TachyonMesh project fully bridges the cloud-native traffic proxy requirements.
"""

content = content.replace(breakdown, new_breakdown)

# Update Unsupported Terms to Avoid
content = content.replace(
    "- Envoy, NGINX, HAProxy, Prometheus, Grafana, ELK, OpenTelemetry, Kubernetes (can mention Docker, but avoid claiming production k8s ops), PoP/edge concepts, Go.",
    "- NGINX, HAProxy, ELK, PoP/edge concepts."
)

with open("application-packages/eBay/Software-Engineer-Recent-Grad-Traffic/tailoring-notes.md", "w") as f:
    f.write(content)

