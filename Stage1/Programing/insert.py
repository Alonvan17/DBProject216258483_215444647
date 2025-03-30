import random
from datetime import datetime,timedelta

male_names = [
    "Aaron", "Adam", "Adrian", "Aidan", "Alan", "Albert", "Alex", "Alexander", "Alfred", "Andrew",
    "Andy", "Anthony", "Arthur", "Asher", "Austin", "Barry", "Ben", "Benjamin", "Bernard", "Bill",
    "Billy", "Blake", "Bob", "Bobby", "Brad", "Bradley", "Brandon", "Brendan", "Brian", "Bruce",
    "Bryan", "Caleb", "Calvin", "Cameron", "Carl", "Carlos", "Carter", "Charles", "Charlie", "Chris",
    "Christian", "Christopher", "Clarence", "Clark", "Clayton", "Clifford", "Clinton", "Clyde", "Cody", "Colin",
    "Connor", "Corey", "Cory", "Craig", "Curtis", "Dale", "Dan", "Daniel", "Darren", "Dave",
    "David", "Dean", "Dennis", "Derek", "Derrick", "Desmond", "Devin", "Dillon", "Dominic", "Don",
    "Donald", "Doug", "Douglas", "Drew", "Duane", "Dustin", "Dwayne", "Dwight", "Dylan", "Earl",
    "Edgar", "Eddie", "Edmund", "Edward", "Edwin", "Eli", "Elias", "Elijah", "Elliot", "Elliott",
    "Ellis", "Elmer", "Emmanuel", "Enrique", "Eric", "Erik", "Ernest", "Ethan", "Eugene", "Evan",
    "Everett", "Felix", "Floyd", "Francis", "Frank", "Frankie", "Franklin", "Fred", "Freddie", "Frederick",
    "Gabriel", "Gareth", "Garrett", "Garry", "Gary", "Gavin", "Geoffrey", "George", "Gerald", "Gilbert",
    "Glen", "Glenn", "Gordon", "Graham", "Grant", "Greg", "Gregg", "Gregory", "Guy", "Harold",
    "Harry", "Harvey", "Hayden", "Heath", "Henry", "Herbert", "Herman", "Howard", "Hugh", "Ian",
    "Isaac", "Isaiah", "Ivan", "Jack", "Jackson", "Jacob", "Jake", "James", "Jamie", "Jared",
    "Jason", "Jasper", "Jay", "Jeff", "Jeffery", "Jeffrey", "Jeremiah", "Jeremy", "Jerome", "Jerry",
    "Jesse", "Jim", "Jimmy", "Joe", "Joel", "John", "Johnny", "Jon", "Jonathan", "Jordan",
    "Jorge", "Jose", "Joseph", "Josh", "Joshua", "Juan", "Julian", "Justin", "Keith", "Kelly",
    "Ken", "Kenneth", "Kent", "Kevin", "Kirk", "Kyle", "Lance", "Larry", "Lawrence", "Lee",
    "Leo", "Leon", "Leonard", "Leroy", "Leslie", "Levi", "Lewis", "Lloyd", "Logan", "Louis",
    "Lucas", "Luis", "Luke", "Malcolm", "Manuel", "Marc", "Marcus", "Mark", "Marlon", "Marshall",
    "Martin", "Marvin", "Mason", "Mathew", "Matthew", "Maurice", "Max", "Maxwell", "Melvin", "Michael",
    "Micheal", "Miguel", "Mike", "Mitchell", "Morris", "Nathan", "Nathaniel", "Neal", "Neil", "Nelson",
    "Nicholas", "Nick", "Noah", "Norman", "Oliver", "Omar", "Oscar", "Owen", "Parker", "Patrick",
    "Paul", "Pedro", "Perry", "Pete", "Peter", "Philip", "Phillip", "Quentin", "Ralph", "Randy",
    "Ray", "Raymond", "Reginald", "Rex", "Richard", "Rick", "Ricky", "Robert", "Roberto", "Rodney",
    "Roger", "Roland", "Ron", "Ronald", "Ronnie", "Ross", "Roy", "Ruben", "Russell", "Ryan",
    "Sam", "Samuel", "Scott", "Sean", "Seth", "Shane", "Shawn", "Sidney", "Spencer", "Stanley",
    "Stephen", "Steve", "Steven", "Stewart", "Stuart", "Sydney", "Tanner", "Taylor", "Ted", "Teddy",
    "Terence", "Terry", "Theodore", "Thomas", "Tim", "Timothy", "Toby", "Todd", "Tom", "Tommy",
    "Tony", "Travis", "Trevor", "Troy", "Tyler", "Vernon", "Victor", "Vincent", "Wade", "Wallace",
    "Walter", "Warren", "Wayne", "Wesley", "Will", "William", "Willie", "Wyatt", "Xavier", "Zachary",
    "Zach", "Aaron", "Adam", "Adrian", "Aidan", "Alan", "Albert", "Alex", "Alexander", "Alfred",
    "Andrew", "Andy", "Anthony", "Arthur", "Asher", "Austin", "Barry", "Ben", "Benjamin", "Bernard",
    "Bill", "Billy", "Blake", "Bob", "Bobby", "Brad", "Bradley", "Brandon", "Brendan", "Brian",
    "Bruce", "Bryan", "Caleb", "Calvin", "Cameron", "Carl", "Carlos", "Carter", "Charles", "Charlie",
    "Chris", "Christian", "Christopher", "Clarence", "Clark", "Clayton", "Clifford", "Clinton", "Clyde", "Cody",
    "Colin", "Connor", "Corey", "Cory", "Craig", "Curtis", "Dale", "Dan", "Daniel", "Darren",
    "Dave", "David", "Dean", "Dennis", "Derek", "Derrick", "Desmond", "Devin", "Dillon", "Dominic",
    "Don", "Donald", "Doug", "Douglas", "Drew", "Duane", "Dustin", "Dwayne", "Dwight", "Dylan",
    "Earl", "Edgar", "Eddie", "Edmund", "Edward", "Edwin", "Eli", "Elias", "Elijah", "Elliot",
    "Elliott", "Ellis", "Elmer", "Emmanuel", "Enrique", "Eric", "Erik", "Ernest", "Ethan", "Eugene",
    "Evan", "Everett", "Felix", "Floyd", "Francis", "Frank", "Frankie", "Franklin", "Fred", "Freddie",
    "Frederick", "Gabriel", "Gareth", "Garrett", "Garry", "Gary", "Gavin", "Geoffrey", "George", "Gerald",
    "Gilbert", "Glen", "Glenn", "Gordon", "Graham", "Grant", "Greg", "Gregg", "Gregory", "Guy",
    "Harold", "Harry", "Harvey", "Hayden", "Heath", "Henry", "Herbert", "Herman", "Howard", "Hugh",
    "Ian", "Isaac", "Isaiah", "Ivan", "Jack", "Jackson", "Jacob", "Jake", "James", "Jamie",
    "Jared", "Jason", "Jasper", "Jay", "Jeff", "Jeffery", "Jeffrey", "Jeremiah", "Jeremy", "Jerome",
    "Jerry", "Jesse", "Jim", "Jimmy", "Joe", "Joel", "John", "Johnny", "Jon", "Jonathan",
    "Jordan", "Jorge", "Jose", "Joseph", "Josh", "Joshua", "Juan", "Julian", "Justin", "Keith",
    "Kelly", "Ken", "Kenneth", "Kent", "Kevin", "Kirk", "Kyle", "Lance", "Larry", "Lawrence",
    "Lee", "Leo", "Leon", "Leonard", "Leroy", "Leslie", "Levi", "Lewis", "Lloyd", "Logan",
    "Louis", "Lucas", "Luis", "Luke", "Malcolm", "Manuel", "Marc", "Marcus", "Mark", "Marlon",
    "Marshall", "Martin", "Marvin", "Mason", "Mathew", "Matthew", "Maurice", "Max", "Maxwell", "Melvin",
    "Michael", "Micheal", "Miguel", "Mike", "Mitchell", "Morris", "Nathan", "Nathaniel", "Neal", "Neil",
    "Nelson", "Nicholas", "Nick", "Noah", "Norman", "Oliver", "Omar", "Oscar", "Owen", "Parker",
    "Patrick", "Paul", "Pedro", "Perry", "Pete", "Peter", "Philip", "Phillip", "Quentin", "Ralph",
    "Randy", "Ray", "Raymond", "Reginald", "Rex", "Richard", "Rick", "Ricky", "Robert", "Roberto",
    "Rodney", "Roger", "Roland", "Ron", "Ronald", "Ronnie", "Ross", "Roy", "Ruben", "Russell",
    "Ryan", "Sam", "Samuel", "Scott", "Sean", "Seth", "Shane", "Shawn", "Sidney", "Spencer",
    "Stanley", "Stephen", "Steve", "Steven", "Stewart", "Stuart", "Sydney", "Tanner", "Taylor", "Ted",
    "Teddy", "Terence", "Terry", "Theodore", "Thomas", "Tim", "Timothy", "Toby", "Todd", "Tom",
    "Tommy", "Tony", "Travis", "Trevor", "Troy", "Tyler", "Vernon", "Victor", "Vincent", "Wade",
    "Wallace", "Walter", "Warren", "Wayne", "Wesley", "Will", "William", "Willie", "Wyatt", "Xavier",
    "Zachary","Zach"
]

female_names = [
    "Emma", "Olivia", "Ava", "Isabella", "Sophia", "Mia", "Amelia", "Harper",
    "Evelyn", "Abigail", "Emily", "Ella", "Elizabeth", "Camila", "Luna", "Sofia",
    "Avery", "Mila", "Aria", "Scarlett", "Penelope", "Layla", "Chloe", "Victoria",
    "Madison", "Eleanor", "Grace", "Nora", "Riley", "Zoey", "Hannah", "Hazel",
    "Lily", "Ellie", "Violet", "Lillian", "Zoe", "Stella", "Aurora", "Natalie",
    "Emilia", "Everly", "Leah", "Aubrey", "Willow", "Addison", "Lucy", "Audrey",
    "Bella", "Nova", "Brooklyn", "Paisley", "Savannah", "Claire", "Skylar",
    "Isla", "Genesis", "Naomi", "Elena", "Caroline", "Eliana", "Anna", "Maya",
    "Valentina", "Ruby", "Kennedy", "Ivy", "Ariana", "Aaliyah", "Cora", "Madelyn",
    "Alice", "Kinsley", "Hailey", "Gabriella", "Allison", "Gianna", "Serenity",
    "Samantha", "Sarah", "Autumn", "Quinn", "Eva", "Piper", "Sophie", "Sadie",
    "Delilah", "Josephine", "Nevaeh", "Adeline", "Arya", "Emery", "Lydia",
    "Clara", "Vivian", "Madeline", "Peyton", "Julia","Rylee"
]

ranks = ['sailor','captain','admiral']

israeli_coastal_cities = [
    "Tel Aviv", "Haifa", "Netanya", "Akko",
    "Ashdod", "Caesarea", "Herzliya", "Bat Yam",
    "Hadera","Nahariya"
]

# Function to generate a random date within a range
def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

start_date = datetime.strptime('2022-05-20', '%Y-%m-%d')
end_date = datetime.strptime('2024-05-20', '%Y-%m-%d')

# Generate a list of 1000 random dates
random_dates = [random_date(start_date, end_date).strftime('%Y-%m-%d') for _ in range(1000)]

def main():
    f = open('insert.sql', 'w')
    #crew
    for i in range(401,801):
        size = random.randint(25,36)
        f.write(f"INSERT INTO Crew (c_ID,C_Size) VALUES ({i},{size});\n")

    #soldier
    for i in range(1001,5001):
        name = random.choice(male_names)
        rank = random.choice(ranks)
        crew = random.randint(401,801)
        f.write(f"INSERT INTO Soldier (s_ID,name,rank, c_ID) VALUES ({i},\'"+name+"\',\'"+rank+f"\',{crew});\n")


    #commander
    for i in range(1002,1801,2):
        f.write(f"INSERT INTO Commander (s_ID,C_ID) VALUES ({i},{int((i-1000)/2+400)});\n")

    #base
    for i in range(101,201):
        loc = random.choice(israeli_coastal_cities)
        f.write(f"INSERT INTO Base (Base_ID,location) VALUES ({i},\'"+loc+"\');\n")

    #sea vessel
    for i in range(401,801):
        launcher = random.randint(8,31)
        female = random.choice(female_names)
        capac = random.randint(80,121)
        firstDate = "to_date(\'" + random.choice(random_dates) + "\',\'yyyy-mm-dd\')"
        secondDate = "to_date(\'" + random.choice(random_dates) + "\',\'yyyy-mm-dd\')"
        base = random.randint(101,201)
        f.write(f"INSERT INTO Sea_Vessel (Sea_ID,launcher_amount,nickname,capacity,test_date,c_id,lease_expiration_date,base_id) "
                f"VALUES ({i},{launcher},\'"+female+f"\',{capac},"+firstDate+f",{i},"+secondDate+f",{base});\n")

    #submarine
    for i in range(401,601):
        dens = random.randint(20,101)
        dep = random.randint(2001,3001)
        f.write(f"INSERT INTO Submarine (Sea_ID,oxygen_density,max_depth) VALUES ({i},{dens},{dep});\n")

    #warship
    for i in range(601,801):
        can = random.randint(5,21)
        f.write(f"INSERT INTO Warship (Sea_ID,cannons_amount) VALUES ({i},{can});\n")

    #destroyer
    for i in range(701,801):
        f.write(f"INSERT INTO Destroyer (Sea_ID) VALUES ({i});\n")

    #missile_ship
    for i in range(601,701):
        misCapac = random.randint(50,301)
        f.write(f"INSERT INTO Missile_ship (Sea_ID,missle_capacity) VALUES ({i},{misCapac});\n")


if __name__ == "__main__":
    main()