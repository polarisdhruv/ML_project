## this is a logger file
import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO


)


# if __name__ == "__main__":
#     logging.info("Logging has started")


# import logging

# logging.basicConfig(filename='app.log', level=logging.INFO)

# def user_login(username, password):
#     logging.info(f"User {username} tried to log in.")
    
#     # Let's say an error happens during login, like wrong password
#     if password != "correct_password":
#         logging.error(f"Login failed for user {username} - Incorrect password.")
#     else:
#         logging.info(f"User {username} logged in successfully.")

# # Example of a user trying to log in
# user_login("dhruv", "wrong_password")


#output
# INFO:root:User dhruv tried to log in.
# ERROR:root:Login failed for user dhruv - Incorrect password.
