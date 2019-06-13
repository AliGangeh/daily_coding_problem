#IBM coding challenge

#given a string with repeated characters, rearrange the string so that no two
#adjacent characters are the same. if this is not possible, return None.
#For example, given "aaabbc", you could return "ababac" given "aaab" return None.

def ordering_string (str):
    stat = {}
    for i in range(0, len(str)):
        if str[i] in stat:
            stat[str[i]] += 1
        else:
            stat[str[i]] = 1
    final_string = []
    for i in range(0, len(str)):
        sorted_stat = [[k, stat[k]] for k in sorted(stat, key=stat.get, reverse=True)]
        if not final_string:
            final_string.append(sorted_stat[0][0])
            stat[sorted_stat[0][0]] -= 1
        elif (sorted_stat[0][1] > 1 and sorted_stat[1][1] == 0):
            return None
        else:
            if not sorted_stat[0][0] == final_string[i-1]:
                final_string.append(sorted_stat[0][0])
                stat[sorted_stat[0][0]] -= 1
            else:
                final_string.append(sorted_stat[1][0])
                stat[sorted_stat[1][0]] -= 1
    print("".join(final_string))
    return ("".join(final_string))

ordering_string("aaaaabbbbbbccccccccccc")
