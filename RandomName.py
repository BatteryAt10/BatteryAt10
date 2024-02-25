import random
Valid = "F"
print("Welcome To Random Name genorator, Pick Gender And Nation And We Will create a random name for you :)")
def AllNationGenderFirstNameList() :
   global british_male_names
   british_male_names = [
    "James", "William", "Thomas", "David", "John",
    "Robert", "Michael", "Daniel", "Richard", "Christopher",
    "Paul", "Mark", "Andrew", "Stephen", "Philip",
    "Edward", "Peter", "Simon", "Nicholas", "Jonathan",
    "Benjamin", "Alexander", "Matthew", "George", "Charles"
    ]
   global british_female_names
   british_female_names = [
    "Emily", "Olivia", "Sophie", "Charlotte", "Amelia",
    "Jessica", "Grace", "Lucy", "Emma", "Ella",
    "Mia", "Chloe", "Alice", "Lily", "Hannah",
    "Georgia", "Ellie", "Abigail", "Megan", "Isabella",
    "Eva", "Ruby", "Eleanor", "Freya", "Scarlett"
    ]
   global french_female_names
   french_female_names = [
    "Camille", "Chloé", "Émilie", "Fleur", "Gabrielle",
    "Isabelle", "Juliette", "Léa", "Manon", "Nathalie",
    "Océane", "Pauline", "Rosalie", "Sylvie", "Valérie",
    "Adèle", "Béatrice", "Céline", "Delphine", "Elise",
    "Florence", "Geneviève", "Hélène", "Inès", "Joséphine"
    ]
   global french_male_names
   french_male_names = [
    "Antoine", "Baptiste", "Cédric", "Damien", "Étienne",
    "François", "Gilles", "Hugo", "Julien", "Luc",
    "Mathieu", "Nicolas", "Olivier", "Pierre", "Quentin",
    "Romain", "Sébastien", "Thierry", "Vincent", "Xavier",
    "Yannick", "Zacharie", "Arnaud", "Benjamin", "Claude"
    ]
   global chinese_male_names
   chinese_male_names = [
    "Wei", "Jian", "Kai", "Xiao", "Chen",
    "Tao", "Yang", "Shen", "Jun", "Bo",
    "Feng", "Hao", "Li", "Ming", "Qiang",
    "Wei", "Xing", "Yi", "Zhi", "Zhong",
    "Chang", "Dawei", "Guang", "Hong", "Jin"
   ]
   global chinese_female_names
   chinese_female_names = [
    "Mei", "Xia", "Li", "Yuan", "Jing",
    "Lin", "Hua", "Juan", "Yan", "Xiu",
    "Xin", "Yu", "Qing", "Rui", "Fang",
    "Hong", "Hui", "Lan", "Na", "Wei",
    "Ying", "Zhen", "Ai", "Bao", "Chun"]
   global aussie_male_names
   aussie_male_names = [
    "Jack", "William", "Thomas", "James", "Oliver",
    "Noah", "Lucas", "Liam", "Ethan", "Mason",
    "Alexander", "Henry", "Charlie", "Daniel", "Samuel",
    "Max", "Benjamin", "Jacob", "Joshua", "Ryan",
    "Aiden", "Harry", "Isaac", "Oscar", "Cooper"
    ]
   global aussie_female_names
   aussie_female_names = [
    "Charlotte", "Olivia", "Ava", "Amelia", "Mia",
    "Harper", "Sophia", "Isabella", "Grace", "Ella",
    "Emily", "Chloe", "Ruby", "Lily", "Zoe",
    "Scarlett", "Matilda", "Sophie", "Emma", "Abigail",
    "Hannah", "Eva", "Layla", "Sienna", "Lucy"
    ]   
   global irish_male_names
   irish_male_names = [
        "Sean", "Patrick", "Conor", "Liam", "Cian",
        "Finn", "Cillian", "Darragh", "Cormac", "Eoin",
        "Aidan", "Declan", "Cathal", "Rory", "Ronan",
        "Tiernan", "Niall", "Oisin", "Tadhg", "Dermot",
        "Brendan", "Malachy", "Oscar", "Padraig", "Ruairi"
    ]

   global irish_female_names
   irish_female_names = [
        "Aoife", "Ciara", "Niamh", "Saoirse", "Siobhan",
        "Roisin", "Orla", "Eabha", "Maeve", "Fiona",
        "Sinead", "Aisling", "Grainne", "Bridget", "Molly",
        "Clodagh", "Deirdre", "Mairead", "Brigid", "Caoimhe",
        "Emer", "Aine", "Eimear", "Aoibheann", "Caitlin"
    ]

   global spanish_male_names
   spanish_male_names = [
        "Santiago", "Mateo", "Alejandro", "Sebastián", "Diego",
        "Carlos", "Javier", "Francisco", "Daniel", "Pablo",
        "Manuel", "José", "Andrés", "Luis", "Jorge",
        "Miguel", "Antonio", "Gabriel", "David", "Fernando",
        "Emilio", "Raúl", "Roberto", "Alberto", "Mario"
    ]

   global spanish_female_names
   spanish_female_names = [
        "Sofía", "Isabella", "Valentina", "Camila", "Mariana",
        "Lucía", "Emma", "Elena", "Ana", "Julia",
        "Carmen", "María", "Lola", "Laura", "Paula",
        "Adriana", "Clara", "Natalia", "Andrea", "Rosa",
        "Luisa", "Antonia", "Diana", "Nerea", "Beatriz"
    ]

   global american_male_names
   american_male_names = [
        "John", "Michael", "Christopher", "James", "Robert",
        "William", "David", "Joseph", "Daniel", "Matthew",
        "Anthony", "Andrew", "Steven", "Brian", "Kevin",
        "Thomas", "Richard", "Timothy", "Jason", "Jeffrey",
        "Mark", "Scott", "Eric", "Justin", "Ryan"
    ]

   global american_female_names
   american_female_names = [
        "Jennifer", "Jessica", "Amanda", "Ashley", "Sarah",
        "Melissa", "Nicole", "Elizabeth", "Stephanie", "Heather",
        "Tiffany", "Amber", "Michelle", "Emily", "Rachel",
        "Lauren", "Brittany", "Megan", "Kayla", "Samantha",
        "Christina", "Amy", "Rebecca", "Danielle", "Laura"
    ]

   global indian_male_names
   indian_male_names = [
        "Aarav", "Aarush", "Aditya", "Arjun", "Dhruv",
        "Ishaan", "Kabir", "Krishna", "Rohan", "Shaurya",
        "Vedant", "Virat", "Yuvraj", "Advik", "Aryan",
        "Dev", "Hrithik", "Jay", "Kunal", "Mayank",
        "Neel", "Raj", "Rishi", "Shiv", "Vijay"
    ]

   global indian_female_names
   indian_female_names = [
        "Aanya", "Aaradhya", "Anaya", "Diya", "Ishani",
        "Kiara", "Leela", "Meera", "Neha", "Pari",
        "Radha", "Riya", "Saanvi", "Sia", "Tara",
        "Trisha", "Vanya", "Vidya", "Zara", "Aditi",
        "Anika", "Isha", "Jiya", "Kavya", "Mira"
    ]
   global danish_male_names
   danish_male_names = [
        "Lars", "Peter", "Jens", "Morten", "Henrik",
        "Thomas", "Anders", "Christian", "Michael", "Søren",
        "Martin", "Niels", "Kim", "Ole", "Jan",
        "Mads", "Jesper", "Kasper", "Jonas", "Lasse",
        "Jakob", "Frederik", "Erik", "Rasmus", "Kristian" ]

   global danish_female_names
   danish_female_names = [
        "Anne", "Mette", "Hanne", "Lene", "Lone",
        "Karen", "Louise", "Marianne", "Tine", "Pernille",
        "Camilla", "Susanne", "Gitte", "Gitte", "Mette",
        "Marie", "Tina", "Sanne", "Line", "Lena",
        "Tanja", "Maria", "Signe", "Mette", "Charlotte"
     ]

AllNationGenderFirstNameList()

def AllNationGenderLastNameList():
    global british_last_names
    british_last_names = [
        "Smith", "Jones", "Taylor", "Brown", "Williams",
        "Wilson", "Evans", "Thomas", "Roberts", "Johnson",
        "Lewis", "Walker", "Robinson", "Wood", "Thompson",
        "White", "Watson", "Jackson", "Wright", "Harris",
        "Clark", "King", "Baker", "Edwards", "Green"
    ]

    global french_last_names
    french_last_names = [
        "Martin", "Bernard", "Dubois", "Thomas", "Robert",
        "Richard", "Petit", "Durand", "Leroy", "Moreau",
        "Simon", "Laurent", "Lefebvre", "Michel", "Garcia",
        "David", "Bertrand", "Roux", "Vincent", "Fournier",
        "Morel", "Girard", "Andre", "Lefevre", "Mercier"
    ]

    global chinese_last_names
    chinese_last_names = [
        "Wang", "Li", "Zhang", "Liu", "Chen",
        "Yang", "Huang", "Zhao", "Zhu", "Zhou",
        "Xu", "Sun", "Ma", "Hu", "Gao",
        "Lin", "He", "Guo", "Lu", "Wu",
        "Cheng", "Jiang", "Tang", "Xie", "Song"
    ]

    global aussie_last_names
    aussie_last_names = [
        "Smith", "Jones", "Brown", "Wilson", "Taylor",
        "Johnson", "White", "Clark", "Williams", "Walker",
        "Thompson", "Anderson", "Thomas", "Harris", "Lee",
        "Robinson", "Wright", "Evans", "Martin", "Jackson",
        "Young", "Adams", "Lewis", "Hill", "King"
    ]

    global irish_last_names
    irish_last_names = [
        "Murphy", "Kelly", "Sullivan", "Walsh", "Smith",
        "O'Brien", "Byrne", "Ryan", "O'Connor", "O'Neill",
        "McCarthy", "O'Sullivan", "Lynch", "Doherty", "Kennedy",
        "Gallagher", "Doherty", "Doyle", "McMahon", "O'Reilly",
        "Kennedy", "Murray", "Quinn", "Moore", "Walsh"
    ]

    global spanish_last_names
    spanish_last_names = [
        "García", "Fernández", "González", "Rodríguez", "López",
        "Martínez", "Sánchez", "Pérez", "Martín", "Gómez",
        "Ruiz", "Hernández", "Jiménez", "Díaz", "Moreno",
        "Álvarez", "Romero", "Navarro", "Torres", "Domínguez",
        "Vázquez", "Ramos", "Gil", "Ramírez", "Serrano"
    ]

    global american_last_names
    american_last_names = [
        "Smith", "Johnson", "Williams", "Brown", "Jones",
        "Miller", "Davis", "West", "Rodriguez", "Martinez",
        "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
        "Thomas", "Taylor", "Moore", "Jackson", "Martin",
        "Lee", "Perez", "Thompson", "White", "Harris"
    ]

    global indian_last_names
    indian_last_names = [
        "Patel", "Sharma", "Singh", "Kumar", "Das",
        "Pandey", "Yadav", "Gupta", "Verma", "Jha",
        "Shah", "Bose", "Mukherjee", "Chatterjee", "Malik",
        "Chauhan", "Rao", "Rajput", "Reddy", "Sinha",
        "Thakur", "Nair", "Jain", "Khan", "Dutta"
    ]
    global danish_last_names
    danish_last_names = [
        "Nielsen", "Hansen", "Pedersen", "Andersen", "Christensen",
        "Larsen", "Jensen", "Sørensen", "Rasmussen", "Petersen",
        "Madsen", "Olsen", "Thomsen", "Kristensen", "Jakobsen",
        "Johansen", "Olesen", "Mortensen", "Møller", "Jacobsen",
        "Knudsen", "Frederiksen", "Damgaard", "Lund", "Hojlund"
    ]

AllNationGenderLastNameList()

def GenderChoise():
  global Valid
  global Gender
  while Valid == "F" :
     User = input("M Or F = ")
     if User == "M" :
         Gender = "Male"
         break
     elif User == "F" :
         Gender = "Female"
         break
     else :
         print("Invalid Gender")
         Valid = "F"

GenderChoise()

def NationType():
   global Nation
   Valid = "F"

   while Valid == "F":
      User = input("""Please Select Your Library Of Nationalities
                   N1 = English N2 = French N3 = Chinese 
                   N4 = Australian N5 = Irish N6 = American
                   N7 = Indian N8 = Spanish N9 = Danish
                   """)
      if User == "N1":
         Nation = "English"
         break
      elif User == "N2":
         Nation = "French"
         break 
      elif User == "N3":
         Nation = "Chinese"
         break 
      elif User == "N4":
         Nation = "Aussie"
         break 
      elif User == "N5":
         Nation = "Irish"
         break 
      elif User == "N6":
         Nation = "American"
         break 
      elif User == "N7":
         Nation = "Indian"
         break 
      elif User == "N8":
         Nation = "Spanish"
         break 
      elif User == "N9":
         Nation = "Danish"
         break 
      else:
         print("Invalid Nation, Make Sure You Use N1 - N9")
         Valid = "F"

NationType()

def FirstName() :
   global Fname 
   if Gender =="Male" :
      if Nation == "English" :
         Fname = random.choice(british_male_names)
      elif Nation == "French" :
          Fname = random.choice(french_male_names)
      elif Nation == "Chinese" :
          Fname = random.choice(chinese_male_names)      
      elif Nation == "Aussie" :
          Fname = random.choice(aussie_male_names)  
      elif Nation == "Irish" :
          Fname = random.choice(irish_male_names)
      elif Nation == "American" :
          Fname = random.choice(american_male_names)
      elif Nation == "Indian" :
          Fname = random.choice(indian_male_names)
      elif Nation == "Spanish" :
          Fname = random.choice(spanish_male_names)
      elif Nation == "Danish" :
          Fname = random.choice(danish_male_names)
   else :
      if Nation == "English" :
         Fname = random.choice(british_female_names)
      elif Nation == "French" :
          Fname = random.choice(french_female_names)
      elif Nation == "Chinese" :
          Fname = random.choice(chinese_female_names)      
      elif Nation == "Aussie" :
          Fname = random.choice(aussie_female_names)  
      elif Nation == "Irish" :
          Fname = random.choice(irish_female_names)
      elif Nation == "American" :
          Fname = random.choice(american_female_names)
      elif Nation == "Indian" :
          Fname = random.choice(indian_female_names)
      elif Nation == "Spanish" :
          Fname = random.choice(spanish_female_names)
      elif Nation == "Danish" :
          Fname = random.choice(danish_female_names)

FirstName()

def lastname() :
      global Lname
      if Nation == "English" :
         Lname = random.choice(british_last_names)
      elif Nation == "French" :
          Lname = random.choice(french_last_names)
      elif Nation == "Chinese" :
          Lname = random.choice(chinese_last_names)      
      elif Nation == "Aussie" :
          Lname = random.choice(aussie_last_names)  
      elif Nation == "Irish" :
          Lname = random.choice(irish_last_names)
      elif Nation == "American" :
          Lname = random.choice(american_last_names)
      elif Nation == "Indian" :
          Lname = random.choice(indian_last_names)
      elif Nation == "Spanish" :
          Lname = random.choice(spanish_last_names)
      elif Nation == "Danish" :
          Lname = random.choice(danish_last_names)

def Fullname() :
    global FUname
    lastname()
    FUname = Fname + " " + Lname
    print("Your Random Name is",FUname)
Fullname()

