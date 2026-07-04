# Sparsely Routed Mixture-of-Experts SLMs

This page provides detailed information about Sparsely Routed Mixture-of-Experts SLMs.

## Architecture Diagram

```mermaid
flowchart LR
    A[Input Token] --> B(Fast Router)
    B --> C[Expert 1]
    B --> D[Expert 2]
```

[Back to README](../README.md)
