encrypted_message = ''  
 
alphabet=["A", "B", "C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
 
message = input()            
for i in message:          
      
    if i not in alphabet:
        encrypted_message += i 
    else:
        encrypted_message += alphabet[(alphabet.index(i)+4) % len(alphabet)]
     
print( encrypted_message)
