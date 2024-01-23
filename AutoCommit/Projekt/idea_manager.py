# idea_manager.py
import os

class IdeaManager:
    def __init__(self, file_path='ideas.txt'):
        self.file_path = file_path
        self.ideas = self.load_ideas()

    def load_ideas(self):
        try:
            with open(self.file_path, 'r') as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return []

    def save_ideas(self):
        with open(self.file_path, 'w') as file:
            file.write('\n'.join(self.ideas))

    def add_idea(self, idea):
        self.ideas.append(idea)
        self.save_ideas()

    def print_ideas(self):
        print("Ideas:")
        for idea in self.ideas:
            print(f"- {idea}")
