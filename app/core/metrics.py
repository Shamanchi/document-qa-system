"""Prometheus metrics."""
from prometheus_client import Counter, Histogram, Gauge, Info

app_info = Info("document_qa_system", "Document QA System info")
app_info.info({"version": "0.1.0"})

http_requests_total = Counter("http_requests_total", "Total HTTP requests", ["method", "endpoint", "status"])
http_request_duration_seconds = Histogram("http_request_duration_seconds", "HTTP latency", ["method", "endpoint"])

documents_uploaded_total = Counter("documents_uploaded_total", "Documents uploaded")
documents_processed_total = Counter("documents_processed_total", "Documents processed", ["status"])
chunks_created_total = Counter("chunks_created_total", "Chunks created")
embeddings_created_total = Counter("embeddings_created_total", "Embeddings created")

qa_queries_total = Counter("qa_queries_total", "QA queries", ["status"])
qa_latency_seconds = Histogram("qa_latency_seconds", "QA latency", buckets=[0.5, 1, 2, 5, 10, 30, 60])

search_queries_total = Counter("search_queries_total", "Search queries")
search_latency_seconds = Histogram("search_latency_seconds", "Search latency", buckets=[0.1, 0.5, 1, 2, 5, 10])

active_documents = Gauge("active_documents", "Active documents in system")