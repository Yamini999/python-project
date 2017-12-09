import math
import csv

def nearest_two_latlongs(origin, destination1,destination2):
    lat1, lon1 = origin
    lat2, lon2 = destination1
    lat3, lon3 = destination2
    
    radius = 6371 # km

    dlat1 = math.radians(lat2-lat1)
    dlon1 = math.radians(lon2-lon1)
    dlat2 = math.radians(lat3-lat1)
    dlon2 = math.radians(lon3-lon1)
    a = math.sin(dlat1/2) * math.sin(dlat1/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon1/2) * math.sin(dlon1/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d1 = radius * c

    b = math.sin(dlat2/2) * math.sin(dlat2/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat3)) * math.sin(dlon2/2) * math.sin(dlon2/2)
    d = 2 * math.atan2(math.sqrt(b), math.sqrt(1-b))
    d2 = radius * d
    if(d1 < d2):
        return destination1
    else:
        return destination2
    
file_access=open("geocode_health_centre.csv","r")
d={}
l2=[]
with open("geocode_health_centre.csv","r") as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    hlist=list(reader)
    
    for i in range(1,len(hlist)):
        
        l1=[[hlist[i][4],hlist[i][6],hlist[i][7]]]
        if hlist[i][1] not in l2:
            for k in range(i+1,len(hlist)):
               
                if(hlist[i][1]==hlist[k][1]):
                    l1.append([hlist[k][4],hlist[k][6],hlist[k][7]])
                   
            l2.append(hlist[i][1])
            
            d[hlist[i][1]]=l1
           
        
li4=[]
li8=[]
lat=input("enter the latitude")
lon=input("enter the longitude")
list1=[float(lat),float(lon)]   
list2=list(d.values())

for i in range(len(list2)):
    
    for j in range(len(list2[i])):
        if(j<len(list2[i])-1):
            if(list2[i][j][1]=='NA' or list2[i][j][2]=="NA"):
                break
            if(list2[i][j][1]=='29.42.0418' or list2[i][j][2]=='29.42.0418'):
                break
            if(list2[i][j][1]=='23.85.227' or list2[i][j][2]=='23.85.227'):
                break
            li1=[list2[i][j][0],float(list2[i][j][1]),float(list2[i][j][2])]
            if(list2[i][j+1][1]=='NA' or list2[i][j+1][2]=="NA"):
                break   
            if(list2[i][j+1][1]=='29.42.0418' or list2[i][j+1][2]=='29.42.0418'):
                break
            if(list2[i][j+1][1]=='Y' or list2[i][j+1][2]=="Y"):
              
                break
            if(list2[i][j+1][1]=='23.85.227' or list2[i][j+1][2]=='23.85.227'):
                break
            if(list2[i][j+1][1]=='30.47.6380' or list2[i][j+1][2]=='30.47.6380'):
                break
            li2=[list2[i][j+1][0],float(list2[i][j+1][1]),float(list2[i][j+1][2])]
        else:
            li1=[list2[i][j-1][0],float(list2[i][j-1][1]),float(list2[i][j-1][2])]
            li2=[list2[i][j][0],float(list2[i][j][1]),float(list2[i][j][2])]
        
        li4.append(li1)
        li4.append(li2)

count=0
while(len(li4)!=2):
  
    li7=nearest_two_latlongs(list1,[li4[0][1],li4[0][2]],[li4[1][1],li4[1][2]])
   
    
    if(li7==[li4[0][1],li4[0][2]]):
        li8=[li4[0][0],li4[0][1],li4[0][2]]
    if(li7==[li4[1][1],li4[1][2]]):
        
        li8=[li4[1][0],li4[1][1],li4[1][2]]
  
    count=count+1
    li4.remove(li4[0])
   
    li4.remove(li4[0])
    
    li4.insert(0,li8)
print(count)  
#temp=li4[0]
#li4[0]=li4[1]
#li4[1]=temp
print(li4)
li6=nearest_two_latlongs(list1,[li4[0][1],li4[0][2]],[li4[1][1],li4[1][2]])
if(li6==[li4[0][1],li4[0][2]]):
    li6=[li4[0][0],li4[0][1],li4[0][2]]
if(li6==[li4[1][1],li4[1][2]]):
    li6=[li4[1][0],li4[1][1],li4[1][2]]    
    
print("minimum distance is:")           
print(li6[0])


