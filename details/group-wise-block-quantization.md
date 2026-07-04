# Group-Wise Block Quantization (GGUF / AWQ Templates)

This page provides detailed information about Group-Wise Block Quantization (GGUF / AWQ Templates).

## Architecture Diagram

```mermaid
flowchart TD
    A[BF16 Weights] -->|Block-wise Scaling| B[INT4 / NF4]
```

[Back to README](../README.md)
