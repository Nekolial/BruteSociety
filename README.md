# BruteSociety
Brute Society is a command-line tool developed in Python to perform brute-force attacks on specific URLs using a wordlist.

Brute Society
Description

Brute Society is a command-line tool developed in Python to perform brute-force attacks on provided URLs using a wordlist. It offers a simple and flexible way to test the security of web applications by identifying potential unauthorized access vulnerabilities.
Key Features

    Brute Force Attacks: The program automates the process of login testing and accessing protected resources by trying a series of password or keyword combinations to find a valid match.
    HTTPS Support: It's recommended to use HTTPS for enhanced security during HTTP requests. Brute Society issues a warning when a URL doesn't use HTTPS.
    User Authentication: If the target URL requires user authentication, the program allows the user to securely provide their login credentials.
    Event Logging: The code includes a logging system to record important events such as successful requests, network errors, and unhandled exceptions, facilitating security investigation and debugging.
    Enhanced Security: The code implements recommended security practices such as input validation, specific error handling, secure usage of authentication credentials, and HTTPS recommendations.

Usage

    Clone the Repository: Download or clone the repository to your local environment.
    Install Dependencies: Make sure you have all dependencies installed. You can install them using pip:

pip install -r requirements.txt

Run the Program: Execute the Python script brute_society.py using Python 3.x. The program will prompt for information such as the target URL, wordlist file, and optionally authentication credentials.

    python brute_society.py

    Review Results: The program will display the HTTP requests made and their corresponding status codes. Additionally, it will log important events in the brute_society.log file for future reference.

Contribution

If you find bugs, vulnerabilities, or have ideas for improvements, feel free to open an issue or submit a pull request. Your contribution is highly welcomed!
License

This project is licensed under the MIT License, which means you can use, modify, and distribute the code freely as long as you include a copy of the license in any distributions you make.
