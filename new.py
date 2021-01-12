import subprocess as sp
import pymysql
import pymysql.cursors



def insertSong():
	try:
        # Takes emplyee details as input
		row = {}
		print("Enter new track details: ")
		row["TrackID"] = int(input("TrackID: "))
		row["TrackName"] = input("TrackName: ")
		row["TrackTime"] = input("TrackTime: ")
		row["AlbumID"] = int(input("AlbumID: "))
		row["Genre"] = input("Genre: ")

		"""
        In addition to taking input, you are required to handle domain errors as well
        For example: the SSN should be only 9 characters long
        Sex should be only M or F
        If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
        HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
		"""

		query = "INSERT INTO TRACK(TrackID,TrackName,TrackTime,AlbumID,Genre) VALUES('%d', '%s', '%s', '%d', '%s')" %(row["TrackID"], row["TrackName"], row["TrackTime"], row["AlbumID"],row["Genre"])

		print(query)
		cur.execute(query)
		con.commit()

		print("Inserted Into Database")

	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print (">>>>>>>>>>>>>", e)
        
	return

def insertAlbum():
	try:
        # Takes emplyee details as input
		row = {}
		print("Enter new Album details: ")
		row["AlbumID"] = int(input("AlbumID: "))
		row["AlbumName"] = input("AlbumName: ")
		row["Number_of_Tracks"] = int(input("No._of_tracks_in_album: "))

		"""
        In addition to taking input, you are required to handle domain errors as well
        For example: the SSN should be only 9 characters long
        Sex should be only M or F
        If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
        HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
		"""

		query = "INSERT INTO ALBUM(AlbumID,AlbumName,Number_of_Tracks) VALUES('%d', '%s', '%d')" %(row["AlbumID"], row["AlbumName"], row["Number_of_Tracks"])

		print(query)
		cur.execute(query)
		con.commit()

		print("Inserted Into Database")

	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print (">>>>>>>>>>>>>", e)

def renameSong():
	try:
        # Takes emplyee details as input
		row = {}
		print("Enter details to rename song: ")
		x = int(input("TrackID: "))
		try:
			query1 = "SELECT TrackID FROM TRACK where TrackID=%d"
            
			cur.execute(query1%x)
			con.commit()
			row["TrackName"] = input("TrackName: ")
            #d = input("TrackName: ")

		except:
			print("TrackID Doesn't Exist")
		"""
        In addition to taking input, you are required to handle domain errors as well
        For example: the SSN should be only 9 characters long
        Sex should be only M or F
        If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
        HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
		"""

		query = "UPDATE TRACK SET TrackName='%s' where TrackID='%d'"
		val=(row["TrackName"],x)

        
		cur.execute(query%val)
		con.commit()

		print("Inserted Into Database")

	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print (">>>>>>>>>>>>>", e)
        
	return
def changeFrequency():
	try:
        # Takes emplyee details as input
		row = {}
		print("Enter Track Id to change It's Frequency: ")
		x = int(input("TrackID: "))
		try:
			query1 = "SELECT TrackID FROM FREQUENCY where TrackID=%d"
            
			cur.execute(query1%x)
			con.commit()
            #row["Count"]+=1;
			row["Count"] = int(input("Count: "))
			query = "UPDATE FREQUENCY SET Count='%d' where TrackID='%d'"
			val=(row["Count"],x)
			cur.execute(query%val)
			con.commit()

		except:
			print("TrackID Doesn't Exist")
		"""
        In addition to taking input, you are required to handle domain errors as well
        For example: the SSN should be only 9 characters long
        Sex should be only M or F
        If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
        HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
		"""

		query2 = "INSERT into FREQUENCY(TrackID,Count) values('%d','%d')" %(x,row["Count"]) 

        
		cur.execute(query2)
		con.commit()

		print("Inserted Into Database")

	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print (">>>>>>>>>>>>>", e)
        
	return

def delete_album():
	try:
		global cur
		row = {}
		print("Enter Album ID:")
		g=int(input())
		query="DELETE FROM ALBUM WHERE AlbumID='%d'"
        #q6="SELECT TrackID FROM TRACK WHERE AlbumID=%d"
		q1="DELETE FROM FREQUENCY where TrackID=(select TrackID from TRACK where AlbumID='%d')"
		q2="DELETE FROM SINGER where PersonID=(select PersonID from PERSON where TrackID=(select TrackID from TRACK where AlbumID='%d'))"
		q3="DELETE FROM MUSIC_DIRECTOR where PersonID=(select PersonID from PERSON where TrackID=(select TrackID from TRACK where AlbumID='%d'))"
		q4="DELETE FROM LYRICIST where PersonID=(select PersonID from PERSON where TrackID=(select TrackID from TRACK where AlbumID='%d'))"
		q5="DELETE FROM RELEASE_DATE where TrackID=(select TrackID from TRACK where AlbumID='%d')"
		q6="DELETE FROM PERSON where TrackID=(select TrackID from TRACK where AlbumID='%d')"
		q7="DELETE From TRACK where AlbumID = '%d' "
		cur.execute(query%g)
		cur.execute(q1%g)
		cur.execute(q2%g)
		cur.execute(q3%g)
		cur.execute(q4%g)
		cur.execute(q5%g)
		cur.execute(q6%g)
		cur.execute(q7%g)
		con.commit()
	except Exception as e:
		con.rollback()
		print("Failed to delete Album")

def songs_of_singer():
	try:
		print("Singername:")
		g=input()
		query="SELECT TrackName from TRACK,PERSON,PERSONS_TRACKS AS PT WHERE Person_Name='%s' and PERSON.PersonID=PT.PersonID and PT.TrackID=TRACK.TrackID"
		cur.execute(query%g)
		con.commit()
		data = cur.fetchall()
		print(data)


	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print (">>>>>>>>>>>>>", e)
        
	return

	print("Not implemented")


def highest_frequency():
	try:
		print("hi")
		query="SELECT TrackName from TRACK where TrackID=(select TrackID from FREQUENCY WHERE FREQUENCY.Count=(select Max(FREQUENCY.Count) from FREQUENCY))"
		cur.execute(query)
		con.commit()
		data = cur.fetchall()
		print(data)


	except Exception as e:
		con.rollback()
		print("Failed")
		print (">>>>>>>>>>>>>", e)
        
	return


	print("Not implemented")

def songs_samedate():
	try:
		query="SELECT GROUP_CONCAT(TrackName),R_Date from TRACK as t join RELEASE_DATE as r using(TrackID) group by R_Date"
		cur.execute(query)
		con.commit()
		data = cur.fetchall()
		print(data)
		for i in data:
			print(i["GROUP_CONCAT(TrackName)"],i["R_Date"])


	except Exception as e:
		con.rollback()
		print("Failed")
		print (">>>>>>>>>>>>>", e)
        
	return


	print("Not implemented")

def bothyoungold():
	try:
		query="SELECT  TrackName from TRACK as t join RELEASE_DATE as r using(TrackID) ORDER BY R_Date limit 1"
		query1="SELECT  TrackName from TRACK as t join RELEASE_DATE as r using(TrackID) ORDER BY R_Date DESC limit 1"
		cur.execute(query)
		con.commit()
		data1 = cur.fetchall()
		cur.execute(query1)
		con.commit()
		data = cur.fetchall()
		print("oldest song: ",data1[0]["TrackName"])
		
		print("youngest song: ",data[0]["TrackName"])
		


	except Exception as e:
		con.rollback()
		print("Failed")
		print (">>>>>>>>>>>>>", e)
        
	return


	print("Not implemented")
def smallestsong():
	try:
		query="SELECT  TrackName from TRACK as t join RELEASE_DATE as r using(TrackID) ORDER BY R_time limit 1"
		cur.execute(query)
		con.commit()
		data = cur.fetchall()
		for i in data:
			print("smallest song is:",data[0]["TrackName"])


	except Exception as e:
		con.rollback()
		print("Failed")
		print (">>>>>>>>>>>>>", e)
        
	return


	print("Not implemented")

def songs_of_an_album():
	try:
		g=input("albumname:")
		query="select TrackName from TRACK WHERE TRACK.AlbumID=(SELECT AlbumID FROM ALBUM WHERE Albumname='%s')"
		cur.execute(query%g)
		con.commit()
		data = cur.fetchall()
		for i in data:
			print(i["TrackName"])


	except Exception as e:
		con.rollback()
		print("Failed")
		print (">>>>>>>>>>>>>", e)
        
	return


	print("Not implemented")

def album_more_songs():
	try:
		
		query="select Albumname from ALBUM ORDER BY Number_of_Tracks Desc limit 1"
		cur.execute(query)
		con.commit()
		data = cur.fetchall()
		for i in data:
			print(i["Albumname"])


	except Exception as e:
		con.rollback()
		print("Failed")
		print (">>>>>>>>>>>>>", e)
        
	return
def songs_of_a_lyricist():
	try:
		g=input("Lyricist:")
		query="SELECT TrackName from TRACK WHERE TrackID IN (SELECT TrackID FROM PERSONS_TRACKS WHERE PERSONS_TRACKS.PersonID=(SELECT PersonID from PERSON WHERE Person_Name='%s' and PersonID IN (SELECT PersonID FROM LYRICIST)))"
		cur.execute(query%g)
		con.commit()
		data = cur.fetchall()
		for i in data:
			print(i["TrackName"])


	except Exception as e:
		con.rollback()
		print("Failed")
		print (">>>>>>>>>>>>>", e)
        
	return

def singer_with_highesttracks():
	try:
		query="SELECT Person_Name FROM (SELECT PersonID FROM SINGER) AS P JOIN PERSON USING(PersonID) ORDER BY Number_of_compositions DESC LIMIT 1"
		cur.execute(query)
		con.commit()
		data = cur.fetchall()
		for i in data:
			print(i["Person_Name"])


	except Exception as e:
		con.rollback()
		print("Failed")
		print (">>>>>>>>>>>>>", e)
        
	return

def oldestlyricist():
	try:
		query="SELECT Person_Name FROM (SELECT DISTINCT(PersonID) FROM LYRICIST) AS P JOIN PERSON USING(PersonID) ORDER BY BirthDay Limit 1"
		cur.execute(query)
		con.commit()
		data = cur.fetchall()
		for i in data:
			print(i["Person_Name"])


	except Exception as e:
		con.rollback()
		print("Failed")
		print (">>>>>>>>>>>>>", e)
        
	return

def lowestfrequency():
	try:
		query="SELECT TrackName from TRACK where TrackID=(select TrackID from FREQUENCY WHERE FREQUENCY.Count=(select Min(FREQUENCY.Count) from FREQUENCY))"
		cur.execute(query)
		con.commit()
		data = cur.fetchall()
		for i in data:
			print(i["TrackName"])


	except Exception as e:
		con.rollback()
		print("Failed")
		print (">>>>>>>>>>>>>", e)
        
	return




def delete_track():
    try:
        global cur
        row = {}
        print("Enter track ID")
        g=int(input())
        query="DELETE FROM TRACK WHERE TrackID=%d"
        q1="UPDATE ALBUM SET Number_of_Tracks=Number_of_Tracks-1 WHERE AlbumID=(SELECT AlbumID FROM TRACK WHERE TrackID=%d)"
        q2= "DELETE FROM PERSONS_TRACKS WHERE TrackID=%d"
        q3="DELETE FROM RELEASE_DATE WHERE TrackID=%d"
        q4="DELETE FROM FREQUENCY WHERE TrackID=%d"
        #cur.execute(q1%g)
        #cur.execute(q2%g)
        cur.execute(q1%g)
        cur.execute(q2%g)
        cur.execute(query%g)
        cur.execute(q3%g)
        cur.execute(q4%g)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to delete")

    return

def modify_singer():
    try:
        global cur
        row = {}
        print("Enter singer ID and new mobile number ")
        # name = input("Name (Singer_ID): ")
        row["PersonID"]=int(input("ID: "))
        row["Mobile_Number"]=input("Mobile Number:  ")
        query="UPDATE PERSON SET Mobile_Number=%s WHERE PersonID=%d"
        val=(row["Mobile_Number"],row["PersonID"])
        cur.execute(query%val)
        con.commit()
        #data=cur.fetchone()
        #print(data)

    except Exception as e:
        con.rollback()
        print("Failed to update Mobile Number")
  
    return



'''def promoteEmployee():
    """
    Function performs one of three jobs
    1. Increases salary
    2. Makes employee a supervisor
    3. Makes employee a manager
    """
    print("Not implemented")


def employeeStatistics():
    """
    Function prints a report containing 
    the number of hours per week the employee works,
    hourly pay, projects employee works on and so on
    """
    print("Not implemented")


def hireAnEmployee():
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter new employee's details: ")
        name = (input("Name (Fname Minit Lname): ")).split(' ')
        row["Fname"] = name[0]
        row["Minit"] = name[1]
        row["Lname"] = name[2]
        row["Ssn"] = input("SSN: ")
        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
        row["Address"] = input("Address: ")
        row["Sex"] = input("Sex: ")
        row["Salary"] = float(input("Salary: "))
        row["Dno"] = int(input("Dno: "))

        """
        In addition to taking input, you are required to handle domain errors as well
        For example: the SSN should be only 9 characters long
        Sex should be only M or F
        If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
        HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
        """

        query = "INSERT INTO EMPLOYEE(Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Dno) VALUES('%s', '%c', '%s', '%s', '%s', '%s', '%c', %f, %d)" %(row["Fname"], row["Minit"], row["Lname"], row["Ssn"], row["Bdate"], row["Address"], row["Sex"], row["Salary"], row["Dno"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)
        
    return'''

def dispatch(ch):
	if(ch==1): 
		insertSong()
	elif(ch==2):
		insertAlbum()
	elif(ch==3):
		renameSong()
	elif(ch==4):
		changeFrequency()
	elif(ch==5):
		delete_album()
	elif(ch==6):
		delete_track()
	elif(ch==7):
		modify_singer()


	elif(ch==8): 
		songs_of_singer()
	elif(ch==9):
		songs_samedate()
	
	elif(ch==10):
		highest_frequency()
	
	
	elif(ch==11):
		bothyoungold()
	elif(ch==12):
		smallestsong()
	elif(ch==13):
		songs_of_an_album()
	elif(ch==14):
		album_more_songs()
	elif(ch==15):
		songs_of_a_lyricist()
	elif(ch==16):
		singer_with_highesttracks()
	elif(ch==17):
		oldestlyricist()
	elif(ch==18):
		lowestfrequency()
        

	'''
	elif(ch==12):
        fireAnEmployee()
    elif(ch==13):
        promoteEmployee()
    elif(ch==14):
        employeeStatistics()
    elif(ch==15):
        employeeStatistics()
    elif(ch==16):
        employeeStatistics()
    else:
        print("Error: Invalid Option")
    '''

# Global
while(1):
    tmp = sp.call('clear',shell=True)
    username = input("Username: ")
    password = input("Password: ")

    try:
        con = pymysql.connect(host='localhost',
                user=username,
                password=password,
                db='MUSIC',
                cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear',shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")
        tmp = input("Enter any key to CONTINUE>")

        with con:
            cur = con.cursor()
            while(1):
                tmp = sp.call('clear',shell=True)
                print("1. Insert a song")
                print("2. Insert Album")
                print("3. Rename Song")
                print("4. Change Frequency of song")
                print("5. Delete Album")
                print("6.Deleting a track")
                print("7.Modifying Singer details  Mobile Number")
                print("8. Total number of songs performed by a Singer ")

                '''
            	print("2. Add Song to favourites")
                print("3. Add album")
                print("4. Delete album")
                print("5. Delete a track")
                print("6. Delete Song from favourites")
                print("7. Get Release Date")'''
                print("9. Total number of songs released on same date")
                
                
                print("10. Track having highest frequency")
                print("11. Oldest and youngest songs")
                print("12. Smallest song(less playtime)")
                print("13. Songs of an album")
                print("14. Album with more songs")
                print("15. Songs of an lyricist")
                print("16. Singer with highest number of tracks")
                print("17. Oldest lyricist")
                print("18. Track with lowest frequency")
               
                print("19. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear',shell=True)
                if ch==19:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")


    except:
        tmp = sp.call('clear',shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
    
