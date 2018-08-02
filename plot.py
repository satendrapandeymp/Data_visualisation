import time, os


num = .1

input_file = open("data1.txt")
text = input_file.read()
input_file.close()

temps = text.split("\n")


lines = []

for i in range(len(temps)/20):
     temp = ""
     for j in range(20):
         temp += (temps[i*20 + j] + "\n")
     lines.append(temp)

for line in lines:
    input_file = open("data2.txt", 'w')
    input_file.write(line)
    input_file.close()
    print line
    time.sleep(num)

#time.sleep(.001)

os.system('kill `ps -ax | grep "gnuplot -e load"`')
#os.system('kill `ps -ax | grep "gnuplot -e load"`')


#os.system('kill `ps -ax | grep "recordmydesktop -o ../Videos/"`')


'''

time.sleep(1)

os.system('kill `ps -ax | grep "recordmydesktop -o ../Videos/{0}.ogv"`'.format(name))

time.sleep(2)

os.system('kill `ps -ax | grep "gnuplot -e load"`')
os.system('kill `ps -ax | grep "gnuplot -e load"`')
os.system('kill `ps -ax | grep "gnuplot -e load"`')
os.system('kill `ps -ax | grep "gnuplot -e load"`')
os.system('kill `ps -ax | grep "gnuplot -e load"`')
os.system('kill `ps -ax | grep "gnuplot -e load"`')


os.remove("../../Results/cat1.csv")

time.sleep(2)

'''
