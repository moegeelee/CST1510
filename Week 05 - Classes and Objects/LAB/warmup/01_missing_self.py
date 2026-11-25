# Python passes the calling object into the first parameter.

class Record:
    def status(self, percent):
        return percent

r = Record()
print(r.status(95))
