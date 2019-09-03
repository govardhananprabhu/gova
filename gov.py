

  
def AND(a, n) : 
  
    ans = lst[0] 
    for i in range(n) : 
        ans &= lst[i] 
          
    return ans 
if __name__ == "__main__" :
    lst =[]
    n = int(input("Enter number of elements : "))  
    for i in range(0, n): 
        ele = int(input()) 
        lst.append(ele) 
        print(lst)       
    n = len(lst) 
    print(AND(lst, n)) 
 
