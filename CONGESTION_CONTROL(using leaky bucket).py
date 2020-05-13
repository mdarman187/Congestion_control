print("\n\n..........CONGESTION CONTROL USING LEAKY BUCKET ALGORITHHM..........\n \n")
bucket_size=int(input("ENTER THE BUCKET SIZE : "))
outgoing_rate=int(input("ENTER THE OUTGOING RATE : "))
if outgoing_rate>bucket_size :
    print("\n\n OUTGOING RATE SHOULD BE LESS THAN BUCKET SIZE")
else:
    n=int(input("\n\nENTER THE NUMBER OF INPUTS : "))
    stored=0
    while n!=0 :
           inc_pack_size=int(input("\nENTER THE INCOMING PACKET SIZE : "))
           if inc_pack_size<=(bucket_size-stored) :
               stored+=inc_pack_size
               print("\n\nBUCKET BUFFER SIZE ",stored," OUT OF ",bucket_size)
           else:
               print("DROPPED NUMBER OF PACKET : ",inc_pack_size-(bucket_size-stored))
               stored=bucket_size
               print("BUCKET BUFFER SIZE ",stored," OUT OF ",bucket_size)
           stored-=outgoing_rate
           if stored<0 :
               stored=0
           print("AFTER OUTGOING ",stored," PACKET LEFT OUT OF ",bucket_size," IN BUFFER\n")
           n-=1
    print("\n\n\n***COMPLETED***")
        
