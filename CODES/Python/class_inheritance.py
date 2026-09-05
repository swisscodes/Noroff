class House:
    htype = "house"
    def __init__(self,windows,doors,wall_color):
            self.windows = windows
            self.doors = doors
            self.wall_color = wall_color
    def __str__(self):
            return f'''A {self.wall_color} {self.htype} \
                with {self.doors} doors \
                and {self.windows} windows.'''
class AbandonedHouse (House):
    htype = "abandoned house"
h1 = House(4,1,"green")
h2 = AbandonedHouse(6,2,"blue")
print(h1)
print(h2)



class Logger:
    def log(self, message: str):
        print(f"[LOG] {message}")

class Notifier:
    def send_alert(self, text: str):
        print(f"[ALERT] {text}")

# Inherits from both parent classes
class MonitoringAgent(Logger, Notifier):
    def check_health(self):
        self.log("Running system check...")
        self.send_alert("Disk usage exceeds 90%!")

agent = MonitoringAgent()
agent.check_health()