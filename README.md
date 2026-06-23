# Cab Booking System

A command-line Cab Booking System built with Python. The project supports customer, driver, and admin roles with ride booking, driver management, fare calculation, and JSON-based data storage.

## Features

### Admin

* Register and login
* View all customers
* View all drivers
* View all rides
* Add drivers
* Remove drivers

### Customer

* Register and login
* Book rides
* View current rides
* View ride history
* Manage favorite locations
* Edit profile
* Change password
* Delete account

### Driver

* Register and login
* Go online/offline
* View pending rides
* Accept rides
* Complete rides
* Edit profile
* Change password
* Delete account

## Ride System

* Multiple vehicle types:

  * Mini Sedan
  * Sedan
  * SUV
  * Auto
* Driver matching based on vehicle type and availability
* Real distance calculation using OpenRouteService
* Automatic fare calculation

## Data Storage

All data is stored in JSON files:

* `m_admin.json`
* `customer.json`
* `driver.json`
* `m_ride.json`
* `location.json`

## Tech Stack

* Python
* JSON
* OpenRouteService API

## Project Structure

```text
cab_booking_system/
├── cli/
│   ├── admin_cli.py
│   ├── customer_cli.py
│   └── driver_cli.py
├── models/
│   ├── admin.py
│   ├── customer.py
│   ├── driver.py
│   ├── ride.py
│   └── location.py
├── services/
│   ├── admin_service.py
│   ├── customer_service.py
│   ├── driver_service.py
│   ├── ride_service.py
│   ├── location_service.py
│   ├── distance_service.py
│   └── base_service.py
├── storage/
│   ├── m_admin.json
│   ├── customer.json
│   ├── driver.json
│   ├── m_ride.json
│   └── location.json
└── main.py
```

## Run

```bash
python main.py
```

## Note

This project was built as a learning project to practice Python OOP, file handling, APIs, and CLI application development.

Admin key = 2580 for registration