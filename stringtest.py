import sys

print("文字列を入力してください. ")
line = sys.stdin.readline().strip()
for c in line:
    print(""+c+"'の文字コードは"+str(ord(c))+"です.")
