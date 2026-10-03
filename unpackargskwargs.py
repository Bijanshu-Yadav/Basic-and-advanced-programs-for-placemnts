def lope(*args,**kwargs):
    print(args)
    print(kwargs)

hello = [23,45,67,23]
students ={
    'Name':'Biajsnhu',
    'Name':'Hitanshu'
}

lope(*hello,**students)