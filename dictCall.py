from spanishDict import categories

class dictCall:
    def __init__(self, categories):
        self.categories = categories
        self.key = list(categories.keys())

    def listCategories(self):
        pos = 1
        for cat in self.key:
            print(f"{pos}. {cat}")
            pos += 1

    def listEnglish(self, choice):
        catName = self.key[choice - 1]
        print(f"\"{catName}\" English Wordbank:\n")
        count = 0
        for span, eng in self.categories[catName].items():
            print(f"{eng}", end=", ")
            count += 1
            if count % 3 == 0:
                print()
        print()

    def listSpanish(self, choice):
        catName = self.key[choice - 1]
        print(f"\"{catName}\" Spanish Wordbank:\n")
        count = 0
        for span, eng in self.categories[catName].items():
            print(f"{span}", end=", ")
            count += 1
            if count % 3 == 0:
                print()
        print()

    def listTranslations(self, choice):
        catName = self.key[choice - 1]
        for span, eng in self.categories[catName].items():
            print(f"{span} = {eng}")
