# Programmer: Billy Felton
# Date: 3.19.2024
# Program: Choose Your Adventure

class OreoCookie:
    def __init__(self):
        self.ingredients = ["chocolate cookies", "cream filling"]
        self.assembly_status = "unassembled"

    def assemble(self):
        if self.assembly_status == "unassembled":
            self.assembly_status = "assembled"
            print(
                "The Oreo cookie is now assembled with its delicious cream filling sandwiched between two chocolate cookies.")

    def dip_in_milk(self):
        if self.assembly_status == "assembled":
            print(
                "The Oreo cookie is dipped into a glass of cold milk, softening it just enough to create the perfect texture.")
        else:
            print("First, assemble the Oreo cookie before dipping it into milk.")

    def eat(self):
        if self.assembly_status == "assembled":
            print(
                "With a satisfying crunch, the Oreo cookie is devoured, leaving behind a smile on the face of the eater.")
            self.assembly_status = "eaten"
        else:
            print("You can't eat an unassembled Oreo cookie!")


# Let's tell the story
if __name__ == "__main__":
    print("\nOnce upon a time, in a cozy kitchen, there was a lonely Oreo cookie waiting to be assembled.")

    oreo = OreoCookie()
    oreo.assemble()

    print("\nThe Oreo cookie was now ready, its chocolate cookies hugged the creamy filling snugly.")

    print(
        "\nThe aroma of freshly baked cookies wafted through the air as the Oreo cookie was gently dipped into a glass of cold milk.")
    oreo.dip_in_milk()

    print("\nThe moment of truth arrived as the eager eater took a bite into the softened Oreo cookie.")
    oreo.eat()
