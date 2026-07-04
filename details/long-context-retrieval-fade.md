# The Long-Context Needle-in-a-Haystack Retrieval Fade

This page provides detailed information about The Long-Context Needle-in-a-Haystack Retrieval Fade.

## Architecture Diagram

```mermaid
flowchart LR
    A[Large Document] -->|Chunk & Search| B[Local Vector DB]
    B --> C[RaCoT Scaffolding]
```

[Back to README](../README.md)
