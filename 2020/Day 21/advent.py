#!/usr/bin/env python3

import sys

def main(args):
    with open(args[1], "r") as file:
        ingredients = []
        allergens = {}
        repices = []

        for line in file:
            line = line.strip().replace(",", " ")[:-1]
            sIngredients, sAllergens = line.split("(contains")
            lIngredients, lAllergens = sIngredients.split(), sAllergens.split()

            repices.append(lIngredients)
            for ingredient in lIngredients:
                if ingredient not in ingredients:
                    ingredients.append(ingredient)

            for allergen in lAllergens:
                if allergen not in allergens:
                    allergens[allergen] = lIngredients
                else:
                    allergens[allergen] = list(set(allergens[allergen]).intersection(lIngredients))

        while True:
            exclusives = []
            for allergen in allergens:
                if len(allergens[allergen]) == 1:
                    exclusives.extend(allergens[allergen])

            if len(exclusives) == len(allergens):
                break

            for allergen in allergens:
                if len(allergens[allergen]) == 1:
                    continue
                allergens[allergen] = list(set(allergens[allergen]).difference(exclusives))
                if len(allergens[allergen]) == 1:
                    exclusives.extend(allergens[allergen])

        ingredientsWithAllergen = []
        for allergen in allergens:
            ingredientsWithAllergen.extend(allergens[allergen])
        ingredientsWithoutAllergen = list(set(ingredients).difference(ingredientsWithAllergen))

        somme = 0
        for repice in repices:
            for ingredient in ingredientsWithoutAllergen:
                somme += repice.count(ingredient)

        print("How many times do ingredients without allergens appear? {}".format(somme))

        allergensInversed = dict((v[0], k) for k, v in allergens.items())
        ingredientsWithAllergenSorted = sorted(ingredientsWithAllergen, key=lambda a: allergensInversed[a])

        print("What is your canonical dangerous ingredient list? {}"
              .format(','.join(ingredientsWithAllergenSorted)))

if __name__ == "__main__":
    main(sys.argv)
