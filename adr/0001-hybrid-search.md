# ADR 0001: Hybrid Search Strategy for Multi-Tenant RAG

## Status
Accepted

## Context
Our enterprise clients require high-precision retrieval across diverse document types (Technical Manuals, Legal Contracts, and Informal Chats). Traditional vector-only search (Dense) struggles with specific keyword matching (e.g., part numbers), while BM25 (Sparse) lacks semantic understanding.

## Decision
We will implement a **Hybrid Search Architecture** using:
1. **Dense Retrieval**: OpenAI `text-embedding-3-small` stored in a filtered Pinecone index.
2. **Sparse Retrieval**: BM25 algorithm implemented via Elasticsearch.
3. **Fusion**: Reciprocal Rank Fusion (RRF) with a standard constant ($k=60$).

## Consequences
- **Pros**: Significant improvement in MRR for technical queries; better "zero-shot" performance.
- **Cons**: Increased indexing latency; higher infrastructure cost for maintaining two search indices.
- **Mitigation**: Asynchronous indexing pipeline using Celery/Redis to decouple ingestion from API response.
