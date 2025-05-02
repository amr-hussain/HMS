# Hospital Management System

A simple and customizable Hospital Management System built as an Odoo module.

## 📦 Module Info

- **Name:** Hospital Management System
- **Author:** Amr
- **Version:** 1.0
- **Category:** Apps
- **Odoo Version:** Odoo 18
- **License:** Open Source MIT license

## 📋 Description

This module provides basic hospital management functionality, allowing you to manage:

- Patients
- Doctors
- Departments
- Patient Reports

It's ideal for small clinics or as a base for a more comprehensive healthcare system.

## ⚙️ Features

- Manage patient records with medical info.
- Assign patients to departments and doctors.
- Generate PDF reports for patients.
- ![odoo_repo](https://github.com/user-attachments/assets/e4e7e3f2-c32a-4379-b36c-0e6f278f998c)
- Role-based access control via security rules.
- Clean and modular architecture following Odoo best practices.

## 📁 Module Structure

```plaintext
hospital_management/
├── models/
│   ├── __init__.py
│   ├── hms_patient.py
│   ├── hms_doctor.py
│   └── hms_department.py
├── views/
│   ├── root_menus.xml
│   ├── hms_patient_views.xml
│   ├── hms_doctor_views.xml
│   └── hms_department_views.xml
├── reports/
│   └── patient_report.xml
├── security/
│   ├── hms_security.xml
│   └── ir.model.access.csv
├── __manifest__.py
└── README.md
