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
    
    def deleteTask(self, task_id):
        """
        Deletes a task by its ID.
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False