# Dataset Size vs. Performance Analysis

## 3. Dataset Size vs. Performance Analysis (LoRA $r=8$, $\alpha=16$, Epoch 10)

### Dataset Size: 500
| Language Pair | N | BLEU | chrF++ | METEOR | TER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| bangla_speech→chittagong_bangla_speech | 500 | 4.02 | 29.72 | 15.82 | 93.02 |
| bangla_speech→mymensingh_bangla_speech | 500 | 28.62 | 58.31 | 50.24 | 54.78 |
| bangla_speech→noakhali_bangla_speech | 500 | 16.09 | 45.82 | 32.54 | 70.48 |
| bangla_speech→sylhet_bangla_speech | 500 | 15.28 | 44.13 | 32.14 | 69.70 |
| chittagong_bangla_speech→bangla_speech | 500 | 5.72 | 31.22 | 19.41 | 91.80 |
| chittagong_bangla_speech→mymensingh_bangla_speech | 500 | 4.50 | 30.39 | 18.10 | 95.53 |
| chittagong_bangla_speech→noakhali_bangla_speech | 500 | 3.69 | 29.58 | 17.10 | 94.63 |
| chittagong_bangla_speech→sylhet_bangla_speech | 500 | 3.98 | 29.14 | 16.82 | 93.38 |
| mymensingh_bangla_speech→bangla_speech | 500 | 31.26 | 59.43 | 50.96 | 51.16 |
| mymensingh_bangla_speech→chittagong_bangla_speech | 500 | 3.67 | 29.43 | 15.19 | 91.62 |
| mymensingh_bangla_speech→noakhali_bangla_speech | 500 | 15.65 | 45.88 | 32.32 | 68.39 |
| mymensingh_bangla_speech→sylhet_bangla_speech | 500 | 13.22 | 42.68 | 30.57 | 70.68 |
| noakhali_bangla_speech→bangla_speech | 500 | 18.06 | 47.20 | 35.32 | 68.27 |
| noakhali_bangla_speech→chittagong_bangla_speech | 500 | 3.29 | 29.65 | 15.61 | 90.80 |
| noakhali_bangla_speech→mymensingh_bangla_speech | 500 | 15.34 | 46.09 | 34.38 | 71.38 |
| noakhali_bangla_speech→sylhet_bangla_speech | 500 | 8.68 | 37.19 | 23.68 | 81.10 |
| sylhet_bangla_speech→bangla_speech | 500 | 18.03 | 46.14 | 35.40 | 67.45 |
| sylhet_bangla_speech→chittagong_bangla_speech | 500 | 3.36 | 28.63 | 14.64 | 93.04 |
| sylhet_bangla_speech→mymensingh_bangla_speech | 500 | 13.78 | 43.20 | 32.24 | 74.90 |
| sylhet_bangla_speech→noakhali_bangla_speech | 500 | 9.03 | 37.23 | 23.62 | 81.88 |
| **OVERALL** | **10000** | **12.09** | **39.56** | **27.30** | **78.79** |

### Dataset Size: 1000
| Language Pair | N | BLEU | chrF++ | METEOR | TER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| bangla_speech→chittagong_bangla_speech | 500 | 5.72 | 34.02 | 19.39 | 84.52 |
| bangla_speech→mymensingh_bangla_speech | 500 | 33.85 | 62.19 | 54.98 | 43.25 |
| bangla_speech→noakhali_bangla_speech | 500 | 19.11 | 49.61 | 36.81 | 63.25 |
| bangla_speech→sylhet_bangla_speech | 500 | 17.27 | 47.54 | 36.25 | 62.24 |
| chittagong_bangla_speech→bangla_speech | 500 | 8.17 | 35.44 | 22.74 | 78.15 |
| chittagong_bangla_speech→mymensingh_bangla_speech | 500 | 5.67 | 32.69 | 19.59 | 85.99 |
| chittagong_bangla_speech→noakhali_bangla_speech | 500 | 4.17 | 31.60 | 18.71 | 88.80 |
| chittagong_bangla_speech→sylhet_bangla_speech | 500 | 4.34 | 30.52 | 17.52 | 88.62 |
| mymensingh_bangla_speech→bangla_speech | 500 | 38.11 | 65.23 | 57.48 | 40.84 |
| mymensingh_bangla_speech→chittagong_bangla_speech | 500 | 5.14 | 33.21 | 18.40 | 84.30 |
| mymensingh_bangla_speech→noakhali_bangla_speech | 500 | 16.96 | 48.77 | 35.53 | 63.51 |
| mymensingh_bangla_speech→sylhet_bangla_speech | 500 | 14.50 | 45.58 | 33.95 | 64.49 |
| noakhali_bangla_speech→bangla_speech | 500 | 22.43 | 52.28 | 40.59 | 56.54 |
| noakhali_bangla_speech→chittagong_bangla_speech | 500 | 4.59 | 32.92 | 18.59 | 84.72 |
| noakhali_bangla_speech→mymensingh_bangla_speech | 500 | 17.57 | 48.86 | 37.12 | 62.01 |
| noakhali_bangla_speech→sylhet_bangla_speech | 500 | 10.34 | 39.46 | 25.45 | 73.13 |
| sylhet_bangla_speech→bangla_speech | 500 | 22.45 | 51.11 | 40.54 | 57.93 |
| sylhet_bangla_speech→chittagong_bangla_speech | 500 | 4.70 | 31.91 | 17.52 | 92.39 |
| sylhet_bangla_speech→mymensingh_bangla_speech | 500 | 15.56 | 46.50 | 36.03 | 68.07 |
| sylhet_bangla_speech→noakhali_bangla_speech | 500 | 10.52 | 39.74 | 25.98 | 76.91 |
| **OVERALL** | **10000** | **14.45** | **42.95** | **30.66** | **71.08** |

### Dataset Size: 1500
| Language Pair | N | BLEU | chrF++ | METEOR | TER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| bangla_speech→chittagong_bangla_speech | 500 | 7.91 | 37.36 | 24.03 | 82.59 |
| bangla_speech→mymensingh_bangla_speech | 500 | 34.79 | 64.13 | 57.47 | 42.09 |
| bangla_speech→noakhali_bangla_speech | 500 | 19.74 | 51.05 | 38.37 | 58.37 |
| bangla_speech→sylhet_bangla_speech | 500 | 18.75 | 49.45 | 38.03 | 58.83 |
| chittagong_bangla_speech→bangla_speech | 500 | 15.12 | 45.76 | 36.33 | 65.63 |
| chittagong_bangla_speech→mymensingh_bangla_speech | 500 | 9.24 | 38.41 | 26.61 | 74.44 |
| chittagong_bangla_speech→noakhali_bangla_speech | 500 | 6.82 | 35.92 | 22.59 | 77.40 |
| chittagong_bangla_speech→sylhet_bangla_speech | 500 | 6.43 | 34.49 | 21.35 | 79.55 |
| mymensingh_bangla_speech→bangla_speech | 500 | 47.51 | 72.21 | 66.08 | 33.44 |
| mymensingh_bangla_speech→chittagong_bangla_speech | 500 | 7.36 | 36.30 | 22.87 | 82.59 |
| mymensingh_bangla_speech→noakhali_bangla_speech | 500 | 16.88 | 49.96 | 37.63 | 62.30 |
| mymensingh_bangla_speech→sylhet_bangla_speech | 500 | 15.42 | 47.27 | 35.98 | 61.66 |
| noakhali_bangla_speech→bangla_speech | 500 | 31.62 | 60.59 | 51.53 | 47.95 |
| noakhali_bangla_speech→chittagong_bangla_speech | 500 | 6.34 | 35.37 | 21.88 | 81.69 |
| noakhali_bangla_speech→mymensingh_bangla_speech | 500 | 19.72 | 51.63 | 41.19 | 56.73 |
| noakhali_bangla_speech→sylhet_bangla_speech | 500 | 10.82 | 41.23 | 28.28 | 69.23 |
| sylhet_bangla_speech→bangla_speech | 500 | 31.10 | 60.09 | 51.84 | 50.07 |
| sylhet_bangla_speech→chittagong_bangla_speech | 500 | 6.52 | 34.89 | 21.24 | 84.68 |
| sylhet_bangla_speech→mymensingh_bangla_speech | 500 | 18.16 | 50.05 | 40.53 | 62.61 |
| sylhet_bangla_speech→noakhali_bangla_speech | 500 | 12.29 | 42.36 | 28.86 | 73.17 |
| **OVERALL** | **10000** | **17.71** | **46.92** | **35.63** | **65.36** |

### Dataset Size: 2000
| Language Pair | N | BLEU | chrF++ | METEOR | TER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| bangla_speech→chittagong_bangla_speech | 500 | 10.17 | 38.88 | 26.37 | 78.36 |
| bangla_speech→mymensingh_bangla_speech | 500 | 33.23 | 63.34 | 56.31 | 48.23 |
| bangla_speech→noakhali_bangla_speech | 500 | 18.95 | 49.30 | 36.61 | 63.97 |
| bangla_speech→sylhet_bangla_speech | 500 | 20.21 | 50.34 | 39.32 | 61.80 |
| chittagong_bangla_speech→bangla_speech | 500 | 15.83 | 46.85 | 37.64 | 67.70 |
| chittagong_bangla_speech→mymensingh_bangla_speech | 500 | 10.13 | 39.38 | 28.70 | 76.45 |
| chittagong_bangla_speech→noakhali_bangla_speech | 500 | 6.57 | 35.00 | 20.98 | 81.05 |
| chittagong_bangla_speech→sylhet_bangla_speech | 500 | 7.35 | 35.45 | 23.35 | 79.78 |
| mymensingh_bangla_speech→bangla_speech | 500 | 46.40 | 71.55 | 65.43 | 40.16 |
| mymensingh_bangla_speech→chittagong_bangla_speech | 500 | 8.48 | 36.99 | 24.06 | 79.89 |
| mymensingh_bangla_speech→noakhali_bangla_speech | 500 | 17.63 | 48.03 | 35.43 | 65.20 |
| mymensingh_bangla_speech→sylhet_bangla_speech | 500 | 16.48 | 47.09 | 34.99 | 65.97 |
| noakhali_bangla_speech→bangla_speech | 500 | 32.12 | 60.77 | 51.86 | 52.67 |
| noakhali_bangla_speech→chittagong_bangla_speech | 500 | 7.57 | 35.58 | 22.19 | 81.40 |
| noakhali_bangla_speech→mymensingh_bangla_speech | 500 | 20.03 | 51.48 | 40.90 | 62.03 |
| noakhali_bangla_speech→sylhet_bangla_speech | 500 | 12.31 | 42.35 | 29.73 | 72.05 |
| sylhet_bangla_speech→bangla_speech | 500 | 32.56 | 60.90 | 52.67 | 50.98 |
| sylhet_bangla_speech→chittagong_bangla_speech | 500 | 8.00 | 35.32 | 22.63 | 81.75 |
| sylhet_bangla_speech→mymensingh_bangla_speech | 500 | 18.01 | 49.77 | 39.81 | 66.96 |
| sylhet_bangla_speech→noakhali_bangla_speech | 500 | 12.86 | 42.18 | 29.28 | 72.98 |
| **OVERALL** | **10000** | **18.28** | **47.03** | **35.91** | **67.55** |

### Dataset Size: 2500
| Language Pair | N | BLEU | chrF++ | METEOR | TER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| bangla_speech→chittagong_bangla_speech | 500 | 10.79 | 39.48 | 26.90 | 76.16 |
| bangla_speech→mymensingh_bangla_speech | 500 | 33.24 | 63.50 | 56.88 | 48.00 |
| bangla_speech→noakhali_bangla_speech | 500 | 20.05 | 50.69 | 37.93 | 63.02 |
| bangla_speech→sylhet_bangla_speech | 500 | 21.32 | 51.66 | 40.94 | 59.96 |
| chittagong_bangla_speech→bangla_speech | 500 | 18.46 | 49.45 | 40.75 | 64.46 |
| chittagong_bangla_speech→mymensingh_bangla_speech | 500 | 11.37 | 41.57 | 30.79 | 73.63 |
| chittagong_bangla_speech→noakhali_bangla_speech | 500 | 8.44 | 37.39 | 24.20 | 77.89 |
| chittagong_bangla_speech→sylhet_bangla_speech | 500 | 9.13 | 37.84 | 25.40 | 76.43 |
| mymensingh_bangla_speech→bangla_speech | 500 | 48.39 | 73.07 | 67.34 | 38.72 |
| mymensingh_bangla_speech→chittagong_bangla_speech | 500 | 8.87 | 37.75 | 25.38 | 80.27 |
| mymensingh_bangla_speech→noakhali_bangla_speech | 500 | 18.49 | 49.79 | 37.21 | 64.72 |
| mymensingh_bangla_speech→sylhet_bangla_speech | 500 | 18.28 | 48.81 | 37.52 | 64.06 |
| noakhali_bangla_speech→bangla_speech | 500 | 34.17 | 62.61 | 53.59 | 50.80 |
| noakhali_bangla_speech→chittagong_bangla_speech | 500 | 8.69 | 36.45 | 23.02 | 79.38 |
| noakhali_bangla_speech→mymensingh_bangla_speech | 500 | 21.96 | 53.09 | 43.79 | 60.50 |
| noakhali_bangla_speech→sylhet_bangla_speech | 500 | 14.15 | 43.96 | 31.55 | 71.25 |
| sylhet_bangla_speech→bangla_speech | 500 | 34.14 | 62.16 | 54.14 | 49.54 |
| sylhet_bangla_speech→chittagong_bangla_speech | 500 | 8.77 | 36.72 | 24.56 | 79.96 |
| sylhet_bangla_speech→mymensingh_bangla_speech | 500 | 20.28 | 51.29 | 42.30 | 63.02 |
| sylhet_bangla_speech→noakhali_bangla_speech | 500 | 14.01 | 43.90 | 31.19 | 71.27 |
| **OVERALL** | **10000** | **19.67** | **48.57** | **37.77** | **65.73** |

### Dataset Size: 3000
| Language Pair | N | BLEU | chrF++ | METEOR | TER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| bangla_speech→chittagong_bangla_speech | 500 | 13.76 | 45.10 | 33.44 | 68.00 |
| bangla_speech→mymensingh_bangla_speech | 500 | 37.38 | 66.43 | 61.81 | 38.78 |
| bangla_speech→noakhali_bangla_speech | 500 | 24.33 | 55.18 | 45.38 | 53.10 |
| bangla_speech→sylhet_bangla_speech | 500 | 24.50 | 55.18 | 44.80 | 51.99 |
| chittagong_bangla_speech→bangla_speech | 500 | 21.53 | 53.20 | 46.68 | 55.56 |
| chittagong_bangla_speech→mymensingh_bangla_speech | 500 | 13.65 | 45.05 | 36.01 | 65.66 |
| chittagong_bangla_speech→noakhali_bangla_speech | 500 | 10.95 | 40.61 | 29.79 | 72.47 |
| chittagong_bangla_speech→sylhet_bangla_speech | 500 | 11.30 | 41.69 | 30.20 | 68.73 |
| mymensingh_bangla_speech→bangla_speech | 500 | 55.79 | 77.13 | 73.20 | 28.04 |
| mymensingh_bangla_speech→chittagong_bangla_speech | 500 | 11.16 | 42.51 | 30.90 | 74.01 |
| mymensingh_bangla_speech→noakhali_bangla_speech | 500 | 21.63 | 53.41 | 43.24 | 55.47 |
| mymensingh_bangla_speech→sylhet_bangla_speech | 500 | 20.55 | 52.08 | 41.68 | 56.79 |
| noakhali_bangla_speech→bangla_speech | 500 | 38.81 | 65.69 | 58.77 | 41.23 |
| noakhali_bangla_speech→chittagong_bangla_speech | 500 | 11.19 | 41.09 | 28.42 | 72.20 |
| noakhali_bangla_speech→mymensingh_bangla_speech | 500 | 24.14 | 56.03 | 47.68 | 51.61 |
| noakhali_bangla_speech→sylhet_bangla_speech | 500 | 15.75 | 47.22 | 35.06 | 65.10 |
| sylhet_bangla_speech→bangla_speech | 500 | 40.05 | 66.59 | 60.65 | 39.36 |
| sylhet_bangla_speech→chittagong_bangla_speech | 500 | 10.93 | 41.14 | 29.75 | 72.28 |
| sylhet_bangla_speech→mymensingh_bangla_speech | 500 | 23.72 | 54.75 | 47.13 | 53.83 |
| sylhet_bangla_speech→noakhali_bangla_speech | 500 | 16.63 | 47.01 | 36.62 | 62.95 |
| **OVERALL** | **10000** | **23.00** | **52.35** | **43.06** | **57.45** |

### Dataset Size: 3500
| Language Pair | N | BLEU | chrF++ | METEOR | TER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| bangla_speech→chittagong_bangla_speech | 500 | 14.18 | 45.81 | 34.28 | 67.67 |
| bangla_speech→mymensingh_bangla_speech | 500 | 40.46 | 67.87 | 63.48 | 37.76 |
| bangla_speech→noakhali_bangla_speech | 500 | 25.42 | 56.07 | 45.88 | 52.43 |
| bangla_speech→sylhet_bangla_speech | 500 | 25.44 | 55.88 | 46.10 | 51.60 |
| chittagong_bangla_speech→bangla_speech | 500 | 22.37 | 53.92 | 46.31 | 54.72 |
| chittagong_bangla_speech→mymensingh_bangla_speech | 500 | 14.76 | 46.45 | 37.90 | 63.76 |
| chittagong_bangla_speech→noakhali_bangla_speech | 500 | 11.79 | 42.18 | 30.43 | 69.01 |
| chittagong_bangla_speech→sylhet_bangla_speech | 500 | 11.80 | 42.14 | 30.58 | 67.74 |
| mymensingh_bangla_speech→bangla_speech | 500 | 55.06 | 76.73 | 71.81 | 29.09 |
| mymensingh_bangla_speech→chittagong_bangla_speech | 500 | 12.32 | 43.53 | 31.60 | 70.22 |
| mymensingh_bangla_speech→noakhali_bangla_speech | 500 | 23.31 | 54.58 | 44.11 | 54.31 |
| mymensingh_bangla_speech→sylhet_bangla_speech | 500 | 21.26 | 52.72 | 42.42 | 56.52 |
| noakhali_bangla_speech→bangla_speech | 500 | 38.37 | 65.45 | 57.69 | 42.14 |
| noakhali_bangla_speech→chittagong_bangla_speech | 500 | 11.81 | 41.74 | 28.97 | 71.22 |
| noakhali_bangla_speech→mymensingh_bangla_speech | 500 | 25.80 | 57.36 | 49.43 | 50.94 |
| noakhali_bangla_speech→sylhet_bangla_speech | 500 | 18.19 | 48.66 | 37.95 | 61.91 |
| sylhet_bangla_speech→bangla_speech | 500 | 40.31 | 66.47 | 59.35 | 40.16 |
| sylhet_bangla_speech→chittagong_bangla_speech | 500 | 11.99 | 42.54 | 31.08 | 70.95 |
| sylhet_bangla_speech→mymensingh_bangla_speech | 500 | 25.11 | 55.87 | 48.48 | 52.81 |
| sylhet_bangla_speech→noakhali_bangla_speech | 500 | 17.96 | 48.62 | 37.69 | 63.48 |
| **OVERALL** | **10000** | **23.99** | **53.23** | **43.78** | **56.51** |

### Dataset Size: 4000
| Language Pair | N | BLEU | chrF++ | METEOR | TER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| bangla_speech→chittagong_bangla_speech | 500 | 16.40 | 47.13 | 35.96 | 65.41 |
| bangla_speech→mymensingh_bangla_speech | 500 | 40.59 | 68.31 | 64.13 | 37.07 |
| bangla_speech→noakhali_bangla_speech | 500 | 27.03 | 56.98 | 47.34 | 51.61 |
| bangla_speech→sylhet_bangla_speech | 500 | 27.56 | 57.33 | 47.28 | 49.94 |
| chittagong_bangla_speech→bangla_speech | 500 | 25.19 | 56.29 | 49.91 | 52.14 |
| chittagong_bangla_speech→mymensingh_bangla_speech | 500 | 16.07 | 47.58 | 39.07 | 62.79 |
| chittagong_bangla_speech→noakhali_bangla_speech | 500 | 12.99 | 43.46 | 32.37 | 67.41 |
| chittagong_bangla_speech→sylhet_bangla_speech | 500 | 13.43 | 43.93 | 33.00 | 65.93 |
| mymensingh_bangla_speech→bangla_speech | 500 | 57.02 | 78.25 | 74.24 | 27.06 |
| mymensingh_bangla_speech→chittagong_bangla_speech | 500 | 13.16 | 44.29 | 33.13 | 70.69 |
| mymensingh_bangla_speech→noakhali_bangla_speech | 500 | 24.92 | 55.85 | 46.55 | 52.52 |
| mymensingh_bangla_speech→sylhet_bangla_speech | 500 | 22.32 | 53.60 | 43.23 | 55.35 |
| noakhali_bangla_speech→bangla_speech | 500 | 40.69 | 67.36 | 60.32 | 39.82 |
| noakhali_bangla_speech→chittagong_bangla_speech | 500 | 13.25 | 43.01 | 30.67 | 70.04 |
| noakhali_bangla_speech→mymensingh_bangla_speech | 500 | 26.43 | 57.72 | 50.42 | 49.99 |
| noakhali_bangla_speech→sylhet_bangla_speech | 500 | 19.08 | 49.30 | 38.32 | 60.40 |
| sylhet_bangla_speech→bangla_speech | 500 | 42.22 | 68.31 | 62.96 | 37.65 |
| sylhet_bangla_speech→chittagong_bangla_speech | 500 | 12.60 | 42.85 | 31.34 | 70.75 |
| sylhet_bangla_speech→mymensingh_bangla_speech | 500 | 25.60 | 56.59 | 50.08 | 51.54 |
| sylhet_bangla_speech→noakhali_bangla_speech | 500 | 19.30 | 49.92 | 40.14 | 59.81 |
| **OVERALL** | **10000** | **25.40** | **54.40** | **45.52** | **54.99** |

### Dataset Size: 4499
| Language Pair | N | BLEU | chrF++ | METEOR | TER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| bangla_speech→chittagong_bangla_speech | 500 | 16.19 | 47.33 | 36.45 | 64.83 |
| bangla_speech→mymensingh_bangla_speech | 500 | 40.32 | 68.14 | 64.20 | 37.00 |
| bangla_speech→noakhali_bangla_speech | 500 | 26.96 | 57.08 | 46.94 | 50.99 |
| bangla_speech→sylhet_bangla_speech | 500 | 27.56 | 57.45 | 48.07 | 49.45 |
| chittagong_bangla_speech→bangla_speech | 500 | 25.31 | 56.45 | 50.11 | 52.85 |
| chittagong_bangla_speech→mymensingh_bangla_speech | 500 | 16.59 | 48.62 | 40.40 | 61.31 |
| chittagong_bangla_speech→noakhali_bangla_speech | 500 | 13.89 | 44.56 | 33.93 | 66.27 |
| chittagong_bangla_speech→sylhet_bangla_speech | 500 | 13.76 | 45.00 | 33.93 | 64.60 |
| mymensingh_bangla_speech→bangla_speech | 500 | 58.38 | 78.70 | 74.91 | 26.51 |
| mymensingh_bangla_speech→chittagong_bangla_speech | 500 | 13.67 | 45.05 | 34.53 | 69.25 |
| mymensingh_bangla_speech→noakhali_bangla_speech | 500 | 25.00 | 56.16 | 46.70 | 52.17 |
| mymensingh_bangla_speech→sylhet_bangla_speech | 500 | 22.70 | 53.78 | 43.98 | 54.61 |
| noakhali_bangla_speech→bangla_speech | 500 | 40.03 | 66.99 | 59.98 | 39.93 |
| noakhali_bangla_speech→chittagong_bangla_speech | 500 | 13.55 | 44.09 | 32.65 | 68.18 |
| noakhali_bangla_speech→mymensingh_bangla_speech | 500 | 26.26 | 58.01 | 50.47 | 49.55 |
| noakhali_bangla_speech→sylhet_bangla_speech | 500 | 18.82 | 50.06 | 38.73 | 59.57 |
| sylhet_bangla_speech→bangla_speech | 500 | 43.20 | 68.81 | 63.04 | 36.81 |
| sylhet_bangla_speech→chittagong_bangla_speech | 500 | 14.15 | 44.16 | 33.02 | 69.07 |
| sylhet_bangla_speech→mymensingh_bangla_speech | 500 | 26.11 | 57.05 | 50.24 | 50.89 |
| sylhet_bangla_speech→noakhali_bangla_speech | 500 | 20.51 | 50.37 | 40.35 | 59.33 |
| **OVERALL** | **10000** | **25.74** | **54.89** | **46.13** | **54.24** |

---

## 4. Dataset Size vs. Performance Analysis (LoRA $r=64$, $\alpha=128$, Epoch 20)

### Dataset Size: 500
| Language Pair | N | BLEU | chrF++ | METEOR | TER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| bangla_speech→chittagong_bangla_speech | 500 | 4.42 | 30.37 | 16.37 | 92.95 |
| bangla_speech→mymensingh_bangla_speech | 500 | 28.87 | 58.42 | 50.63 | 54.50 |
| bangla_speech→noakhali_bangla_speech | 500 | 15.43 | 45.87 | 32.85 | 72.57 |
| bangla_speech→sylhet_bangla_speech | 500 | 14.34 | 44.15 | 32.35 | 72.17 |
| chittagong_bangla_speech→bangla_speech | 500 | 5.78 | 31.31 | 19.86 | 92.98 |
| chittagong_bangla_speech→mymensingh_bangla_speech | 500 | 4.78 | 30.63 | 18.43 | 94.47 |
| chittagong_bangla_speech→noakhali_bangla_speech | 500 | 3.43 | 29.47 | 16.94 | 95.42 |
| chittagong_bangla_speech→sylhet_bangla_speech | 500 | 3.50 | 28.73 | 16.87 | 96.21 |
| mymensingh_bangla_speech→bangla_speech | 500 | 32.46 | 60.12 | 51.30 | 50.18 |
| mymensingh_bangla_speech→chittagong_bangla_speech | 500 | 3.83 | 30.02 | 15.58 | 92.79 |
| mymensingh_bangla_speech→noakhali_bangla_speech | 500 | 14.22 | 45.81 | 32.29 | 71.41 |
| mymensingh_bangla_speech→sylhet_bangla_speech | 500 | 11.80 | 42.19 | 30.08 | 75.85 |
| noakhali_bangla_speech→bangla_speech | 500 | 18.32 | 47.59 | 35.59 | 66.70 |
| noakhali_bangla_speech→chittagong_bangla_speech | 500 | 2.93 | 29.56 | 15.85 | 94.55 |
| noakhali_bangla_speech→mymensingh_bangla_speech | 500 | 15.43 | 46.07 | 34.64 | 70.64 |
| noakhali_bangla_speech→sylhet_bangla_speech | 500 | 8.32 | 36.92 | 23.43 | 82.00 |
| sylhet_bangla_speech→bangla_speech | 500 | 14.27 | 45.67 | 34.91 | 66.65 |
| sylhet_bangla_speech→chittagong_bangla_speech | 500 | 3.54 | 28.39 | 15.06 | 98.47 |
| sylhet_bangla_speech→mymensingh_bangla_speech | 500 | 11.13 | 42.51 | 32.00 | 73.21 |
| sylhet_bangla_speech→noakhali_bangla_speech | 500 | 7.05 | 36.57 | 24.22 | 89.45 |
| **OVERALL** | **10000** | **11.47** | **39.51** | **27.46** | **80.26** |

### Dataset Size: 1000
| Language Pair | N | BLEU | chrF++ | METEOR | TER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| bangla_speech→chittagong_bangla_speech | 500 | 7.24 | 35.96 | 23.65 | 88.54 |
| bangla_speech→mymensingh_bangla_speech | 500 | 34.31 | 63.19 | 56.54 | 42.23 |
| bangla_speech→noakhali_bangla_speech | 500 | 19.74 | 50.33 | 38.73 | 58.72 |
| bangla_speech→sylhet_bangla_speech | 500 | 17.79 | 48.20 | 37.35 | 59.30 |
| chittagong_bangla_speech→bangla_speech | 500 | 14.41 | 45.17 | 36.31 | 66.31 |
| chittagong_bangla_speech→mymensingh_bangla_speech | 500 | 8.71 | 37.99 | 26.36 | 74.90 |
| chittagong_bangla_speech→noakhali_bangla_speech | 500 | 5.33 | 34.44 | 20.81 | 79.54 |
| chittagong_bangla_speech→sylhet_bangla_speech | 500 | 6.18 | 33.88 | 20.87 | 79.62 |
| mymensingh_bangla_speech→bangla_speech | 500 | 46.30 | 71.70 | 66.47 | 34.12 |
| mymensingh_bangla_speech→chittagong_bangla_speech | 500 | 6.99 | 35.69 | 22.82 | 86.72 |
| mymensingh_bangla_speech→noakhali_bangla_speech | 500 | 16.31 | 48.86 | 37.41 | 64.58 |
| mymensingh_bangla_speech→sylhet_bangla_speech | 500 | 14.46 | 45.77 | 34.24 | 65.32 |
| noakhali_bangla_speech→bangla_speech | 500 | 30.96 | 60.31 | 52.30 | 48.43 |
| noakhali_bangla_speech→chittagong_bangla_speech | 500 | 6.38 | 34.48 | 21.19 | 82.66 |
| noakhali_bangla_speech→mymensingh_bangla_speech | 500 | 20.06 | 51.47 | 41.63 | 57.47 |
| noakhali_bangla_speech→sylhet_bangla_speech | 500 | 10.75 | 40.79 | 27.99 | 70.55 |
| sylhet_bangla_speech→bangla_speech | 500 | 31.88 | 59.98 | 52.34 | 47.45 |
| sylhet_bangla_speech→chittagong_bangla_speech | 500 | 6.48 | 34.30 | 21.34 | 85.17 |
| sylhet_bangla_speech→mymensingh_bangla_speech | 500 | 18.04 | 48.79 | 39.19 | 61.36 |
| sylhet_bangla_speech→noakhali_bangla_speech | 500 | 11.25 | 40.89 | 27.95 | 77.84 |
| **OVERALL** | **10000** | **17.13** | **46.10** | **35.28** | **66.66** |

### Dataset Size: 1500
| Language Pair | N | BLEU | chrF++ | METEOR | TER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| bangla_speech→chittagong_bangla_speech | 500 | 10.01 | 40.67 | 28.88 | 75.50 |
| bangla_speech→mymensingh_bangla_speech | 500 | 34.25 | 64.37 | 58.23 | 44.80 |
| bangla_speech→noakhali_bangla_speech | 500 | 21.84 | 52.37 | 41.61 | 56.61 |
| bangla_speech→sylhet_bangla_speech | 500 | 20.55 | 51.35 | 40.60 | 56.50 |
| chittagong_bangla_speech→bangla_speech | 500 | 18.41 | 49.58 | 41.75 | 60.84 |
| chittagong_bangla_speech→mymensingh_bangla_speech | 500 | 11.52 | 41.67 | 31.02 | 69.48 |
| chittagong_bangla_speech→noakhali_bangla_speech | 500 | 8.36 | 37.53 | 25.70 | 77.56 |
| chittagong_bangla_speech→sylhet_bangla_speech | 500 | 7.95 | 37.26 | 25.25 | 76.39 |
| mymensingh_bangla_speech→bangla_speech | 500 | 50.96 | 74.48 | 70.35 | 31.03 |
| mymensingh_bangla_speech→chittagong_bangla_speech | 500 | 9.24 | 39.34 | 27.03 | 77.05 |
| mymensingh_bangla_speech→noakhali_bangla_speech | 500 | 19.36 | 50.75 | 40.15 | 58.63 |
| mymensingh_bangla_speech→sylhet_bangla_speech | 500 | 17.11 | 48.52 | 37.53 | 60.20 |
| noakhali_bangla_speech→bangla_speech | 500 | 34.59 | 63.16 | 55.15 | 44.31 |
| noakhali_bangla_speech→chittagong_bangla_speech | 500 | 8.11 | 37.31 | 24.80 | 78.85 |
| noakhali_bangla_speech→mymensingh_bangla_speech | 500 | 21.48 | 53.43 | 43.73 | 54.78 |
| noakhali_bangla_speech→sylhet_bangla_speech | 500 | 13.20 | 43.98 | 31.92 | 66.91 |
| sylhet_bangla_speech→bangla_speech | 500 | 36.08 | 63.22 | 57.01 | 43.49 |
| sylhet_bangla_speech→chittagong_bangla_speech | 500 | 8.55 | 37.63 | 25.71 | 77.45 |
| sylhet_bangla_speech→mymensingh_bangla_speech | 500 | 19.67 | 51.44 | 42.76 | 60.82 |
| sylhet_bangla_speech→noakhali_bangla_speech | 500 | 13.86 | 44.06 | 33.28 | 69.66 |
| **OVERALL** | **10000** | **19.86** | **49.10** | **39.12** | **62.14** |

### Dataset Size: 2000
| Language Pair | N | BLEU | chrF++ | METEOR | TER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| bangla_speech→chittagong_bangla_speech | 500 | 13.61 | 44.28 | 32.97 | 69.16 |
| bangla_speech→mymensingh_bangla_speech | 500 | 37.79 | 66.19 | 61.34 | 38.92 |
| bangla_speech→noakhali_bangla_speech | 500 | 23.51 | 54.76 | 45.14 | 53.40 |
| bangla_speech→sylhet_bangla_speech | 500 | 23.35 | 54.12 | 43.82 | 53.60 |
| chittagong_bangla_speech→bangla_speech | 500 | 20.93 | 52.45 | 46.17 | 56.24 |
| chittagong_bangla_speech→mymensingh_bangla_speech | 500 | 13.63 | 44.43 | 35.55 | 66.52 |
| chittagong_bangla_speech→noakhali_bangla_speech | 500 | 10.22 | 40.15 | 29.30 | 72.61 |
| chittagong_bangla_speech→sylhet_bangla_speech | 500 | 10.42 | 40.18 | 28.42 | 70.91 |
| mymensingh_bangla_speech→bangla_speech | 500 | 54.41 | 76.91 | 73.40 | 28.29 |
| mymensingh_bangla_speech→chittagong_bangla_speech | 500 | 11.05 | 41.74 | 30.56 | 71.95 |
| mymensingh_bangla_speech→noakhali_bangla_speech | 500 | 20.93 | 53.03 | 43.53 | 55.10 |
| mymensingh_bangla_speech→sylhet_bangla_speech | 500 | 20.48 | 51.44 | 41.10 | 57.13 |
| noakhali_bangla_speech→bangla_speech | 500 | 37.88 | 65.54 | 59.09 | 41.75 |
| noakhali_bangla_speech→chittagong_bangla_speech | 500 | 11.06 | 40.56 | 28.77 | 71.95 |
| noakhali_bangla_speech→mymensingh_bangla_speech | 500 | 23.92 | 55.45 | 46.61 | 52.74 |
| noakhali_bangla_speech→sylhet_bangla_speech | 500 | 15.86 | 46.50 | 34.99 | 64.00 |
| sylhet_bangla_speech→bangla_speech | 500 | 39.00 | 66.35 | 60.75 | 39.29 |
| sylhet_bangla_speech→chittagong_bangla_speech | 500 | 10.64 | 40.41 | 28.85 | 73.37 |
| sylhet_bangla_speech→mymensingh_bangla_speech | 500 | 23.06 | 54.47 | 46.45 | 54.57 |
| sylhet_bangla_speech→noakhali_bangla_speech | 500 | 16.43 | 47.17 | 37.12 | 63.25 |
| **OVERALL** | **10000** | **22.50** | **51.81** | **42.70** | **57.83** |

### Dataset Size: 2500
| Language Pair | N | BLEU | chrF++ | METEOR | TER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| bangla_speech→chittagong_bangla_speech | 500 | 13.46 | 44.88 | 33.07 | 68.20 |
| bangla_speech→mymensingh_bangla_speech | 500 | 39.35 | 67.47 | 63.13 | 37.95 |
| bangla_speech→noakhali_bangla_speech | 500 | 24.54 | 55.14 | 44.76 | 53.98 |
| bangla_speech→sylhet_bangla_speech | 500 | 25.38 | 55.64 | 46.21 | 51.83 |
| chittagong_bangla_speech→bangla_speech | 500 | 21.35 | 52.70 | 44.31 | 56.42 |
| chittagong_bangla_speech→mymensingh_bangla_speech | 500 | 14.83 | 45.44 | 36.61 | 65.18 |
| chittagong_bangla_speech→noakhali_bangla_speech | 500 | 11.98 | 41.91 | 30.23 | 69.55 |
| chittagong_bangla_speech→sylhet_bangla_speech | 500 | 12.02 | 42.23 | 30.30 | 68.73 |
| mymensingh_bangla_speech→bangla_speech | 500 | 53.39 | 75.61 | 70.40 | 30.21 |
| mymensingh_bangla_speech→chittagong_bangla_speech | 500 | 11.34 | 42.73 | 30.23 | 72.00 |
| mymensingh_bangla_speech→noakhali_bangla_speech | 500 | 22.74 | 54.25 | 44.09 | 54.75 |
| mymensingh_bangla_speech→sylhet_bangla_speech | 500 | 21.48 | 52.55 | 42.19 | 56.66 |
| noakhali_bangla_speech→bangla_speech | 500 | 36.61 | 64.69 | 56.09 | 42.89 |
| noakhali_bangla_speech→chittagong_bangla_speech | 500 | 11.47 | 41.33 | 28.86 | 72.46 |
| noakhali_bangla_speech→mymensingh_bangla_speech | 500 | 24.90 | 56.43 | 47.79 | 52.00 |
| noakhali_bangla_speech→sylhet_bangla_speech | 500 | 16.86 | 47.76 | 36.31 | 63.25 |
| sylhet_bangla_speech→bangla_speech | 500 | 37.70 | 65.00 | 57.89 | 41.78 |
| sylhet_bangla_speech→chittagong_bangla_speech | 500 | 10.97 | 41.01 | 28.84 | 74.15 |
| sylhet_bangla_speech→mymensingh_bangla_speech | 500 | 23.86 | 54.95 | 47.95 | 53.72 |
| sylhet_bangla_speech→noakhali_bangla_speech | 500 | 17.61 | 47.97 | 37.10 | 62.14 |
| **OVERALL** | **10000** | **23.15** | **52.48** | **42.82** | **57.48** |

### Dataset Size: 3000
| Language Pair | N | BLEU | chrF++ | METEOR | TER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| bangla_speech→chittagong_bangla_speech | 500 | 15.49 | 47.06 | 36.03 | 66.72 |
| bangla_speech→mymensingh_bangla_speech | 500 | 39.21 | 67.51 | 62.78 | 38.11 |
| bangla_speech→noakhali_bangla_speech | 500 | 27.11 | 57.04 | 47.36 | 50.94 |
| bangla_speech→sylhet_bangla_speech | 500 | 27.23 | 57.23 | 47.09 | 50.17 |
| chittagong_bangla_speech→bangla_speech | 500 | 24.06 | 55.80 | 49.40 | 52.69 |
| chittagong_bangla_speech→mymensingh_bangla_speech | 500 | 15.64 | 47.67 | 39.35 | 62.72 |
| chittagong_bangla_speech→noakhali_bangla_speech | 500 | 13.48 | 44.07 | 33.66 | 66.64 |
| chittagong_bangla_speech→sylhet_bangla_speech | 500 | 12.77 | 43.82 | 33.23 | 66.80 |
| mymensingh_bangla_speech→bangla_speech | 500 | 56.88 | 78.22 | 74.77 | 27.24 |
| mymensingh_bangla_speech→chittagong_bangla_speech | 500 | 13.56 | 45.07 | 34.28 | 68.34 |
| mymensingh_bangla_speech→noakhali_bangla_speech | 500 | 24.32 | 55.26 | 46.08 | 53.15 |
| mymensingh_bangla_speech→sylhet_bangla_speech | 500 | 22.90 | 54.13 | 43.76 | 55.33 |
| noakhali_bangla_speech→bangla_speech | 500 | 39.37 | 66.57 | 60.10 | 41.07 |
| noakhali_bangla_speech→chittagong_bangla_speech | 500 | 13.36 | 43.79 | 32.16 | 68.89 |
| noakhali_bangla_speech→mymensingh_bangla_speech | 500 | 25.90 | 57.43 | 49.47 | 50.45 |
| noakhali_bangla_speech→sylhet_bangla_speech | 500 | 18.23 | 49.52 | 38.52 | 60.74 |
| sylhet_bangla_speech→bangla_speech | 500 | 41.28 | 67.85 | 62.31 | 38.18 |
| sylhet_bangla_speech→chittagong_bangla_speech | 500 | 13.35 | 44.06 | 32.84 | 68.91 |
| sylhet_bangla_speech→mymensingh_bangla_speech | 500 | 25.45 | 56.23 | 49.39 | 52.30 |
| sylhet_bangla_speech→noakhali_bangla_speech | 500 | 19.31 | 50.00 | 40.09 | 60.09 |
| **OVERALL** | **10000** | **25.00** | **54.41** | **45.63** | **55.06** |

### Dataset Size: 3500
| Language Pair | N | BLEU | chrF++ | METEOR | TER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| bangla_speech→chittagong_bangla_speech | 500 | 16.90 | 48.09 | 37.38 | 64.72 |
| bangla_speech→mymensingh_bangla_speech | 500 | 40.63 | 68.47 | 64.50 | 37.21 |
| bangla_speech→noakhali_bangla_speech | 500 | 27.16 | 57.33 | 48.18 | 51.24 |
| bangla_speech→sylhet_bangla_speech | 500 | 28.20 | 57.82 | 48.27 | 50.66 |
| chittagong_bangla_speech→bangla_speech | 500 | 25.03 | 56.62 | 50.08 | 51.69 |
| chittagong_bangla_speech→mymensingh_bangla_speech | 500 | 16.38 | 48.23 | 39.97 | 61.89 |
| chittagong_bangla_speech→noakhali_bangla_speech | 500 | 13.62 | 44.40 | 34.71 | 67.04 |
| chittagong_bangla_speech→sylhet_bangla_speech | 500 | 13.88 | 45.20 | 34.28 | 63.95 |
| mymensingh_bangla_speech→bangla_speech | 500 | 57.21 | 78.36 | 74.45 | 27.22 |
| mymensingh_bangla_speech→chittagong_bangla_speech | 500 | 14.38 | 46.17 | 34.93 | 66.70 |
| mymensingh_bangla_speech→noakhali_bangla_speech | 500 | 24.97 | 56.13 | 47.22 | 52.33 |
| mymensingh_bangla_speech→sylhet_bangla_speech | 500 | 23.08 | 54.52 | 44.78 | 54.86 |
| noakhali_bangla_speech→bangla_speech | 500 | 39.59 | 67.18 | 60.39 | 39.82 |
| noakhali_bangla_speech→chittagong_bangla_speech | 500 | 13.57 | 44.33 | 32.73 | 69.20 |
| noakhali_bangla_speech→mymensingh_bangla_speech | 500 | 26.85 | 58.37 | 50.89 | 49.78 |
| noakhali_bangla_speech→sylhet_bangla_speech | 500 | 19.17 | 50.23 | 38.69 | 59.75 |
| sylhet_bangla_speech→bangla_speech | 500 | 43.56 | 69.41 | 63.93 | 36.20 |
| sylhet_bangla_speech→chittagong_bangla_speech | 500 | 13.82 | 44.73 | 33.83 | 69.25 |
| sylhet_bangla_speech→mymensingh_bangla_speech | 500 | 26.57 | 57.20 | 50.68 | 50.75 |
| sylhet_bangla_speech→noakhali_bangla_speech | 500 | 20.11 | 50.75 | 40.43 | 59.16 |
| **OVERALL** | **10000** | **25.83** | **55.17** | **46.52** | **54.25** |

### Dataset Size: 4000
| Language Pair | N | BLEU | chrF++ | METEOR | TER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| bangla_speech→chittagong_bangla_speech | 500 | 17.20 | 49.01 | 38.16 | 64.81 |
| bangla_speech→mymensingh_bangla_speech | 500 | 41.02 | 68.85 | 65.18 | 36.56 |
| bangla_speech→noakhali_bangla_speech | 500 | 27.43 | 57.53 | 48.17 | 50.85 |
| bangla_speech→sylhet_bangla_speech | 500 | 28.55 | 58.31 | 48.48 | 48.60 |
| chittagong_bangla_speech→bangla_speech | 500 | 26.40 | 57.63 | 51.55 | 50.84 |
| chittagong_bangla_speech→mymensingh_bangla_speech | 500 | 18.25 | 49.78 | 41.95 | 60.04 |
| chittagong_bangla_speech→noakhali_bangla_speech | 500 | 14.70 | 45.56 | 35.52 | 65.23 |
| chittagong_bangla_speech→sylhet_bangla_speech | 500 | 14.84 | 45.88 | 35.85 | 63.48 |
| mymensingh_bangla_speech→bangla_speech | 500 | 58.31 | 79.11 | 75.57 | 26.31 |
| mymensingh_bangla_speech→chittagong_bangla_speech | 500 | 15.11 | 47.06 | 36.40 | 66.27 |
| mymensingh_bangla_speech→noakhali_bangla_speech | 500 | 25.18 | 56.37 | 46.90 | 52.20 |
| mymensingh_bangla_speech→sylhet_bangla_speech | 500 | 23.92 | 55.10 | 45.49 | 54.14 |
| noakhali_bangla_speech→bangla_speech | 500 | 41.39 | 68.02 | 61.45 | 38.66 |
| noakhali_bangla_speech→chittagong_bangla_speech | 500 | 15.05 | 45.47 | 34.08 | 66.36 |
| noakhali_bangla_speech→mymensingh_bangla_speech | 500 | 27.40 | 58.77 | 51.22 | 48.88 |
| noakhali_bangla_speech→sylhet_bangla_speech | 500 | 19.25 | 50.37 | 40.03 | 59.44 |
| sylhet_bangla_speech→bangla_speech | 500 | 43.59 | 69.38 | 63.70 | 36.26 |
| sylhet_bangla_speech→chittagong_bangla_speech | 500 | 14.86 | 45.43 | 34.68 | 67.34 |
| sylhet_bangla_speech→mymensingh_bangla_speech | 500 | 25.77 | 57.63 | 51.64 | 50.57 |
| sylhet_bangla_speech→noakhali_bangla_speech | 500 | 20.11 | 50.63 | 41.03 | 59.70 |
| **OVERALL** | **10000** | **26.50** | **55.79** | **47.35** | **53.41** |

### Dataset Size: 4499
| Language Pair | N | BLEU | chrF++ | METEOR | TER |
| :--- | :--- | :--- | :--- | :--- | :--- |
| bangla_speech→chittagong_bangla_speech | 500 | 17.84 | 49.54 | 39.98 | 62.20 |
| bangla_speech→mymensingh_bangla_speech | 500 | 43.09 | 69.95 | 66.51 | 35.49 |
| bangla_speech→noakhali_bangla_speech | 500 | 28.17 | 58.25 | 48.99 | 49.87 |
| bangla_speech→sylhet_bangla_speech | 500 | 30.01 | 59.38 | 49.80 | 48.28 |
| chittagong_bangla_speech→bangla_speech | 500 | 27.51 | 58.86 | 52.93 | 49.09 |
| chittagong_bangla_speech→mymensingh_bangla_speech | 500 | 18.57 | 50.66 | 43.41 | 59.02 |
| chittagong_bangla_speech→noakhali_bangla_speech | 500 | 15.21 | 46.26 | 36.10 | 64.74 |
| chittagong_bangla_speech→sylhet_bangla_speech | 500 | 15.78 | 47.19 | 37.21 | 61.89 |
| mymensingh_bangla_speech→bangla_speech | 500 | 58.71 | 79.29 | 76.07 | 25.69 |
| mymensingh_bangla_speech→chittagong_bangla_speech | 500 | 16.01 | 47.83 | 38.01 | 64.97 |
| mymensingh_bangla_speech→noakhali_bangla_speech | 500 | 26.13 | 57.14 | 48.46 | 51.10 |
| mymensingh_bangla_speech→sylhet_bangla_speech | 500 | 24.53 | 55.84 | 46.61 | 53.04 |
| noakhali_bangla_speech→bangla_speech | 500 | 42.78 | 68.99 | 62.36 | 37.72 |
| noakhali_bangla_speech→chittagong_bangla_speech | 500 | 15.06 | 45.60 | 34.78 | 68.03 |
| noakhali_bangla_speech→mymensingh_bangla_speech | 500 | 28.99 | 59.66 | 52.69 | 48.00 |
| noakhali_bangla_speech→sylhet_bangla_speech | 500 | 20.13 | 51.61 | 41.19 | 58.52 |
| sylhet_bangla_speech→bangla_speech | 500 | 44.35 | 70.32 | 65.05 | 35.38 |
| sylhet_bangla_speech→chittagong_bangla_speech | 500 | 15.92 | 46.70 | 36.08 | 66.39 |
| sylhet_bangla_speech→mymensingh_bangla_speech | 500 | 28.20 | 59.18 | 53.23 | 48.69 |
| sylhet_bangla_speech→noakhali_bangla_speech | 500 | 22.24 | 52.45 | 43.11 | 56.70 |
| **OVERALL** | **10000** | **27.55** | **56.73** | **48.63** | **52.32** |