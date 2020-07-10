from lab1 import Registry
# if __name__ == "main":
new_r = Registry()
new_r.register('gerhard@mail.utoronto.ca', 35)
new_r.register('tom@mail.utoronto.ca', 25)
new_r.register('toni@mail.utoronto.ca', 15)
new_r.register('gerhard@mail.utoronto.ca', 25)
info = new_r.get_runners_in_category('<30')
print(info)

