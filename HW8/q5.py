

# class indenter():
    
#     def __init__(self) -> None:
#         self.indent = -1
        
#     def __enter__(self):
#         return "    "
#     def print(self):
#         print(self)
#     def __exit__(self, exc_type, exc_value, exc_tb):
#         return "    "

# with indenter() as Indent:
#     Indent.print("hi")

from textwrap import indent

class Indenter:

    def __init__(self):
        self.level = -1

    def print(self, text):
        for _ in range(self.level):
             text = indent(text, "    ")
        print(text)

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.level -= 1


with Indenter() as Indent:
    Indent.print("Hi")
    with Indent:
        Indent.print("Talk is Cheap!")
        with Indent:
            Indent.print("Show me the Code...")
    Indent.print("Torvalds")
