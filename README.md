# Selenium Python Hybrid Framework

A robust and scalable hybrid framework built with Selenium and Python for automating software tests. This framework uses the Page Object Model (POM) combined with data-driven and keyword-driven testing approaches to ensure efficiency, reusability, and maintainability. Designed specifically to automate tests for the nopCommerce website.

## Features

- **Page Object Model (POM):** Simplifies test case maintenance by abstracting UI elements.
- **Data-Driven Testing:** Supports external data sources (e.g., CSV, Excel) for flexible test data.
- **Keyword-Driven Testing:** Easily extendable for non-programmers to contribute test cases.
- **Detailed Reporting:** Includes logging and test result reports for analysis.
- **Modular and Reusable Components:** Ensures scalability and reduces code duplication.

## Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/alamarnissi/python-selenium-automation-framework.git
   cd python-selenium-automation-framework
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Download ChromeDriver:

   - Find the version matching your Chrome browser from [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/).
   - Place the `chromedriver` executable in the root directory of the project.

5. Configure Test Data and Parameters: 
   - Update the test data in the testData directory and modify configurations in config.ini if needed.

## Project Structure

```plaintext
python-selenium-automation-framework/
|-- Logs/                     # Stores execution logs
|-- pageObjects/              # Page Object Model classes
|-- TestData/                 # Test data files (e.g., Excel)
|-- testCases/                # Test scripts
|-- utilities/                # Utility functions (e.g., logger, config loader)
|-- Reports/                  # Test result reports
|-- Configurations/           # Framework configuration file
|-- requirements.txt          # Python dependencies
|-- README.md                 # Project documentation
```

## Running Tests Locally

1. Navigate to the root directory of the project.

2. Basic Test Execution:

   ```bash
   pytest -v -s testCases/testLogin.py --browser=chrome
   ```
This will:
   - Run the `testLogin` test case using Chrome.

3. Parallel Execution with HTML Reporting:

Use the following command for parallel test execution with a detailed HTML report:
   ```bash
   pytest -v -s -n=2 --html=Reports\report.html testCases/testLogin.py --browser=chrome
   ```
**Explanation of Command:**
   - `pytest`: Executes tests using Pytest.
   - `-v`: Enables verbose output.
   - `-s`: Displays console outputs during the test.
   - `-n=2`: Executes tests in parallel across 2 threads using the `pytest-xdist` package.
   - `--html=Reports\report.html`: Generates a detailed HTML report in the Reports directory.
   - `testCases/testLogin.py`: Specifies the test file to execute.
   - `--browser=chrome`: Specifies the browser to use for test execution. Modify to `firefox`, `edge`, etc., as needed.

3. View the generated HTML report located in the `reports/` folder.

## Writing New Tests

1. Create a new Page Object Model class in the `pageObjects/` directory for the desired page.

2. Add test data in the `TestData/` directory as needed.

3. Write your test scripts in the `testCases/` directory, following the existing test patterns.

## Dependencies

This framework uses the following Python packages:

   - `selenium==4.27.1`: For browser automation.
   - `pytest==8.3.4`: For running test cases.
   - `pytest-html==4.1.1`: For generating detailed HTML test reports.
   - `pytest-xdist==3.6.1`: For parallel test execution.
   - `openpyxl==3.1.5`: For working with Excel files (test data).
   - `allure-pytest==2.13.5`: For generating Allure reports.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Happy Testing!
