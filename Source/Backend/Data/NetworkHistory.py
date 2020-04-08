from Source.Backend.Data.Network import Network


class NetworkHistory:

    # Stores changes occurring over the network.
    def store_network_changes(self, object):
        return None

    # Removes any approved changes from the stack to send the History class to be saved as local changes.
    def send_changes(self, object):
        # return approvedChanges
        pass
