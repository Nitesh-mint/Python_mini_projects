'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given scores. Store them in a list and find the score of the runner-up'''
n = int(input("Num:"))
arr = map(int, input().split())

score = sorted(set(arr))#sorted sorts elements and set removes duplicates
print(score[-2])