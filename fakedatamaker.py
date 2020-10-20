driverId = []
counter = 3
for i in range(10):
    driverId.append('D00{}'.format(counter))
    counter+=1
print(driverId)
drivernames = ['Hamaad Kouma','Sophie Battle','Evan Whitaker','Wilson Laing','Mimi Frost','Rees Simmonds','Maxim Irwin','Hermione Sargent','Katelin OBrien','Roy Dalton']
birthdates = ['06-01-1987','06-02-1987','06-03-1987','06-04-1987','06-05-1987','06-06-1987','06-07-1987','06-08-1987','06-09-1987','06-10-1987',]
startdates = ['06-01-2005','06-02-2005','06-03-2005','06-04-2005','06-05-2005','06-06-2005','06-07-2005','06-08-2005','06-09-2005','06-10-2005',]
areas = ['Baner','Balewadi','Aundh','Pashan','PS','PC','hinjewadi','wakad','tathavde','camp']
carnum = ['MH12KL1365','MH12KL1366','MH12KL1367','MH12KL1368','MH12KL1369','MH12KL1360','MH12KL1361','MH12KL1362','MH12KL1363','MH12KL2004']
CustomerNames = ["Izabelle Ferry","Vivek Bradford","Jordan Hawes","Alfie-Lee Haigh","Billy Osborn","Mercedes Portillo","Nicole Middleton","Stacie Devine","Humera Ingram","Ayman Snider"]
CustomerNumber = []
counter = 3
for i in range(10):
    CustomerNumber.append('C00{}'.format(counter))
    counter+=1
CustomerPhoneNames = ['8893457327','8893457328','8893457329','8893457320','8893457321','8893457322','8893457323','8893457324','8893457325','8893457326']
CustomerEmail = ['devs1229@gmail.com','devs1220@gmail.com','devs1221@gmail.com','devs1222@gmail.com','devs1223@gmail.com','devs1224@gmail.com','devs1225@gmail.com','devs1226@gmail.com','devs1227@gmail.com','devs1228@gmail.com',]
CustomerGender = ['M','F','M','F','M','F','M','F','M','F']
gadditype = ['HONDA CITY','TERRANO','HONDA CITY','TERRANO','HONDA CITY','TERRANO','HONDA CITY','TERRANO','HONDA CITY','TERRANO']
bolpetrol = ['PETROL', 'DIESEL','PETROL', 'DIESEL','PETROL', 'DIESEL','PETROL', 'DIESEL','PETROL', 'DIESEL']
gaddicolor = ['RED' , 'BLACK' , 'WHITE' , 'RED' , 'BLACK' , 'WHITE' , 'RED' , 'BLACK' , 'WHITE' , 'BLACK']
rideNumber = []
counter = 3
for i in range(10):
    rideNumber.append('R000{}'.format(counter))
    counter+=1
counter = 3
vehicalID = []
for i in range(10):
    vehicalID.append('R000{}'.format(counter))
    counter+=1
# INSERT INTO Ride values('R0003', '2019-08-12 10:35:00', 5, 'MH12IJ44432', 'D002', 'C003', '2019-08-12 11:15:02', 0);
for i in range(10):
    print("INSERT INTO Ride values('{ridenum}', '{driverid}', '{vehicaliid}', '{gaddiCOL}', '{typeoffuel}');".format(vehicaliid = vehicalID[i] , ridenum = rideNumber[i],typeoffuel = bolpetrol[i] ,driverid = driverId[i] , GADDINAME = gadditype[i]  , gaddiCOL = gaddicolor[i] ,drivername = drivernames[i] , dobdate = birthdates[i] , somearea = areas[i] , gaddinumber = carnum[i] , startdate = startdates[i]))

