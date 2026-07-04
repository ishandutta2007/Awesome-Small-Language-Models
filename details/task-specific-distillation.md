# The Task-Specific Distillation Era

This page provides detailed information about The Task-Specific Distillation Era.

## Architecture Diagram

```mermaid
flowchart TD
    A[Large Model (BERT)] -->|Knowledge Distillation| B(Small Model - DistilBERT)
    B --> C{Downstream Tasks}
    C --> D[Classification]
    C --> E[Entity Recognition]
```

[Back to README](../README.md)
