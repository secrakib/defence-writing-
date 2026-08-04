# Thesis Results: Bangla Dialect Translation Evaluation

## 1. Baseline Model Comparisons

### BanglaT5 (20 Epochs)
* **Execution Time / Log Marker**: 7990.2s

#### Per-dialect-pair results:
| Language Pair | Samples | BLEU | chrF | METEOR | TER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| bangla_speech→barishal_bangla_speech | 445 | 24.66 | 54.36 | 48.08 | 47.41 |
| bangla_speech→chittagong_bangla_speech | 1074 | 16.13 | 45.32 | 34.70 | 63.37 |
| bangla_speech→kishorgonj_bangla_speech | 43 | 10.05 | 37.52 | 23.40 | 71.68 |
| bangla_speech→mymensingh_bangla_speech | 585 | 38.52 | 66.21 | 58.04 | 40.23 |
| bangla_speech→narail_bangla_speech | 47 | 9.38 | 40.41 | 26.25 | 68.75 |
| bangla_speech→narsingdi_bangla_speech | 53 | 13.75 | 42.63 | 23.68 | 69.62 |
| bangla_speech→noakhali_bangla_speech | 510 | 26.54 | 57.38 | 47.34 | 50.92 |
| bangla_speech→rajshahi_bangla_speech | 90 | 3.66 | 30.06 | 20.49 | 84.32 |
| bangla_speech→rangpur_bangla_speech | 118 | 4.52 | 29.64 | 20.55 | 80.24 |
| bangla_speech→sylhet_bangla_speech | 754 | 25.34 | 55.52 | 43.42 | 52.00 |
| bangla_speech→tangail_bangla_speech | 44 | 11.01 | 38.75 | 26.11 | 73.25 |
| barishal_bangla_speech→bangla_speech | 445 | 41.70 | 65.91 | 61.52 | 34.66 |
| barishal_bangla_speech→chittagong_bangla_speech | 413 | 7.58 | 33.32 | 23.49 | 75.41 |
| barishal_bangla_speech→mymensingh_bangla_speech | 324 | 23.86 | 52.30 | 44.64 | 51.00 |
| barishal_bangla_speech→noakhali_bangla_speech | 255 | 16.80 | 44.06 | 36.90 | 59.48 |
| barishal_bangla_speech→rajshahi_bangla_speech | 76 | 3.58 | 27.36 | 17.93 | 89.03 |
| barishal_bangla_speech→rangpur_bangla_speech | 67 | 4.73 | 24.55 | 16.98 | 82.75 |
| barishal_bangla_speech→sylhet_bangla_speech | 399 | 12.19 | 41.26 | 33.55 | 64.75 |
| chittagong_bangla_speech→bangla_speech | 1074 | 31.61 | 59.17 | 55.28 | 44.37 |
| chittagong_bangla_speech→barishal_bangla_speech | 413 | 15.16 | 42.40 | 36.15 | 61.55 |
| chittagong_bangla_speech→mymensingh_bangla_speech | 569 | 14.74 | 45.70 | 36.11 | 64.35 |
| chittagong_bangla_speech→noakhali_bangla_speech | 510 | 14.10 | 44.09 | 33.62 | 66.54 |
| chittagong_bangla_speech→rajshahi_bangla_speech | 61 | 2.38 | 27.48 | 20.36 | 85.20 |
| chittagong_bangla_speech→rangpur_bangla_speech | 59 | 3.57 | 21.80 | 13.68 | 85.05 |
| chittagong_bangla_speech→sylhet_bangla_speech | 654 | 12.50 | 42.18 | 30.85 | 67.78 |
| kishorgonj_bangla_speech→bangla_speech | 43 | 18.15 | 43.05 | 29.46 | 66.17 |
| mymensingh_bangla_speech→bangla_speech | 585 | 53.26 | 75.11 | 70.04 | 29.44 |
| mymensingh_bangla_speech→barishal_bangla_speech | 324 | 23.84 | 53.67 | 47.78 | 48.91 |
| mymensingh_bangla_speech→chittagong_bangla_speech | 569 | 13.84 | 43.48 | 31.20 | 68.32 |
| mymensingh_bangla_speech→noakhali_bangla_speech | 510 | 24.15 | 54.93 | 45.81 | 53.32 |
| mymensingh_bangla_speech→rajshahi_bangla_speech | 74 | 2.86 | 28.10 | 19.04 | 87.33 |
| mymensingh_bangla_speech→rangpur_bangla_speech | 65 | 3.84 | 20.66 | 12.30 | 89.20 |
| mymensingh_bangla_speech→sylhet_bangla_speech | 557 | 20.04 | 52.11 | 40.81 | 56.91 |
| narail_bangla_speech→bangla_speech | 47 | 18.07 | 52.09 | 38.36 | 60.32 |
| narsingdi_bangla_speech→bangla_speech | 53 | 18.65 | 45.86 | 30.95 | 66.45 |
| noakhali_bangla_speech→bangla_speech | 510 | 38.64 | 66.39 | 59.81 | 39.94 |
| noakhali_bangla_speech→barishal_bangla_speech | 255 | 19.45 | 49.98 | 44.55 | 52.64 |
| noakhali_bangla_speech→chittagong_bangla_speech | 510 | 15.31 | 43.58 | 32.17 | 67.97 |
| noakhali_bangla_speech→mymensingh_bangla_speech | 510 | 24.77 | 56.36 | 48.45 | 51.58 |
| noakhali_bangla_speech→sylhet_bangla_speech | 510 | 16.32 | 48.25 | 36.50 | 61.48 |
| rajshahi_bangla_speech→bangla_speech | 90 | 16.36 | 40.54 | 35.17 | 66.60 |
| rajshahi_bangla_speech→barishal_bangla_speech | 76 | 3.24 | 30.65 | 22.86 | 79.28 |
| rajshahi_bangla_speech→chittagong_bangla_speech | 61 | 1.92 | 24.33 | 13.28 | 88.75 |
| rajshahi_bangla_speech→mymensingh_bangla_speech | 74 | 8.98 | 34.85 | 24.75 | 78.33 |
| rajshahi_bangla_speech→rangpur_bangla_speech | 71 | 1.58 | 19.35 | 11.90 | 89.51 |
| rajshahi_bangla_speech→sylhet_bangla_speech | 48 | 5.19 | 30.58 | 22.73 | 88.26 |
| rangpur_bangla_speech→bangla_speech | 118 | 15.59 | 42.54 | 37.21 | 67.10 |
| rangpur_bangla_speech→barishal_bangla_speech | 67 | 10.45 | 35.08 | 29.76 | 74.77 |
| rangpur_bangla_speech→chittagong_bangla_speech | 59 | 3.40 | 21.89 | 13.49 | 95.39 |
| rangpur_bangla_speech→mymensingh_bangla_speech | 65 | 4.10 | 33.48 | 26.56 | 80.85 |
| rangpur_bangla_speech→rajshahi_bangla_speech | 71 | 2.34 | 23.13 | 17.43 | 92.53 |
| rangpur_bangla_speech→sylhet_bangla_speech | 46 | 5.79 | 29.68 | 20.89 | 83.26 |
| sylhet_bangla_speech→bangla_speech | 754 | 42.24 | 67.32 | 59.53 | 38.06 |
| sylhet_bangla_speech→barishal_bangla_speech | 399 | 18.48 | 47.48 | 41.71 | 56.41 |
| sylhet_bangla_speech→chittagong_bangla_speech | 654 | 13.97 | 42.93 | 30.43 | 68.75 |
| sylhet_bangla_speech→mymensingh_bangla_speech | 557 | 24.29 | 54.96 | 45.66 | 53.44 |
| sylhet_bangla_speech→noakhali_bangla_speech | 510 | 18.75 | 50.01 | 38.84 | 59.56 |
| sylhet_bangla_speech→rajshahi_bangla_speech | 48 | 2.53 | 24.47 | 15.04 | 91.10 |
| sylhet_bangla_speech→rangpur_bangla_speech | 46 | 1.40 | 19.65 | 10.50 | 90.08 |
| tangail_bangla_speech→bangla_speech | 44 | 13.54 | 40.49 | 28.09 | 78.72 |
| **OVERALL** | **18062** | **23.22** | **51.20** | **41.41** | **56.85** |

---

### NLLB (Fine-tuning completed)
* **Execution Time / Log Marker**: 4320.8s

#### Dialect Pair Breakdown Metrics:
| Language Pair | Samples | BLEU | chrF++ | METEOR | TER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| bangla_speech→barishal_bangla_speech | 445 | 14.24 | 43.03 | 33.08 | 64.34 |
| bangla_speech→chittagong_bangla_speech | 1074 | 18.42 | 42.98 | 35.83 | 66.54 |
| bangla_speech→kishorgonj_bangla_speech | 43 | 11.76 | 37.55 | 25.04 | 69.18 |
| bangla_speech→mymensingh_bangla_speech | 585 | 27.47 | 58.05 | 47.42 | 51.18 |
| bangla_speech→narail_bangla_speech | 47 | 9.89 | 44.02 | 29.79 | 64.45 |
| bangla_speech→narsingdi_bangla_speech | 53 | 13.86 | 42.12 | 29.63 | 64.24 |
| bangla_speech→noakhali_bangla_speech | 510 | 16.62 | 48.66 | 33.84 | 62.92 |
| bangla_speech→rajshahi_bangla_speech | 90 | 2.49 | 29.94 | 18.47 | 87.10 |
| bangla_speech→rangpur_bangla_speech | 118 | 4.54 | 29.68 | 19.67 | 80.51 |
| bangla_speech→sylhet_bangla_speech | 754 | 14.43 | 45.19 | 31.51 | 64.37 |
| bangla_speech→tangail_bangla_speech | 44 | 11.81 | 38.94 | 29.35 | 71.97 |
| barishal_bangla_speech→bangla_speech | 445 | 41.17 | 64.64 | 60.01 | 38.70 |
| barishal_bangla_speech→chittagong_bangla_speech | 413 | 1.55 | 23.15 | 11.65 | 88.66 |
| barishal_bangla_speech→mymensingh_bangla_speech | 324 | 17.33 | 46.49 | 37.52 | 58.54 |
| barishal_bangla_speech→noakhali_bangla_speech | 255 | 6.90 | 34.92 | 22.45 | 73.23 |
| barishal_bangla_speech→rajshahi_bangla_speech | 76 | 2.87 | 27.98 | 16.47 | 89.32 |
| barishal_bangla_speech→rangpur_bangla_speech | 67 | 1.39 | 19.68 | 9.12 | 91.37 |
| barishal_bangla_speech→sylhet_bangla_speech | 399 | 7.69 | 33.65 | 25.25 | 71.96 |
| chittagong_bangla_speech→bangla_speech | 1074 | 40.78 | 66.34 | 64.40 | 38.30 |
| chittagong_bangla_speech→barishal_bangla_speech | 413 | 7.21 | 34.14 | 25.34 | 72.81 |
| chittagong_bangla_speech→mymensingh_bangla_speech | 569 | 15.38 | 47.02 | 35.17 | 63.97 |
| chittagong_bangla_speech→noakhali_bangla_speech | 510 | 11.80 | 41.60 | 27.48 | 70.89 |
| chittagong_bangla_speech→rajshahi_bangla_speech | 61 | 3.36 | 29.97 | 19.80 | 85.25 |
| chittagong_bangla_speech→rangpur_bangla_speech | 59 | 1.81 | 22.22 | 11.21 | 87.54 |
| chittagong_bangla_speech→sylhet_bangla_speech | 654 | 8.03 | 37.99 | 24.41 | 72.29 |
| kishorgonj_bangla_speech→bangla_speech | 43 | 17.79 | 48.16 | 37.33 | 62.45 |
| mymensingh_bangla_speech→bangla_speech | 585 | 38.81 | 66.97 | 58.63 | 40.16 |
| mymensingh_bangla_speech→barishal_bangla_speech | 324 | 9.19 | 36.95 | 27.32 | 69.48 |
| mymensingh_bangla_speech→chittagong_bangla_speech | 569 | 3.33 | 29.33 | 14.07 | 85.14 |
| mymensingh_bangla_speech→noakhali_bangla_speech | 510 | 13.16 | 45.33 | 30.98 | 65.80 |
| mymensingh_bangla_speech→rajshahi_bangla_speech | 74 | 2.15 | 28.64 | 18.38 | 90.05 |
| mymensingh_bangla_speech→rangpur_bangla_speech | 65 | 2.38 | 19.94 | 11.39 | 91.14 |
| mymensingh_bangla_speech→sylhet_bangla_speech | 557 | 11.82 | 42.69 | 28.42 | 67.19 |
| narail_bangla_speech→bangla_speech | 47 | 19.31 | 56.64 | 42.45 | 55.47 |
| narsingdi_bangla_speech→bangla_speech | 53 | 22.60 | 48.50 | 32.73 | 63.55 |
| noakhali_bangla_speech→bangla_speech | 510 | 33.63 | 62.42 | 54.29 | 46.43 |
| noakhali_bangla_speech→barishal_bangla_speech | 255 | 8.33 | 35.32 | 26.04 | 71.40 |
| noakhali_bangla_speech→chittagong_bangla_speech | 510 | 3.70 | 28.65 | 13.82 | 85.76 |
| noakhali_bangla_speech→mymensingh_bangla_speech | 510 | 18.72 | 51.10 | 41.16 | 58.34 |
| noakhali_bangla_speech→sylhet_bangla_speech | 510 | 9.81 | 39.95 | 25.66 | 70.49 |
| rajshahi_bangla_speech→bangla_speech | 90 | 18.55 | 43.60 | 37.80 | 63.05 |
| rajshahi_bangla_speech→barishal_bangla_speech | 76 | 6.33 | 30.85 | 20.68 | 81.84 |
| rajshahi_bangla_speech→chittagong_bangla_speech | 61 | 1.97 | 24.87 | 13.33 | 86.88 |
| rajshahi_bangla_speech→mymensingh_bangla_speech | 74 | 4.71 | 28.17 | 18.28 | 85.12 |
| rajshahi_bangla_speech→rangpur_bangla_speech | 71 | 1.12 | 19.63 | 10.95 | 90.54 |
| rajshahi_bangla_speech→sylhet_bangla_speech | 48 | 2.14 | 24.38 | 14.06 | 87.45 |
| rangpur_bangla_speech→bangla_speech | 118 | 16.46 | 45.78 | 40.21 | 65.67 |
| rangpur_bangla_speech→barishal_bangla_speech | 67 | 6.22 | 31.36 | 21.59 | 83.78 |
| rangpur_bangla_speech→chittagong_bangla_speech | 59 | 3.17 | 26.23 | 15.91 | 89.80 |
| rangpur_bangla_speech→mymensingh_bangla_speech | 65 | 3.27 | 28.78 | 19.10 | 88.15 |
| rangpur_bangla_speech→rajshahi_bangla_speech | 71 | 2.57 | 26.20 | 18.10 | 93.41 |
| rangpur_bangla_speech→sylhet_bangla_speech | 46 | 2.27 | 24.13 | 15.05 | 87.12 |
| sylhet_bangla_speech→bangla_speech | 754 | 36.88 | 65.29 | 58.66 | 42.48 |
| sylhet_bangla_speech→barishal_bangla_speech | 399 | 11.28 | 37.01 | 28.80 | 69.10 |
| sylhet_bangla_speech→chittagong_bangla_speech | 654 | 3.93 | 29.49 | 14.21 | 84.41 |
| sylhet_bangla_speech→mymensingh_bangla_speech | 557 | 18.75 | 50.92 | 39.61 | 59.57 |
| sylhet_bangla_speech→noakhali_bangla_speech | 510 | 12.65 | 43.73 | 29.26 | 68.36 |
| sylhet_bangla_speech→rajshahi_bangla_speech | 48 | 5.37 | 29.35 | 17.90 | 87.34 |
| sylhet_bangla_speech→rangpur_bangla_speech | 46 | 1.22 | 19.08 | 9.07 | 90.91 |
| tangail_bangla_speech→bangla_speech | 44 | 18.97 | 46.48 | 37.03 | 66.89 |

---

### mBART (Fine-tuning completed)
* **Execution Time / Log Marker**: 13888.9s

#### Dialect Pair Breakdown Metrics:
| Language Pair | Samples | BLEU | chrF++ | METEOR | TER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| bangla_speech→barishal_bangla_speech | 445 | 13.35 | 35.60 | 25.86 | 71.90 |
| bangla_speech→chittagong_bangla_speech | 1074 | 22.60 | 45.66 | 40.64 | 61.90 |
| bangla_speech→kishorgonj_bangla_speech | 43 | 4.47 | 27.92 | 15.63 | 79.93 |
| bangla_speech→mymensingh_bangla_speech | 585 | 12.32 | 39.53 | 28.10 | 74.49 |
| bangla_speech→narail_bangla_speech | 47 | 5.08 | 33.26 | 23.43 | 73.44 |
| bangla_speech→narsingdi_bangla_speech | 53 | 4.95 | 31.14 | 19.89 | 78.48 |
| bangla_speech→noakhali_bangla_speech | 510 | 9.07 | 36.85 | 24.66 | 78.47 |
| bangla_speech→rajshahi_bangla_speech | 90 | 2.33 | 22.49 | 13.55 | 92.37 |
| bangla_speech→rangpur_bangla_speech | 118 | 4.86 | 25.69 | 17.09 | 82.91 |
| bangla_speech→sylhet_bangla_speech | 754 | 10.87 | 36.96 | 25.12 | 75.24 |
| bangla_speech→tangail_bangla_speech | 44 | 7.48 | 30.01 | 23.64 | 78.34 |
| barishal_bangla_speech→bangla_speech | 445 | 18.70 | 40.61 | 33.83 | 65.05 |
| barishal_bangla_speech→chittagong_bangla_speech | 413 | 5.79 | 25.49 | 15.77 | 85.32 |
| barishal_bangla_speech→mymensingh_bangla_speech | 324 | 11.83 | 37.47 | 27.73 | 69.73 |
| barishal_bangla_speech→noakhali_bangla_speech | 255 | 5.62 | 31.48 | 21.35 | 76.38 |
| barishal_bangla_speech→rajshahi_bangla_speech | 76 | 2.63 | 23.18 | 14.25 | 91.12 |
| barishal_bangla_speech→rangpur_bangla_speech | 67 | 1.46 | 17.51 | 8.36 | 93.26 |
| barishal_bangla_speech→sylhet_bangla_speech | 399 | 8.48 | 31.73 | 23.56 | 74.96 |
| chittagong_bangla_speech→bangla_speech | 1074 | 28.39 | 50.90 | 51.20 | 53.69 |
| chittagong_bangla_speech→barishal_bangla_speech | 413 | 11.22 | 33.68 | 25.86 | 72.06 |
| chittagong_bangla_speech→mymensingh_bangla_speech | 569 | 8.80 | 36.88 | 26.27 | 75.88 |
| chittagong_bangla_speech→noakhali_bangla_speech | 510 | 6.99 | 34.31 | 22.31 | 78.90 |
| chittagong_bangla_speech→rajshahi_bangla_speech | 61 | 2.26 | 24.22 | 17.65 | 89.47 |
| chittagong_bangla_speech→rangpur_bangla_speech | 59 | 1.87 | 20.67 | 12.65 | 87.23 |
| chittagong_bangla_speech→sylhet_bangla_speech | 654 | 8.02 | 35.54 | 24.16 | 75.46 |
| kishorgonj_bangla_speech→bangla_speech | 43 | 14.58 | 34.28 | 24.31 | 76.58 |
| mymensingh_bangla_speech→bangla_speech | 585 | 13.87 | 40.26 | 31.08 | 70.45 |
| mymensingh_bangla_speech→barishal_bangla_speech | 324 | 13.41 | 34.49 | 25.18 | 72.06 |
| mymensingh_bangla_speech→chittagong_bangla_speech | 569 | 8.64 | 33.04 | 19.83 | 79.34 |
| mymensingh_bangla_speech→noakhali_bangla_speech | 510 | 7.92 | 36.22 | 24.97 | 77.44 |
| mymensingh_bangla_speech→rajshahi_bangla_speech | 74 | 1.32 | 22.29 | 14.73 | 92.99 |
| mymensingh_bangla_speech→rangpur_bangla_speech | 65 | 2.24 | 17.70 | 10.19 | 92.24 |
| mymensingh_bangla_speech→sylhet_bangla_speech | 557 | 8.86 | 35.63 | 23.12 | 76.45 |
| narail_bangla_speech→bangla_speech | 47 | 5.79 | 34.33 | 21.17 | 79.76 |
| narsingdi_bangla_speech→bangla_speech | 53 | 8.18 | 32.13 | 19.44 | 80.65 |
| noakhali_bangla_speech→bangla_speech | 510 | 12.16 | 38.94 | 30.29 | 72.79 |
| noakhali_bangla_speech→barishal_bangla_speech | 255 | 11.01 | 32.65 | 23.49 | 74.91 |
| noakhali_bangla_speech→chittagong_bangla_speech | 510 | 8.04 | 31.70 | 18.39 | 81.00 |
| noakhali_bangla_speech→mymensingh_bangla_speech | 510 | 10.08 | 37.38 | 26.89 | 75.67 |
| noakhali_bangla_speech→sylhet_bangla_speech | 510 | 7.24 | 34.54 | 22.28 | 78.32 |
| rajshahi_bangla_speech→bangla_speech | 90 | 4.89 | 21.61 | 15.89 | 88.31 |
| rajshahi_bangla_speech→barishal_bangla_speech | 76 | 7.34 | 22.11 | 15.35 | 89.26 |
| rajshahi_bangla_speech→chittagong_bangla_speech | 61 | 1.46 | 17.01 | 8.89 | 93.75 |
| rajshahi_bangla_speech→mymensingh_bangla_speech | 74 | 1.23 | 21.35 | 12.70 | 92.17 |
| rajshahi_bangla_speech→rangpur_bangla_speech | 71 | 0.92 | 15.38 | 8.61 | 93.35 |
| rajshahi_bangla_speech→sylhet_bangla_speech | 48 | 9.32 | 25.55 | 17.26 | 84.62 |
| rangpur_bangla_speech→bangla_speech | 118 | 8.05 | 30.02 | 22.87 | 81.97 |
| rangpur_bangla_speech→barishal_bangla_speech | 67 | 2.85 | 22.45 | 14.52 | 90.09 |
| rangpur_bangla_speech→chittagong_bangla_speech | 59 | 4.48 | 18.61 | 11.67 | 94.74 |
| rangpur_bangla_speech→mymensingh_bangla_speech | 65 | 1.88 | 23.27 | 13.97 | 92.71 |
| rangpur_bangla_speech→rajshahi_bangla_speech | 71 | 1.14 | 19.74 | 11.81 | 98.56 |
| rangpur_bangla_speech→sylhet_bangla_speech | 46 | 8.13 | 26.48 | 19.19 | 79.83 |
| sylhet_bangla_speech→bangla_speech | 754 | 14.10 | 40.29 | 33.32 | 70.58 |
| sylhet_bangla_speech→barishal_bangla_speech | 399 | 10.81 | 33.38 | 25.64 | 74.62 |
| sylhet_bangla_speech→chittagong_bangla_speech | 654 | 8.91 | 33.05 | 20.01 | 80.07 |
| sylhet_bangla_speech→mymensingh_bangla_speech | 557 | 8.88 | 37.04 | 26.14 | 77.41 |
| sylhet_bangla_speech→noakhali_bangla_speech | 510 | 7.08 | 34.77 | 23.04 | 80.91 |
| sylhet_bangla_speech→rajshahi_bangla_speech | 48 | 1.93 | 26.75 | 18.28 | 90.25 |
| sylhet_bangla_speech→rangpur_bangla_speech | 46 | 1.22 | 17.82 | 8.63 | 93.39 |
| tangail_bangla_speech→bangla_speech | 44 | 8.09 | 28.48 | 19.83 | 87.16 |

---

### 100 Epochs of Best Model (BanglaT5)
* **Execution Time / Log Marker**: 851.1s

#### Per-dialect-pair results:
| Language Pair | Samples | BLEU | chrF | METEOR | TER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| bangla_speech→barishal_bangla_speech | 445 | 37.87 | 64.00 | 58.53 | 38.46 |
| bangla_speech→chittagong_bangla_speech | 1074 | 28.46 | 56.73 | 51.15 | 50.26 |
| bangla_speech→kishorgonj_bangla_speech | 43 | 12.72 | 40.98 | 28.88 | 64.16 |
| bangla_speech→mymensingh_bangla_speech | 585 | 39.96 | 68.13 | 60.77 | 39.04 |
| bangla_speech→narail_bangla_speech | 47 | 12.28 | 45.94 | 33.50 | 59.38 |
| bangla_speech→narsingdi_bangla_speech | 53 | 20.61 | 47.24 | 32.52 | 60.13 |
| bangla_speech→noakhali_bangla_speech | 510 | 29.45 | 59.92 | 50.48 | 49.23 |
| bangla_speech→rajshahi_bangla_speech | 90 | 7.91 | 34.18 | 24.20 | 77.12 |
| bangla_speech→rangpur_bangla_speech | 118 | 11.52 | 38.52 | 32.02 | 69.16 |
| bangla_speech→sylhet_bangla_speech | 754 | 29.49 | 59.93 | 50.58 | 47.43 |
| bangla_speech→tangail_bangla_speech | 44 | 14.82 | 42.81 | 34.50 | 64.65 |
| barishal_bangla_speech→bangla_speech | 445 | 50.10 | 72.94 | 69.75 | 28.15 |
| barishal_bangla_speech→chittagong_bangla_speech | 413 | 15.82 | 43.54 | 35.75 | 64.98 |
| barishal_bangla_speech→mymensingh_bangla_speech | 324 | 35.55 | 61.85 | 54.95 | 42.21 |
| barishal_bangla_speech→noakhali_bangla_speech | 255 | 23.16 | 51.84 | 45.06 | 52.27 |
| barishal_bangla_speech→rajshahi_bangla_speech | 76 | 5.57 | 32.05 | 21.26 | 82.51 |
| barishal_bangla_speech→rangpur_bangla_speech | 67 | 11.42 | 34.96 | 30.59 | 71.97 |
| barishal_bangla_speech→sylhet_bangla_speech | 399 | 21.63 | 50.43 | 46.61 | 58.41 |
| chittagong_bangla_speech→bangla_speech | 1074 | 42.76 | 68.37 | 67.31 | 35.13 |
| chittagong_bangla_speech→barishal_bangla_speech | 413 | 27.89 | 55.10 | 50.48 | 49.80 |
| chittagong_bangla_speech→mymensingh_bangla_speech | 569 | 20.83 | 52.38 | 44.42 | 57.43 |
| chittagong_bangla_speech→noakhali_bangla_speech | 510 | 18.75 | 49.19 | 39.19 | 60.86 |
| chittagong_bangla_speech→rajshahi_bangla_speech | 61 | 7.14 | 32.09 | 23.11 | 77.96 |
| chittagong_bangla_speech→rangpur_bangla_speech | 59 | 11.78 | 33.60 | 29.01 | 71.65 |
| chittagong_bangla_speech→sylhet_bangla_speech | 654 | 19.22 | 50.89 | 42.69 | 58.35 |
| kishorgonj_bangla_speech→bangla_speech | 43 | 19.90 | 47.36 | 39.01 | 57.99 |
| mymensingh_bangla_speech→bangla_speech | 585 | 55.00 | 76.89 | 72.71 | 27.75 |
| mymensingh_bangla_speech→barishal_bangla_speech | 324 | 36.70 | 62.86 | 57.10 | 40.47 |
| mymensingh_bangla_speech→chittagong_bangla_speech | 569 | 19.32 | 49.02 | 38.76 | 62.37 |
| mymensingh_bangla_speech→noakhali_bangla_speech | 510 | 27.71 | 58.11 | 49.85 | 50.10 |
| mymensingh_bangla_speech→rajshahi_bangla_speech | 74 | 6.26 | 32.64 | 22.32 | 84.37 |
| mymensingh_bangla_speech→rangpur_bangla_speech | 65 | 11.00 | 33.09 | 25.99 | 77.84 |
| mymensingh_bangla_speech→sylhet_bangla_speech | 557 | 25.51 | 56.89 | 47.80 | 51.49 |
| narail_bangla_speech→bangla_speech | 47 | 28.23 | 60.44 | 47.09 | 47.77 |
| narsingdi_bangla_speech→bangla_speech | 53 | 27.73 | 53.83 | 46.25 | 55.48 |
| noakhali_bangla_speech→bangla_speech | 510 | 41.39 | 68.90 | 63.68 | 38.48 |
| noakhali_bangla_speech→barishal_bangla_speech | 255 | 33.78 | 60.92 | 56.43 | 42.68 |
| noakhali_bangla_speech→chittagong_bangla_speech | 510 | 19.33 | 48.34 | 37.90 | 63.00 |
| noakhali_bangla_speech→mymensingh_bangla_speech | 510 | 28.20 | 59.86 | 53.25 | 49.15 |
| noakhali_bangla_speech→sylhet_bangla_speech | 510 | 21.55 | 53.52 | 44.07 | 56.20 |
| rajshahi_bangla_speech→bangla_speech | 90 | 23.40 | 46.72 | 43.53 | 56.99 |
| rajshahi_bangla_speech→barishal_bangla_speech | 76 | 6.79 | 35.42 | 27.25 | 75.70 |
| rajshahi_bangla_speech→chittagong_bangla_speech | 61 | 8.45 | 30.40 | 18.99 | 80.94 |
| rajshahi_bangla_speech→mymensingh_bangla_speech | 74 | 10.19 | 34.70 | 26.19 | 77.02 |
| rajshahi_bangla_speech→rangpur_bangla_speech | 71 | 7.09 | 28.89 | 21.11 | 83.63 |
| rajshahi_bangla_speech→sylhet_bangla_speech | 48 | 13.35 | 35.77 | 30.27 | 70.04 |
| rangpur_bangla_speech→bangla_speech | 118 | 23.39 | 49.30 | 47.59 | 57.22 |
| rangpur_bangla_speech→barishal_bangla_speech | 67 | 11.76 | 37.90 | 33.12 | 71.17 |
| rangpur_bangla_speech→chittagong_bangla_speech | 59 | 11.33 | 31.25 | 22.14 | 80.92 |
| rangpur_bangla_speech→mymensingh_bangla_speech | 65 | 11.10 | 35.34 | 27.36 | 77.81 |
| rangpur_bangla_speech→rajshahi_bangla_speech | 71 | 5.55 | 28.70 | 21.02 | 88.22 |
| rangpur_bangla_speech→sylhet_bangla_speech | 46 | 16.43 | 38.64 | 33.51 | 69.10 |
| sylhet_bangla_speech→bangla_speech | 754 | 45.65 | 71.05 | 64.71 | 34.67 |
| sylhet_bangla_speech→barishal_bangla_speech | 399 | 32.04 | 59.22 | 54.88 | 44.87 |
| sylhet_bangla_speech→chittagong_bangla_speech | 654 | 21.50 | 49.72 | 39.89 | 60.69 |
| sylhet_bangla_speech→mymensingh_bangla_speech | 557 | 28.21 | 59.30 | 51.39 | 50.00 |
| sylhet_bangla_speech→noakhali_bangla_speech | 510 | 23.91 | 54.21 | 43.61 | 55.90 |
| sylhet_bangla_speech→rajshahi_bangla_speech | 48 | 5.73 | 32.98 | 21.76 | 80.93 |
| sylhet_bangla_speech→rangpur_bangla_speech | 46 | 12.27 | 36.15 | 26.93 | 76.45 |
| tangail_bangla_speech→bangla_speech | 44 | 20.47 | 45.39 | 35.72 | 66.22 |
| **OVERALL** | **18062** | **29.26** | **57.26** | **49.68** | **50.59** |

---

## 2. Model Specifications & Comparison

### Quick Comparison Table
| Feature | NLLB-600M | BanglaT5 | mBART-Large-50 |
| :--- | :--- | :--- | :--- |
| **Parameters** | 615M | 247M | 611M |
| **Architecture** | Encoder–Decoder Transformer | T5 Encoder–Decoder | BART Encoder–Decoder |
| **Encoder / Decoder Layers** | 12 / 12 | 12 / 12 | 12 / 12 |
| **Hidden Size** | 1024 | 768 | 1024 |
| **Attention Heads** | 16 | 12 | 16 |
| **FFN Size** | 4096 | 3072 | 4096 |
| **Vocabulary** | ~256K (SentencePiece) | 32K (SentencePiece) | ~250K (SentencePiece) |
| **Languages Supported** | 200 | Primarily Bangla | 50 |
| **Primary Use Case** | Multilingual MT | Bangla NLG | Multilingual MT |

### Detailed Specifications

#### NLLB-200 Distilled 600M
* **Parameters**: 615,071,744 (~615M)
* **Architecture**: Transformer Encoder–Decoder
* **Encoder / Decoder layers**: 12 / 12
* **Hidden dimension ($d_{model}$)**: 1024
* **FFN dimension**: 4096
* **Attention heads**: 16
* **Tokenizer**: SentencePiece
* **Vocabulary**: ~256K
* **Languages**: 200
* **Translation Mode**: Many-to-many (ACL Anthology)

#### BanglaT5
* **Parameters**: 247M
* **Architecture**: T5
* **Encoder / Decoder layers**: 12 / 12
* **Hidden dimension**: 768
* **FFN dimension**: 3072
* **Attention heads**: 12
* **Vocabulary**: 32K SentencePiece
* **Pretraining corpus**: ~27.5 GB Bangla text
* **Design Goal**: Designed for Bangla NLG tasks (translation, summarization, QA, dialogue, etc.) (ACL Anthology)

#### mBART-Large-50 Many-to-Many
* **Parameters**: 610,879,488 (~611M)
* **Architecture**: BART Encoder–Decoder
* **Encoder / Decoder layers**: 12 / 12
* **Hidden dimension**: 1024
* **FFN dimension**: 4096
* **Attention heads**: 16
* **Vocabulary**: ~250K SentencePiece
* **Languages**: 50
* **Translation Mode**: Many-to-many (ACL Anthology)