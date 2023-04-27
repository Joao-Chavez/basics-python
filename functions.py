
def hello_world():
    print("Hello, world!")

def hello_world_name(first_name):
    print(f"Hello, {first_name}!")

def hello_world_args(*args):
    first_name = args[0]
    second_name = args[1]
    third_name = args[2]

    #print(args)
    #print(type(args)) #Type sirve para saber el tipo de dato
    #print(first_name)
    print(f"Hello, {first_name} / {second_name} / {third_name}!")

def hello_world_keyword_args(first_person, second_person):
    print(f"Hello, {first_person} / {second_person}")

def hello_world_arbitrary_keyword_args(**kwargs):
    
    if kwargs.get['second_person'] is None:
        print("No hay persona")
    else:
        print(f"Hello, {kwargs['first_person']} / {kwargs['second_person']}!")
        
    #print(kwargs)
    #print(type(kwargs))
    #print("Hello from here!")
    #print(kwargs.get('second_person')) #SI TE SALE "NONE" ES PORQUE NO EXISTE
    print(f"Hello, {kwargs['first_person']} / {kwargs['second_person']}!")

#hello_world()
#hello_world_name("Joao")
#hello_world_name("Paulo")
#hello_world_args("Hugo", "Iván", "Pancho")
#hello_world_keyword_args(first_person="Joao", second_person="Paulo")
hello_world_arbitrary_keyword_args(first_person="Hugo", second_person="Iván")
hello_world_arbitrary_keyword_args(first_person="Hugo")