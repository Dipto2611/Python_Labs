import matplotlib.pyplot as p

#note: 
# for %age 1.0 means 28%
# for %age 1.1 means 28.1%
#and go on as u like
#startangle means the staring angle 


Stdmarks=[45,78,25]

p.subplot(1,2,1)
p.pie(Stdmarks, autopct="%1.1f%%")
p.title("Marks")
# p.show()

streams=["arts","sci","comms"]

p.subplot(1,2,2)
p.pie(Stdmarks, labels=streams, autopct="%1.1f%%")
p.title("Marks & %")
p.show()
