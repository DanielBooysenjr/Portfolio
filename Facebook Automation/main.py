# # Run this file

from post_information import Post_Information
from open_facebook import Facebook_Init
from group_navigation import GroupPosting
from logger import *

class Facebook_Bot:
    def __init__(self):
        Post_Information()
        Facebook_Init()
        GroupPosting()
