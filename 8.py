#recursion basics

#head recursion
# count = 0
# def func():
#     global count
#     if count==4:
#         return
#     print("sahil")
#     count+=1
#     func()


# func()


#tail recursion

count = 0

def func():
    global count
    if count==4:
        return
    count+=1
    func()
    print("anirudh")


func()