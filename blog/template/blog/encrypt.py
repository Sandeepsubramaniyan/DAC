def encryption( ):
    latitude=input('Enter the Latitude')
    longitude=input('Enter Longitude:')
    message=str(latitude+longitude)
    alphabet="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    key = input("Enter a encrypt key of your Choice (at lease 8 Numbers long): ")
    encrypt =''
    for i in message:
      position=alphabet.find(i)
      newposition=(position+ int(key) )%94
      encrypt+=alphabet [newposition]
    output = (encrypt)
    print ('Encrypted Message: '+ (output) )
    print ('Encryption Key: '+ (key) )
encryption()