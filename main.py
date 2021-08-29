# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sqlite3
from data.securities import liste_indices as indices
from data.securities import liste_actions_pme as actions_pme
from data.securities import print_indices as prt_ind
from data.securities import print_actions_pme as prt_act
from objects.db_conn import db_exist
from objects.logger import log_init as log
from objects.CreateTicket import CreateTicketGroup
from objects.DownloadTicket import DownloadTicket
from objects.ReadTicket import ReadTicket

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    #print(prt_act(actions_pme()))
    team = CreateTicketGroup(actions_pme())
#    DownloadTicket(team).execute()
    ReadTicket('ABC Arbitrage', 'info').execute()
    #team_it = iter(team)

    #for i in range(len(actions_pme()[1])):
     #   print(actions_pme()[1][next(team_it)])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
