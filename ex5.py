name = 'Zed A Shaw'
age = 35 # not a lie
inch_to_cm = 2.54
print inch_to_cm
height = 74.0 * inch_to_cm
print height
lb_to_kg = 0.453592
weight = 180.0 * lb_to_kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s" % name
print "He's %f cm tall" % height
print "He's %d kg heavy" % weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth

print "If I add %d, %d and %d I get %d" % (age, height, weight, age + height + weight)
