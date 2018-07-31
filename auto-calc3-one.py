import time # imports time module
# ------------------------
# HEADING MESSAGE
# ------------------------
def message3():
    print("\nWelcome to auto-calc3\n"
          "author: Visnu Pritom Chowdhury\n"
          "e-mail: pr3370m@gmail.com\n"
          "\n"
          ">> BETA PHASE | USE WITH CAUTION <<\n")

message3()

# ------------------------
# HYPERNATREMIA
# ------------------------
# from message3 import message3

def hyperna_msg3():
    print("Sodium content in fluids: ")
    print("+-------------------+")
    print("| G-ORS : 75 mmol/l |")
    print("| 1/2 NS: 77 mmol/l |")
    print("| 1/2 AC: 66 mmol/l |")
    print("+-------------------+\n")

def hyperna_calc3():
    print("FLUID VOLUME CALCULATION:")
    wt = float(input(" Weight (kg): "))
    serum = input(" Serum Sodium (mmol/l): ")
    fluid = int(input(" Fluid choice\
\n (1) G-ORS\
\n (2) 1/2 NS\
\n (3) 1/2 Acetate\
\nEnter code: "))
    if fluid == 1:
        fluid = 75
    elif fluid == 2:
        fluid = 77
    elif fluid == 3:
        fluid = 66
    corr = ((10/((float(serum)-float(fluid))/((float(wt)*0.6)+1)))*1000)/24
    print("\nCorrection volume:", round(corr, 2), "ml/hr\n")

    print("25% DIET CURTAIL")
    kwash = str(input(" Marasmus(1) | Kwash(2): "))
    if kwash == "1":
        curt = (wt*10)*0.75
    elif kwash == "2":
        curt = (wt*9)*0.75
    print("\nCurtailed diet:", round(curt, 2), "ml/2h + Salt added.")

# hyperna_msg3()
# hyperna_calc3()
# #input("Press `Enter' to exit.")

# ------------------------
# SEVERE SEPSIS
# ------------------------
# from message3 import message3

def sevsepsis3():
    wt = float(input("Weight (kg): "))
    sam = str(input("SAM-SUW(1) Non-SAM(2): "))
    if sam == "1":
        bolus = float(wt*20)
        bt = float(wt*10)
        print("\nIn Children:")
        print("Bolus 1:", round(bolus, 2), "ml in 1 hr (HS/NS),", "If MAP <50")
        print("Bolus 2:", round(bolus, 2), "ml in 1 hr (HS/NS),", "If MAP <50")
        print("Bolus 3:", round(bt, 2), "ml WBT,", "If MAP <50 mmHg")
        print("START Ionotropes, monitor BP every 15 min\n")
    elif sam == "2":
        bolus = float(wt*20)
        print("\nIn Children:")
        print("\nBolus 1:", round(bolus, 2), "ml in 30 min (HS/NS),", "If MAP <50")
        print("Bolus 2:", round(bolus, 2), "ml in 30 min (HS/NS),", "If MAP <50")
        print("Bolus 3:", round(bolus, 2), "ml in 30 min (HS/NS),", "If MAP <50")
        print("START Ionotropes, monitor BP every 15 min\n")

# sevsepsis3()

# ------------------------
# SEVERE DEHYDRATION
# ------------------------
import sys
# from message3 import message3

def sevdh3():
    wt = float(input("Weight (kg): "))
    raw_age = str(input("Age less than 1 yr? (y/n): "))
    age_n = float(input("Patient's age (number only): "))
    if raw_age == "Y" or raw_age == "y":
        age = float(age_n/12)
    elif raw_age == "N" or raw_age == "n":
        age = age_n
    else:
        print("Please restart the application!")
        input("Press `Enter' to restart")
        sys.exit()
    sam = str(input("SAM(1) / NON-SAM(2): "))
    if sam == "1":
        if age < 0.16666:
            print("\n1st hr:", round(wt*20, 2), "ml IV only (1/2 AC +5% Dex +13 KCL)")
            print("2nd hr:", round(wt*10, 2), "ml IV (1/2 AC +5% Dex +13 KCL) +", \
                  round(wt*10, 2), "ml oral (GORS)")
            print("3rd, 4th hr:", round(wt*10, 2), "ml/hr (GORS)")
            print("Next 8-10 hrs:", round(wt*5, 2), "ml/hr (GORS), \
till correction\n")
        elif age >= 0.16666:
            print("\n1st hr:", round(wt*20, 2), "ml IV only (AC +5% Dex +7 KCL)")
            print("2nd hr:", round(wt*10, 2), "ml IV (AC +5% Dex +7 KCL) +", \
                  round(wt*10, 2), "ml oral (GORS)")
            print("3rd, 4th hr:", round(wt*10, 2), "ml/hr (GORS)")
            print("Next 8-10 hrs:", round(wt*5, 2), "ml/hr (GORS), \
till correction\n")
    elif sam == "2":
        if age < 0.16666:
            print("\n")
            print(round(wt*30, 2), "ml in 1 hr (1/2 AC/NS), then")
            print(round(wt*70, 2), "ml in 5 hrs (1/2 AC/NS)\n")
        elif age >= 0.16666 and age < 1:
            print("\n")
            print(round(wt*30, 2), "ml in 1 hr (AC/NS), then")
            print(round(wt*70, 2), "ml in 5 hrs (AC/NS)\n")
        elif age >= 1:
            print("\n")
            print(round(wt*30, 2), "ml in 1/2 hr (AC/NS), then")
            print(round(wt*70, 2), "ml in 2.5 hrs (AC/NS)\n")
    else:
        print("Please restart the application.")

# sevdh3()

# ------------------------
# SOME DEHYDRATION
# ------------------------
# from message3 import message3

def somedh3():
  wt = float(input("Weight (kg): "))
  sam = str(input("SAM-SUW(1)/ Non-SAM(2) ?\nEnter code: "))
  if sam == "1":
    print("\n", round(wt*10, 2), "ml/hr for 2 hrs, \
then\n", round(wt*5, 2), "ml/hr for 8-10 hrs (GORS)\n")
  elif sam == "2":
    print("\n", round(wt*75, 2), "ml over 4-6 hrs (GORS)\n")
  else:
    print(" \nPlease try again.")

# somedh3()
# input("Press `Enter' to exit.")

# ------------------------
# X% DEHYDRATION
# ------------------------
def xdh3():
    x = float(input("\nPercentage(%) of dehydration (number only): "))
    wt = float(input("Weight (kg): "))
    xdh_corr = wt * (x * 10)
    print(round(xdh_corr, 2), "ml in 4-6 hrs\n")

# xdh3()
# input("Please press `Enter' to exit.")

# ------------------------
# MAP
# ------------------------
# from message3 import message3

def map_bp3():
    sbp = float(input(" Systolic BP (mmHg): "))
    dbp = float(input("Diastolic BP (mmHg): "))
    map_bp = (dbp*2 + sbp)/3
    # MAP formula 2:
    # map_bp = ((sbp-dbp)/3)+dbp
    print("\nMAP is", round(map_bp, 2), "mmHg\
\n>> Reference value (mm Hg): Child >50, Adult >65 <<")


# map_bp3()
# input("Please press `Enter' to exit")

# ------------------------
# DIET
# ------------------------
def diet3():
    wt = float(input("  Weight (kg): "))
    each_feed = float(input("Feed vol (ml): "))
    interval = float(input("Interval (hr): "))
    times = 24 / interval
    t_vol = (each_feed * times) / wt
    kind = str(input(" (1) MIF\
\n (2) MS\
\n (3) MS100\
\n (4) FSRS\
\n (5) 3/4 FSRS\
\n (6) Soyabased formula\
\n (7) 3/4 Soyabased formula\
\nEnter code: "))
    if kind == "1" or kind == "6":
        t_cal = t_vol * 0.68
    elif kind == "2":
        t_cal = t_vol * 0.67
    elif kind == "3":
        t_cal = t_vol * 1.0
    elif kind == "4":
        t_cal = t_vol * 0.70
    elif kind == "5":
        t_cal = t_vol * 0.566
    elif kind == "7":
        t_cal = t_vol * 0.51
    else:
        print("Please try again.")
    print("\nVolume :", round(t_vol, 2), "ml/kg/day")
    print("Calorie:", round(t_cal, 2), "kcal/kg/day \n")

# diet3()

# ------------------------
# DIET
# ------------------------
# from message3 import message3

def drop_rate3():
    vol = float(input("\nRequired IV volume (ml): "))
    hr = float(input("Intended time (hr): "))
    drop_fac = str(input("Infusion set type:\
\n (1) Blood set\
\n (2) Regular set\
\n (3) Micro-burette set\
\nEnter code: "))
    if drop_fac == "1":
        inf_set = 10
    elif drop_fac == "2":
        inf_set = 15
    elif drop_fac == "3":
        inf_set = 60
    dpm = (vol*inf_set)/(hr*60)
    if drop_fac == "1":
        print("\nAt", int(dpm), "drops/min", round(vol, 2), "ml IV will take ~", int(hr), "hrs")
        print("Drop factor : 1 ml =", inf_set, "drops\n")
    elif drop_fac == "2":
        print("\nAt", int(dpm), "drops/min", round(vol, 2), "ml IV will take ~", int(hr), "hrs")
        print("Drop factor : 1 ml =", inf_set, "drops\n")
    elif drop_fac == "3":
        print("\nAt", int(dpm), "drops/min", round(vol, 2), "ml IV will take ~", int(hr), "hrs")
        print("Drop factor : 1 ml =", inf_set, "microdrops\n")

# drop_rate3()

# ------------------------
# MAIN
# ------------------------
# from message3 import message3
# imports the function called message, from the file named message

def main():
    choice = str(input("Choose your module: \
    \n [1] Hypernatremia\
    \n [2] Fluid \
    \n [3] MAP \
    \n [4] Diet\
    \n [5] Drops/min\
    \nEnter the code [1-5]: "))
    if choice == "1":
        hyperna_msg3()
        hyperna_calc3()
        # from hyperna3 import hyperna_msg3
        # from hyperna3 import hyperna_calc3
    elif choice == "2":
        choice_2 = str(input("Choose from the list:\
            \n [1] Severe Sepsis\
            \n [2] Severe Dehydration\
            \n [3] Some Dehydration\
            \n [4] `X'% dehydration\
            \nEnter the code [1-4]: "))
        if choice == "2" and choice_2 == "1":
            sevsepsis3()
            # from sevsepsis3 import sevsepsis3
        elif choice == "2" and choice_2 == "2":
            sevdh3()
            # from sevdh3 import sevdh3
        elif choice == "2" and choice_2 == "3":
            somedh3()
            # from somedh3 import somedh3
        elif choice == "2" and choice_2 == "4":
            xdh3()
            # from xdh3 import xdh3
    elif choice == "3":
        map_bp3()
        # from map_bp3 import map_bp3
    elif choice == "4":
        diet3()
        # from diet3 import diet3
    elif choice == "5":
        drop_rate3()
        # from drop_rate3 import drop_rate3
    else:
        print("Please try again.")
    user_resp = input("Are you done? [y/n]: ")
    user_resp_l = user_resp.lower()
    if user_resp_l == "n":
        main()
    else:
        print("\n>>>> Thank you for using auto-calc3! <<<<\
              \n> This program with close in 3 seconds! <")
        # exit()

if __name__ == "__main__":
    main()

time.sleep(3) # closes the terminal after 3 seconds