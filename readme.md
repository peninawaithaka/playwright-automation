# Test Automation Framework

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green)
![Behave](https://img.shields.io/badge/Behave-BDD-00ADD8?logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Framework-0A9EDC?logo=pytest&logoColor=white)

---

## Overview

A Python-based test automation framework demonstrating **UI, API, and CI testing** within a single project.

The framework is designed with a clear separation of concerns and follows **real-world automation patterns** to ensure scalability, maintainability, and cross-browser support.

---

## Tech Stack

- **Language:** Python 3.10  
- **UI Testing:** Playwright  
- **BDD Framework:** Behave  
- **API Testing:** Pytest  
- **Reporting:** Allure  
- **CI/CD:** GitHub Actions  

---
## Project Structure

```
playwright-automation/
│
├── .github/
│ └── workflows/
│ └── ci.yml
│
├── api-testing/
│
├── config/
│ ├── browser.py
│ └── config.json
│
├── features/
│ ├── login/
│ ├── product/
│ ├── steps/
│ ├── views/
│ └── environment.py
│
├── reports/
│ ├── screenshots/
│ └── allure-results/
│
├── .gitignore
├── requirements.txt
└── README.md
```
