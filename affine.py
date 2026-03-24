import random
def compute_gcd(val1,val2):
    while val1!=val2:
        if val1>val2:
            val1=val1-val2
        else:
            val2=val2-val1
    return val1

def generate_keys():
    modulus=26
    coprime_numbers=[]
    all_numbers=[]
    for i in range(1,modulus+1):
        if compute_gcd(i,modulus)==1:
            coprime_numbers+=[i]
        all_numbers+=[i]
    second_key=random.choice(all_numbers)
    first_key=random.choice(coprime_numbers)
    return first_key,second_key

def encode_message(input_text):
    result=""
    lowercase="abcdefghijklmnopqrstuvwxyz" 
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_flag=True 
    while key_flag:
        user_choice=input("If you have keys - press y , if not - press n we will automatically create keys : [y,n]? ")
        if user_choice=='y':
            first_param,second_param = map(int, input("Enter keys a and b separated by space: (example: 5 17) ").split())
            key_flag=False
        elif user_choice=='n':
            print("We are automatically creating keys....")
            first_param,second_param=generate_keys()
            print(f"Your pair of keys is ({first_param},{second_param})")
            key_flag=False
        else:
            print("Select correct option")
    for character in input_text:
        if character in lowercase:
            position=lowercase.find(character)     
            encoded_value=(first_param*position+second_param)%26
            result+=str(lowercase[encoded_value])
        elif character in uppercase:
            position=uppercase.find(character)
            encoded_value=(first_param*position+second_param)%26
            result+=str(uppercase[encoded_value]) 
        else:
            result+=character           
    return result

def decode_message(encrypted_text):
    result=""
    lowercase="abcdefghijklmnopqrstuvwxyz" 
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    first_key, second_key = map(int, input("Enter keys a and b separated by space: ").split())
    modular_inverse=1
    while (first_key*modular_inverse)%26!=1:
        modular_inverse+=1
    for character in encrypted_text:
        if character in lowercase:
            position=lowercase.find(character)     
            decoded_value=modular_inverse*(position-second_key)%26
            result+=str(lowercase[decoded_value])
        elif character in uppercase:
            position=uppercase.find(character)
            decoded_value=modular_inverse*(position-second_key)%26
            result+=str(uppercase[decoded_value])
        else:
            result+=character      
    return result