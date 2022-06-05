# 파일 = open('a.txt', 'w')
# 파일.write('hello')
# 파일.close()

# 파일 = open('a.txt', 'a')
# 파일.write('\n반가워')

# 파일 = open('a.txt', 'r')
# print( 파일.read() )
# 파일.close()

f = open('data.csv', 'w')
f.write('김, 이, 박')
f.write('/n김, 이, 박')
f.close()