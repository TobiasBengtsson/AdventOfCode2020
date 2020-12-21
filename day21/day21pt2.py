import sys

all_ing = set()
all_ing_list = []
allerg_poss_ing = {}
for line in sys.stdin:
    line = line.rstrip('\n')
    ing_spl, allerg_spl = line.split('(')
    ingredients = set(ing_spl.strip().split())
    for ingredient in ingredients:
        all_ing.add(ingredient)
        all_ing_list.append(ingredient)

    allergens = allerg_spl.strip('contains').strip().split(',')
    for allergen in allergens:
        allergen = allergen.strip(')').strip()
        if allergen not in allerg_poss_ing:
            allerg_poss_ing[allergen] = ingredients
        else:
            allerg_poss_ing[allergen] = allerg_poss_ing[allergen].intersection(ingredients)

resolved = set()
resolved_ing = set()

while len(resolved) < len(allerg_poss_ing.keys()):
    for allergen in allerg_poss_ing:
        if allergen in resolved:
            continue

        for r in resolved_ing:
            if r in allerg_poss_ing[allergen]:
                allerg_poss_ing[allergen].remove(r)

        if len(allerg_poss_ing[allergen]) == 1:
            resolved.add(allergen)
            for single_ing in allerg_poss_ing[allergen]:
                resolved_ing.add(single_ing)

output = ''

for allergen in sorted(allerg_poss_ing.keys()):
    output += allerg_poss_ing[allergen].pop() + ','

print(output[:-1])
