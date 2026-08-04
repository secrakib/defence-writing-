# Experimental Setup & Hyperparameter Specifications: Dataset Scaling vs. Performance

### 1. Dataset Scaling Experimental Protocol

The dataset size scaling study evaluates model translation generalization under varying volumes of parallel sentence pairs. Data leakage is prevented by splitting raw multi-dialect parallel sentence rows before permutation into directional translation pairs.

* **Baseline Target Architecture**: `csebuetnlp/banglat5_small`
* **Dataset Splitting Protocol**: 
  * **Raw Training Row Allocation**: 90% (Max 4,499 raw parallel sentence rows)
  * **Fixed Test Set Allocation**: 10% (500 raw parallel sentence rows $\rightarrow$ 10,000 directional evaluation pairs across 20 dialect combinations)
* **Iterative Raw Dataset Size Steps ($N_{\text{raw}}$)**: $\{500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4499\}$ parallel rows

---

### 2. Hyperparameter Matrix for Scaling Experiments

| Parameter Class | Hyperparameter / Component | Value / Configuration |
| :--- | :--- | :--- |
| **Model Configuration** | Base Model Name | `csebuetnlp/banglat5` |
| | Model Type | Sequence-to-Sequence Transformer |
| | Tokenizer Scheme | AutoTokenizer (BanglaT5 Byte-Pair Encoding) |
| **Sequence Dimensions**| Max Source Sequence Length ($L_{\text{src}}$) | 128 tokens |
| | Max Target Sequence Length ($L_{\text{tgt}}$) | 128 tokens |
| | Sequence Packing | Enabled (Per dialect pair, max chunk = 128, EOS separator) |
| **PEFT / DoRA Settings**| PEFT Parameterization | DoRA Enabled (`use_dora=True`) |
| | Adapter Rank ($r$) | 8 |
| | Adapter Scaling Alpha ($\alpha$) | 16 |
| | Dropout Probability | 0.05 |
| | Target Modules | Query (`q`), Value (`v`), Key (`k`), Output (`o`), Dense Feed-Forward (`wi`, `wo`) |
| **Optimization Strategy**| Optimization Algorithm | Paged AdamW 8-bit (`paged_adamw_8bit`) |
| | Learning Rate ($\eta$) | $5 \times 10^{-4}$ |
| | LR Decay Schedule | Cosine Decay Schedule |
| | Warmup Ratio | 0.06 |
| | Weight Decay Factor | 0.01 |
| | Regularization / Smoothing | Label Smoothing ($\epsilon = 0.1$) |
| **Batching & Execution**| Per-Device Batch Size | 45 |
| | Gradient Accumulation Steps | 2 |
| | Effective Batch Size | 90 |
| | Mixed Precision Setup | FP16 (`fp16=True`, `bf16=False`) |
| | Temperature-Scaled Sampling | Weighted Random Sampler ($T = 2.0$) |
| **Training Schedule** | Epochs per Scaling Step | 10 Epochs (Trained independently from scratch per size $N_{\text{raw}}$) |
| | Save Strategy | Save checkpoint per epoch (`save_strategy="epoch"`) |
| | Validation Strategy | Disabled during scaling training (`eval_strategy="no"`) |
| **Inference & Metrics** | Generation Search Method | Beam Search ($N_{\text{beams}} = 4$) |
| | Primary Metric Metrics | BLEU, chrF++, METEOR, TER |
| | Reporting Grain | Per-dialect direction pair breakdown + OVERALL aggregated score |