# Final Exam AIDI 2004 - Akash

class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.counter = 1

    def addTask(self, title, priority):
        self.tasks[self.counter] = {
            "title": title,
            "priority": priority
        }
        self.counter += 1