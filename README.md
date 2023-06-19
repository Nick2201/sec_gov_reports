# SEC Gov Reports: Company Repositories Classification

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4.0%2B-red)
![Pandas](https://img.shields.io/badge/Pandas-1.3.0%2B-orange)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-yellow)

This Python project, **SEC Gov Reports**, is an extension of the previous project, "International Company Trading Data Extraction." It allows you to retrieve companies' repositories from the SEC.gov website and classify them into selected categories such as sector, industry, and more. The project utilizes various technical skills, including SQLAlchemy, Pandas, Selenium, and Power BI, to provide a comprehensive solution.

## Features

- Retrieve company repositories from the SEC.gov website.
- Classify the repositories based on selected categories such as sector and industry.
- Utilize SQLAlchemy for efficient database management.
- Analyze and process data using Pandas.
- Automate website interaction using Selenium.
- [ ] Visualize and present data using Power BI.

## Prerequisites

- Python 3.8 or higher
- SQLAlchemy 1.4.0 or higher
- Pandas 1.3.0 or higher
- Selenium 4.0 or higher
- [ ] Power BI (for data visualization)

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/sec-gov-reports.git
```

2. Navigate to the project directory:

```bash
cd sec-gov-reports
```

3. Install the dependencies using [Poetry](https://python-poetry.org/):

```bash
poetry install
```

## Usage

1. Set up your database connection by modifying the `config.py` file.
2. Customize the selected categories for classification in the `classify.py` file.
3. Run the classification script:

```bash
poetry run python classify.py
```

4. The script will retrieve company repositories from the SEC.gov website, classify them based on the selected categories, and store the results in the database.

## Configuration

The project uses the [Poetry](https://python-poetry.org/) dependency manager and build tool. The project configuration can be found in the `pyproject.toml` file.

The database connection and other configuration settings can be modified in the `config.py` file.

## WATCH RAW TABLE of accumulative REPORTS
![image](https://github.com/Nick2201/sec_gov_reports/assets/71185932/3ad7b029-84de-4061-858c-42d5c5044359)

## IN PROGRESS ...
### Power BI Integration

To leverage Power BI for data visualization, follow these steps:

1. Export the classified data from the database into a format compatible with Power BI (postgresql).
2. Open Power BI and connect to the exported data.
3. Create visualizations, reports, and dashboards based on your requirements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or a pull request in the [repository](https://github.com/your-username/sec-gov-reports).

## Acknowledgements

This project was developed to enhance the functionality of the previous project, "International Company Trading Data Extraction," by retrieving company repositories from the SEC.gov website and classifying them into selected categories.

## Contact

For any questions or inquiries, please contact [your-email@example.com](mailto:your-email@example.com).

Enjoy classifying and analyzing company repositories with SEC Gov Reports!
