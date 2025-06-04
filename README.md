# SauceDemo UI Test Suite

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd saucedemo_tests
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## How to Run Tests
```bash
pytest
```

This will:
- Run all tests
- Generate `report.html`
- Use multiple CPUs via `pytest-xdist`

## Assumptions
- Tests run using standard user credentials
- Chrome is installed and available in PATH
- Page load times are stable; explicit waits may be added for real-world scenarios
