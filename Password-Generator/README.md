# Password Generator 

## Overview
This repository contains two distinct approaches to generating different types of passwords and PIN codes: an Object-Oriented Programming (OOP) approach and a Functional Programming (FP) approach. Each approach is implemented in its own directory and showcases the benefits of the respective programming paradigm. Additionally, the repository includes an interactive dashboard app using Streamlit, which is based on the OOP approach.

## Repository Structure
```
.
└── src/
    ├── GUI/
        ├── images/        
                └── banner.jpeg     
        ├── README.md
        ├── dashboard.py            
        └── password-generator      
    ├── OOP-approach/
    │   ├── main.py
    │   └── README.md
    └── functional-approach/
        ├── main.py
        └── README.md
```


## Approaches
1. **Object-Oriented Programming (OOP)**
The OOP approach organizes the code into classes, encapsulating data and behavior. This approach is beneficial for complex systems that require multiple interacting components, where inheritance and polymorphism can provide significant advantages.

    * **Features**:
      * Encapsulation of password and pincode generation logic within classes.
      * Extensibility through subclassing and method overriding.
      * Clear separation of concerns, making the code more maintainable.
    * **Usage**: Refer to the README.md in the oop-approach/ directory for detailed usage instructions.

2. **Functional Programming (FP)**
The FP approach emphasizes the use of pure functions, immutability, and higher-order functions. This approach is ideal for scenarios where simplicity, clarity, and avoidance of side effects are prioritized.

    * **Features**:
    
      * Simple and straightforward function-based implementation.
      * Easier to reason about due to the lack of side effects.
      * Promotes code reusability through composition of smaller functions.
    * Usage: Refer to the README.md in the functional-approach/ directory for detailed usage instructions.

3. **Interactive Dashboard (Streamlit)**
The Streamlit-based dashboard provides an interactive way to generate passwords using a web interface. It leverages the OOP approach to offer a user-friendly method for creating various types of passwords.

    * **Features:**
        * User-friendly interface with real-time updates.
        * Multiple password generation options (random, pincode, memorable).
        * Easy to run locally.


## Installation
To use either approach, navigate to the corresponding directory and install any dependencies as specified in the README.md file within that directory.

## Choosing Between Approaches
* **OOP Approach**: Ideal if your project involves complex structures and you prefer encapsulating behavior and data within objects.
* **Functional Approach**: Suitable for projects that emphasize simplicity, statelessness, and the use of pure functions.
