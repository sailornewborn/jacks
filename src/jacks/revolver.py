import jacks
class GetPrimerFire:
    def __init__(self, primer: int = 1):

        self.primer = primer
        self.track = []
        self.track.append(primer)
    def get_fire(self):
        shot = jacks.get_key_address_int(self.primer)
        self.primer = shot
        self.track.append(self.primer)
    def get_current_primer(self):
        return self.primer

    def get_current_track(self):
        return self.track
