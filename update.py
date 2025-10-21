from mistyPy.GenerateRobot import RobotGenerator;
from dotenv import load_dotenv
import os
load_dotenv() # take environment variables from .env.
RobotGenerator(os.getenv("MISTY_TIER_IP"));