from genetic_algorithm import *
target = 371
p_count = 100
i_length = 6
i_min = 0
i_max = 100
p = population(p_count, i_length, i_min, i_max)
history = [grade(p, target),]
for i in xrange(100):
    p = evolve(p, target)
    history.append(grade(p, target))

for datum in history:
   print datum
