import pywifi
import time
import numpy

#存储参考点的wifi数据（没有点0和点24）
historyDate=[{}]
for i in range(1,60):
    if i==24:
        historyDate.append({})
    else:
        historyDate.append({})
        f=open(f"{i}.txt","r")
        line = f.readline()
        line = line[:-1]
        #print(line)
        singleWifiList=line.split()
        historyDate[i][singleWifiList[0]]=singleWifiList[1]
        while line:  # 直到读取完文件
            line = f.readline()  # 读取一行文件，包括换行符
            line = line[:-1]  # 去掉换行符
            if len(line)!=0: #如果这一行不是空行
                #print(line)
                singleWifiList = line.split()
                historyDate[i][singleWifiList[0]] = singleWifiList[1]
        f.close()  # 关闭文件
#将历史数据以字典形式存到对应的historyDate里

'''
for i in historyDate[59]:
    print(i)
    print(historyDate[59][i])
'''



#将各参考点的坐标信息存到字典里，key为参考点序号，value为参考点坐标（列表形式存储）
pointsCoordinates={}
pointsCoordinates[1]=[25,20]
pointsCoordinates[2]=[29,20]
pointsCoordinates[3]=[25,18]
pointsCoordinates[4]=[29,18]
pointsCoordinates[5]=[24,19]
pointsCoordinates[6]=[23,18]
pointsCoordinates[7]=[21,18]
pointsCoordinates[8]=[20,18]
pointsCoordinates[9]=[19,20]
pointsCoordinates[10]=[17,20]
pointsCoordinates[11]=[16,18]
pointsCoordinates[12]=[14,18]
pointsCoordinates[13]=[13,20]
pointsCoordinates[14]=[11,20]
pointsCoordinates[15]=[10,18]
pointsCoordinates[16]=[8,18]
pointsCoordinates[17]=[5,18]
pointsCoordinates[18]=[5,20]
pointsCoordinates[19]=[1,20]
pointsCoordinates[20]=[1,18]
pointsCoordinates[21]=[7,2]
pointsCoordinates[22]=[9,5]
pointsCoordinates[23]=[11,5]
pointsCoordinates[25]=[14,7]
pointsCoordinates[26]=[14,5]
pointsCoordinates[27]=[16,5]
pointsCoordinates[28]=[15,2]
pointsCoordinates[29]=[18,3]
pointsCoordinates[30]=[19,5]
pointsCoordinates[31]=[21,5]
pointsCoordinates[32]=[22,3]
pointsCoordinates[33]=[24,2]
pointsCoordinates[34]=[25,3]
pointsCoordinates[35]=[25,5]
pointsCoordinates[36]=[29,5]
pointsCoordinates[37]=[29,3]
pointsCoordinates[38]=[31,3]
pointsCoordinates[39]=[31,18]
pointsCoordinates[40]=[7,16]
pointsCoordinates[41]=[7,15]
pointsCoordinates[42]=[7,14]
pointsCoordinates[43]=[7,13]
pointsCoordinates[44]=[7,12]
pointsCoordinates[45]=[7,11]
pointsCoordinates[46]=[7,10]
pointsCoordinates[47]=[7,9]
pointsCoordinates[48]=[7,8]
pointsCoordinates[49]=[7,7]
pointsCoordinates[50]=[24,7]
pointsCoordinates[51]=[24,8]
pointsCoordinates[52]=[24,9]
pointsCoordinates[53]=[24,10]
pointsCoordinates[54]=[24,11]
pointsCoordinates[55]=[24,12]
pointsCoordinates[56]=[24,13]
pointsCoordinates[57]=[24,14]
pointsCoordinates[58]=[24,15]
pointsCoordinates[59]=[24,16]





'''
#获取当前点的wifi数据
wifi = pywifi.PyWiFi() #定义接口操作
iface = wifi.interfaces()[0] #iface是获取的wifi接口，一个电脑一般只有一个wifi接口

wifis=[{},{},{},{},{},{},{},{},{},{}] #存储第1到第10次扫描的结果
for i in range(10):
    iface.scan() #扫描接收到的wifi
    time.sleep(1)
    results=iface.scan_results() #获取先前扫描到的结果，存储在results列表中
    for result in results:
        wifis[i][result.bssid]=result.signal;
    time.sleep(1)

avgWifi=wifis[0] #存储每个wifi信号的mac地址和10次平均RSSI值, avgWifi的初始设定值是第一次扫描得到的wifi信息

#清除avgWifi中所有在第2到10次扫描中的某一次/几次没有扫描到的wifi信息
for i in range(1,10):
    tempList=list(avgWifi.keys())
    for j in tempList:
        if wifis[i].__contains__(j)==False:
            del avgWifi[j]
#此时avgWifi中的wifi信号就是在10次扫描中都出现的wifi信号

avgWifiKeys=avgWifi.keys()
for Key in avgWifiKeys:
    for i in range(1,10):
        avgWifi[Key]=avgWifi[Key]+wifis[i][Key]
    avgWifi[Key]=avgWifi[Key]/10
#此时avgWifi中存储了10次平均的wifi信号和强度值

sigma={} #sigma存储各AP发出的信号对应的σ值
for Key in avgWifiKeys:
    sigma[Key]=0
for key in sigma.keys():
    for i in range(10):
        sigma[key]+=(wifis[i][key]-avgWifi[key])**2
    sigma[key]=(sigma[key]/10)**0.5

minWifiRssi={} #存储各AP信号对应的μ-1.65σ
maxWifiRssi={} #存储各AP信号对应的μ+1.65σ
for key in avgWifi.keys():
    minWifiRssi[key]=avgWifi[key]-1.65*sigma[key]
    maxWifiRssi[key]=avgWifi[key]+1.65*sigma[key]
finalWifi={} #最终输出的wifi的RSSI值
for key in avgWifi.keys():
    finalWifi[key]=0
num=0 #记录一个AP信号在10次测量中的RSSI值处于90%以内的次数
for key in avgWifi.keys():
    for i in range(10):
        if (wifis[i][key]>minWifiRssi[key] and wifis[i][key]<maxWifiRssi[key]) or wifis[i][key]==avgWifi[key]: #如果该次测量中，wifi的强度值处于合理区间
            finalWifi[key]+=wifis[i][key]
            num+=1
    if num!=0:
        finalWifi[key]/=num
        num=0
    else:
        del finalWifi[key]
#此时finalWifi中存储了10次平均的wifi信号和强度值
'''


#利用之前测的数据，真正的代码中要删掉这一段
finalWifi={}
#f=open("测试3.txt","r")
f=open("测试1.txt","r")
line = f.readline()
line = line[:-1]
singleWifiList=line.split()
finalWifi[singleWifiList[0]]=singleWifiList[1]
while line:  # 直到读取完文件
    line = f.readline()  # 读取一行文件，包括换行符
    line = line[:-1]  # 去掉换行符
    if len(line)!=0: #如果这一行不是空行
        singleWifiList = line.split()
        finalWifi[singleWifiList[0]] = singleWifiList[1]
f.close()  # 关闭文件





#开始计算当前点与所有参考点的wifi信号的欧式距离
distancesDict={}
for i in range(1,60):
    if i!=24:
        Distance=0
        for Key in finalWifi.keys():
            if historyDate[i].__contains__(Key): #如果参考点i处有AP=Key的wifi信号
                Distance=Distance+(float(finalWifi[Key])-float(historyDate[i][Key]))**2
            else:
                Distance=Distance+float(finalWifi[Key])**2
        distancesDict[i]=Distance**0.5
#各参考点与当前点的RSSI值的欧氏距离存储在distances的对应序号中



#将欧氏距离排序，并获得距离最小的K（5）个点
distances=[] #存储单纯的欧式距离
for key in distancesDict.keys():
    distances.append(distancesDict[key])
k=5
sortedDistances=sorted(distances) #从小到大排序后的欧式距离列表
useDistances=sortedDistances[:k] #前K个用到的欧式距离
usePoints=[] #存储用到的参考点的序号
for i in range(k):
    for key in distancesDict.keys():
        if distancesDict[key]==useDistances[i]:
            usePoints.append(key)
sumOfReciDistance=0 #sumOfWeight是k个点的欧式距离倒数之和
for i in range(k):
    sumOfReciDistance+=1/useDistances[i]
weights=[] #存储第1到第k个参考点对应的权值
for i in range(k):
    weights.append((1/useDistances[i])/sumOfReciDistance)

avgX=0 #计算出的当前点的X坐标
avgY=0 #计算出的当前点的Y坐标
for i in range(k):
    avgX += weights[i] * pointsCoordinates[usePoints[i]][0]
    avgY += weights[i] * pointsCoordinates[usePoints[i]][1]
print(f"({round(avgX,2)},{round(avgY,2)})")


'''
#将欧氏距离排序，并获得距离最小的K（5）个点
distances=[] #存储单纯的欧式距离
for key in distancesDict.keys():
    distances.append(distancesDict[key])
k=5
sortedDistances=sorted(distances) #从小到大排序后的欧式距离列表
useDistances=sortedDistances[:k] #前K个用到的欧式距离
usePoints=[] #存储用到的参考点的序号
for key in distancesDict.keys():
    if distancesDict[key] in useDistances:
        usePoints.append(key)

avgX=0 #计算出的当前点的X坐标
avgY=0 #计算出的当前点的Y坐标
for i in range(5):
    avgX += pointsCoordinates[usePoints[i]][0]
    avgY += pointsCoordinates[usePoints[i]][1]
avgX/=5
avgY/=5
print(f"({round(avgX,2)},{round(avgY,2)})")
'''