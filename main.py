from client import client
from key import token


# To load new modules, copy/paste the line below, uncommented, with X filled in for the name of your file
# from modules import X

from modules import help
# from modules import message_log
from modules import ping

client.run(token)
