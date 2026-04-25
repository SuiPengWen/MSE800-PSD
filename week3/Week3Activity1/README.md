# Week 3 Activity 1: Database Design - Student & Course System

## Overview
This ER diagram models a student course enrollment system. It defines the core entities, their attributes, and the relationships between them.

## Entities
1. **Student**
   - Attributes: `student_id(PK)`, `name`, `email`
   - `student_id` is the primary key, uniquely identifying each student.

2. **Course**
   - Attributes: `course_id(PK)`, `course_name`
   - `course_id` is the primary key, uniquely identifying each course.

## Relationships
- **Enroll (Many-to-Many)**
  - A student can enroll in multiple courses (M).
  - A course can have multiple enrolled students (N).
  - The relationship `Enroll` has an attribute `Grade`, which stores the student's final mark for the course.

## Purpose
This design will form the basis for creating the corresponding database tables, including foreign keys to implement the relationships.