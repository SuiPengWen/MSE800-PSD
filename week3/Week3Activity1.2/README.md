# Week 3 Activity 1.2: Updated ER Diagram - Student & Course System

## Overview
This ER diagram models a student course enrollment system, extended with a new `Lecturer` entity as required in the activity.

## Entities
### 1. Student
Represents a student enrolled in the system.
- Attributes:
  - `student_id(PK)`: Unique identifier for each student (Primary Key)
  - `name`: Student's full name
  - `email`: Student's contact email

### 2. Course
Represents a course offered in the program.
- Attributes:
  - `course_id(PK)`: Unique identifier for each course (Primary Key)
  - `course_name`: Name of the course
  - `lecturer_id(FK)`: Foreign key referencing the lecturer teaching this course

### 3. Lecturer (New Entity)
Represents an academic staff member teaching courses.
- Attributes:
  - `lecturer_id(PK)`: Unique identifier for each lecturer (Primary Key)
  - `name`: Lecturer's full name
  - `email`: Lecturer's work email
  - `department`: The academic department the lecturer belongs to
  - `office_number`: The lecturer's office location

## Relationships
### 1. Enroll (Many-to-Many)
- Connects `Student` and `Course`
- Cardinality: N:M (A student can enroll in multiple courses; a course can have multiple students)
- Relationship attribute:
  - `Grade`: Stores the student's final mark for the course

### 2. Teach (One-to-Many)
- Connects `Lecturer` and `Course`
- Cardinality: 1:M (One lecturer can teach multiple courses; a course has one lecturer)
- Implemented via `lecturer_id(FK)` in the `Course` entity, referencing `Lecturer.lecturer_id(PK)`

## Purpose
This ER diagram forms the basis for creating the corresponding database tables, including foreign key constraints to enforce relationships between entities.