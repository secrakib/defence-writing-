# Poly-Dialectal Neural Machine Translation System for Bangla

## Agenda
* Introduction
* Literature Review
* Hypothesis & Objectives
* Methodology
* Dataset Overview
* Results & Evaluation
* Limitations & Future Work
* Conclusion

---

## Introduction
* **Language Context**: Bangla has many regional dialects that differ significantly in:
  * Vocabulary
  * Phonology
  * Structure
* **Problem**: Communication gaps exist between:
  * Regional dialect and Standard Bangla
  * One regional dialect and another
* **Current State**: Most Bangla NLP tools support only Standard Bangla.
* **Proposal**: This research proposes a Poly-Dialectal Neural Machine Translation System for:
  * Dialect → Standard Bangla
  * Standard Bangla → Dialect
  * Dialect → Dialect

### Contribution & Novelty
1. **Largest Dataset**: Constructed the largest machine translation dataset to date for Bengali, specifically designed for multi-dialect translation, encompassing eight distinct dialects.
2. **Multilingual NMT Evaluation**: Conducted a comprehensive evaluation of multilingual neural machine translation (NMT) models to assess their effectiveness in handling intra-language dialectal variation.
3. **Systematic Linguistic Analysis**: Performed a systematic analysis of Bengali dialects through a machine learning perspective, enabling a quantitative characterization of linguistic similarities and divergences across dialects.

---

## Hypothesis & Objectives

### Hypothesis
A machine translation model trained on a multi-dialectal parallel corpus will demonstrate improved generalization across Bangla regional dialects compared to models trained on isolated uni-dialectal data.

### Objectives
* Develop a poly-dialectal translation system for Bangla.
* Enable translation across Standard Bangla and multiple regional dialects.
* Build a multi-dialect parallel corpus.
* Evaluate NMT models' performance in a multi-dialectal setting.
* Promote digital inclusion and linguistic accessibility for Bangla speakers.

---

## Literature Review
* **ANCHOLIK-NER**: Paul et al., *"A Benchmark Dataset for Bangla Regional Named Entity Recognition,"* arXiv, 2025.
* **ANUBHUTI**: Kundu et al., *"A Comprehensive Corpus for Sentiment Analysis in Bangla Regional Languages,"* arXiv, 2026.
* **BanglaDial**: Mahi et al., *"A merged and imbalanced text dataset for Bengali regional dialect analysis,"* Data in Brief, 2025.
* **BdRegionText**: Sultana et al., *"Resource Creation and Evaluation for Bangla Regional Text Classification,"* Indonesian Journal of Electrical Engineering and Computer Science, 2024.
* **BhasaBodh**: Bhuiyan et al., *"Bridging Bangla Dialects and Romanized Forms through Machine Translation"*.
* **BIDWESH**: Fayaz et al., *"A Bangla Regional Based Hate Speech Detection Dataset,"* arXiv, 2025.
* **ChatgaiyyaAlap**: Chowdhury et al., *"A dataset for conversion from Chittagonian dialect to standard Bangla,"* Data in Brief, 2025.
* **BanglaCHQ-Prantik**: Mahjabin et al., *"Human-LLM Benchmarks for Bangla Dialect Translation,"* BLP-2025.
* **DIALTSA-BN**: Jawad et al., *"Benchmarking LLMs on Bangla Dialect Translation and Sentiment Analysis,"* BLP-2025.
* **ONUBAD**: Sultana et al., *"A comprehensive dataset for automated conversion of Bangla regional dialects,"* Data in Brief, 2025.
* **Vashantor**: Faria et al., *"A Large-scale Multilingual Benchmark Dataset for Translation of Bangla Regional Dialects,"* arXiv, 2025.

---

## Methodology

1. **Collect and Integrate Data**:
   * BanglaDial
   * Vashantor
   * ONUBAD
   * Anubhuti
   * Ancholik-NER
   * BhasaBodh
   * Chatgaiyya Alap
2. **Preprocess**:
   * Cleaning
   * Normalization
   * Tokenization
   * Script alignment
3. **Fine-tune Transformer Models**:
   * mT5
   * mBART-50
   * NLLB-200
   * BanglaT5
4. **Train Directions**:
   * Dialect → Standard Bangla
   * Standard Bangla → Dialect
   * Dialect → Dialect
5. **Evaluation Metrics**:
   * BLEU
   * chrF / chrF++
   * METEOR
   * TER

---

## Dataset & Linguistic Examples

### Sample Sentence Across Dialects
* **Standard Bangla**: আপনি দয়া করে আমাকে লবণ এগিয়ে দিতে পারবেন
* **Sylhet**: আফনে দয়া কইরা আমারে নুন আজ্ঞাইয়া দিতা ফারবাইননি
* **Barishal**: আমনে দয়া কইরা মোরে লবণডা আউজ্ঞাইয়া দিতারবেন।
* **Mymensingh**: লবণ ডা একটু আজ্ঞোয়া দিতে পারবাইন
* **Rangpur**: বাহে নুন টা এখনা এইপাকে দিবার পাইবেন
* **Rajshahi**: আমাগে লবণ ডা আগিয়ে দাও তো।

### Initial Dataset Comparison
*Note: ANCHOLIK-NER overlaps with ONUBAD and Vashantor.*

| Dataset | Standard Bengali | Sylhet | Chittagong | Barisal | Noakhali | Rangpur | Rajshahi | Mymensingh |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Ancholik-ner | 3,481 | 3,481 | 3,481 | 3,481 | 3,481 | 0 | 0 | 3,481 |
| Anubhuti | 2,500 | 2,500 | 2,500 | 0 | 0 | 0 | 0 | 2,500 |
| Bangla Dialect Dataset | 3,452 | 442 | 577 | 790 | 0 | 655 | 891 | 712 |
| Bhasabodh | 980 | 980 | 980 | 0 | 0 | 0 | 0 | 0 |
| Chatgaiya Alap | 4,011 | 0 | 4,011 | 0 | 0 | 0 | 0 | 0 |
| Onubad | 980 | 980 | 980 | 980 | 0 | 0 | 0 | 0 |
| Vhasantor | 2,500 | 2,500 | 2,500 | 0 | 2,500 | 0 | 0 | 2,500 |
| **Our Dataset** | **11,056** | **6,422** | **10,567** | **4,270** | **5,000** | **655** | **891** | **5,712** |

### Final Dataset Breakdown

| Dataset | Standard Bengali | Sylhet | Chittagong | Barisal | Noakhali | Rangpur | Rajshahi | Mymensingh | Narail | Kishoreganj | Narsingdi | Tangail |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Ancholik-ner | 3,481 | 3,481 | 3,481 | 3,481 | 3,481 | 0 | 0 | 3,481 | 0 | 0 | 0 | 0 |
| Anubhuti | 2,500 | 2,500 | 2,500 | 0 | 0 | 0 | 0 | 2,500 | 0 | 0 | 0 | 0 |
| Bangla Dialect Dataset | 3,452 | 442 | 577 | 790 | 0 | 655 | 891 | 712 | 0 | 0 | 0 | 0 |
| Bhasabodh | 980 | 980 | 980 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Chatgaiya Alap | 4,011 | 0 | 4,011 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Onubad | 980 | 980 | 980 | 980 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Vhasantor | 2,500 | 2,500 | 2,500 | 0 | 2,500 | 0 | 0 | 2,500 | 0 | 0 | 0 | 0 |
| **Our Dataset** | **13,556** | **6,422** | **10,567** | **4,270** | **5,000** | **1,155** | **891** | **5,712** | **500** | **500** | **500** | **500** |
| **Grand Total** | **31,460** | **17,305** | **25,596** | **9,521** | **10,981** | **1,810** | **1,782** | **14,905** | **500** | **500** | **500** | **500** |

### Dataset Volume Comparison Against Best Competitors

| Dialect | Our Dataset | Best Competitor | How Much Bigger |
| :--- | :--- | :--- | :--- |
| Standard Bengali | 11,056 | 4,011 (Chatgaiya Alap) | 2.76× bigger (175% larger) |
| Sylhet | 6,422 | 3,481 (Ancholik-ner) | 1.84× bigger (84% larger) |
| Chittagong | 10,567 | 4,011 (Chatgaiya Alap) | 2.63× bigger (163% larger) |
| Barisal | 4,270 | 3,481 (Ancholik-ner) | 1.23× bigger (23% larger) |
| Noakhali | 5,000 | 2,500 (Vhasantor) | 2.00× bigger (100% larger) |
| Rangpur | 655 | 655 (Bangla Dialect) | Equal (0% larger) |
| Rajshahi | 891 | 891 (Bangla Dialect) | Equal (0% larger) |
| Mymensingh | 5,712 | 3,481 (Ancholik-ner) | 1.64× bigger (64% larger) |

---

## Limitations & Conclusion

### Limitations
* **Computational Cost**: Training neural machine translation (NMT) models on large-scale corpora is computationally expensive and time-intensive due to the complexity and size of the models.
* **Resource Constraints**: The creation of parallel datasets across multiple regional dialects is highly resource-demanding, often requiring extensive manual effort and, in some cases, may be infeasible.

### Conclusion
* This work proposes a regional poly-dialectal translation framework for Bangla, addressing the challenges of intra-language variation.
* It introduces the largest multi-dialect dataset for Bangla to date, enabling robust research and development in dialect-aware NLP.
* The study aims to advance inclusiveness in Bangla NLP by improving representation and performance across diverse dialectal communities.