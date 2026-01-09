# 🛒 Ecommerce Automation Framework

An end-to-end **Selenium + Pytest automation framework** built using **Python**, following the **Page Object Model (POM)** design pattern.  
This project automates core e-commerce workflows such as **login, product selection, cart, checkout, and order confirmation**.

---

## 🚀 Tech Stack

- **Language:** Python 3  
- **Automation Tool:** Selenium WebDriver  
- **Test Framework:** Pytest  
- **Design Pattern:** Page Object Model (POM)  
- **Reporting:** pytest-html  
- **Test Data:** JSON-based parameterization  
- **Browser Support:** Chrome, Firefox  
- **Version Control:** Git & GitHub  

---

## 📂 Project Structure

## 📂 Project Structure

```text
ecommerce-automation-framework/
│
├── pageObjects/
│   ├── loginPage.py
│   ├── shopPage.py
│   └── checkoutPage.py
│
├── tests/
│   ├── test_login.py
│   └── test_e2e_checkout.py
│
├── testData/
│   └── checkoutData.json
│
├── utilities/
│   └── baseClass.py
│
├── reports/
│   ├── report.html
│   └── screenshots/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore

```
---

## 🧪 Test Coverage

- ✅ Login validation (positive & negative)
- ✅ Product selection
- ✅ Add to cart
- ✅ Checkout flow
- ✅ Country selection
- ✅ Order confirmation
- ✅ JSON-based parameterized tests
- ✅ Screenshot capture on failure

---

## 🏃 How to Run the Tests

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

2️⃣ Run all tests
```
pytest
```

3️⃣ Run smoke tests
```
pytest -m smoke
```

4️⃣ Run regression tests
```
pytest -m regression
```

5️⃣ Run tests in parallel
```
pytest -n 2
```

6️⃣ Generate HTML report
```
pytest --html=reports/report.html
```

📊 Reports & Screenshots
- HTML reports generated using pytest-html

- Screenshots are automatically captured when a test fails

- Reports and screenshots are stored in the reports/ directory

🧠 Key Framework Features
- Page Object Model for better maintainability

- Explicit waits for stable execution

- JSON-based data-driven testing

- Cross-browser support

- Clean Git setup with .gitignore

- Scalable and CI-ready framework

👩‍💻 Author
Anuja Shejwal
QA Automation Engineer

🔗 GitHub: https://github.com/anujashejwal

⭐ Future Enhancements
- GitHub Actions CI integration

- Allure reporting

- Docker-based execution

- API + UI hybrid automation

---

