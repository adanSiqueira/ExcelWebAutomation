<h1 align="center">System Inclusion Automator</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
  <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white">
  <img src="https://img.shields.io/badge/OpenPyXL-FFD43B?style=for-the-badge&logo=python&logoColor=green">
  <img src="https://img.shields.io/badge/Tkinter-FF6600?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/CustomTkinter-2C2D72?style=for-the-badge&logo=python&logoColor=white">
</p>

This project automates the inclusion of product data into a web system using **Selenium** for browser automation, **OpenPyXL** for reading Excel files, and **CustomTkinter** for providing a simple and modern GUI interface.  
It is designed to speed up repetitive tasks by reading structured data from Excel and automatically filling out online forms without manual typing.

> 📂 The program allows the user to load an Excel file via a graphical interface, map the required fields, and automatically send the data to the target system.  
> 💡 Built for ease of use, it requires no coding skills to operate.

---

## 🔍 Project Overview

The application is composed of:

### 1. **Graphical Interface**
- Developed using **CustomTkinter**
- Dark mode design
- Allows the user to select the Excel file containing product data
- Displays the chosen file path in the interface

### 2. **Automation Core**
- **Selenium WebDriver** handles browser automation
- Automatically locates and interacts with HTML elements on the web system:
  - Text inputs (`<input>` and `<textarea>`)
  - Buttons (by text, CSS, or XPath selectors)
- Supports hidden (headless) browser execution for background automation

### 3. **Excel Data Reading**
- **OpenPyXL** loads the spreadsheet
- Reads each row and maps it to the form fields in the system

---

## 🛠️ Technologies Used

- **Python** – Core programming language  
- **Selenium** – Web browser automation  
- **OpenPyXL** – Excel file reading  
- **CustomTkinter** – Modern and customizable GUI  
- **Tkinter** – Standard Python GUI library  
- **cx_Freeze** – Packaging into an executable file for Windows  

---
