import os
import re
os.chdir(r"C:\Users\ishan\Documents\Projects\Awesome-Small-Language-Models")

details_dir = "details"
os.makedirs(details_dir, exist_ok=True)

files_data = {
    "task-specific-distillation.md": {
        "title": "The Task-Specific Distillation Era",
        "diagram": "```mermaid\nflowchart TD\n    A[Large Model (BERT)] -->|Knowledge Distillation| B(Small Model - DistilBERT)\n    B --> C{Downstream Tasks}\n    C --> D[Classification]\n    C --> E[Entity Recognition]\n```"
    },
    "early-generative-prototyping.md": {
        "title": "The Under-trained Generative Prototyping Era",
        "diagram": "```mermaid\nflowchart LR\n    A[Small Dataset] --> B[GPT-2 Small 117M]\n    B --> C[Text Generation]\n    C -.-> D[Hallucinations]\n```"
    },
    "inference-optimal-overtraining.md": {
        "title": "The Inference-Optimal Over-training Revolution",
        "diagram": "```mermaid\nflowchart TD\n    A[Small Parameter Count] --> C[Dense Model]\n    B[Massive Data 15T Tokens] --> C\n    C --> D[Llama 3 8B / Phi-3]\n```"
    },
    "reinforcement-learned-distilled.md": {
        "title": "The Reinforcement-Learned & Distilled Reasoning Era",
        "diagram": "```mermaid\nflowchart LR\n    A[Ultra-large Reasoning Model] -->|Distill| B[DeepSeek-R1-Distill]\n    B --> C[System 2 Reasoning]\n```"
    },
    "native-over-trained-slms.md": {
        "title": "Native Over-trained SLMs (Inference-Optimized)",
        "diagram": "```mermaid\nflowchart TD\n    A[Web-scale Data Pools] --> B(Small Parameter Envelope)\n    B --> C[Fast Inference Throughput]\n```"
    },
    "distilled-open-weights-slms.md": {
        "title": "Distilled Open-Weights SLMs (Reasoning Distillation)",
        "diagram": "```mermaid\nflowchart TD\n    A[Logical Traces] --> B(SFT / DPO)\n    B --> C[Bake Structural Habits]\n```"
    },
    "sparsely-routed-moe.md": {
        "title": "Sparsely Routed Mixture-of-Experts SLMs",
        "diagram": "```mermaid\nflowchart LR\n    A[Input Token] --> B(Fast Router)\n    B --> C[Expert 1]\n    B --> D[Expert 2]\n```"
    },
    "group-wise-block-quantization.md": {
        "title": "Group-Wise Block Quantization (GGUF / AWQ Templates)",
        "diagram": "```mermaid\nflowchart TD\n    A[BF16 Weights] -->|Block-wise Scaling| B[INT4 / NF4]\n```"
    },
    "unified-memory-caching.md": {
        "title": "Unified Memory Caching Abstrations (PagedAttention for Edge)",
        "diagram": "```mermaid\nflowchart TD\n    A[KV Cache] -->|PagedAttention| B[Non-contiguous Memory Pages]\n```"
    },
    "long-context-retrieval-fade.md": {
        "title": "The Long-Context Needle-in-a-Haystack Retrieval Fade",
        "diagram": "```mermaid\nflowchart LR\n    A[Large Document] -->|Chunk & Search| B[Local Vector DB]\n    B --> C[RaCoT Scaffolding]\n```"
    },
    "hardware-memory-bandwidth.md": {
        "title": "The Hardware Memory-Bandwidth Generation Ceiling",
        "diagram": "```mermaid\nflowchart TD\n    A[Fused Operator Runtimes] -->|Cache Active Layers| B[Local SRAM]\n```"
    },
    "local-on-device-privacy.md": {
        "title": "Local On-Device Consumer Privacy Assistants & Electronics",
        "diagram": "```mermaid\nflowchart LR\n    A[Sensitive Data] --> B[Local SLM]\n    B --> C[No Cloud Upload]\n```"
    },
    "decentralized-robotic-edge.md": {
        "title": "Decentralized Offline Software Maintenance & Robotic Edge Automation",
        "diagram": "```mermaid\nflowchart TD\n    A[Sensory Inputs] --> B[Edge Compute]\n    B --> C[Robotic Control]\n```"
    },
    "enterprise-document-data.md": {
        "title": "Sovereign Enterprise Document Data Extraction & Compliance Filtering",
        "diagram": "```mermaid\nflowchart LR\n    A[Confidential Files] --> B[Private Server Node]\n    B --> C[Compliance Auditing]\n```"
    }
}

for filename, data in files_data.items():
    content = f"# {data['title']}\n\nThis page provides detailed information about {data['title']}.\n\n## Architecture Diagram\n\n{data['diagram']}\n\n[Back to README](../README.md)\n"
    with open(os.path.join(details_dir, filename), "w") as f:
        f.write(content)

with open("README.md", "r") as f:
    readme = f.read()

replacements = {
    "**The Task-Specific Distillation Era (BERT / DistilBERT, ~2018–2019)**": "[**The Task-Specific Distillation Era (BERT / DistilBERT, ~2018–2019)**](./details/task-specific-distillation.md)",
    "**The Under-trained Generative Prototyping Era (GPT-2 / Early Decoders, ~2019–2022)**": "[**The Under-trained Generative Prototyping Era (GPT-2 / Early Decoders, ~2019–2022)**](./details/early-generative-prototyping.md)",
    "**The Inference-Optimal Over-training Revolution (Llama-3 / Phi-3, ~2023–2025)**": "[**The Inference-Optimal Over-training Revolution (Llama-3 / Phi-3, ~2023–2025)**](./details/inference-optimal-overtraining.md)",
    "**The Reinforcement-Learned & Distilled Reasoning Era (Present)**": "[**The Reinforcement-Learned & Distilled Reasoning Era (Present)**](./details/reinforcement-learned-distilled.md)",
    "**A. Native Over-trained SLMs (Inference-Optimized)**": "[**A. Native Over-trained SLMs (Inference-Optimized)**](./details/native-over-trained-slms.md)",
    "**B. Distilled Open-Weights SLMs (Reasoning Distillation)**": "[**B. Distilled Open-Weights SLMs (Reasoning Distillation)**](./details/distilled-open-weights-slms.md)",
    "**C. Sparsely Routed Mixture-of-Experts SLMs (Sparse-Edge MoE)**": "[**C. Sparsely Routed Mixture-of-Experts SLMs (Sparse-Edge MoE)**](./details/sparsely-routed-moe.md)",
    "**Group-Wise Block Quantization (GGUF / AWQ Templates)**": "[**Group-Wise Block Quantization (GGUF / AWQ Templates)**](./details/group-wise-block-quantization.md)",
    "**Unified Memory Caching Abstrations (PagedAttention for Edge)**": "[**Unified Memory Caching Abstrations (PagedAttention for Edge)**](./details/unified-memory-caching.md)",
    "**The Long-Context Needle-in-a-Haystack Retrieval Fade**": "[**The Long-Context Needle-in-a-Haystack Retrieval Fade**](./details/long-context-retrieval-fade.md)",
    "**The Hardware Memory-Bandwidth Generation Ceiling**": "[**The Hardware Memory-Bandwidth Generation Ceiling**](./details/hardware-memory-bandwidth.md)",
    "**Local On-Device Consumer Privacy Assistants & Electronics**": "[**Local On-Device Consumer Privacy Assistants & Electronics**](./details/local-on-device-privacy.md)",
    "**Decentralized Offline Software Maintenance & Robotic Edge Automation**": "[**Decentralized Offline Software Maintenance & Robotic Edge Automation**](./details/decentralized-robotic-edge.md)",
    "**Sovereign Enterprise Document Data Extraction & Compliance Filtering**": "[**Sovereign Enterprise Document Data Extraction & Compliance Filtering**](./details/enterprise-document-data.md)"
}

for old, new in replacements.items():
    readme = readme.replace(old, new)

with open("README.md", "w") as f:
    f.write(readme)
