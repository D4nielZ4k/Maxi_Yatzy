

##UPPER TABEL ________________
#function does what its name indicates     
def ones_sixes(ls,numer):
    counts = map_list_to_dict(ls)
    if numer in counts and counts[numer] > 0 :
        return numer * counts[numer]
    return 0 


#LOWER TABEL __________________
#function does what its name indicates
def one_pair(ls):
    counts = map_list_to_dict(ls)
    for num in sorted(counts.keys(), reverse=True):
        if counts[num] >= 2:
            return num * 2
    return 0

#function does what its name indicates
def two_pair(ls):
    counts = map_list_to_dict(ls)
    num_1 = 0
    num_2 = 0
    
    for num in sorted(counts.keys(), reverse=True):
        if counts[num] >= 2:
            if num_1 == 0:
                num_1 = num
            elif num_2 == 0:
                num_2 = num

            if num_1 != 0 and num_2 != 0:
                break

    if num_1 != 0 and num_2 != 0:
        return (num_1 + num_2) * 2 
    return 0 

#function does what its name indicates
def three_pair(ls):
    counts = map_list_to_dict(ls)
    num_1 = 0
    num_2 = 0
    num_3 = 0 
    
    for num in sorted(counts.keys(), reverse=True):
        if counts[num] >= 2:
            if num_1 == 0:
                num_1 = num
            elif num_2 == 0:
                num_2 = num
            elif num_3 == 0:
                num_3 = num

            if num_1 != 0 and num_2 != 0 and num_3 != 0:
                break

    if num_1 != 0 and num_2 != 0 and num_3 != 0:
        return (num_1 + num_2 + num_3) * 2 
    return 0

#function does what its name indicates
def three_of_a_kind (ls):
    counts = map_list_to_dict(ls)
    for num in sorted(counts.keys(), reverse=True):
        if counts[num] >= 3:
            return num * 3
    return 0

#function does what its name indicates
def four_of_a_kind (ls):
    counts = map_list_to_dict(ls)
    for num in sorted(counts.keys(), reverse=True):
        if counts[num] >= 4:
            return num * 4
    return 0


# FIVE OF A KIND Five dice showing the same value.
#function does what its name indicates
def five_of_a_kind(ls):
    counts = map_list_to_dict(ls)
    for num in sorted(counts.keys(), reverse=True):
        if counts[num] >= 5:
            return num * 5
    return 0



# SMALL STRAIGHT Five dice showing the values from 1-5. 15 pts.
#function does what its name indicates
def smal_straight(ls):
    ref_list =[]
    sort_list = sorted(ls)
    for i in sort_list:
        if i == 6 : sort_list.remove(i)
        if i != 6 : ref_list.append(i)
    fi_list = list(dict.fromkeys(sort_list))
    currect = [1, 2, 3, 4, 5]
    if fi_list == currect: return 15
    return 0

#DONE   BIG STRAIGHT Five dice showing the values from 2-6. 20 pts.
#function does what its name indicates
def large_straight(ls):
    ref_list =[]
    sort_list = sorted(ls)
    for i in sort_list:
        if i == 1 : sort_list.remove(i)
        if i != 1 : ref_list.append(i)
    fi_list = list(dict.fromkeys(sort_list))
    currect = [2, 3, 4, 5, 6]
    if fi_list == currect: return 20
    return 0


# Six dice showing the values from 1-6. 21 pts.
#function does what its name indicates
def full_straight(ls):
   sorted_list = sorted(ls)
   currect = [1, 2 ,3 , 4, 5, 6]
   if sorted_list == currect: return sum(ls)
   return 0


 #DONE FULL HOUSE A Pair and a Three of a Kind.
 #function does what its name indicates
def full_house(ls):
    counts = map_list_to_dict(ls)
    pair_num = 0 
    three_of_kind_num = 0 
    for num in sorted(counts.keys(), reverse=True):
        if counts[num] == 2:
            pair_num = num 
        if counts[num] >= 3:
            three_of_kind_num = num
    if pair_num != 0 and three_of_kind_num != 0: return pair_num * 2 + three_of_kind_num * 3
    return 0
 
#GOOD  VILLA Two Three of a Kinds
#function does what its name indicates
def villa (ls):
    counts = map_list_to_dict(ls)
    kinds = 0
    num_1 = 0 
    num_2 = 0
    for i in counts:
        if counts[i] == 3: kinds += 1
        if num_1 == 0 : num_1 = i
        num_2 = i
    if kinds ==2: return num_1 * 3 + num_2 * 3      
    return 0


#DONE TOWER A Pair and a Four of A Kind.
#function does what its name indicates
def towel(ls):
    counts = map_list_to_dict(ls)
    of_kind = 0
    pair = 0
    for i in counts:
        if counts[i] == 4: of_kind = i
        if counts[i] == 2: pair = i

    if of_kind != 0 and pair != 0: return (pair * 2 + of_kind * 4)     
    return 0


#GOOD
#function does what its name indicates
def chance(ls):
    return sum(ls)

#GOOD
#function does what its name indicates
def maxi_yatzy (ls):
    counts = map_list_to_dict(ls)
    for num in sorted(counts.keys(), reverse=True):
        if counts[num] == 6:
            return 100
    return 0


#function does what its name indicates
def map_list_to_dict(ls):
    final_dict = dict()
    for i in ls:
        if i in final_dict:
            final_dict[i] += 1  
        else:
            final_dict[i] = 1  
    return final_dict



## Simple TESTS list
#numers = [5, 6, 6, 6, 6, 6]

## Simple TESTS
#print("one pair from ",numers, "too ===   ",one_pair(numers))
##print ("two pair from ",numers, "too ===   ",two_pair(numers))
#print ("three pair from ",numers, "too ===   ",three_pair(numers))

#print("tre of kind ",numers, "too ===   ",three_of_a_kind(numers))
#print("four of kind ",numers, "too ===   ",four_of_a_kind(numers))
#print("five of kind " , five_of_a_kind(numers))
#print("smal_straight ",numers, "too ===   ",smal_straight(numers))
#print("big_straight ",numers, "too ===   ",large_straight(numers))
#print("full_house ",numers, "too ===   ",full_house(numers))
#print("chance ",numers, "too ===   ",chance(numers))
#print("maxi_yatzy",numers, "too ===   ",maxi_yatzy(numers))


#print("villa ->>>>>>>>>> " , villa(numers))
#print("TOWEL --------> " ,  towel(numers))


#print( "ones_sixes !!!!!  ", ones_sixes(numers, 6))
#print( "ones_fives !!!!!  ", ones_sixes(numers, 5))
#rint( "ones_four !!!!!  ", ones_sixes(numers, 4))
#rint( "ones_three !!!!!  ", ones_sixes(numers, 3))
#rint( "ones_two !!!!!  ", ones_sixes(numers, 2))
#print( "ones_ones !!!!!  ", ones_sixes(numers, 1))