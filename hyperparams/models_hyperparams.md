# Comprehensive Hyperparameter Specifications for Poly-Dialectal NMT Fine-Tuning

### 1. Unified Architectural & Fine-Tuning Configurations (Models All Together)

| Hyperparameter Category | Hyperparameter / Property | BanglaT5 | mBART-50 Large | NLLB-200 Distilled |
| :--- | :--- | :--- | :--- | :--- |
| **Model Registry** | **HuggingFace Checkpoint** | `csebuetnlp/banglat5` | `facebook/mbart-large-50-many-to-many-mmt` | `facebook/nllb-200-distilled-600M` |
| | **Base Parameter Count** | ~60M | ~611M | ~600M |
| | **Source/Target Language Tags** | Prefixed (`translate src to tgt:`) | `bn_IN` | `ben_Beng` |
| **Sequence Setup** | **Max Source Length ($L_{\text{src}}$)** | 128 | 128 | 128 |
| | **Max Target Length ($L_{\text{tgt}}$)** | 128 | 128 | 128 |
| | **Sequence Packing** | Homogeneous chunking per dialect pair with EOS separation | Disabled | Disabled |
| **Optimization** | **Optimizer** | Paged AdamW 8-bit | Paged AdamW 8-bit | Paged AdamW 8-bit |
| | **Base Learning Rate ($\eta$)** | $5 \times 10^{-4}$ | $5 \times 10^{-4}$ | $5 \times 10^{-4}$ |
| | **Learning Rate Scheduler** | Cosine Annealing | Cosine Annealing | Cosine Annealing |
| | **Warmup Ratio** | 0.06 | 0.06 | 0.06 |
| | **Weight Decay** | 0.01 | 0.01 | 0.01 |
| | **Label Smoothing ($\epsilon$)** | 0.1 | 0.1 | 0.1 |
| **Batching & Hardware**| **Per-Device Batch Size** | 32 | 8 | 8 |
| | **Gradient Accumulation Steps** | 2 | 8 | 8 |
| | **Effective Batch Size** | 64 | 64 | 64 |
| | **Mixed Precision Format** | FP16 | FP16 | FP16 |
| **PEFT / DoRA Setup** | **Adapter Scheme** | PEFT / Weight-Decomposed Low-Rank Adaptation (DoRA) | PEFT / DoRA | PEFT / DoRA |
| | **Adapter Rank ($r$)** | 64 | 64 | 64 |
| | **Scaling Factor ($\alpha$)** | 128 | 128 | 128 |
| | **Dropout Rate** | 0.05 | 0.05 | 0.05 |
| | **Target Projections** | `q, v, k, o, wi, wo` | `q_proj, k_proj, v_proj, out_proj, fc1, fc2` | `q_proj, k_proj, v_proj, out_proj, fc1, fc2` |
| **Training Schedule** | **Max Epochs** | 90 | 10 | 10 |
| | **Early Stopping Patience** | 3 (monitored on chrF++) | Disabled (`eval_strategy="no"`) | Disabled (`eval_strategy="no"`) |
| | **Data Sampling Temperature** | $T = 2.0$ (Weighted Random Sampler) | $T = 2.0$ (Weighted Random Sampler) | $T = 2.0$ (Weighted Random Sampler) |
| **Inference Generation**| **Beam Search Size** | 4 | 4 | 4 |
| | **Evaluation Metrics** | BLEU, chrF++, METEOR, TER | BLEU, chrF++, METEOR, TER | BLEU, chrF++, METEOR, TER |