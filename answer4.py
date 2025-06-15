empty_dic={}
def add_dic():
    name=input("enter your name :")
    email=input("enter your email :")
    phone_num=input("enter your phone number :")

    empty_dic[name]={'email':email,'phone_num':phone_num}
    print(f"'{name}' your details added succesfully")
def view_dic():
    if not empty_dic:
        print("no data feeded")
    else:
        for name,info in empty_dic.items():
            print(f"Name :'{name}'")
            print(f"email : '{info['email']}")
            print(f"phone number : {info['phone_num']}\n")
def update_dic():
    name=input("enter your name :")
    if name in empty_dic:
        email=input("enter your new email :")
        phone_num=input("enter your new phon enumber :")

        empty_dic[name]={'email':email,'phone_num':phone_num}
        print(f" {name} your data update succesfully")
    else:
        print("something went wrong ")

def del_dic():
    name=input("enter your name :")
    if name in empty_dic:
        del empty_dic[name]
        print(f"your data delte successfully")
    else:
        print("data couldnt try to delete try agai")
        
while True:
    choice=input("enter your choice on 1-5")
    if choice=='1':
        add_dic()
    elif choice=='2':
        view_dic()
    elif choice=='3':
        update_dic()
    elif choice=='4':
        del_dic()
    elif choice=='5':
        print(f"Exis the function ")
    else:
        print(f"invalid choice bye")















    
























