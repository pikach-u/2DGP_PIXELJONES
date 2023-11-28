import json
numbers = [1,2,3,4]

numbers_string = json.dumps(numbers) #list를 json 형식으로 변환 s:string
print(type(numbers_string))
print(numbers_string)

value_string = '{ "x":10, "y":20, "size":4.5}'
value = json.loads(value_string)    #data를 원래 형식으로 복구시켜준다
print(type(value))
print(value)