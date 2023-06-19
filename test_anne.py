# class Recipe:
#     def __init__(self, name, country, ingredients, preparation_time, cooking_method, nutritional_info):
#         self.name = name
#         self.country = country
#         self.ingredients = ingredients
#         self.preparation_time = preparation_time
#         self.cooking_method = cooking_method
#         self.nutritional_info = nutritional_info

# class MoroccanRecipe(Recipe):
#     def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info):
#         super().__init__(name, "Morocco", ingredients, preparation_time, cooking_method, nutritional_info)

# class EthiopianRecipe(Recipe):
#     def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info):
#         super().__init__(name, "Ethiopia", ingredients, preparation_time, cooking_method, nutritional_info)


# class NigerianRecipe(Recipe):
#     def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info):
#         super().__init__(name, "Nigeria", ingredients, preparation_time, cooking_method, nutritional_info)

# recipe1 = MoroccanRecipe("Vegetables", ["couscous", "carrots", "water", "onions"], 40, "Steaming", "High in fiber")
# recipe2 = EthiopianRecipe("Banana", ["chicken", "onions", "spice mix"], 90, "Stewing", "Spicy and flavorful")
# recipe3 = NigerianRecipe("Rice", ["rice", "tomatoes", "onions", " peppers"], 15, "Simmering", "Rich and aromatic")

# def work():
#     print(f"Recipe: {recipe1.name}")
#     print(f"Country: {recipe1.country}")
#     print(f"Ingredients: {', '.join(recipe1.ingredients)}")
#     print(f"Preparation Time: {recipe1.preparation_time} minutes")
#     print(f"Cooking Method: {recipe1.cooking_method}")
#     print(f"Nutritional Info: {recipe1.nutritional_info}")

#     print()

#     print(f"Recipe: {recipe2.name}")
#     print(f"Country: {recipe2.country}")
#     print(f"Ingredients: {', '.join(recipe2.ingredients)}")
#     print(f"Preparation Time: {recipe2.preparation_time} minutes")
#     print(f"Cooking Method: {recipe2.cooking_method}")
#     print(f"Nutritional Info: {recipe2.nutritional_info}")

#     print()
#     print(f"Recipe: {recipe3.name}")
#     print(f"Country: {recipe3.country}")
#     print(f"Ingredients: {', '.join(recipe3.ingredients)}")
#     print(f"Preparation Time: {recipe3.preparation_time} minutes")
#     print(f"Cooking Method: {recipe3.cooking_method}")
#     print(f"Nutritional Info: {recipe3.nutritional_info}")

# if __name__ == "__main__":
#     work()

class ancestralStrories:
    def __init__(self,length,moral_lessons,age_group):
        self.length=length
        self.moral_lessons=moral_lessons
        self.age_group=age_group
        self.story=[]
    def Story(self):
        if self.story=="oral" and self.story_teller=="old":
            return f"the story was given to childern aged {self.age_group}"
        elif self.story=="written" and self.story_teller=="teenage":
            return f"the story was written for children aged {self.age_group}"
        else :return f" no story"
    def storyTeller(self):
        if self.story.teller=="youth" and self.length=="short":
            return f"the story was {self.length}"
        elif self.story_teller=="old" and self.length=="long":
            return f"the story was {self.length} "
        else: return f" no story teller"
    def Translator(self):
        if self.age_group=="children" and self.story_teller=="learnt":
            return f"the translator was for {self.age_group}"
        else :return f"no translator"
    ancestralStrories=Story("oral")
    print(ancestralStrories)
