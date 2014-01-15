#writing a bio

name = "Kevin"
age = 21
school = "UNC-Chapel Hill"
fresh_age = age - 4
unc_prez = "James K. Polk"
unc_prez_age = 49
age_difference = unc_prez_age - age
potus_average_age = 54.8
presidents = 44
first_prez = 1789
last_prez = 2016
prez_average = (last_prez - first_prez) / presidents
term = 4
two_term = 4*2

print "My name is %s." % name
print "I am %d years old." % age
print "When I started school at", school, "I was", fresh_age, "years old."
print "One U.S. president who went to school at %s was %s." % (school, unc_prez)
print "Polk was", unc_prez_age, "when he took office."
print "I am", age_difference, "years younger than Polk."
print "There have been", presidents, "presidents since %d." % first_prez
print "Assuming Obama finishes his term in", last_prez, "each president will have served an average of", prez_average, "years in office."
print "Each term is", term, "years long. If a president serves two terms, it will be for", two_term, "years."
