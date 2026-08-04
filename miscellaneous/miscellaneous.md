# Project Requirements and Paper Structure

## 1. Additional Dataset Collection

In addition to the collected datasets, we manually created **500 high-quality Standard Bangla ↔ Dialect parallel sentence pairs** for each of the following dialects:

* Rangpur
* Tangail
* Kishoreganj
* Narail
* Narsingdi

These datasets are **bidirectional**, containing both:

* Standard Bangla → Dialect
* Dialect → Standard Bangla

To ensure data quality, each dialect dataset was independently evaluated and verified by **three native speakers** of the corresponding dialect.

---

## 2. Training Strategy

The experimental pipeline consists of two stages:

### Stage 1: Best Model Selection

* Train all candidate models for **20 epochs** using the complete dataset.
* Use identical LoRA hyperparameters for all models to ensure a fair comparison.
* Select the best-performing model based on evaluation metrics.

### Stage 2: Final Training

* Retrain the selected best model for **100 epochs**.
* Analyze the learning behavior and final performance in detail.

The analysis should include:

* Translation quality improvements after extended training.
* Error analysis.
* Linguistic analysis explaining **why certain dialects are more or less similar to Standard Bangla**.
* Pairwise ("all-to-all") comparison among dialects to identify which dialects are linguistically closer or farther from one another and provide possible linguistic explanations.

---

## 3. Optimal Dataset Size Study

Conduct an experiment to determine the optimal dataset size.

Requirements:

* Use a **fully parallel dataset** consisting of:

  * Standard Bangla
  * Sylheti
  * Noakhali
  * Chittagong
  * Mymensingh
* Train using progressively larger subsets beginning from **5,000 parallel instances**.
* Use **two different LoRA configurations** for this experiment.
* Analyze:

  * Performance vs. dataset size
  * Saturation point
  * Trade-offs between data quantity and translation quality

---

## 4. Results Organization

The Results chapter should contain two major parts.

### Part I — Best Model Search

Present the comparison of all candidate models trained for 20 epochs.

Include:

* Overall comparison
* Tables
* Figures
* Discussion
* Selection rationale

### Part II — Final Best Model Results

Present the detailed results of the selected model trained for 100 epochs.

Include:

* Overall metrics
* Per-dialect performance
* Qualitative examples
* Error analysis
* Discussion

---

## 5. Evaluation Metrics

Create a dedicated subsection explaining all evaluation metrics used in the paper.

For each metric include:

* Definition
* Mathematical formula
* Interpretation
* Advantages
* Limitations
* Trade-offs
* Why the metric is appropriate for this task

The explanation should be sufficiently detailed for readers unfamiliar with machine translation evaluation.

---

## 6. Hyperparameters

Include a dedicated **Hyperparameters** section.

The information should be obtained from:

* `hyperparams.md`

Present the hyperparameters clearly in tables along with brief explanations where appropriate.

---

## 7. Comparative Performance

Include a section comparing the proposed approach with previous work.

The comparison should discuss:

* Previous state-of-the-art results
* Datasets used
* Models used
* Evaluation metrics
* Strengths and weaknesses
* Improvements achieved by our approach
* Possible reasons for performance differences

---

## 8. Deployment

Include a dedicated deployment section describing the developed web application.

All deployment-related information should be obtained from:

* `deployment.md`

The section should describe:

* System architecture
* Model serving
* Backend
* Frontend
* User workflow
* Deployment pipeline
* Screenshots (if available)

---

## 9. Models Section

Expand the **Models** subsection significantly.

It should provide:

* Better organization and formatting.
* Detailed descriptions of every model used.
* Architecture overview.
* Model capabilities.
* Advantages and limitations.
* Reasons for selecting each model.
* Suitability for Bangla dialect translation.
* Comparison between the candidate models.

This section should be substantially more comprehensive than the current version and should serve as a strong background for the experimental study.
