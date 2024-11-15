from abc import ABC, abstractmethod
 
class Bike(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
         
    @abstractmethod
    def printDetails(self):
        pass
 
    def accelerate(self):
        print("Speed up ...")
 
    def break_applied(self):
        print("Bike stopped")
 
class Hatchback(Bike):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
 
    def automatic(self):
        print("Not having this feature")
 
class R15(Bike):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
 
    def automatic(self):
        print("Available")
 
Bike1 = Hatchback("Yamaha", "ZMR", "2023")
 
Bike1.printDetails()
Bike1.accelerate()
Bike1.automatic()
#example 2:
from abc import ABC, abstractmethod
class Media(ABC):
    def __init__(self, title, format_type):
        self.title = title
        self.format_type = format_type
    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def showDetails(self):
        pass
    def stop(self):
        print(self.title)
class Audio(Media):
    def __init__(self, title, format_type, duration):
        self.title=title
        self.format_type=format_type
        self.duration = duration
    def play(self):
        print(self.title)
        print(self.format_type)
        
    def showDetails(self):
        print(self.title)
        print(self.format_type)
        print(self.duration)
class Video(Media):
    def __init__(self, title, format_type, resolution):
        self.title=title
        self.format_type=format_type
        self.resolution = resolution
    def play(self):
        print(self.title)
        print(self.format_type)
        print(self.resolution)
    def showDetails(self):
        print(self.title)
        print(self.format_type)
        print(self.resolution)
a = Audio("Shape of You", "MP3", 4)
v = Video("Inception", "MP4", "1080p")
a.showDetails()
a.play()
a.stop()
v.showDetails()
v.play()
v.stop()