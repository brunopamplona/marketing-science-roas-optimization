# 📊 Marketing Science Case: ROAS Optimization & Creative Analytics

## 📌 Overview
This project demonstrates how data science and machine learning can be applied to optimize paid media performance across platforms and creatives.

The goal is to move beyond descriptive analytics and extract **actionable insights for budget allocation, audience strategy, and creative optimization**.

---

## 🎯 Business Questions

### 1. Multi-Platform Performance
- Which factors are most predictive of success?
  - Platform
  - Audience
  - Creative format

- Which platform delivers the highest ROAS?
- What are the most profitable combinations of objective + audience?

---

### 2. Creative Performance
- Which creative formats drive higher returns?
- What type of messaging generates more conversions?
- What features most influence engagement?

---

## 🧠 Methodology

### Data Analysis
- Aggregations (ROAS, CPA by platform)
- Strategy ranking (revenue and efficiency)

### Machine Learning
- Model: Random Forest Regressor

### Targets:
- ROAS prediction
- Engagement Score prediction

### Feature Importance
Used to identify key drivers of performance:
- Platform vs Audience vs Creative
- Headline, CTA, visual elements

---

## 📈 Key Insights

### Paid Media
- Platform is the strongest predictor of performance (~43%)
- Google Ads delivers ~2x higher ROAS with lower CPA
- Retargeting is the most profitable strategy

### Creative Strategy
- UGC videos and short-form content outperform static formats
- Urgency-based headlines drive the highest conversions
- Engagement is driven by a balanced mix of:
  - CTA (~20%)
  - Headline (~20%)
  - Creative type (~19%)

---

## 🚀 Business Implications

- Budget should be concentrated on high-ROAS platforms
- Retargeting should be prioritized as a core growth lever
- Creative strategy should focus on:
  - Short-form video
  - Human presence (faces)
  - Strong CTA + urgency messaging

---

## ⚠️ Limitations

- Results are based on observational data (no causal inference)
- No incrementality testing (A/B or geo experiments)
- Does not account for diminishing returns or saturation

---

## 🔮 Next Steps

- Run incrementality experiments (iROAS / iCAC)
- Build Marketing Mix Models (MMM)
- Introduce creative scoring using NLP & Computer Vision
- Optimize budget allocation using marginal ROAS curves

---

## 🛠️ Tech Stack

- Python 3.11
- Pandas
- Scikit-learn

---
## 📁 Project Structure

```
├── data/
│   ├── campanhas_multiplatforma.csv
│   └── analise_criativos.csv
├── notebooks/
│   ├── multiplatform_analysis.ipynb
│   └── creative_analysis.ipynb
├── src/
│   ├── modeling.py
│   └── preprocessing.py
└── outputs/
    └── readouts/
        └── recomendacoes_estrategicas_otimizacao_roas.pptx
```
---

## 💡 Key Takeaway

Performance marketing is not only about *where* you advertise, but also *who* you target and *how* you communicate.

This project shows how combining data analysis with machine learning can unlock better decisions across the entire funnel.
