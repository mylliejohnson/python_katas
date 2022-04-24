def human_years_cat_years_dog_years(human_years):
    # Your code here
    humanYears, catYears, dogYears = human_years, 0, 0
    res = []
    
    if human_years == 1:
        catYears = 15
        dogYears = 15
        res.append(humanYears)
        res.append(catYears)
        res.append(dogYears)
    if human_years == 2:
        catYears = 24
        dogYears = 24
        res.append(humanYears)
        res.append(catYears)
        res.append(dogYears)
    if human_years > 2:
        catYears = 24 + (4 * (human_years - 2))
        dogYears = 24 + (5 * (human_years - 2))
        res.append(humanYears)
        res.append(catYears)
        res.append(dogYears)
    
    return res