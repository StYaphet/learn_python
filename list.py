#1. 访问列表元素
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print (bicycles)
print (bicycles[0])
print (bicycles[0].title())
print (bicycles[-1])
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

#2. 修改、添加和删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)
motorcycles[0] = "ducati"
motorcycles[0] = "honda"
print (motorcycles)
motorcycles.append("ducati")
print (motorcycles)

motorcycles = []
print (motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles.insert(0, "ducati")
print(motorcycles)
del(motorcycles[0])
print(motorcycles)
del(motorcycles[1])
print(motorcycles)
motorcycles.insert(1, "yamaha")
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print("The last motorcycle I owned was a " + popped_motorcycle.title() + ".")
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove("honda")
print(motorcycles)
motorcycles.insert(0, "honda")
print(motorcycles)

#3. 组织列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)
print(len(cars))


















