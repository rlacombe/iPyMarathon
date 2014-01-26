# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# This notebook computes your Maximum Hear Rate and your Hear Rate Zones for marathon training.
# 
# Start by inputing your age.

# <codecell>

age = 29

# <headingcell level=2>

# Maximum Heart Frequency

# <markdowncell>

# The following section computes the Maximum Heart Frequency using various scientific methods.
# 
# Sources:
# 
# - http://www.sportnat.com/100km/cardio/Definir-FCM.html
# - http://www.brianmac.co.uk/maxhr.htm

# <codecell>

def MHR_AstrandRyhming(age):
    return (220.0 - age)

def MHR_Inbar(age):
    return (205.8 - (0.685*age))

def MHR_RobersLanwher(age):
    return (208.754 - (0.734 * age))

def MHR_Miller(age):
    return (217 - (0.85 * age))

def MHR_average(age):
    return (MHR_AstrandRyhming(age) 
            + MHR_Inbar(age) 
            + MHR_RobersLanwher(age)
            + MHR_Miller(age))/4

MHR = MHR_average(age)

print "Maximum Heart Frequency\n=======================\n"
print "Astrand & Ryhming: "+str(MHR_AstrandRyhming(age))
print "Inbar (1994): "+str(MHR_Inbar(age))
print "Robers & Lanwher (2002): "+str(MHR_RobersLanwher(age))
print "Miller: "+str(MHR_Miller(age))
print "\nAverage: "+str(MHR_average(age))
print "\nWorking MHR: "+str(int(MHR))

# <headingcell level=2>

# Heart Rate Zones

# <markdowncell>

# The following section computes training Heart Rate Zones.
# 
# Sources: 
# 
# - http://www.3-fitness.com/tarticles/zones.htm

# <codecell>

print "Heart Rate Zones\n================\n"
print "Endurance (70%): "+str(int(.7 * MHR))
print "Tempo (75% to 78%): "+str(int(.75 * MHR))+" to "+str(int(.78 * MHR))
print "Race Pace (80%): "+str(int(.8 * MHR))
print "Threshold (85%): "+str(int(.85 * MHR))
print "Superthreshold (90%): "+str(int(.9 * MHR))
print "Speed (95%): "+str(int(.95 * MHR))

