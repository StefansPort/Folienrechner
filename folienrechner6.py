#!/usr/bin/env python
# coding: utf-8

# In[1]:


import locale
locale.setlocale(locale.LC_ALL, 'de_DE')

aa = locale.atof(input('Anzahl der Anbieter: "(1-5)"'))

if aa == 1:
    
    rg1 = locale.atof(input('Rollengewicht Anbieter 1:    '))
    kg1 = locale.atof(input('Kerngewicht Anbieter 1:      '))
    fp1 = locale.atof(input('Folienpreis Anbieter 1 / kg: '))

    eg1 = float(rg1) - float(kg1)
    rp1 = float(rg1) * float(fp1)
    efp1 = float(rp1) / float(eg1)
    efpg1 = round(efp1, 3)

    print("")
    print("----------------------------------------")
    print("----------------ERGEBNIS----------------")
    print("----------------------------------------")
    print("")

    print("Rollengewicht            : " + str(rg1) + " kg")
    print("Kerngewicht              : " + str(kg1)+ "  kg")
    print("Effektives Foliengewicht : " + str(eg1)+ " kg")
    print("Effektiver Folienpreis   : " + str(efpg1)+ " € / kg")

if aa == 2:
    rg1 = locale.atof(input('Rollengewicht Anbieter 1:    '))
    kg1 = locale.atof(input('Kerngewicht Anbieter 1:      '))
    fp1 = locale.atof(input('Folienpreis Anbieter 1 / kg: '))
    
    rg2 = locale.atof(input('Rollengewicht Anbieter 2:    '))
    kg2 = locale.atof(input('Kerngewicht Anbieter 2:      '))
    fp2 = locale.atof(input('Folienpreis Anbieter 2 / kg: '))
 
    eg1 = float(rg1) - float(kg1)
    rp1 = float(rg1) * float(fp1)
    efp1 = float(rp1) / float(eg1)
    efpg1 = round(efp1, 3)

    eg2 = float(rg2) - float(kg2)
    rp2 = float(rg2) * float(fp2)
    efp2 = float(rp2) / float(eg2)
    efpg2 = round(efp2, 3)
    
    print("")
    print("----------------------------------------")
    print("----------------ERGEBNIS----------------")
    print("----------------------------------------")
    print("")
    print("Rollengewicht            : " + str(rg1) + " kg")
    print("Kerngewicht              : " + str(kg1)+ "  kg")
    print("Effektives Foliengewicht : " + str(eg1)+ " kg")
    print("Effektiver Folienpreis   : " + str(efpg1)+ " € / kg")
    print("----------------------------------------")
    print("Rollengewicht            : " + str(rg2) + " kg")
    print("Kerngewicht              : " + str(kg2)+ "  kg")
    print("Effektives Foliengewicht : " + str(eg2)+ " kg")
    print("Effektiver Folienpreis   : " + str(efpg2)+ " € / kg")
    print("----------------------------------------")

if aa == 3:
    rg1 = locale.atof(input('Rollengewicht Anbieter 1:    '))
    kg1 = locale.atof(input('Kerngewicht Anbieter 1:      '))
    fp1 = locale.atof(input('Folienpreis Anbieter 1 / kg: '))
    
    rg2 = locale.atof(input('Rollengewicht Anbieter 2:    '))
    kg2 = locale.atof(input('Kerngewicht Anbieter 2:      '))
    fp2 = locale.atof(input('Folienpreis Anbieter 2 / kg: '))
    
    rg3 = locale.atof(input('Rollengewicht Anbieter 3:    '))
    kg3 = locale.atof(input('Kerngewicht Anbieter 3:      '))
    fp3 = locale.atof(input('Folienpreis Anbieter 3 / kg: '))

    eg1 = float(rg1) - float(kg1)
    rp1 = float(rg1) * float(fp1)
    efp1 = float(rp1) / float(eg1)
    efpg1 = round(efp1, 3)

    eg2 = float(rg2) - float(kg2)
    rp2 = float(rg2) * float(fp2)
    efp2 = float(rp2) / float(eg2)
    efpg2 = round(efp2, 3)
    
    eg3 = float(rg3) - float(kg3)
    rp3 = float(rg3) * float(fp3)
    efp3 = float(rp3) / float(eg3)
    efpg3 = round(efp3, 3)
    
    print("")
    print("----------------------------------------")
    print("----------------ERGEBNIS----------------")
    print("----------------------------------------")
    print("")
    print("Rollengewicht            : " + str(rg1) + " kg")
    print("Kerngewicht              : " + str(kg1)+ "  kg")
    print("Effektives Foliengewicht : " + str(eg1)+ " kg")
    print("Effektiver Folienpreis   : " + str(efpg1)+ " € / kg")
    print("----------------------------------------")
    print("Rollengewicht            : " + str(rg2) + " kg")
    print("Kerngewicht              : " + str(kg2)+ "  kg")
    print("Effektives Foliengewicht : " + str(eg2)+ " kg")
    print("Effektiver Folienpreis   : " + str(efpg2)+ " € / kg")
    print("----------------------------------------")
    print("Rollengewicht            : " + str(rg3) + " kg")
    print("Kerngewicht              : " + str(kg3)+ "  kg")
    print("Effektives Foliengewicht : " + str(eg3)+ " kg")
    print("Effektiver Folienpreis   : " + str(efpg3)+ " € / kg")
    print("----------------------------------------")
    
if aa == 4: 
    rg1 = locale.atof(input('Rollengewicht Anbieter 1:    '))
    kg1 = locale.atof(input('Kerngewicht Anbieter 1:      '))
    fp1 = locale.atof(input('Folienpreis Anbieter 1 / kg: '))
    
    rg2 = locale.atof(input('Rollengewicht Anbieter 2:    '))
    kg2 = locale.atof(input('Kerngewicht Anbieter 2:      '))
    fp2 = locale.atof(input('Folienpreis Anbieter 2 / kg: '))
    
    rg3 = locale.atof(input('Rollengewicht Anbieter 3:    '))
    kg3 = locale.atof(input('Kerngewicht Anbieter 3:      '))
    fp3 = locale.atof(input('Folienpreis Anbieter 3 / kg: '))

    rg4 = locale.atof(input('Rollengewicht Anbieter 4:    '))
    kg4 = locale.atof(input('Kerngewicht Anbieter 4:      '))
    fp4 = locale.atof(input('Folienpreis Anbieter 4 / kg: '))
 
    eg1 = float(rg1) - float(kg1)
    rp1 = float(rg1) * float(fp1)
    efp1 = float(rp1) / float(eg1)
    efpg1 = round(efp1, 3)

    eg2 = float(rg2) - float(kg2)
    rp2 = float(rg2) * float(fp2)
    efp2 = float(rp2) / float(eg2)
    efpg2 = round(efp2, 3)
    
    eg3 = float(rg3) - float(kg3)
    rp3 = float(rg3) * float(fp3)
    efp3 = float(rp3) / float(eg3)
    efpg3 = round(efp3, 3)
    
    eg4 = float(rg4) - float(kg4)
    rp4 = float(rg4) * float(fp4)
    efp4 = float(rp4) / float(eg4)
    efpg4 = round(efp4, 3)

    print("")
    print("----------------------------------------")
    print("----------------ERGEBNIS----------------")
    print("----------------------------------------")
    print("")
    print("Rollengewicht            : " + str(rg1) + " kg")
    print("Kerngewicht              : " + str(kg1)+ "  kg")
    print("Effektives Foliengewicht : " + str(eg1)+ " kg")
    print("Effektiver Folienpreis   : " + str(efpg1)+ " € / kg")
    print("----------------------------------------")
    print("Rollengewicht            : " + str(rg2) + " kg")
    print("Kerngewicht              : " + str(kg2)+ "  kg")
    print("Effektives Foliengewicht : " + str(eg2)+ " kg")
    print("Effektiver Folienpreis   : " + str(efpg2)+ " € / kg")
    print("----------------------------------------")
    print("Rollengewicht            : " + str(rg3) + " kg")
    print("Kerngewicht              : " + str(kg3)+ "  kg")
    print("Effektives Foliengewicht : " + str(eg3)+ " kg")
    print("Effektiver Folienpreis   : " + str(efpg3)+ " € / kg")
    print("----------------------------------------")   
    print("Rollengewicht            : " + str(rg4) + " kg")
    print("Kerngewicht              : " + str(kg4)+ "  kg")
    print("Effektives Foliengewicht : " + str(eg4)+ " kg")
    print("Effektiver Folienpreis   : " + str(efpg4)+ " € / kg")
    print("----------------------------------------")   
    
if aa == 5:
    rg1 = locale.atof(input('Rollengewicht Anbieter 1:    '))
    kg1 = locale.atof(input('Kerngewicht Anbieter 1:      '))
    fp1 = locale.atof(input('Folienpreis Anbieter 1 / kg: '))
    
    rg2 = locale.atof(input('Rollengewicht Anbieter 2:    '))
    kg2 = locale.atof(input('Kerngewicht Anbieter 2:      '))
    fp2 = locale.atof(input('Folienpreis Anbieter 2 / kg: '))
    
    rg3 = locale.atof(input('Rollengewicht Anbieter 3:    '))
    kg3 = locale.atof(input('Kerngewicht Anbieter 3:      '))
    fp3 = locale.atof(input('Folienpreis Anbieter 3 / kg: '))

    rg4 = locale.atof(input('Rollengewicht Anbieter 4:    '))
    kg4 = locale.atof(input('Kerngewicht Anbieter 4:      '))
    fp4 = locale.atof(input('Folienpreis Anbieter 4 / kg: '))

    rg5 = locale.atof(input('Rollengewicht Anbieter 5:    '))
    kg5 = locale.atof(input('Kerngewicht Anbieter 5:      '))
    fp5 = locale.atof(input('Folienpreis Anbieter 5 / kg: '))

    eg1 = float(rg1) - float(kg1)
    rp1 = float(rg1) * float(fp1)
    efp1 = float(rp1) / float(eg1)
    efpg1 = round(efp1, 3)

    eg2 = float(rg2) - float(kg2)
    rp2 = float(rg2) * float(fp2)
    efp2 = float(rp2) / float(eg2)
    efpg2 = round(efp2, 3)
    
    eg3 = float(rg3) - float(kg3)
    rp3 = float(rg3) * float(fp3)
    efp3 = float(rp3) / float(eg3)
    efpg3 = round(efp3, 3)
    
    eg4 = float(rg4) - float(kg4)
    rp4 = float(rg4) * float(fp4)
    efp4 = float(rp4) / float(eg4)
    efpg4 = round(efp4, 3)
    
    eg5 = float(rg5) - float(kg5)
    rp5 = float(rg5) * float(fp5)
    efp5 = float(rp5) / float(eg5)
    efpg5 = round(efp5, 3)

    print("")
    print("----------------------------------------")
    print("----------------ERGEBNIS----------------")
    print("----------------------------------------")
    print("")
    print("Rollengewicht            : " + str(rg1) + " kg")
    print("Kerngewicht              : " + str(kg1)+ "  kg")
    print("Effektives Foliengewicht : " + str(eg1)+ " kg")
    print("Effektiver Folienpreis   : " + str(efpg1)+ " € / kg")
    print("----------------------------------------")
    print("Rollengewicht            : " + str(rg2) + " kg")
    print("Kerngewicht              : " + str(kg2)+ "  kg")
    print("Effektives Foliengewicht : " + str(eg2)+ " kg")
    print("Effektiver Folienpreis   : " + str(efpg2)+ " € / kg")
    print("----------------------------------------")
    print("Rollengewicht            : " + str(rg3) + " kg")
    print("Kerngewicht              : " + str(kg3)+ "  kg")
    print("Effektives Foliengewicht : " + str(eg3)+ " kg")
    print("Effektiver Folienpreis   : " + str(efpg3)+ " € / kg")
    print("----------------------------------------")   
    print("Rollengewicht            : " + str(rg4) + " kg")
    print("Kerngewicht              : " + str(kg4)+ "  kg")
    print("Effektives Foliengewicht : " + str(eg4)+ " kg")
    print("Effektiver Folienpreis   : " + str(efpg4)+ " € / kg")
    print("----------------------------------------")   
    print("Rollengewicht            : " + str(rg5) + " kg")
    print("Kerngewicht              : " + str(kg5)+ "  kg")
    print("Effektives Foliengewicht : " + str(eg5)+ " kg")
    print("Effektiver Folienpreis   : " + str(efpg5)+ " € / kg")
    print("----------------------------------------")   
   
print("Ende")


# In[ ]:




