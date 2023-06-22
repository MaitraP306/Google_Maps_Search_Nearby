def binary_searchupper(a, l, h, k):
    if h < l:
        return "not found"
    elif l == h:
        if a[l][1] <= k:
            return l
        else:
            return "not found"
    else:
        mid = (l + h) // 2
        if a[mid][1] < k:
            if a[mid+1][1] > k:
                return mid
            return binary_searchupper(a, mid + 1, h, k)
        elif a[mid][1] == k:
            return mid
        else:
            return binary_searchupper(a, l, mid - 1, k)

def binary_searchlower(a, l, h, k):
    if h < l:
        return "not found"
    elif l == h:
        if a[l][1] >= k:
            return l
        else:
            return "not found"
    else:
        mid = (l + h) // 2
        if a[mid][1] < k:
            return binary_searchlower(a, mid + 1, h, k)
        elif a[mid][1] == k:
            return mid
        else:
            if a[mid - 1][1] < k:
                return mid
            else:
                return binary_searchlower(a, l, mid - 1, k)

class Node:
    def __init__(self , data):
        self.left = None
        self.right = None
        self.data = data
        self.yleft = []
        self.yright = []
        self.subsetleft = []
        self.subsetright = []

def construct_tree(data , datay , n ):
    if(n==0):
        return None
    elif(n==1):
        new_node = Node(data[0])
        return new_node
    else:
        node = Node(data[(n-1)//2])
        ytreer = []
        ytreel = []
        for k in range(0 , len(datay)):
            if(datay[k]!=None):
                if(datay[k][0]> data[(n-1)//2][0]):
                    ytreer.append(datay[k])
                else:
                    ytreel.append(datay[k])
        node.yleft = ytreel
        node.yright = ytreer
        node_left = construct_tree(data[0:(n-1)//2 +1] , ytreel ,  (n-1)//2 +1)
        node_right = construct_tree(data[(n-1)//2 +1:n] ,ytreer , n//2)
        node.subsetleft = data[0:(n-1)//2 +1]
        node.subsetright = data[(n-1)//2 +1:n]
        node.left = node_left
        node.right = node_right
        return node

def searchyr(node, minimum, maximum):
    ytreer = node.yright
    if minimum<ytreer[0][1]:
        lowerlimit =0
        upperlimit = binary_searchupper(ytreer, 0, len(ytreer) - 1, maximum)
        if lowerlimit == "not found" or upperlimit == "not found":
            return []
    else:
        lowerlimit = binary_searchlower(ytreer, 0, len(ytreer) - 1, minimum)
        upperlimit = binary_searchupper(ytreer, 0, len(ytreer) - 1, maximum)
        if lowerlimit == "not found" or upperlimit == "not found":
            return []
    ans = ytreer[lowerlimit: upperlimit+1]
    return ans

def searchyl(node, minimum , maximum):
    ytreel = node.yleft
    if minimum<ytreel[0][1]:
        lowerlimit =0
        upperlimit = binary_searchupper(ytreel, 0, len(ytreel) - 1, maximum)
        if lowerlimit == "not found" or upperlimit == "not found":
            return []
    else:
        lowerlimit = binary_searchlower(ytreel, 0, len(ytreel) - 1, minimum)
        upperlimit = binary_searchupper(ytreel, 0, len(ytreel) - 1, maximum)
        if lowerlimit == "not found" or upperlimit == "not found":
            return []
    ans = ytreel[lowerlimit: upperlimit+1]
    return ans

def findsplit(node , mini , maxi):
    if(node==None):
        return None
    if(node.data[0]<mini):
        return findsplit(node.right , mini , maxi)
    else:
        if(node.data[0]>maxi):
            return findsplit(node.left , mini , maxi)
        else:
            return node

def minim(node , xmini , xmaxi , ymini , ymaxi , ans):
    if(node == None):
        return ans
    if(node.left == None and node.right == None):
        if(node.data[0]>= xmini and node.data[0]<= xmaxi and node.data[1]>= ymini and node.data[1]<= ymaxi ):
            ans.append(node.data)
        return ans
    if(node.data[0]>= xmini and node.data[0]<= xmaxi):
        temp = searchyr(node , ymini , ymaxi )
        for i in range(0 , len(temp)):
            ans.append(temp[i])
        node = node.left
        return(minim(node , xmini , xmaxi , ymini , ymaxi , ans))
    elif(node.data[0]<xmini):
        node = node.right
        return(minim(node , xmini , xmaxi , ymini , ymaxi , ans))
    else:
        node = node.left
        return(minim(node , xmini , xmaxi , ymini , ymaxi , ans))

def maxim(node , xmini , xmaxi , ymini , ymaxi , ans):
    if(node == None):
        return ans
    if(node.left == None and node.right == None):
        if(node.data[0]>= xmini and node.data[0]<= xmaxi and node.data[1]>= ymini and node.data[1]<= ymaxi ):
            ans.append(node.data)
        return ans
    if(node.data[0]>= xmini and node.data[0]<= xmaxi):
        temp = searchyl(node , ymini , ymaxi )
        for i in range(0 , len(temp)):
            ans.append(temp[i])
        node = node.right
        return(maxim(node , xmini , xmaxi , ymini , ymaxi , ans))
    elif(node.data[0]<xmini):
        node = node.right
        return(maxim(node , xmini , xmaxi , ymini , ymaxi , ans))
    else:
        node = node.left
        return(maxim(node , xmini , xmaxi , ymini , ymaxi , ans))
   
def search(query , root):
    xmini = query[0][0] - query[1]
    xmax = query[0][0] + query[1]
    ymini = query[0][1] - query[1]
    ymax = query[0][1] + query[1]
    node = root
    ans = []
    node = findsplit(node , xmini , xmax)
    if(node==None):
        return ans
    if(node.left == None and node.right == None ):
        if(node.data[0]>= xmini and node.data[0]<= xmax and node.data[1]>= ymini and node.data[1]<= ymax):
            ans.append(node.data)
        return ans
    temp1 = minim(node.left , xmini , xmax , ymini , ymax , [])
    temp2 = maxim(node.right , xmini , xmax , ymini , ymax , [])
    ans = temp1+temp2
    return ans

class PointDatabase:
    def __init__(self,pointlist):
        lx = sorted(pointlist)
        ly = sorted(pointlist,key = lambda x: x[1])
        self.root = construct_tree(lx,ly,len(lx))
    def searchNearby(self,q,d):
        return sorted(search([q,d],self.root))
