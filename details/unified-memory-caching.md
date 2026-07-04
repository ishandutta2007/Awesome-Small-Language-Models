# Unified Memory Caching Abstrations (PagedAttention for Edge)

This page provides detailed information about Unified Memory Caching Abstrations (PagedAttention for Edge).

## Architecture Diagram

```mermaid
flowchart TD
    A[KV Cache] -->|PagedAttention| B[Non-contiguous Memory Pages]
```

[Back to README](../README.md)
