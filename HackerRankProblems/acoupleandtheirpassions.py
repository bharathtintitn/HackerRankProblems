import sys

class Country(object):
  def __init__(self, args):
    self.country = args[0]
    self.latitude = args[1]
    self.longitude = args[2]
    self.count = int(args[3])
    self.passion = []
    self.countPassion = 0
    if self.count > 0:
      for i in xrange(self.count):
        self.passion.append(args[i+4])

  def isPresent(self, passion):
    if passion in self.passion:
      return True
    return False

  def __str__(self):
    return self.country + " "+self.latitude+" "+self.longitude \
        +" "+str(self.count)+" ".join(self.passion)+" "+str(self.countPassion)

  def countrySort(self, country):

    if self.countPassion == country.countPassion:
      if self.country > country.county:
        return False
      return True
    elif self.countPassion < country.countPassion:
      return True

    return False

G = int(raw_input().strip())
passions = []
for _ in xrange(G):
  temp = raw_input().strip().split()
  passions.append(temp)

N = int(raw_input().strip())
country = []
for _ in xrange(N):
  temp = raw_input().strip().split()
  country.append(Country(temp))

print "Passions ", passions
print "----------"

for item in passions:
  for i in item:
    for coun in country:
      if i in coun.passion:
        coun.countPassion += 1

country = sorted(country, key=lambda x: x.countPassion)
best = country[N].countPassion
print "Highest passion is ", best

for i in reversed(xrange(N-1)):
  temp = []

for item in country:
  print "countries:",item 


