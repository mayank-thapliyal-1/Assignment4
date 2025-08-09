try:
 file = open('sample.text','r')
 print("Reading file Content")
 i =1
 for line in file:
     print("line",i,": ",line)
     i=i+1
except FileNotFoundError:
    print('File not fount')
finally:
    print('all done')


