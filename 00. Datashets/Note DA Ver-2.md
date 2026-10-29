ROADMAP AKSELERASI: DATA ANALYST TO ML ENGINEER
================================================================
Timeline: Disesuaikan berdasarkan pace aktual (2 minggu = 4 minggu materi)
Kecepatan: 2x dari rencana awal
================================================================

PROGRESS TRACKER
================================================================
[x] Minggu 1: Python Review & File Processing ........... DONE
[x] Minggu 2: NumPy & Vectorized Computations ........... DONE
[x] Minggu 3: Pandas Core (Filtering & Manipulation) .... IN PROGRESS
    - [x] Load CSV dengan encoding handling (utf-8-sig, na_values)
    - [x] Deteksi missing value eksplisit (isnull) & implisit (angka 0, Not rated)
    - [x] Tampilkan baris error dengan .loc filtering
    - [x] Deteksi inkonsistensi teks (Gender 10 variasi, Payment 11 variasi)
    - [x] Standarisasi dengan str.strip().str.lower() + map()
    - [!] BUG: Payment_Method mapping error (key uppercase tapi data sudah lowercase)
    - [ ] Handling invalid data (Age>120, Price<0 -> NaN)
    - [ ] Deteksi outlier (IQR & Z-Score)
    - [ ] Feature engineering teks (split Cuisines, Cuisine_Count)
    - [ ] Export dataset bersih
[ ] Minggu 4: Pandas Advanced (groupby, agg, merge, pivot_table)


================================================================
TAHUN 1: FONDASI DATA ANALYST & APPLIED MACHINE LEARNING
================================================================
Estimasi real: ~12 MINGGU untuk siap apply kerja DA (bukan 24)
Alasan: pace 2x + fokus tanpa PowerBI blocker


BULAN 1 (Minggu 1-4): PYTHON DATA WRANGLING
================================================================
> Fokus: Transisi dari basic Python ke data manipulation tanpa Excel.
> Status: SEDANG BERLANGSUNG

* Minggu 1: Python Review & File Processing [DONE]
  * Target: OOP dasar, List Comprehension, Exception Handling, File I/O (CSV, JSON).
  * Output: Script CLI parsing file log/CSV.
  * Notebook: week1/*.py, trial1.ipynb

* Minggu 2: NumPy & Vectorized Computations [DONE]
  * Target: NumPy Array, Slicing, Broadcasting, Vectorization vs Loop.
  * Output: 5 latihan matrix manipulation & statistika dasar.
  * Notebook: week2/trial2-4.ipynb

* Minggu 3: Pandas Core - Cleaning & Filtering [IN PROGRESS]
  * Target: .loc, .iloc, multi-condition filtering, missing value handling,
    konversi tipe data, standarisasi kategorikal, deteksi outlier.
  * Dataset: Zomato (9.551 baris) + Pakistan E-Commerce Sales (89.984 baris)
  * Notebook: Training.ipynb (latihan mandiri), week3.ipynb (guided), Example.ipynb
  * Catatan:
    - Training.ipynb = latihan mandiri, JANGAN diubah oleh AI
    - week3.ipynb = guided notebook dengan IQR & Z-Score outlier detection
    - Example.ipynb = referensi Zomato cleaning workflow

* Minggu 4: Pandas Advanced (Aggregation & Reshaping)
  * Target: groupby(), agg(), merge(), concat(), pivot_table(), melt().
  * Output: Notebook EDA rangkuman metrik bisnis per segmen/kategori.
  * Dataset: Gunakan sales_cleaned.csv hasil dari Minggu 3.


BULAN 2 (Minggu 5-8): DATABASE & PRODUCTION SQL
================================================================
> Fokus: Tarik data dari database relasional seperti di lingkungan kerja nyata.

* Minggu 5: Setup Database & SQL Fundamentals
  * Target: Setup PostgreSQL lokal (Docker/pgAdmin). SELECT, WHERE, ORDER BY,
    GROUP BY, HAVING, agregasi dasar.
  * Output: Schema database toko retail + populate dummy data.

* Minggu 6: Complex JOINs & Data Integrity
  * Target: INNER, LEFT, RIGHT, FULL OUTER JOIN. Primary Key vs Foreign Key.
    Antisipasi row duplication akibat bad JOIN.
  * Output: 10 soal SQL Easy-Medium di HackerRank / DataLemur.

* Minggu 7: CTE & Subqueries
  * Target: WITH ... AS (CTE), temporary table, query refactoring.
  * Output: Pipeline query analitik laporan bulanan bertingkat (min. 2 CTE chaining).

* Minggu 8: Window Functions
  * Target: ROW_NUMBER(), RANK(), DENSE_RANK(), LAG(), LEAD(),
    SUM() OVER (PARTITION BY ... ORDER BY ...).
  * Output: 5 soal Window Functions di StrataScratch / DataLemur
    (YoY growth, Customer Cohort).


BULAN 3 (Minggu 9-12): EDA, VISUALIZATION & BUSINESS METRICS
================================================================
> Fokus: Menerjemahkan data menjadi grafik dan KPI bisnis.

* Minggu 9: EDA Workflow
  * Target: Univariate analysis (distribusi, skewness), Bivariate analysis
    (korelasi, boxplot), outlier detection (IQR & Z-score).
  * Output: Template notebook standar sanity-check dataset baru.

* Minggu 10: Visualization (Seaborn & Plotly)
  * Target: Distribution plots, Heatmaps, Scatter matrices, Pairplots,
    Interactive Plotly charts.
  * Output: Laporan visualisasi interaktif 1 halaman HTML.

* Minggu 11: Business Metrics & KPI Framework
  * Target: CAC, LTV, Churn Rate, Retention Rate, AOV, MoM Growth.
  * Output: Script Python cohort retention table dari data transaksi.

* Minggu 12: End-to-End DA Mini Project
  * Target: SQL + Pandas + Plotly. Tarik data PostgreSQL, olah, visualisasikan.
  * Output: PROJECT 1 di GitHub - Customer Retention & Revenue Diagnostic Report.
  *** CHECKPOINT: SIAP APPLY KERJA DATA ANALYST ***


BULAN 4 (Minggu 13-16): STATISTIKA INFERENSIAL & A/B TESTING
================================================================
> Fokus: Memastikan temuan data valid secara statistik.

* Minggu 13: Probabilitas & Distribusi Data
  * Target: Central Limit Theorem, Normal Distribution, Skewed Distributions,
    Log Transformation.
  * Output: Simulasi sampling distribusi menggunakan scipy.stats.

* Minggu 14: Hypothesis Testing
  * Target: Z-Test, Independent & Paired T-Test, ANOVA, uji asumsi
    (Shapiro-Wilk, Levene's).
  * Output: Pengujian signifikansi perbedaan performa 2 grup marketing.

* Minggu 15: Chi-Square & Korelasi
  * Target: Chi-Square Test of Independence, Pearson vs Spearman Correlation.
  * Output: Analisis hubungan antar variabel kategorik pada dataset churn.

* Minggu 16: A/B Testing Design & Analysis
  * Target: Sample Size, Statistical Power, MDE, p-value interpretation,
    Type I vs Type II Error.
  * Output: Notebook lengkap analisis A/B Test landing page.


BULAN 5 (Minggu 17-20): REGRESI & DASAR ML
================================================================
> Fokus: Transisi dari analisis deskriptif ke pemodelan prediktif.

* Minggu 17: Linear Regression
  * Target: Simple & Multiple Linear Regression, OLS, R-Squared, Residual analysis.
  * Output: Model regresi harga rumah (statsmodels).

* Minggu 18: Scikit-Learn Workflow
  * Target: train_test_split, StandardScaler, MinMaxScaler, fit-transform,
    metrik regresi (MAE, MSE, RMSE).
  * Output: Pipeline regresi pertama Scikit-Learn.

* Minggu 19: Logistic Regression (Klasifikasi)
  * Target: Sigmoid, Decision boundary, Confusion Matrix, Precision, Recall,
    F1-Score, ROC-AUC.
  * Output: Model prediksi Customer Churn (Binary Classification).

* Minggu 20: Overfitting & Regularization
  * Target: Bias-Variance Tradeoff, Cross-Validation, Ridge (L2) vs Lasso (L1).
  * Output: Eksperimen efek Ridge/Lasso terhadap koefisien model.


BULAN 6 (Minggu 21-24): TREE-BASED MODELS & PORTFOLIO
================================================================
> Fokus: Algoritma ML tabular paling dominan.

* Minggu 21: Decision Trees & Random Forest
  * Target: Gini Impurity, Entropy, Information Gain, Bagging, Feature Importance.
  * Output: Model Random Forest klasifikasi kredit/risiko nasabah.

* Minggu 22: Gradient Boosting (XGBoost / LightGBM)
  * Target: Boosting vs Bagging, XGBoost/LightGBM, Hyperparameter tuning
    (GridSearchCV, Optuna).
  * Output: Optimasi model klasifikasi dengan XGBoost.

* Minggu 23: Interpretasi Model (SHAP & LIME)
  * Target: SHAP values (Global summary & Local waterfall plot).
  * Output: Visualisasi SHAP pada model klasifikasi.

* Minggu 24: Portfolio Showcase
  * Target: Rapikan GitHub, README format Context -> Problem -> Method -> Impact.
  * Output: Portfolio DA/Junior ML: GitHub repo komprehensif.
  *** MILESTONE 1: DATA ANALYST PROFESIONAL + ML FOUNDATIONS ***


================================================================
TAHUN 1 LANJUTAN (Bulan 7-12): ENGINEERING & DEPLOYMENT
================================================================

BULAN 7 (Minggu 25-28): MATHEMATICS FOR ML & UNSUPERVISED
  * Linear Algebra, Kalkulus & Optimization
  * Clustering (K-Means, DBSCAN), PCA

BULAN 8 (Minggu 29-32): ADVANCED FEATURE ENGINEERING & PIPELINE
  * Imbalanced Data (SMOTE), Feature Engineering Lanjutan
  * Scikit-Learn Pipeline, Model Serialisasi (joblib)

BULAN 9 (Minggu 33-36): VERSION CONTROL & CODE QUALITY
  * Git workflow profesional, Virtual Environments
  * Code Quality (ruff, black, type hints), pytest

BULAN 10 (Minggu 37-40): BACKEND API (FastAPI)
  * REST API, Pydantic validation, Model serving endpoint
  * Batch inference & logging

BULAN 11 (Minggu 41-44): DOCKER
  * Dockerfile, Containerizing ML App
  * Docker Compose, Debugging containers

BULAN 12 (Minggu 45-48): DEPLOYMENT & EVALUASI TAHUN 1
  * Cloud deployment (Render/Railway)
  * Streamlit UI, Load testing
  * PROJECT 2: Deployed ML App (live demo + GitHub)


================================================================
TAHUN 2 (Bulan 13-24): MACHINE LEARNING ENGINEERING & MLOps
================================================================

BULAN 13 (Minggu 49-52): DEEP LEARNING (PyTorch)
  * Tensors & Autograd, MLP, Training Loop, Regularization

BULAN 14 (Minggu 53-56): NLP / COMPUTER VISION (Pilih Satu)
  * Text Processing & Embeddings, Transformer Architecture
  * Hugging Face Ecosystem, Fine-Tuning

BULAN 15 (Minggu 57-60): EXPERIMENT TRACKING
  * MLflow (Tracking & Model Registry), Weights & Biases

BULAN 16 (Minggu 61-64): DATA VERSIONING
  * DVC (Data Version Control), DVC Pipelines
  * Data Validation (Great Expectations / Pandera)

BULAN 17 (Minggu 65-68): CI/CD FOR ML
  * GitHub Actions, Automated Model Evaluation Gate
  * Continuous Deployment pattern

BULAN 18 (Minggu 69-72): HIGH-PERFORMANCE SERVING
  * ONNX Runtime, Async task processing
  * Dedicated serving engines, Redis caching

BULAN 19 (Minggu 73-76): PRODUCTION MONITORING
  * Data Drift vs Concept Drift, Evidently AI
  * Prometheus & Grafana, Alerting & Retraining strategy

BULAN 20 (Minggu 77-80): CLOUD (AWS / GCP)
  * IAM, S3/GCS, EC2/Compute Engine
  * SageMaker/Vertex AI, BigQuery, Cost management

BULAN 21 (Minggu 81-84): LLM & AI AGENTS
  * LLM APIs & Structured Outputs, RAG Architecture
  * RAG Evaluation, AI Agents & Tools Integration

BULAN 22 (Minggu 85-88): CAPSTONE - PLANNING
  * Problem & Data sourcing, Pipeline & Versioning
  * Model Development & Experiment Tracking, Architecture review

BULAN 23 (Minggu 89-92): CAPSTONE - DEPLOYMENT
  * Production Serving, CI/CD Pipeline
  * Monitoring & Drift, Full Integration Test

BULAN 24 (Minggu 93-96): FINAL SHOWCASE & INTERVIEW PREP
  * GitHub repo berstandar industri, Technical writing/blog
  * Resume alignment, Mock interview & System Design practice
  *** TARGET AKHIR: ML ENGINEER JUNIOR-TO-MID LEVEL ***


================================================================
CATATAN PENTING
================================================================

1. BUG DI Training.ipynb (Minggu 3):
   Payment_Method mapping error. Data sudah di-lowercase tapi dictionary key
   masih uppercase ('COD', 'CASH ON DELIVERY', 'Wallet'). Juga 'bank tf'
   salah, harusnya 'bank transfer'. Akibatnya 42.367 baris jadi NaN
   (harusnya hanya ~5.959). FIX SENDIRI sebagai latihan.

2. City mapping di Training.ipynb juga menambah NaN dari 2.205 jadi 4.919
   karena 'abbottabad' tidak ada di dictionary. Tambahkan sendiri.

3. Profit Margin negatif (285 baris) BUKAN invalid data. Itu rugi beneran
   (promo besar, return, dll). Jangan diubah ke NaN.

4. File reference:
   - D:\Data Analyst\Python\Training.ipynb -> Latihan mandiri, JANGAN diubah AI
   - D:\Data Analyst\Python\week3.ipynb -> Guided notebook (IQR, Z-Score)
   - D:\Data Analyst\Python\Example.ipynb -> Referensi Zomato cleaning
   - D:\Data Analyst\Python\Matrix.md -> File ini (roadmap & tracker)
