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

ans = set()
for ingredient in all_ing:
    ans.add(ingredient)
    for allergen in allerg_poss_ing:
        if ingredient in allerg_poss_ing[allergen]:
            ans.remove(ingredient)
            break

count = 0
for ans_i in ans:
    count += all_ing_list.count(ans_i)

print(count)
