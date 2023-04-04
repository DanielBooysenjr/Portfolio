import smtplib
import datetime as dt
import os
import glob

current_date = dt.datetime.now()
formatted_date = current_date.strftime("%Y-%m-%d %H:%M")

# Setting up the email address and password for authentication
my_email = "Your Email"
password = "Your Password"

class Report:
    # Creating sending email function
    def send_email(self):
        # Connect to the Gmail SMTP server and login with the given credentials
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            
            # Get the path of the logs directory
            logs_dir = os.path.join(os.getcwd(), "logs")
            
            # Get the list of all log files in the directory
            log_files = glob.glob(os.path.join(logs_dir, "*.log"))
            
            # Sort the log files by creation time and get the last one
            last_log_file = sorted(log_files, key=os.path.getctime)[-1]
            
            # Read the contents of the last log file
            with open(last_log_file, "r") as file:
                log_contents = file.read()
            
            # Send an email to the recipient with the contents of the last log file
            connection.sendmail(
                from_addr=my_email,
                to_addrs="To Email",
                msg=f"Subject: Facebook Marketing for {formatted_date}\n\n{log_contents}"
            )

# report = Report()
# report.send_email()