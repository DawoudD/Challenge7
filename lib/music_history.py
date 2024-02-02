class music_history:
    def __init__(self):
        self.tracks = []

    def add(self, trackID):
        if trackID is None:
            raise Exception("your history is empty!")
        self.tracks.append(trackID)
        

    def get_history(self):
        return self.tracks