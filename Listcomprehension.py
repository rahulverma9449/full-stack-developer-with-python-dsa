li=[1,2,3,4]
li_new=[]
for ele in li:
    li_new.append(ele**2)
print(li_new)

li_new_c=[ele**2 for ele in li]

li_new_c

li_even_square=[ele**2 for ele in li if ele%2==0]

li_even_square

li_even_square=[]
for ele in li:
    if ele %2==0:
        li_even_square.append(ele)

li_even_square

li=[1,2,3,4,5,6,7,8,9]
li_new=[]
for ele in li:
    if ele%2==0:
        if ele %3==0:
            li_new.append(ele)
print(li_new)

li_new_2=[ele  for ele in li if ele%2==0 if ele%3==0]

print(li_new_2)

li_1=[1,2,3,4,5]
li_2=[2,4,6,7]
li_inter=[]
for ele in li_1:
    for ele_2 in li_2:
        if ele==ele_2:
            li_inter.append(ele)
print(li_inter)

li_1=[1,2,3,4,5]
li_2=[2,4,6,7]
li_inter=[ele for ele in li_1 for ele2 in li_2 if ele==ele2]

print(li_inter)

li=[1,2,3,4,5]
li_inter=[ele**2 if ele%2==0 else ele for ele in li]

li_inter

s="Parikh"
li=[ele for ele in s]

li

li=["Parikh","Rohan","Ankush"]
l1_2d=[[s for s in ele]for ele in li]

l1_2d
