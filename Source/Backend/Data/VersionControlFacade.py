from Source.Backend.Data.NetworkHistory import NetworkHistory
from Source.Backend.Data.History import History


class VersionControlFacade:

    # instance of Network History and History classes
    network = NetworkHistory()
    local = History()

    # The purpose of this method is to delegate the changes occurring over the network to the Network History class.
    def send_to_network(self,object):
        return None

    # The purpose of this method is to delegate the local changes to the History class
    def send_to_history(self,object):
        return None

    # The purpose of this method is to delegate the information received from the History class to the DB Subsystem.
    def send_to_DB(self,object):
        return None