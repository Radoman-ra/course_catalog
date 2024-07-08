# Employee Catalog System

## Task Description

The task is to develop an employee catalog using classes.

### Employee

An employee should have the following attributes and functionality:

- **Attributes:**
  - Name
  - Job Title
  - Date of Birth
  - Phone Number
  - Hourly Wage

- **Fields:**
  - `id`
  - `name`
  - `job_title`
  - `description`
  - `phone`
  - `hourly_wage`

- **Functions and Capabilities:**
  - Override `to_string` method to display data in a single line.
  - Data validation.

### Phonebook

The phonebook should have the following functions and capabilities:

- Add an employee to the catalog.
- Remove an employee.
- Update employee attributes by `id`.
- Search for employees by attributes (name, job title, date of birth + sort by hourly wage).
- Display employee details by `id` in the console, showing full information about the employee.

## To Do

- [X] Custom Validator
  - [x] Remove error handler from Employee class.
- [x] Catalog Class
  - [x] Input/Output handling.
  - [x] Validate that non-empty objects are passed.
  - [x] Add a single employee or an array of employees.
  - [x] Static `id` field for Employee.
  - [x] Remove employee by `id`.
  - [x] Update employee by `id`.
  - [x] Retrieve all employees from the catalog.
    - [x] Search for employees by attributes.
      - [x] Name
      - [x] Job Title
      - [x] Date of Birth (born after or within a date range)
      - [x] Sort by Hourly Wage
