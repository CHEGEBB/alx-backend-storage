# Project Title: Redis Basic

## Description
This project focuses on utilizing Redis for basic operations and implementing a simple cache system. You'll learn how to interact with Redis, store data, retrieve it efficiently, and implement decorators to enhance functionality.

## Table of Contents
- [Curriculum](#curriculum)
- [Resources](#resources)
- [Tasks](#tasks)
  - [0. Writing strings to Redis](#0-writing-strings-to-redis)
  - [1. Reading from Redis and recovering original type](#1-reading-from-redis-and-recovering-original-type)
  - [2. Incrementing values](#2-incrementing-values)
  - [3. Storing lists](#3-storing-lists)
  - [4. Retrieving lists](#4-retrieving-lists)
  - [5. Implementing an expiring web cache and tracker](#5-implementing-an-expiring-web-cache-and-tracker)


## Resources
- Redis Crash Course Tutorial
- Redis commands
- Redis python client
- How to Use Redis With Python

## Tasks

### 0. Writing strings to Redis
- **Domain**: Back-end
- **Weight**: 1
- **Project Duration**: Jun 19, 2024, 6:00 AM to Jun 20, 2024, 6:00 AM
- **Checker Release**: Jun 19, 2024, 12:00 PM
- **Auto Review**: Launched at the deadline
- **Description**: Implement a Cache class to perform basic Redis operations and utilize it to store data.

### 1. Reading from Redis and recovering original type
- **Domain**: Back-end
- **Description**: Develop methods to read data from Redis and recover the original type, along with implementing additional helper methods for string and integer conversions.

### 2. Incrementing values
- **Domain**: Back-end
- **Description**: Implement a decorator to count method calls and increment values in Redis, enhancing the functionality of the Cache class.

### 3. Storing lists
- **Domain**: Back-end
- **Description**: Implement a decorator to store the history of inputs and outputs for a specific function using Redis lists, expanding the capabilities of the Cache class.

### 4. Retrieving lists
- **Domain**: Back-end
- **Description**: Develop a function to retrieve and display the history of function calls from Redis, providing insights into the usage of specific methods in the Cache class.

### 5. Implementing an expiring web cache and tracker
- **Domain**: Back-end
- **Description**: Create a function to retrieve HTML content from URLs, tracking access counts and implementing an expiring cache system using Redis to improve performance.

Copyright © 2024 ALX, All rights reserved.