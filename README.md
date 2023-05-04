# email-automation
This project automates the sending of emails using the Gmail API. It generates random subjects and email bodies, and sends them through the configured Gmail account. The program repeats this process 10 times, with a 2-second delay between each email.

The provided code is a Python script that automates the process of sending emails using the Gmail API. Let's break down the different components and steps of the code:

Importing Libraries: At the beginning of the code, necessary libraries are imported. These libraries include modules for file handling, random number generation, date and time manipulation, Gmail API authentication, Base64 encoding for email messages, and MIME message construction.

Defining Scopes: A list of scopes (SCOPES) is defined, which determines the permissions required to access the Gmail API and send emails. These scopes determine the level of access granted to the program for interacting with the Gmail account.

Sending Email Function: The code defines a function called send_email that is used to send emails through the Gmail API. This function takes three parameters: the recipient email address (to), the email subject (subject), and the email body (body).

Authentication and Authorization: The code checks if there are valid authentication credentials stored in a token file. If valid credentials exist, they are used to authenticate and authorize the program to access the Gmail API. If no valid credentials are found, the program initiates a user authentication process. This involves generating access credentials through the Google authentication flow.

Building the Gmail Service: Once valid credentials are obtained, the Gmail service is built using those credentials. This service will be used to interact with the Gmail API and send the emails.

Constructing the Message: The program creates a MIMEMultipart message object, which represents the email to be sent. The recipient (to), subject (subject), and body (body) of the email are set in the message object.

Sending the Message: The program encodes the MIME message in Base64 format and sends it using the messages().send() method of the Gmail service. If the email is sent successfully, a success message is displayed along with the message ID. If an error occurs during the sending process, an error message is displayed.

Main Loop: The program contains a main loop (the main() function) that runs 10 times. In each iteration, it generates random subject and body for the email and calls the send_email() function to send the email. After sending the email, a message indicating that the email has been sent is displayed. A 2-second delay is added between each send using the time.sleep() method.

Running the Program: At the end of the code, it checks if the file is being run directly and not imported as a module. In that case, the main() function is called to initiate the execution of the program.

In summary, this code automates the process of sending emails by utilizing the Gmail API. It generates random subject and body for the emails and sends them through the configured Gmail account.