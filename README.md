# Employee_salary APIs

Employee Salary Service (FastAPI + TDD)

A backend service to manage employees and compute salary-related information.
Built using FastAPI, SQLite, and SQLAlchemy, following a strict Test-Driven Development (TDD) workflow.

✨ Features
1. Employee CRUD

Create, read, update, and delete employees

Fields:

Full name

Job title

Country

Salary

Data persisted in SQLite

2. Salary Calculation

Calculate deductions and net salary for a given employee.

Deduction Rules

Country	Deduction
India	10% TDS
United States	12% TDS
Others	No deduction
3. Salary Metrics

Salary min / max / average by country

Average salary by job title

Handles edge cases (no employees, empty results)

🧱 Tech Stack

Python 3.10+ (tested on 3.11/3.12)

FastAPI

SQLAlchemy

SQLite

Pytest

HTTPX
