
---

## 🛩️ Aviator 4x Prediction Bot (Image-Based)

This project is a web-based Aviator predictor that analyzes screenshots of crash game multipliers and predicts the chance of hitting a **4x+ multiplier**. Built with **Flask**, **OCR (pytesseract)**, and **Matplotlib**, it features a clean UI for image upload and visual feedback.

---

### 🔍 Features

* 📤 Upload a screenshot of Aviator crash multipliers
* 🔎 OCR (Optical Character Recognition) extracts values like `1.2x`, `2.3x`, `5.1x`
* 📈 Generates a live graph of recent crashes
* 🔮 Predicts if a high multiplier (4x+) is likely soon
* 🖼️ Displays uploaded image and multipliers clearly
* ⚙️ Designed to deploy on **Vercel** (via `@vercel/python` runtime)

---

### 🧠 Prediction Logic

The app uses a rule-based logic to estimate the likelihood of a 4x multiplier:

* If 6+ low multipliers occurred since last 4x → High chance
* Else → Wait or monitor closely

> You can upgrade it to ML-based models later.

---

### 🛠️ Tech Stack

* Python 3
* Flask
* pytesseract (OCR)
* matplotlib
* HTML/CSS
* Hosted on Vercel (serverless Python)

---

### 🚀 Deployment

This project is ready for **1-click deployment** on Vercel.

1. Clone this repo
2. Upload to GitHub
3. Go to [https://vercel.com/import](https://vercel.com/import)
4. Connect repo and deploy

---

### 📷 Screenshot Preview

> *(Include a screenshot of the UI here if you want)*

---

### 📂 Project Structure

```
.
├── app.py
├── api/
│   └── index.py
├── templates/
│   └── index.html
├── static/
│   └── uploads/
├── vercel.json
├── requirements.txt
```

---

### 📌 Credits

Built with ❤️ by \[Abhi] — powered by Flask + Vercel + AI.

---

